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

### 【强制】Reject 红线 — 拒绝所有此类内容

以下类型 **无条件拒绝**，不论包装得多好：

| 类型 | 特征 | 典型词汇 |
|------|------|---------|
| 鸡汤文 | 空泛正能量、无具体方法 | "加油你最棒"、"要相信自己"、"努力就会成功" |
| 毒鸡汤 | 过度简化、归因偏差 | "穷是因为你不努力"、"有问题从自己身上找原因" |
| 软文/营销文 | 故事包装产品/服务 | 故事前面很长，突然转到某产品/课程 |
| 营销号 | 内容全是卖课/咨询广告 | 每篇都引导加微信、限时优惠、错过等一年 |
| 标题党 | 标题很炸、内容很水 | "我靠XX年薪百万"、"这才是真正的自律" |
| 投射文 | 把个人特殊经历普适化 | "我这么做成功了，你也可以" |
| 情绪包 | 刺激情绪、无信息量 | 纯发泄、纯感动、纯安慰、贩卖焦虑 |

### 高质量内容的 5 个特征

必须满足至少 2 项才能入库：

1. **有论证** — 引用研究、数据或清晰的逻辑推理
2. **有框架** — 可复制的方法论，不是个人感悟
3. **有边界** — 明确说明"这适合什么情况/不适合什么情况"
4. **有实践** — 具体步骤、工具、模板，拿来即用
5. **有批判性** — 承认局限性，不是绝对化断言

### 快速识别测试

阅读前问 3 个问题：
1. 这篇文章的核心论点是什么？能用一句话概括吗？
2. 作者提供了什么证据支持这个论点？
3. 我能从今天开始做什么具体的事情？

如果答不出来 → **Reject**

## Maintenance

- **index.md**: Update count after batch ingestion
- **log.md**: Rotate when > 500 lines
- **Orphan pages**: Run periodic link validation
- **Template sync**: Update templates/ when new patterns emerge
