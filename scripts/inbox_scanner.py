#!/usr/bin/env python3
"""
wiki-life inbox 扫描脚本
自动扫描 raw/inbox/ 目录，生成入库建议报告
"""

import os
import sys
import re
import hashlib
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class InboxItem:
    path: Path
    title: str
    source_type: str
    tags: List[str] = field(default_factory=list)
    quality_score: Optional[float] = None
    suggestion: str = ""

class InboxScanner:
    def __init__(self, wiki_root: Path):
        self.wiki_root = wiki_root
        self.inbox_dir = wiki_root / "raw" / "inbox"
        self.entities_dir = wiki_root / "entities"
        self.concepts_dir = wiki_root / "concepts"
        
    def scan(self) -> List[InboxItem]:
        """扫描 inbox 目录，返回待处理项目列表"""
        items = []
        
        if not self.inbox_dir.exists():
            print(f"inbox 目录不存在: {self.inbox_dir}")
            return items
            
        # 递归扫描所有子目录（rss/ newsletter/ wechat/），⚠️ 不能只 glob 顶层
        for file_path in self.inbox_dir.rglob("*.md"):
            # candidates.md 是 newsletter 的 URL 列表，不是文章，跳过
            if file_path.name == "candidates.md":
                continue
            item = self._parse_item(file_path)
            if item:
                items.append(item)
                
        return items
    
    def _parse_yaml_line(self, line: str) -> tuple:
        """简单解析 YAML 行"""
        if ':' not in line:
            return None, None
        
        key, value = line.split(':', 1)
        key = key.strip()
        value = value.strip().strip('"\'')
        
        # 处理列表
        if value.startswith('[') and value.endswith(']'):
            items = re.findall(r'[\'"]?([^\'",\[\]]+)[\'"]?', value)
            return key, [i.strip() for i in items if i.strip()]
        
        # 处理简单值
        if value.lower() in ('true', 'yes'):
            return key, True
        if value.lower() in ('false', 'no'):
            return key, False
        
        return key, value
    
    def _parse_item(self, path: Path) -> Optional[InboxItem]:
        """解析单个 inbox 文件"""
        try:
            content = path.read_text(encoding='utf-8')
            
            # 提取 YAML frontmatter
            title = path.stem
            source_type = 'unknown'
            tags = []
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter_text = parts[1]
                    
                    for line in frontmatter_text.split('\n'):
                        line = line.strip()
                        if not line or line.startswith('#'):
                            continue
                            
                        key, value = self._parse_yaml_line(line)
                        
                        if key == 'title':
                            title = value if value else path.stem
                        elif key == 'type':
                            source_type = value if value else 'unknown'
                        elif key == 'tags':
                            if isinstance(value, list):
                                tags = value
                            elif isinstance(value, str):
                                tags = [value]
            
            return InboxItem(
                path=path,
                title=title,
                source_type=source_type,
                tags=tags
            )
            
        except Exception as e:
            print(f"解析失败 {path}: {e}")
            # 返回基础项
            return InboxItem(
                path=path,
                title=path.stem,
                source_type='unknown',
                tags=[]
            )
    
    def _check_duplicate(self, item: InboxItem) -> bool:
        """检查是否重复（简单版）"""
        title_normalized = item.title.lower().replace(' ', '')
        
        # 检查现有实体
        for entity_file in self.entities_dir.glob("*.md"):
            if title_normalized in entity_file.stem.lower():
                return True
                
        # 检查现有概念
        for concept_file in self.concepts_dir.glob("*.md"):
            if title_normalized in concept_file.stem.lower():
                return True
                
        return False
    
    def _suggest_category(self, item: InboxItem) -> str:
        """根据标签和标题推荐分类"""
        title_lower = item.title.lower()
        tags_lower = [t.lower() for t in item.tags]
        
        # 职业相关
        if any(k in title_lower or k in tags_lower for k in ['career', 'job', '职业', '工作', 'salary', '薪资']):
            return "entities/career-development (merge)"
            
        # 财务相关
        if any(k in title_lower or k in tags_lower for k in ['finance', 'money', '财务', '投资', 'saving']):
            return "entities/personal-finance (merge)"
            
        # 关系相关
        if any(k in title_lower or k in tags_lower for k in ['relationship', 'communication', '关系', '沟通', 'marriage']):
            return "entities/relationship-maintenance (merge)"
            
        # 习惯相关
        if any(k in title_lower or k in tags_lower for k in ['habit', 'routine', '习惯', '举止']):
            return "entities/habit-building-system (merge)"
            
        # 决策相关
        if any(k in title_lower or k in tags_lower for k in ['decision', 'framework', '决策', '框架']):
            return "entities/decision-frameworks (merge)"
            
        # 默认建议新建 entity
        return "raw/articles/ (archive)"
    
    def generate_report(self, items: List[InboxItem]) -> str:
        """生成扫描报告"""
        lines = []
        lines.append("# Inbox 扫描报告")
        lines.append(f"\n生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"发现项目: {len(items)}")
        lines.append("\n---\n")
        
        if not items:
            lines.append("✅ 没有待处理的 inbox 项目")
            return "\n".join(lines)
        
        for i, item in enumerate(items, 1):
            is_dup = self._check_duplicate(item)
            suggestion = self._suggest_category(item)
            
            lines.append(f"## {i}. {item.title}")
            lines.append(f"- **文件**: `{item.path.name}`")
            lines.append(f"- **类型**: {item.source_type}")
            lines.append(f"- **标签**: {', '.join(item.tags) if item.tags else '无'}")
            lines.append(f"- **重复检查**: {'⚠️ 可能重复' if is_dup else '✅ 未发现重复'}")
            lines.append(f"- **入库建议**: {suggestion}")
            
            if is_dup:
                lines.append("- **操作**: 检查现有实体，如内容重叠度高则 merge，否则独立库")
            else:
                lines.append("- **操作**: 使用 `web-content-reviewer` 评估质量后入库")
            
            lines.append("")
        
        lines.append("---\n")
        lines.append("## 入库流程")
        lines.append("1. 使用 `skill_view('wiki-pipeline')` 查看完整流程")
        lines.append("2. 使用 `web-content-reviewer` 评估文章质量 (v×c ≥ 45)")
        lines.append("3. 符合标准则移动到 raw/articles/ 并更新前置 metadata")
        lines.append("4. 更新相关 entity 或创建新 entity")
        lines.append("5. 从 inbox 删除原文件")
        
        return "\n".join(lines)
    
    def run(self, output_file: Optional[Path] = None):
        """运行完整扫描流程"""
        print(f"🔍 扫描 inbox: {self.inbox_dir}")
        
        items = self.scan()
        report = self.generate_report(items)
        
        # 保存报告
        if output_file is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = self.wiki_root / "scripts" / f"inbox_report_{timestamp}.md"
        
        output_file.write_text(report, encoding='utf-8')
        print(f"📝 报告已保存: {output_file}")
        
        # 输出摘要
        print(f"\n摘要:")
        print(f"  总项目: {len(items)}")
        dups = sum(1 for item in items if self._check_duplicate(item))
        print(f"  可能重复: {dups}")
        print(f"  新项目: {len(items) - dups}")
        
        return items

def main():
    # 确定 wiki 根目录
    script_dir = Path(__file__).parent
    wiki_root = script_dir.parent
    
    scanner = InboxScanner(wiki_root)
    scanner.run()

if __name__ == "__main__":
    main()
