---
title: Wiki-Life Schema
created: 2026-06-11
updated: 2026-06-11
type: schema
tags: [meta]
---

# Wiki-Life Schema

> 个人成长 wiki 的结构契约。本文件定义"什么样的页面/字段/链接是合法的"，QUALITY.md 定义"什么样的内容值得入库"，AGENTS.md 定义"操作流程"。三者互补。

## Domain

个人成长、自律、职业发展、心理健康、亲密关系、认知提升、财务、沟通技巧。

**与 ~/wiki（AI/ML 研究）分离**：所有技术/工程类内容仍归 ~/wiki，本库不接收技术主题。

## Conventions

- 文件名：lowercase, hyphens, no spaces（如 `nonviolent-communication.md`）
- 每个 wiki 页面以 YAML frontmatter 开头
- 使用 `[[subdir/page-slug]]` 格式做内链，**每页最少 2 条出链**（不包含 raw/ 来源）
- 每个 entity/concept 页面应包含 `→ [[raw/articles/xxx|原文存档]]` 回链到来源
- 更新页面时必须 bump `updated` 日期
- 新页面必须加入 `index.md` 对应章节
- 每次重要操作必须 append 到 `log.md`
- **Provenance 标记**：合成 3+ 来源的页面，在段落末尾追加 `^[raw/articles/source.md]`
- `confidence` 字段对主观性强、争议大的主题强烈推荐
- 评分门槛：`review_value × review_confidence ≥ 45`（生活内容比技术内容低 4 分）

## Frontmatter

### Standard fields (所有页面)

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | case | review
tags: [from taxonomy below]
sources: [raw/articles/source-name]     # omit .md extension
confidence: high | medium | low         # 推荐，主观/争议内容必填
provenance_state: extracted | merged | inferred | ambiguous   # optional
contradicted_by: [other-page-slug]      # optional
---
```

### Review metadata (scored-review workflows only)

```yaml
review_value: 8            # 0-10
review_confidence: 7       # 0-10
review_recommendation: strong | worth-reading | reference
review_stars: 4            # 1-5
```

**评分规范化**：
- `value ≥ 9` 且 `confidence ≥ 8` → strong + 5 星
- `value ≥ 8` 且 `confidence ≥ 7` → strong + 4 星
- 保留但低于 strong → worth-reading + 3 星
- 参考性内容 → reference + 1-2 星

**保存门槛**：`review_value × review_confidence ≥ 45`（低于此值默认不入库，除非有明确独特价值）。

### Raw source frontmatter

```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest>        # body-content SHA-256，frontmatter 剥离后计算
---
```

## Page Types

| 目录 | 角色 | 写入规则 |
|------|------|---------|
| `raw/articles/` | 证据层（已通过评分） | 只追加只读，不修改原文 |
| `raw/inbox/` | 候选区（待审） | 自动抓取，14 天未 promote 自动清理 |
| `entities/` | 实体页（系统/方法论/人物） | 跨多份资料沉淀的实践框架 |
| `concepts/` | 概念页（认知模型/心智模型） | 跨多份资料抽象的可复用心智工具 |
| `comparisons/` | 对照页（方法论对比） | 长期更新，每次新资料补充新维度 |
| `queries/` | 高价值问答 + 导航页 | 解决重要问题/给出阅读路径才沉淀 |
| `cases/` | 真实案例（个人/他人） | 用于验证 / 反驳 entity 中的方法论 |
| `reviews/` | 复盘页（实践后的反馈） | 闭环：方法论 → 案例 → 复盘 |
| `moc/` | 主题地图（Map of Content） | 阅读顺序地图（"先读 X 再读 Y"），不是清单 |
| `drafts/` | 对外输出草稿 | 知识库的终局是输出，不是收藏 |

**关键分层信条**：
- `raw/` 坏了后面全乱 — 只追加只读
- `concepts/` 不是文章摘要 — 是可被反复引用的抽象
- `concepts/` 和 `entities/` 必须分开 — 否则术语/工具/系统全混
- `moc/` 是阅读路线，不是目录
- `drafts/` 强制"输出闭环" — 没产出的知识等于没学

## Tag Taxonomy

### 主题分类
- **自律领域**：habit, willpower, time-management, self-discipline, energy-management
- **认知领域**：mental-model, decision-making, cognitive-bias, learning-method, meta-cognition
- **心理领域**：emotion-regulation, anxiety, mindfulness, cbt, act, mbsr, mental-health
- **关系领域**：communication, nvc, conflict-resolution, intimacy, family
- **职业领域**：career, interview, job-search, skill-development, side-project
- **财务领域**：personal-finance, investment, frugality, financial-independence

### 内容类型
- **类型标签**：framework, method, system, principle, research, case-study, anti-pattern
- **可信度标签**：evidence-based, experimental, anecdotal, popular-belief
- **来源标签**：book, paper, blog, podcast, interview, course

**禁用标签**：评分（star-3 / score-72 等）—— 评分走 frontmatter 字段，不进 tag。

## Page Thresholds

- 在 2+ 来源出现 OR 单一来源中处于核心地位 → 创建独立页
- 仅顺带提及或细枝末节 → 不创建页
- 单页超 ~200 行 → 拆分

## Quality Red Lines（与 QUALITY.md 联动）

以下 7 类内容**禁止入库**（详见 QUALITY.md）：
1. 鸡汤文 — 只有情绪起伏没有认知增量
2. 毒鸡汤 — 单因归因 + 制造焦虑
3. 软文/营销文 — 故事铺垫后推销
4. 营销号 — 所有内容都是导流入口
5. 标题党 — 标题与正文不符
6. 投射文 — N=1 经验当普适真理
7. 复读机 — 重复市面常识无新洞察

## Validation

- 结构性修改后运行 lint（如有 lint 脚本）
- 验证：index 计数 / frontmatter 完整性 / 内链有效性 / raw source hash / review metadata 范围
- 活跃页面集：`entities/`, `concepts/`, `comparisons/`, `queries/`, `cases/`, `reviews/`, `moc/`, `drafts/`, `raw/articles/`
- 操作目录不入 index：`raw/inbox/`, `scripts/`, `templates/`, `_archive/`, 编辑器/运行时元数据

## Update Policy

新信息与已有内容冲突时：
1. 检查日期 — 新源通常 supersede 老源
2. 如真有矛盾，并列两种立场 + 日期 + 来源
3. frontmatter 标记：`contradicted_by: [page-name]`
4. 必要时升级到 `comparisons/` 做长期对比页

## 与 ~/wiki（AI/ML）的差异

| 维度 | ~/wiki | ~/wiki-life |
|------|--------|-------------|
| 评分门槛 | v×c ≥ 49 | v×c ≥ 45 |
| 核心领域 | AI/ML 研究、Agent 技术 | 个人成长、生活系统 |
| 内容性质 | 客观技术 + 工程实践 | 主观经验 + 实证方法 |
| 红线 | 失实/无效技术声明 | 鸡汤/软文/广告/营销号 |
| 长期更新 | 跟随技术演化 | 跟随个人实践复盘 |
