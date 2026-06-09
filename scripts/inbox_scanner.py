#!/usr/bin/env python3
"""
wiki-life inbox scanner - 自动扫描外部内容并导入inbox
支持: RSS feeds, WeChat MP RSS, 本地新闻稿件目录监控

Usage:
    python inbox_scanner.py [--dry-run]
"""

import os
import sys
import yaml
import json
import hashlib
import argparse
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
import feedparser
import requests

# 配置
WIKI_ROOT = Path.home() / "wiki-life"
INBOX_DIRS = {
    'rss': WIKI_ROOT / "raw/inbox/rss",
    'wechat': WIKI_ROOT / "raw/inbox/wechat",
    'newsletter': WIKI_ROOT / "raw/inbox/newsletter",
}
SOURCES_FILE = WIKI_ROOT / "SOURCES.md"
LOG_FILE = WIKI_ROOT / "scripts/scan_log.json"

def load_sources():
    """从SOURCES.md解析数据源配置"""
    # 简化实现: 仅支持已配置的RSS feeds
    # 完整实现需要解析YAML前置数据
    rss_feeds = [
        "https://zenhabits.net/feed/",
        "https://jamesclear.com/feed",
        "https://fs.blog/feed/",
        "https://markmanson.net/feed",
        "https://www.thesimpledollar.com/feed/",
        "https://waitbutwhy.com/feed",
    ]
    return {'rss': rss_feeds}

def sanitize_filename(title):
    """将标题转换为安全的文件名"""
    # 移除特殊字符，限制长度
    safe = "".join(c if c.isalnum() or c in "-_ " else "_" for c in title)
    return safe[:80].strip()

def generate_sha256(url, title):
    """生成文章SHA256 hash用于去重"""
    content = f"{url}:{title}".encode('utf-8')
    return hashlib.sha256(content).hexdigest()[:16]

def check_duplicate(sha256_hash):
    """检查是否已存在"""
    # 检查raw/articles/下的文件
    articles_dir = WIKI_ROOT / "raw/articles"
    for article in articles_dir.glob("*.md"):
        content = article.read_text(encoding='utf-8')
        if sha256_hash in content:
            return True
    # 检查inbox中的文件
    for inbox_dir in INBOX_DIRS.values():
        for item in inbox_dir.glob("*.md"):
            content = item.read_text(encoding='utf-8')
            if sha256_hash in content:
                return True
    return False

def fetch_rss_feed(url):
    """获取RSS feed"""
    try:
        feed = feedparser.parse(url)
        return feed.entries
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def create_inbox_item(title, url, source_type, pub_date=None, summary=None):
    """创建inbox文件"""
    sha256 = generate_sha256(url, title)
    filename = f"{datetime.now().strftime('%Y%m%d')}_{sanitize_filename(title)}.md"
    
    content = f"""---
title: "{title}"
created: {datetime.now().strftime('%Y-%m-%d')}
updated: {datetime.now().strftime('%Y-%m-%d')}
type: inbox
tags: [inbox, {source_type}, pending-review]
source_url: "{url}"
ingested: {datetime.now().strftime('%Y-%m-%d')}
sha256: "{sha256}"
provenance_state: "inbox"
---

# {title}

**来源**: {url}
**收集日期**: {datetime.now().strftime('%Y-%m-%d')}
**状态**: 待审核

---

## 摘要

{summary or '暂无摘要'}

---

## 内容

待提取...

---

## 审核清单

- [ ] 是否为鸡汤/软文/营销号？
- [ ] 是否有论证/框架/边界/实践/批判性？
- [ ] v×c 是否 ≥ 45？
- [ ] 是否需要归档到raw/articles/？

---

**SHA256**: `{sha256}`
"""
    
    return filename, content

def scan_rss_feeds(dry_run=False):
    """扫描RSS feeds"""
    sources = load_sources()
    new_items = []
    
    print(f"Scanning {len(sources['rss'])} RSS feeds...")
    
    for feed_url in sources['rss']:
        print(f"  Checking: {feed_url}")
        entries = fetch_rss_feed(feed_url)
        
        for entry in entries[:5]:  # 每个feed最多处理5篇新文章
            title = entry.get('title', 'Untitled')
            url = entry.get('link', '')
            summary = entry.get('summary', '')[:500]  # 限制摘要长度
            
            sha256 = generate_sha256(url, title)
            
            if check_duplicate(sha256):
                print(f"    ⏭️  SKIP (exists): {title[:60]}...")
                continue
            
            filename, content = create_inbox_item(
                title=title,
                url=url,
                source_type='rss',
                summary=summary
            )
            
            if not dry_run:
                inbox_path = INBOX_DIRS['rss'] / filename
                inbox_path.write_text(content, encoding='utf-8')
                new_items.append({
                    'file': str(inbox_path),
                    'title': title,
                    'source': feed_url
                })
                print(f"    ✅ ADD: {title[:60]}...")
            else:
                print(f"    [DRY-RUN] Would add: {title[:60]}...")
                new_items.append({
                    'title': title,
                    'source': feed_url
                })
    
    return new_items

def generate_report(new_items, dry_run=False):
    """生成扫描报告"""
    report = f"""# Inbox扫描报告

**扫描时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**新增项目**: {len(new_items)}
**模式**: {'测试模式(不保存)' if dry_run else '正式模式'}

---

## 新增内容

"""
    
    for item in new_items:
        report += f"- {item['title']}\n"
        if 'file' in item:
            report += f"  - 文件: `{item['file']}`\n"
    
    if not new_items:
        report += "*未发现新内容*\n"
    
    report += f"""

---

## 下一步

1. 审核inbox中的内容
2. 对高质量内容执行 `scripts/promote_to_article.py`
3. 执行 `git add . && git commit -m "ingest batch N: description"`

*自动生成于: inbox_scanner.py*
"""
    
    return report

def main():
    parser = argparse.ArgumentParser(description='Scan external sources and populate inbox')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without saving')
    args = parser.parse_args()
    
    # 确保目录存在
    for dir_path in INBOX_DIRS.values():
        dir_path.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("wiki-life inbox scanner")
    print("=" * 60)
    
    # 扫描RSS
    new_items = scan_rss_feeds(dry_run=args.dry_run)
    
    # 生成报告
    report = generate_report(new_items, dry_run=args.dry_run)
    
    # 保存报告
    report_path = WIKI_ROOT / f"scripts/scan_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    if not args.dry_run and new_items:
        report_path.write_text(report, encoding='utf-8')
        print(f"\n报告已保存: {report_path}")
    
    print(f"\n批次完成: 发现 {len(new_items)} 项新内容")
    print("=" * 60)
    
    return 0 if not args.dry_run or new_items else 1

if __name__ == "__main__":
    sys.exit(main())
