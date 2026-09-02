# `references/workflow.md`

# Workflow Protocol

本文档定义 `aistar-director` 的项目生命周期、阶段状态、确认机制、版本控制、回退机制、需求变更、影响分析和用户覆盖行为。

本文件是整个 Skill 的**通用流程控制协议**。

其他模块不得自行定义与本文冲突的状态或确认逻辑。

---

# 1. Workflow 核心目标

`aistar-director` 的工作流必须同时满足：

1. **可控**：用户可以决定何时确认、修改、回退或暂停。
2. **可追踪**：任何产出都可以追溯到上游。
3. **可锁定**：已经确认的内容不会被后续阶段偷偷修改。
4. **可迭代**：用户可以针对局部内容修改，而无需整体重做。
5. **可回退**：发现上游问题时，可以返回必要阶段。
6. **可扩展**：后续可以加入新的生成模型或制作环节。
7. **高效率**：不因为流程控制本身增加不必要的沟通成本。

---

# 2. 核心生产链

标准流程：

```text
INPUT
↓
BRIEF
↓
CREATIVE_STRATEGY
↓
SCRIPT
↓
VISUAL_ASSETS
↓
STORYBOARD
↓
PRODUCTION_STRATEGY
↓
PROMPT
↓
FINAL_PACKAGE
↓
RETROSPECTIVE
↓
PERSONAL_EVOLUTION
```

其中：

- `VISUAL_ASSETS` 可以在 Script 确认后、Storyboard 过程中建立。
- `PRODUCTION_STRATEGY` 可以在 Storyboard 阶段同步形成。
- `RETROSPECTIVE` 在项目完成后执行。
- `PERSONAL_EVOLUTION` 属于项目后的个人经验沉淀，不影响当前已交付结果，除非用户主动重新打开项目。

---

# 3. Project Stage

项目阶段使用以下标准名称：

```text
INPUT
BRIEF
STRATEGY
SCRIPT
ASSETS
STORYBOARD
PRODUCTION
PROMPT
FINAL
RETROSPECTIVE
EVOLUTION
```

其中：

| Stage | 含义 |
|---|---|
| INPUT | 接收和解析客户原始需求 |
| BRIEF | 形成结构化需求 |
| STRATEGY | 确定视频类型和创作策略 |
| SCRIPT | 形成生产型脚本 |
| ASSETS | 建立视觉资产和参考素材关系 |
| STORYBOARD | 形成 AI Production Storyboard |
| PRODUCTION | 确定 AI / 实拍 / 素材 / 后期分工 |
| PROMPT | 生成 Seedance Prompt |
| FINAL | 形成最终生产包 |
| RETROSPECTIVE | 项目复盘 |
| EVOLUTION | 个人 Skill 进化 |

---

# 4. Stage Status

每个主要阶段统一使用：

```text
DRAFT
REVIEW
LOCKED
COMPLETED
```

状态含义：

### DRAFT

当前阶段正在生成或修改。

允许：

- AI 继续完善
- 用户修改
- 用户提出问题

不得：

- 自动进入下一阶段

---

### REVIEW

当前阶段已经形成一个完整候选版本，等待用户决定。

允许：

```text
MODIFY
BACK
APPROVE
APPROVE_AND_CONTINUE
```

---

### LOCKED

用户已经确认当前版本。

含义：

> 当前阶段内容已经获得用户批准，后续阶段不得未经授权修改。

允许：

- 被下游引用
- 被用户主动要求修改
- 通过 Change Request 回退

默认不得：

- 自动修改
- 因下游生成需要而偷偷调整

---

### COMPLETED

当前阶段及其必要下游流程已经完成。

例如：

```text
PROMPT → LOCKED
↓
FINAL → COMPLETED
```

`COMPLETED` 是项目交付状态，不代表之后永远不能修改。

若用户重新打开项目，应创建新的 Change Request 或 Revision。

---

# 5. User Actions

统一支持：

```text
MODIFY
BACK
APPROVE
APPROVE_AND_CONTINUE
```

---

# 6. APPROVE

含义：

> 用户认可当前阶段，但暂时不进入下一阶段。

执行：

```text
REVIEW
↓
LOCKED
```

然后：

> 停止自动生成。

适用场景：

- 用户准备把当前内容发给客户。
- 用户需要人工检查。
- 用户暂时结束当前工作。
- 用户需要先补充素材。
- 用户希望保留当前状态但稍后继续。

---

# 7. APPROVE_AND_CONTINUE

含义：

> 用户认可当前阶段，并要求立即进入下一阶段。

执行：

```text
REVIEW
↓
LOCKED
↓
NEXT STAGE
```

必须：

1. 锁定当前版本。
2. 记录确认。
3. 加载下一阶段相关 reference。
4. 读取当前阶段锁定内容。
5. 生成下一阶段。

这是默认推荐动作。

---

# 8. MODIFY

用户提出修改意见时：

```text
REVIEW
↓
MODIFY
↓
DRAFT
↓
REVIEW
```

修改逻辑：

1. 判断用户修改的是哪个对象。
2. 判断修改的是哪个字段。
3. 判断是否影响其他字段。
4. 判断是否影响下游。
5. 只修改必要范围。
6. 创建新版本。
7. 保留上一版本历史。

---

# 9. Partial Modification Rule

默认采用：

> **局部修改优先。**

例如用户说：

> “这一镜的运镜慢一点。”

默认仅修改：

```text
SHOT-04-02.camera_movement
```

而不是重写：

- Script
- 整个 Storyboard
- 其他镜头
- 所有 Prompt

---

# 10. Impact Analysis

任何修改都必须先判断影响范围。

影响类型：

```text
NONE
LOCAL
DOWNSTREAM
UPSTREAM
GLOBAL
```

---

## 10.1 NONE

只影响当前显示内容，不影响正式对象。

例如：

> 用户要求改变排版。

---

## 10.2 LOCAL

只影响当前对象。

例如：

> 修改一个 Prompt 的运镜。

---

## 10.3 DOWNSTREAM

当前修改可能影响下游。

例如：

> 修改 Script 的核心信息。

可能影响：

```text
Script
↓
Storyboard
↓
Prompt
```

---

## 10.4 UPSTREAM

当前问题表明上游设计存在问题。

例如：

> Storyboard 无法合理视觉化 Script 中的核心概念。

可能需要退回：

```text
Storyboard
↓
Script
```

---

## 10.5 GLOBAL

影响整个项目。

例如：

> 客户将视频目标从“品牌宣传”改成“招商转化”。

可能影响：

```text
Brief
Strategy
Script
Storyboard
Prompt
```

---

# 11. Impact Analysis 输出格式

发生重要修改时，用以下结构说明：

```text
修改：
……

直接影响：
……

可能影响：
……

无需修改：
……

建议操作：
……
```

示例：

```text
修改：
将项目受众从政府领导改为潜在投资企业。

直接影响：
Brief / Target Audience

可能影响：
Strategy / Script / Storyboard / Prompt

无需修改：
已有视觉资产中的产品素材

建议操作：
回退至 Strategy。
```

---

# 12. BACK

`BACK` 表示：

> 当前阶段发现上游问题，需要返回已经完成的上游阶段。

例如：

```text
STORYBOARD
↓
BACK
↓
SCRIPT
```

---

# 13. BACK 不等于删除历史

回退时必须：

1. 保留当前版本。
2. 创建新的版本链。
3. 记录回退原因。
4. 重新生成受影响的下游内容。

例如：

```text
SCRIPT V1 LOCKED
↓
STORYBOARD V1
↓
发现问题
↓
BACK
↓
SCRIPT V2
↓
STORYBOARD V2
```

不得删除：

```text
SCRIPT V1
STORYBOARD V1
```

---

# 14. Versioning

所有具有实质内容变化的对象必须版本化：

```text
BRIEF V1
BRIEF V2

SCRIPT V1
SCRIPT V2

STORYBOARD V1
STORYBOARD V2

PROMPT V1
PROMPT V2
```

---

# 15. 什么情况下必须创建新版本

以下情况必须产生新版本：

- 用户修改内容。
- Skill 根据用户意见重新生成内容。
- 上游内容变化导致重新生成。
- 用户从上一阶段回退后重新生成。
- Personal Rule 引起内容发生变化。

以下情况不需要创建新版本：

- 单纯重新展示。
- 格式调整且不改变语义。
- 排版变化。
- 用户要求再次解释当前版本。

---

# 16. Version Naming

建议采用：

```text
<OBJECT>-V<number>
```

例如：

```text
BRIEF-V1
STRATEGY-V2
SCRIPT-V3
STORYBOARD-V4
PROMPT-V2
```

如果具体到镜头：

```text
SHOT-04-02-V2
PROMPT-04-02-V3
```

---

# 17. Version History

每个对象至少记录：

```text
version
status
created_at
reason
created_from
user_change
impact
```

示例：

```yaml
version: 2
status: REVIEW
created_from: 1
reason: "客户要求突出国际化业务"
user_change: true
impact:
  upstream: []
  downstream:
    - STORYBOARD
    - PROMPT
```

第一版实现不要求实际使用程序自动维护 YAML 文件，但输出逻辑必须遵循这一结构。

---

# 18. Locked Content Rule

一旦：

```text
OBJECT
→ LOCKED
```

则默认：

```text
READ ONLY
```

任何修改都必须经过：

```text
MODIFY
或
CHANGE REQUEST
```

---

# 19. Change Request

当用户对已经锁定的项目提出新的业务要求时，建立：

```text
CHANGE REQUEST
```

Change Request 至少包括：

```text
CR ID
提出内容
提出时间
提出人
影响对象
影响阶段
建议回退点
用户决定
最终处理结果
```

示例：

```text
CR-003

新增需求：
加入国际化业务内容。

影响：
BRIEF
STRATEGY
SCRIPT

建议回退：
STRATEGY

用户决定：
接受回退。

结果：
Strategy V2
```

---

# 20. Change Request 与普通 MODIFY 的区别

### MODIFY

针对当前阶段已经在 REVIEW 状态下的修改。

例如：

> “把这一段旁白写短一些。”

### CHANGE REQUEST

针对已经 LOCKED 或 COMPLETED 的内容发生新的项目要求。

例如：

> “客户今天追加要求加入海外业务。”

---

# 21. User Override

如果 AI 提出建议，而用户坚持其他方案：

记录：

```text
AI_RECOMMENDATION
USER_DECISION
OVERRIDE = TRUE
```

例如：

```text
AI建议：
该镜头复杂度 ★★★★★，建议拆成两个镜头。

用户决定：
保持一个镜头。

OVERRIDE:
TRUE
```

Skill 必须尊重用户的最终决定。

---

# 22. Override 原则

User Override 可以覆盖：

- AI 建议
- Base Skill 的柔性建议
- Personal Skill 的柔性建议

不能覆盖：

- 安全边界
- 明确的事实真实性要求
- 系统级硬约束

---

# 23. Confirmation Protocol

所有阶段进入 REVIEW 后：

不要只问：

> “可以吗？”

应给用户明确操作选项：

```text
【确认】
【确认并继续】
【修改】
【退回上一步】
```

同时说明：

```text
当前版本
当前状态
主要结果
关键待确认事项
```

---

# 24. 默认确认提示

推荐格式：

```text
状态：SCRIPT V2 · REVIEW

本阶段已完成：
……

需要你决定：
【确认并继续】进入分镜
【确认】锁定脚本但暂不继续
【修改】告诉我需要调整的内容
【退回上一步】返回创作策略
```

不要重复解释用户已经明确知道的信息。

---

# 25. Confirmation Scope

如果一个用户同时说：

> “脚本没问题，分镜也继续做，Prompt 最后再让我看。”

应解析成：

```text
SCRIPT → APPROVE_AND_CONTINUE
STORYBOARD → REVIEW
PROMPT → 暂不生成
```

用户可以一次性表达多个阶段的确认策略。

但任何存在 P0 问题的阶段不能跳过必要确认。

---

# 26. Workflow Modes

## Mode A — Collaborative

默认：

```text
BRIEF → REVIEW
STRATEGY → REVIEW
SCRIPT → REVIEW
STORYBOARD → REVIEW
PROMPT → REVIEW
```

---

## Mode B — Fast

默认自动继续：

```text
BRIEF
→ STRATEGY
→ SCRIPT
→ ASSETS
→ STORYBOARD
→ PRODUCTION
→ PROMPT
→ FINAL
```

仅在以下情况暂停：

- P0 缺失
- 严重冲突
- Fact Lock 无法确认
- 高风险制作方案
- 用户主动要求确认

---

# 27. Stage Skipping

允许在特定情况下跳过阶段，但必须满足：

1. 上游信息已经充分。
2. 跳过阶段不会导致信息损失。
3. 当前 Workflow Mode 允许自动跳过。
4. 必须记录被跳过的阶段。

例如：

> 用户已经提供完整、确认过的 Script 和 Storyboard。

则可以直接：

```text
SCRIPT
→ STORYBOARD
→ PROMPT
```

无需重新生成 Script。

---

# 28. External Artifact Rule

如果用户已经提供某一阶段的正式成果，例如：

> 客户已经确认的脚本。

不要强制重新生成。

应该：

1. 解析用户提供内容。
2. 将其视为外部输入。
3. 标记来源：
   `客户已提供 / 用户已确认`
4. 建立内部对象。
5. 进入下一阶段。

---

# 29. Existing Project Resume

如果用户说：

> “继续昨天的项目。”

首先检查现有 Project State。

确认：

```text
current_stage
last_locked_version
open_questions
pending_changes
```

然后从最近一个有效状态继续。

不得默认从 Brief 重新开始。

---

# 30. Error Recovery

如果当前阶段出现异常：

### 情况 A：信息不足

→ 标记 P0/P1/P2。

### 情况 B：上游冲突

→ 标记 Impact。

### 情况 C：当前镜头不可执行

→ 尝试简化制作方案。

### 情况 D：Prompt 风险过高

→ 建议拆镜 / 改制作方式。

### 情况 E：用户不同意 AI 建议

→ 允许 User Override。

---

# 31. Never Silently Repair

禁止：

> 发现上游问题后，默默修改上游内容。

必须：

```text
发现问题
↓
说明问题
↓
说明影响
↓
提出建议
↓
等待用户决定
```

---

# 32. Quality Gate Integration

每个核心阶段必须在进入 REVIEW 前完成自己的质量检查。

```text
BRIEF
→ Brief Quality Gate

STRATEGY
→ Strategy Quality Gate

SCRIPT
→ Script Quality Gate

STORYBOARD
→ Storyboard Quality Gate

PROMPT
→ Prompt Quality Gate
```

质量检查失败：

> 不进入 APPROVE 流程。

但如果是非阻塞问题：

> 可以标记 Warning 后继续。

---

# 33. Blocking vs Warning

检查问题分两类：

### BLOCKING

必须处理：

- P0 缺失
- 严重事实冲突
- 违反 Fact Lock
- 无法执行的核心创作要求
- 关键内容前后矛盾

### WARNING

建议处理：

- 风格不统一
- 景别重复
- 成本偏高
- AI 风险偏高
- 可以进一步优化但不影响交付

---

# 34. Stage Completion Rule

一个阶段只有同时满足：

```text
Quality Gate Passed
+
User Approved
```

才能进入：

```text
LOCKED
```

极速模式下：

> 用户没有逐阶段确认，但满足自动模式规则后，可以视为 Auto-Approved。

此时必须记录：

```text
approval_mode = AUTO
```

---

# 35. Auto-Approved

仅允许在：

```text
Mode B
或
极速模式下的非暂停阶段
```

出现。

例如：

```yaml
approval:
  mode: AUTO
  reason: "Semi-automatic workflow; STORYBOARD is not a checkpoint."
```

---

# 36. Current Stage

任何时候必须能回答：

> **当前项目处于哪个阶段？**

例如：

```text
current_stage: STORYBOARD
status: REVIEW
version: V3
```

如果当前 stage 不明确，不应继续生成。

---

# 37. Final Package

当 Prompt 被确认以后：

```text
PROMPT
→ LOCKED

FINAL
→ COMPLETED
```

Final Package 包括：

- Brief Summary
- Creative Strategy
- Script
- Storyboard
- Visual Assets
- Production Strategy
- Seedance Prompts
- Post-production Notes
- Risks / Warnings

用户如果只要求 Prompt：

> 可以只交付 Prompt Package。

---

# 38. Project Completion

项目只有在：

```text
FINAL = COMPLETED
```

后才进入：

```text
RETROSPECTIVE
```

项目复盘不会自动修改已经完成的项目产物。

---

# 39. Retrospective Boundary

复盘产生：

```text
Experience
Candidate Improvement
Personal Evolution
```

但不得直接：

```text
Project Output
→ 修改
```

如需修改当前项目：

> 必须重新打开项目并通过 Revision / Change Request。

---

# 40. Workflow Invariants

以下原则在任何模式下都必须成立：

### Invariant 1

已锁定内容不可被下游阶段偷偷修改。

### Invariant 2

用户明确修改意见优先于 AI 自己的偏好。

### Invariant 3

事实不得通过 AI 推测进行替换。

### Invariant 4

回退不会删除历史版本。

### Invariant 5

局部修改优先于全量重生成。

### Invariant 6

项目复盘不得直接改写项目交付物。

### Invariant 7

Personal Skill 不得覆盖 Fact Lock。

### Invariant 8

所有重大修改必须可以追踪来源。

---

# 41. Workflow Event Log

重要行为应该记录事件：

```text
PROJECT_CREATED
STAGE_STARTED
STAGE_REVIEW
APPROVED
APPROVED_AND_CONTINUED
MODIFIED
BACKED
LOCKED
CHANGE_REQUEST_CREATED
OVERRIDE_ACCEPTED
STAGE_AUTO_APPROVED
PROJECT_COMPLETED
RETROSPECTIVE_CREATED
PERSONAL_RULE_PROPOSED
PERSONAL_RULE_ACCEPTED
```

V1 不要求用独立数据库记录。

可以使用项目上下文中的结构化文本维护。

---

# 42. 最小 Event Record

每个关键事件至少包含：

```yaml
event:
  type:
  timestamp:
  stage:
  object_id:
  version:
  actor:
  reason:
  impact:
```

其中：

```text
actor =
USER
AI
AUTO
```

---

# 43. Workflow 与 Personal Skill 的边界

Workflow 规则属于：

> Base Skill。

Personal Skill 可以影响：

- 默认创作建议
- 风格选择
- 某些非硬性制作偏好
- Prompt 表达倾向
- 推荐镜头习惯

Personal Skill 不得改变：

- 状态机
- Lock 原则
- Fact Lock
- Change Request
- 版本历史
- 用户确认权
- 安全与事实约束

---

# 44. Workflow 与具体模型的边界

Workflow 不依赖 Seedance。

例如未来：

```text
PROMPT
→ SEEDANCE_RENDERER
```

可以替换成：

```text
PROMPT
→ VEO_RENDERER
```

Workflow 本身不变。

---

# 45. Efficiency Principle

工作流本身也必须追求效率。

因此：

### 不重复确认

用户已经明确确认的内容，不重复询问。

### 不重复生成

没有变化的内容，不重新生成。

### 不重复解释

用户明确知道的信息，不反复讲解。

### 不扩大修改范围

能改一镜，不改整段。

### 不扩大回退范围

能回退到 Script，不回到 Brief。

---

# 46. Workflow 优先级

遇到流程与创作建议冲突时：

```text
Workflow Integrity
>
Fact Integrity
>
User Decision
>
Creative Optimization
```

也就是说：

> 即使 AI 认为某个修改“更好”，也不能绕过工作流直接修改用户已经锁定的内容。

---

# 47. Final Operational Rule

始终遵循：

> **先确定状态，再执行动作；先判断影响，再修改；先锁定当前成果，再进入下一阶段。**

工作流的最终目标不是增加审批，而是：

> **让每一次创作决策都有明确归属，让每一次修改都只影响真正需要改变的部分。**