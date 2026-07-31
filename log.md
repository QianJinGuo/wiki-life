# Wiki Operation Log

Format: `## [YYYY-MM-DD] action | subject`

---

## [2025-06-09] init | wiki-life created

Initialized life improvement wiki with structure:
- 5 core areas: 自律, 职业发展, 心理健康, 亲密关系, 认知提升
- Directory: entities/, concepts/, comparisons/, queries/, raw/
- Scoring threshold: v×c ≥ 45 (adjusted for subjective content)

## [2025-06-09] ingest | 3 articles + 8 synthesis pages | Total 11 pages

**Batch 1 - 决策框架**:
1. musk-first-principles-thinking-framework.md | v×c=72
2. tim-cook-operational-excellence-framework.md | v×c=66  
3. jensen-huang-decision-framework.md | v×c=70
4. concepts/first-principles-thinking.md | 概念定义页
5. entities/decision-frameworks.md | 综合对比页

**Batch 2 - 生活系统**:
6. queries/actionable-methods.md | 可执行方法汇总(query)
7. entities/habit-building-system.md | 习惯回路+环境设计(v×c=68)
8. entities/self-discipline.md | 意志力管理+系统设计(v×c=66)
9. entities/career-development.md | 职业三维度+求职系统(v×c=68)
10. entities/mental-wellness.md | CBT+ACT+MBSR实证方法(v×c=66)

**Quality**: 所有内容通过五维验证(论证/框架/边界/实践/批判性)
**Template**: 3个复用模板(article-note/concept-page/weekly-review)

**Batch 3 - 表达/关系/认知/财务**:
11. entities/communication-skills.md | SCQA+STAR-L+PREP (v×c=68)
12. entities/relationship-maintenance.md | 爱的语言+NVC+戈特曼法则 (v×c=70)
13. entities/cognitive-enhancement.md | 费曼法+二阶思维+故意练习 (v×c=69)
14. entities/personal-finance.md | 四维度健康+MPT+储蓄框架 (v×c=67)

**Total**: 16 pages | 9 entities | 1 concept | 3 queries | 3 sources

**Batch 4 - 时间/健康/创造力**:
15. entities/time-management-system.md | GTD+时间块+深度工作 (v×c=69)
16. entities/health-optimization-system.md | 睡眠+营养+运动三支柱 (v×c=70)
17. entities/creativity-system.md | 设计思维+CPS+头脑风暴 (v×c=71)

**Final Total**: 19 pages | 12 entities | 1 concept | 3 queries | 3 sources

添加模板: templates/daily-plan-example.md | 基于时间块的高效一天完整模板

**Final Total v1.1**: 20 pages | 12 entities | 1 concept | 4 templates | 3 sources

## [2026-06-11] structure | SCHEMA.md + moc/ + drafts/ 创建（9 步法 P0 对齐）

按 hermes-wiki-9-step-auto-growing-knowledge-network 方法论补齐三件套：
- **SCHEMA.md**：独立 schema 契约文件（之前 AGENTS.md/QUALITY.md 混合承担），明确 frontmatter / type / tag taxonomy / 评分门槛 v×c≥45 / 7 类红线
- **moc/**：新建主题地图层
  - `moc/personal-growth-reading-path.md`：12 entity 的 4 层阅读路径（地基→习惯→系统→高阶）
  - `moc/wiki-life-master-map.md`：总入口 MOC（按"读什么/问什么"分流）
- **drafts/**：新建对外输出层
  - `drafts/README.md`：使用规范 + 5 个推荐选题（从 12 entity 反向蒸馏）

**Total**: 12 entities | 4 concepts | 7 queries | 2 moc | 0 drafts (待写) | 3 raw


## [2026-07-02] ingest | easy-is-overrated

自动入库 (wiki-life-inbox-scan + life-screener)
- **标题**: Easy is Overrated
- **评分**: v×c=8×8=64 | stars=4
- **来源**: https://calnewport.com/easy-is-overrated/
- **理由**: 命中论证、批判性、实践三维；引用《Organization Science》任务组数据，逻辑推理清晰，无鸡汤/营销红线


## [2026-07-04] ingest | https-pradyuprasadcom-writings-how-to-ask-for-help

自动入库 (wiki-life-inbox-scan + life-screener)
- **标题**: https://pradyuprasad.com/writings/how-to-ask-for-help/
- **评分**: v×c=7×7=49 | stars=4
- **来源**: https://pradyuprasad.com/writings/how-to-ask-for-help/
- **理由**: 命中论证（核心原则+启发式框架）、边界（区分三种可信度来源）、实践（具体操作建议）三维；未触发红线，基于逻辑推理与个人经验，非鸡汤/营销


## [2026-07-09] ingest | career-advice-age-of-agents

自动入库 (wiki-life-inbox-scan + life-screener)
- **标题**: Career Advice in the Age of AI Agents
- **评分**: v×c=8×7=56 | stars=4
- **来源**: https://addyosmani.com/blog/career-advice-age-of-agents/
- **理由**: 命中论证(稀缺性框架)、边界(区分AI能力边界)、实践(个人经历佐证)、批判性(质疑传统职业路径)四维；无红线触发，属于有效方法类内容


## [2026-07-27] ingest | https-fsblog-great-talks-common-denominator-success-albert-g

自动入库 (wiki-life-inbox-scan + life-screener)
- **标题**: https://fs.blog/great-talks/common-denominator-success-albert-gray/
- **评分**: v×c=8×6=48 | stars=4
- **来源**: https://fs.blog/great-talks/common-denominator-success-albert-gray/
- **理由**: 论证、框架、边界、实践四维满足；无红线


## [2026-07-28] create | comparison-trap-anxiety + agent-learning-under-anxiety

手动创建（用户触发）
- **标题1**: 比较陷阱与焦虑：当同龄人领先时的实操应对
- **标题2**: 焦虑状态下的技术学习法：以 Agent/Harness 为例
- **理由**: 用户表达比较焦虑 + 学习焦虑，创建两篇实操框架页：五步焦虑应对框架 + 锚点学习法
