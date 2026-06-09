# 数据来源配置

本 wiki 的内容来源分三层：

---

## 第一层：自动抓取 (Inbox Pipeline)

定期运行的 cron job 自动收集到 `raw/inbox/`，待审核。

| 渠道 | 配置文件 | 执行频率 | 输出目录 |
|------|----------|----------|----------|
| RSS | `.rss-sources.yml` | 每 2h | `raw/inbox/rss/` |
| Newsletter | `.newsletter-sources.yml` | 每 4h | `raw/inbox/newsletter/` |
| 微信公众号 | `.wechat-sources.yml` | 每 2h | `raw/inbox/wechat/` |

### 审核流程

```
Inbox 文件 → web-content-reviewer 评分 → 合格(v×c≥45) → 正式入库
                ↓
            不合格 → 删除/归档
```

---

## 第二层：主动添加 (Manual Ingest)

遇到好内容时，直接使用 `manual-article-ingestion` skill：

```bash
# 例子：添加一篇文章
skill_view(name='manual-article-ingestion')
# 然后执行入库流程
```

或手动创建：

1. 保存原文到 `raw/articles/YYYY-MM-DD-slug.md`
2. 填充 frontmatter (url, sha256, tags)
3. 更新 `index.md`
4. 记录到 `log.md`

---

## 第三层：原创内容 (Original)

自己的思考、复盘、总结：

- 周复盘：`queries/weekly-review-YYYY-WXX.md`
- 读书笔记：直接创建 concept/entity 页
- 个人案例：`queries/case-studies.md`

---

## 推荐的起步内容源

### 立即开始 (0 配置)

1. **你收藏的文章** — 导出书签/收藏夹，批量入库
2. **书单** — 读过的个人成长书籍分章节整理
3. **你的经验** — 用周复盘模板记录真实案例

### 短期配置 (1-2 周)

1. **订阅 2-3 个高质 newsletter**
   - 中文: 《整理事情》《知识工厂》
   - 英文: James Clear, Mark Manson

2. **关注 5-10 个微信公众号**
   - 心理: KnowYourself, 宁远心理
   - 职业: 职场升值加
   - 习惯: 习惯君

### 长期运营 (1 个月后)

1. 配置 RSS 订阅 (zenhabits, James Clear 等)
2. 设置 cron job 自动化抓取
3. 建立审核 SOP

---

## 执行入库的命令

```bash
# 1. 手动单篇
hermes skill run manual-article-ingestion \
  --url "https://example.com/article" \
  --wiki ~/wiki-life

# 2. 批量扫描 inbox
cd ~/wiki-life && node scripts/inbox-scan.mjs

# 3. 验证状态
node scripts/wiki-lint.mjs ~/wiki-life
```

---

## 数据流向图

```
外部来源
    ┌─────────────┐
    │                │
RSS    Newsletter    微信公众号   手动输入
 │         │            │           │
 └───────┼──────────────┼────────────┴
          │
    raw/inbox/     <— 待审核
          │
          ▼
   web-content-reviewer 评分
          │
    ┌─────┼─────┐
    │      │      │
  合格   待定   拒绝
    │      │      │
    ▼      ▼      ▼
 raw/    raw/    删除/
articles/ inbox/   归档
 并更新     复审
entities/ 周期
concepts/
