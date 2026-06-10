---
title: "Week 3-4 详细学习计划：Agent框架实战"
created: 2025-06-10
updated: 2025-06-10
type: guide
tags: [learning, agent, langchain, week-plan, actionable]
confidence: 0.85
provenance_state: "extracted"
---

# Week 3-4 详细学习计划：Agent框架实战

**目标**：掌握主流Agent框架，产出2个可展示的项目
**时间投入**：每天3小时（工作日2h + 周末4h）
**产出**：GitHub 2个Repo + 1篇技术博客

---

## 📅 Week 3：LangChain/LangGraph 深度实践

### Day 1-2：LangChain基础（6h）

**上午（2h）：核心概念**
- [ ] 阅读LangChain官方文档Architecture部分
- [ ] 理解Chain、Agent、Tool的概念层次
- [ ] 掌握PromptTemplate和OutputParser

**实践任务**：
```python
# 必做：实现基础的LLMChain
from langchain import OpenAI, PromptTemplate, LLMChain

# 任务：创建一个能回答技术问题的简单Chain
# 要求：包含System Prompt + User Input + 格式化输出
```

**下午/晚上（2h）：工具调用**
- [ ] 学习@tool装饰器
- [ ] 集成Search API（SerpAPI/Tavily）
- [ ] 实现Calculator工具

**产出检查**：
- [ ] 能运行一个带工具调用的Agent
- [ ] 理解`agent_scratchpad`的作用

---

### Day 3-4：ReAct Agent实现（6h）

**上午（2h）：理论学习**
- [ ] 精读ReAct论文（Reasoning + Acting）
- [ ] 理解 Thought → Action → Observation 循环
- [ ] 对比CoT、ReAct、Reflexion的区别

**下午（2h）：代码实现**
```python
# 必做：从零实现简化版ReAct Agent
# 不依赖LangChain的Agent类，自己实现循环逻辑

class ReActAgent:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools
    
    def run(self, query, max_steps=5):
        # 实现思考-行动-观察循环
        pass
```

**晚上（2h）：调试与优化**
- [ ] 处理工具调用失败的情况
- [ ] 实现重试机制
- [ ] 添加日志和可视化（看Agent怎么思考）

**产出检查**：
- [ ] GitHub提交：react-agent-from-scratch
- [ ] README包含架构图和运行示例

---

### Day 5-6：LangGraph状态机（6h）

**上午（2h）：图论基础**
- [ ] 理解StateGraph概念
- [ ] 学习Node、Edge、Conditional Edge
- [ ] 掌握State管理

**下午（2h）：多Agent系统**
```python
# 必做：实现多角色协作系统
# 例如：Researcher → Writer → Editor

from langgraph.graph import StateGraph

# 定义三个Agent节点
# 实现条件路由（Editor决定是否通过）
# 添加循环（如果不通过，返回Writer）
```

**晚上（2h）：持久化与记忆**
- [ ] 集成Memory（短期+长期）
- [ ] 实现Checkpointer
- [ ] 支持人机交互（Human-in-the-loop）

**产出检查**：
- [ ] 能运行一个多步骤工作流
- [ ] 理解状态如何在节点间传递

---

### Day 7：Week 3总结（4h）

**上午（2h）：项目完善**
- [ ] 整理本周代码
- [ ] 写单元测试
- [ ] 优化README

**下午（2h）：技术博客**
- [ ] 写一篇《从零实现ReAct Agent》
- [ ] 包含：原理、代码、踩坑记录
- [ ] 发布到GitHub或知乎/掘金

---

## 📅 Week 4：AutoGen/CrewAI + 项目实战

### Day 1-2：AutoGen多Agent协作（6h）

**上午（2h）：AutoGen架构**
- [ ] 理解ConversableAgent
- [ ] 学习UserProxyAgent和AssistantAgent
- [ ] 掌握GroupChat机制

**实践任务**：
```python
# 必做：模拟软件开发团队
# PM Agent：明确需求
# Architect Agent：设计架构
# Developer Agent：写代码
# Reviewer Agent：Code Review

# 要求：能完成一个简单功能（如计算器）的完整流程
```

**下午/晚上（2h）：高级特性**
- [ ] 实现自定义Agent（继承并重写方法）
- [ ] 添加代码执行环境（DockerContainer）
- [ ] 实现函数调用（Function Calling）

**产出检查**：
- [ ] 运行一个4-Agent协作系统
- [ ] 观察并记录Agent间的对话

---

### Day 3-4：项目1 - 代码审查Agent（6h）

**需求定义**：
- 输入：Pull Request的代码diff
- 输出：代码审查意见（风格、潜在bug、优化建议）
- 技术：RAG（加载团队规范）+ LLM分析

**实现步骤**：

Day 3上午（2h）：基础架构
```python
# 1. 加载代码和上下文
# 2. 解析diff（使用git库）
# 3. 设计审查Prompt
```

Day 3下午（2h）：RAG集成
```python
# 1. 加载团队代码规范（向量化）
# 2. 检索相关规范
# 3. 生成个性化审查意见
```

Day 4上午（2h）：多Agent协作
```python
# 1. Style Checker Agent
# 2. Bug Finder Agent
# 3. Performance Agent
# 4. Summarizer Agent

# 输出：结构化的审查报告
```

Day 4下午（2h）：测试与部署
- [ ] 用真实PR测试
- [ ] 添加GitHub Webhook支持
- [ ] 写Dockerfile

**产出检查**：
- [ ] GitHub Repo：code-review-agent
- [ ] 包含：Demo视频、架构图、使用说明

---

### Day 5-6：项目2 - 数据分析Agent（6h）

**需求定义**：
- 输入：自然语言查询（如"分析Q3销售趋势"）
- 输出：数据可视化 + 洞察报告
- 技术：Pandas + LLM + Plotly

**实现步骤**：

Day 5上午（2h）：数据接口
```python
# 1. 连接数据源（CSV/DB/API）
# 2. 实现Schema提取
# 3. 生成SQL/Pandas代码
```

Day 5下午（2h）：分析工作流
```python
# 1. Planner Agent：规划分析步骤
# 2. Coder Agent：生成分析代码
# 3. Executor Agent：安全执行（沙箱）
# 4. Reporter Agent：生成报告
```

Day 6上午（2h）：可视化
- [ ] 集成Plotly/Matplotlib
- [ ] 实现图表生成
- [ ] 添加交互功能

Day 6下午（2h）：优化与文档
- [ ] 处理执行错误
- [ ] 添加示例数据集
- [ ] 完善README

**产出检查**：
- [ ] GitHub Repo：data-analyst-agent
- [ ] 支持至少3种图表类型
- [ ] 有在线Demo或GIF演示

---

### Day 7：Week 4总结（4h）

**上午（2h）：代码整理**
- [ ] 统一代码风格（Black格式化）
- [ ] 添加类型提示
- [ ] 完善错误处理

**下午（2h）：简历更新**
- [ ] 更新GitHub Profile
- [ ] 简历添加2个项目
- [ ] 准备项目介绍（STAR法则）

---

## 🛠️ 开发环境配置

### 必装工具
```bash
# Python环境
python -m venv agent-env
source agent-env/bin/activate

# 核心库
pip install langchain langgraph openai
pip install chromadb tiktoken
pip install pandas plotly

# 开发工具
pip install black isort pytest
pip install jupyter notebook

# 可选
pip install autogen crewai
```

### 推荐的IDE配置
- **VSCode** + Python插件
- **Cursor**（AI辅助编程，提高效率）
- **GitHub Copilot**（代码补全）

### API密钥管理
```python
# 使用.env文件
# 永远不要提交密钥到GitHub

from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
```

---

## 📊 每日检查清单

### Morning（开始工作前）
- [ ] 回顾昨日进度
- [ ] 明确今日3个核心任务
- [ ] 设置番茄钟（25分钟专注）

### Work Session（每个2h块）
- [ ] 关闭手机通知
- [ ] 只保留必要标签页
- [ ] 遇到卡住 >30分钟，先跳过或查文档

### Evening（结束前）
- [ ] 提交代码到GitHub
- [ ] 记录今日完成和明日计划
- [ ] 更新学习进度表

---

## 🎯 Week 3-4 成功标准

### 必须完成
- [ ] 2个完整的Agent项目（GitHub）
- [ ] 1篇技术博客
- [ ] 能解释ReAct原理和代码实现
- [ ] 能设计多Agent协作架构

### 加分项
- [ ] 项目获得Star或Issue反馈
- [ ] 博客阅读量 >1000
- [ ] 实现一个创新功能（非教程示例）
- [ ] 性能优化（延迟降低50%）

---

## 🆘 常见问题解决

### "代码跑不通"
1. 检查Python版本（推荐3.9+）
2. 确认所有依赖安装
3. 看错误信息，Google前3条结果
4. 去LangChain GitHub Issues搜索

### "不知道写什么项目"
1. 解决自己的痛点（自动化重复工作）
2. 复现经典论文（ReAct、AutoGPT）
3. 改进现有工具（加个AI功能）

### "时间不够用"
1. 降低范围：先完成MVP，再优化
2. 使用Cursor/Copilot加速编码
3. 周末加班补进度

---

## 📚 参考资源

### 官方文档
- [LangChain文档](https://python.langchain.com/)
- [LangGraph教程](https://langchain-ai.github.io/langgraph/)
- [AutoGen文档](https://microsoft.github.io/autogen/)

### 推荐教程
- [[raw/articles/deep-work-cal-newport|Deep Work]] - 专注学习方法
- [[entities/cognitive-enhancement|认知提升]] - 高效学习策略

### 社区
- LangChain Discord
- AutoGen GitHub Discussions
- 知乎Agent话题

---

准备好开始这2周的密集训练了吗？记住：**完成比完美重要**。

**v×c = 72** (value=8 × confidence=0.9)

← 返回 [[queries/agent-engineer-interview-prep|面试准备指南]] | [[queries/life-dashboard|Life Dashboard]]
