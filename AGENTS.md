# AGENTS.md — Agent Instructions for Life Wiki

This file provides operational guidance to AI agents when editing this personal development wiki.

## What This Repo Is

An Obsidian-style life improvement wiki in Chinese. Focus areas:
- **自律 & 习惯养成** — 时间管理、意志力、行为设计
- **职业发展** — 求职策略、面试技巧、职业规划、副业探索
- **心理健康** — 情绪管理、焦虑应对、正念、心态建设
- **亲密关系** — 夫妻沟通、冲突解决、亲密关系维护
- **认知提升** — 学习方法、决策思维、元认知

A Markdown knowledge base — no build step.

## Content Workflow

Every change follows this lifecycle:

1. **Ingest** — save source in `raw/articles/` with raw-source frontmatter
2. **Synthesize** — create or update pages in `entities/`, `concepts/`, or `comparisons/`
3. **Index** — add entries in `index.md` under the correct section
4. **Log** — append to `log.md` using `## [YYYY-MM-DD] action | subject`
5. **Validate** — verify frontmatter integrity

## Directory Structure

```
wiki-life/
├── raw/
│   ├── articles/        # Approved ingested sources
│   └── inbox/           # Pending review
│       ├── rss/         # RSS feeds
│       ├── wechat/      # WeChat articles
│       └── newsletter/  # Newsletter links
├── entities/            # Deep dives: topics, systems, frameworks
├── concepts/            # Core concepts, mental models
├── comparisons/         # Side-by-side method comparisons
├── queries/             # Navigation pages, reading lists
├── templates/           # Reusable templates
├── scripts/             # Utility scripts
├── index.md             # Master index
└── log.md               # Operation history
```

## Key Conventions

- **File names**: lowercase, hyphens, no spaces
  - Good: `concepts/nonviolent-communication.md`
  - Avoid: `concepts/Nonviolent Communication.md`

- **Frontmatter** (every page):
```yaml
---
title: "中文标题"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity|concept|comparison|query|source
tags: [tag1, tag2]
---
```

- **Type definitions**:
  - `entity`: 深度主题页 (如 [[entities/self-discipline|自律系统]])
  - `concept`: 核心概念定义 (如 [[concepts/delayed-gratification|延迟满足]])
  - `comparison`: 方法对比 (如 [[comparisons/pomodoro-vs-timeblocking|番茄法vs时间块]])
  - `query`: 导航/清单页 (如 [[queries/job-search-toolkit|求职工具箱]])
  - `source`: 原始文章存档 (in `raw/articles/`)

- **Wikilinks**: `[[path/slug|显示文本]]` — always include subdirectory prefix

- **Tag taxonomy** (core tags):
  - 领域: `#self-discipline`, `#career`, `#mental-health`, `#relationship`, `#cognition`
  - 类型: `#article`, `#study`, `#tool`, `#template`, `#case`
  - 可操作性: `#actionable`, `#framework`, `#reflection`

- **Source attribution**:
  - Every prose paragraph should end with citation: `^[raw/articles/slug.md]`
  - Ingested articles get `sha256` in frontmatter for deduplication

## Scoring & Ingestion Threshold

Life content is more subjective than tech. Adjusted thresholds:

| Metric | Threshold | Notes |
|--------|-----------|-------|
| Value × Confidence | ≥ 45 | (vs 49 in tech wiki) |
| Actionability | 独特方法/工具/模板可破格 | |
| Personal insight | 反常识经验、真实案例可破格 | |

Reject criteria:
- 鸡汤文 (空泛无具体方法)
- 与已有内容重复且无新视角
- 纯情绪宣泄无结构化洞察

## Maintenance

- **index.md**: Update count after batch ingestion
- **log.md**: Rotate when > 500 lines
- **Orphan pages**: Run periodic link validation
- **Template sync**: Update templates/ when new patterns emerge
