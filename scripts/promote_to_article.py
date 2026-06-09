#!/usr/bin/env python3
"""
将inbox内容导入到raw/articles/
Usage:
    python promote_to_article.py <inbox_file_path>
"""

import sys
import re
import yaml
from pathlib import Path
from datetime import datetime

def extract_frontmatter(content):
    """提取YAML frontmatter"""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1)), content[match.end():]
        except:
            return None, content
    return None, content

def promote_inbox_item(inbox_path):
    """将inbox项目导入articles"""
    inbox_path = Path(inbox_path)
    if not inbox_path.exists():
        print(f"❌ 文件不存在: {inbox_path}")
        return False
    
    content = inbox_path.read_text(encoding='utf-8')
    frontmatter, body = extract_frontmatter(content)
    
    if not frontmatter:
        print(f"❌ 无法解析frontmatter: {inbox_path}")
        return False
    
    # 更新frontmatter
    frontmatter['type'] = 'source'
    frontmatter['updated'] = datetime.now().strftime('%Y-%m-%d')
    frontmatter['provenance_state'] = 'extracted'
    
    # 生成新文件名
    title = frontmatter.get('title', 'untitled')
    safe_title = "".join(c if c.isalnum() or c in "-_ " else "_" for c in title)[:50]
    
    # 检查tags确定分类
    tags = frontmatter.get('tags', [])
    
    # 生成新内容
    new_frontmatter = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False)
    new_content = f"""---
{new_frontmatter}---

# {title}

**来源**: {frontmatter.get('source_url', 'unknown')}
**归档日期**: {datetime.now().strftime('%Y-%m-%d')}

---

## 要点摘录

(待填充)

---

## 核心内容

{body}

---

## 评注

**v×c = ?** (待评分)

---

## 关联页面

- [[index|返回索引]]

*归档自: {inbox_path.name}*
"""
    
    # 保存到articles目录
    target_dir = Path.home() / "wiki-life/raw/articles"
    target_dir.mkdir(parents=True, exist_ok=True)
    
    target_path = target_dir / f"{safe_title}_{datetime.now().strftime('%Y%m%d')}.md"
    target_path.write_text(new_content, encoding='utf-8')
    
    # 移除或移动inbox文件
    inbox_path.unlink()
    
    print(f"✅ 已导入: {target_path}")
    print(f"   原inbox文件已移除")
    return True

def main():
    if len(sys.argv) < 2:
        print("使用方法: python promote_to_article.py <inbox_file_path>")
        print("例子: python promote_to_article.py ~/wiki-life/raw/inbox/rss/20250609_article.md")
        return 1
    
    inbox_file = sys.argv[1]
    success = promote_inbox_item(inbox_file)
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
