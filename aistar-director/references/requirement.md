# `references/requirement.md`

# Requirement Intelligence Protocol

本文档定义 `aistar-director` 如何理解、提取、判断、补全和确认客户的视频需求，并将非结构化输入转换为可供后续创作阶段使用的 **Structured Brief**。

本文件的核心目标：

> **让 AI 在开始创作之前，先真正理解客户要解决什么问题、给谁看、要说什么、哪些内容不能错，以及哪些地方仍然需要确认。**

---

# 1. Requirement Intelligence 的职责

Requirement Intelligence 负责：

```text
原始客户输入
↓
输入解析
↓
信息抽取
↓
信息归类
↓
事实识别
↓
需求完整性检查
↓
冲突检测
↓
风险识别
↓
默认假设
↓
Structured Brief
↓
用户确认
```

不得直接从原始输入跳到：

- Script
- Storyboard
- Seedance Prompt

---

# 2. 输入类型

Skill 应尽可能接受以下输入。

## 2.1 直接文字

包括：

- 用户直接描述
- 客户 Brief
- 微信/飞书/邮件聊天记录
- 会议纪要
- 客户修改意见
- 领导讲话稿
- 产品介绍文字
- 官网文字
- 宣传文案

---

## 2.2 表格

例如：

| 项目 | 内容 |
|---|---|
| 视频用途 | 招商会 |
| 视频时长 | 90秒 |
| 目标受众 | 潜在投资企业 |
| 核心卖点 | 区位、产业、政策 |
| 必须出现 | 园区、交通、企业案例 |

处理原则：

1. 自动识别表头。
2. 识别字段之间的关系。
3. 转换成 Brief。
4. 保留原始字段语义。
5. 不因表格结构而丢失信息。

---

## 2.3 文件

可能包括：

- Word
- Excel
- PDF
- PPT
- 图片
- 视频
- 音频

文件可能承担不同职责：

```text
事实资料
品牌资料
产品资料
视觉参考
历史素材
参考作品
创意参考
```

不要把所有文件都视为同一种素材。

---

## 2.4 语音

语音输入首先转换成可分析文本。

需要注意：

语音中的：

- 停顿
- 重复
- 犹豫
- 修改
- “大概”
- “最好”
- “类似”
- “领导比较喜欢”

可能包含需求强度信息。

例如：

> “最好能够有点科技感。”

与：

> “必须是科技感，不能做成传统企业宣传片。”

在需求优先级上完全不同。

---

# 3. 原始输入的第一轮解析

收到输入后，不要立即总结。

首先区分：

### Explicit Content

客户明确说了什么。

### Implied Content

根据客户信息可以合理推导什么。

### Creative Direction

客户表达了什么创作偏好。

### Unknown

当前无法判断什么。

例如：

```text
客户：
“这是给招商会播放的园区宣传片，要大气一点，重点讲产业和政策。”

提取：

客户明确要求：
视频用于招商会；
项目是园区宣传视频；
重点内容为产业和政策。

基于客户信息推导：
核心受众可能为潜在投资企业。

AI建议：
建议采用招商/投资说服型结构，而不是传统园区形象片。

待确认：
是否需要展示具体招商政策；
目标视频时长。
```

---

# 4. 信息来源标签

所有进入 Structured Brief 的重要信息必须带来源。

标准标签：

```text
客户明确要求
基于客户信息推导
AI 建议
待确认
```

---

# 5. Source Precedence

如果同一信息出现多个来源冲突，优先级：

```text
客户明确要求
>
基于客户信息推导
>
AI 建议
>
默认假设
```

但如果两个“客户明确要求”本身冲突：

> 不得自行选择。

必须产生：

```text
需求冲突
```

并要求确认。

---

# 6. Brief 的核心数据结构

Structured Brief 至少包含：

```text
project_info
business_objective
audience
core_message
content_hierarchy
must_include
optional_include
must_avoid
creative_direction
format
usage
assets
references
production_constraints
fact_constraints
compliance
desired_response
assumptions
open_questions
risks
source_annotations
```

---

# 7. Project Info

记录：

```text
project_name
client
project_owner
project_type
requested_video_form
deadline
release_date
```

注意：

`requested_video_form` 是：

> 客户要求的视频形式。

它不等同于 Skill 最终判断的：

> video_type。

例如：

```text
requested_video_form:
企业宣传片

Skill判断：
招商/投资说服型
```

---

# 8. Business Objective

必须回答：

> **客户为什么要制作这个视频？**

推荐分类：

```text
品牌认知
产品销售
服务推广
招商
投资
政府宣传
项目汇报
成果展示
客户获取
招聘
培训
政策传播
活动传播
内部沟通
新媒体传播
其他
```

允许多选，但必须识别：

```text
primary_objective
secondary_objectives
```

---

# 9. Objective 与 Topic 的区别

严格区分：

### Topic

> 视频讲什么？

### Objective

> 为什么要讲？

例如：

```text
Topic：
介绍智慧园区建设成果。

Objective：
吸引潜在投资企业考察园区。
```

后续创作策略主要由 Objective 驱动。

---

# 10. Audience

至少包含：

```text
primary_audience
secondary_audience
audience_knowledge
desired_perception_change
desired_action
```

分别回答：

### Primary Audience

最重要的观看对象。

### Secondary Audience

次要观看对象。

### Audience Knowledge

受众已经知道什么。

### Desired Perception Change

希望改变什么认知。

### Desired Action

看完以后希望做什么。

---

# 11. Audience 冲突检查

如果存在多个受众：

> 必须判断它们的诉求是否兼容。

例如：

```text
政府领导
潜在投资企业
普通市民
```

如果三者都被要求作为同等核心受众：

> 标记为潜在问题。

建议确认：

> 谁是第一核心受众？

---

# 12. Core Message

必须确定：

> **观众看完后最应该记住的一句话是什么？**

结构：

```text
primary_message
supporting_messages[]
```

默认要求：

```text
1 个核心信息
+
不超过 3～5 个核心支撑信息
```

如果客户提供的信息过多：

> 不要自动全部作为核心信息。

应进行信息层级化并提示用户。

---

# 13. Content Hierarchy

将信息分为：

```text
P1 核心信息
P2 支撑信息
P3 背景信息
P4 可删除信息
```

注意这里的 P1/P2/P3/P4 是：

> **内容重要性**

不要与需求缺失检查中的：

> P0/P1/P2

混淆。

建议实现时使用不同字段名称：

```text
content_priority:
CORE
SUPPORTING
BACKGROUND
OPTIONAL
```

---

# 14. Must Include

记录：

> 无论创意如何变化，都必须在最终方案中出现的内容。

例如：

```text
公司名称
Logo
产品名称
核心数据
领导姓名
真实建筑
项目名称
联系方式
CTA
```

每项可记录：

```text
required
reason
source
verification_status
```

---

# 15. Optional Include

记录：

> 有价值，但并非必须。

例如：

```text
员工场景
未来城市
抽象科技视觉
企业文化
客户故事
```

---

# 16. Must Avoid

记录明确禁止内容。

包括：

```text
竞品
错误数据
未经授权人物
未经授权建筑
错误政策信息
不符合品牌标准的颜色
改变产品外观
夸大宣传
不允许的 AI 虚构
```

---

# 17. Fact Constraints

对所有事实性内容进行单独标记。

例如：

```yaml
fact_constraints:
  - fact: "项目总投资"
    value: "120亿元"
    source: "DOC-03"
    verification: "client_provided"

  - fact: "园区建筑"
    source: "IMG-04"
    verification: "reference_required"
```

如果无法验证：

```text
verification:
unverified
```

则不得在后续阶段将其当作已确认事实。

---

# 18. Fact Lock

满足以下条件的信息，可以进入 Fact Lock：

1. 客户明确提供。
2. 有可靠客户资料支持。
3. 已经过用户确认。
4. 已有项目正式版本引用。

Fact Lock 内容：

> 后续 Script / Storyboard / Prompt 不得擅自修改。

---

# 19. Creative Direction

客户常用表达包括：

```text
大气
高级
科技感
有温度
国际化
年轻
专业
可信
震撼
克制
现代
未来
```

这些表达不要直接原样写入 Prompt。

先转换成：

```text
emotion
visual_language
camera_language
color_direction
lighting_direction
editing_rhythm
sound_direction
```

例如：

```text
客户明确要求：
大气、科技感、高级。

结构化解释：

emotion：
宏大、专业、可信

visual_language：
现代城市、真实人物、数字化空间

camera_language：
稳定、克制、渐进

lighting：
冷白 + 品牌蓝

editing_rhythm：
前慢、中快、结尾舒缓
```

---

# 20. Creative Ambiguity

如果客户的创意词语含义过于宽泛：

> 不应该立即要求客户定义所有细节。

优先：

1. 提供一个合理解释。
2. 明确这是 AI 建议。
3. 只有当不同解释会导致完全不同的视频方案时才要求确认。

例如：

> “年轻化”

可以解释为：

> 更快节奏、人物更年轻、图形更现代、色彩更活跃。

然后询问：

> 哪一个维度是客户真正想要的？

而不是直接问：

> “年轻化是什么意思？”

---

# 21. Video Format

记录：

```text
duration
aspect_ratio
resolution
language
voiceover
subtitle
orientation
delivery_platform
playback_context
```

---

# 22. Duration

时长必须记录：

```text
target_duration
acceptable_range
```

例如：

```text
target_duration:
90s

acceptable_range:
80–100s
```

如果客户只说：

> “大约两分钟。”

可以转化：

```text
target_duration:
120s

assumption:
±15s
```

并标记：

> AI 默认假设。

---

# 23. Usage

记录：

```text
会议大屏
招商会
展会
发布会
官网
企业官网
微信公众号
抖音
视频号
小红书
销售拜访
内部培训
电视/户外
其他
```

Usage 会影响：

- 节奏
- 画幅
- 信息密度
- 字幕
- CTA
- 音量
- 开场速度

因此不得简单记录后就忽略。

---

# 24. Reference Works

客户如果说：

> “希望像某个片子。”

必须进一步分析：

```text
reference_style
reference_structure
reference_camera
reference_color
reference_music
reference_editing
reference_specific_shots
```

并区分：

### Whole Reference

客户喜欢整支片。

### Partial Reference

客户只喜欢其中某些部分。

例如：

```text
客户喜欢：
前20秒开场
人物跟拍
音乐节奏

客户不喜欢：
后半段复杂 CG
```

---

# 25. Reference Asset Analysis

当客户提供图片、视频等参考素材时：

不要简单写：

> “参考素材：IMG-01”。

应该标记它的职责：

```text
identity
appearance
product
environment
composition
camera
movement
lighting
style
audio
rhythm
```

如果职责不明确：

> 标记待确认或作为 AI 建议。

---

# 26. Production Constraints

记录：

```text
available_budget_level
production_deadline
available_live_action
available_stock_footage
available_client_assets
AI_allowed
AI_restrictions
postproduction_capability
voiceover_capability
```

V1 不要求精确计算人民币预算。

可以采用：

```text
低
中
高
```

表示资源约束。

---

# 27. AI Permission

必须明确：

```text
allow_ai_fabrication
allow_ai_characters
allow_ai_buildings
allow_ai_products
allow_ai_historical_reconstruction
allow_ai_voice
allow_ai_face_simulation
```

这些选项非常重要，尤其政府项目。

例如：

```text
allow_ai_buildings:
false
```

则后续看到具体政府建筑时：

> 默认要求真实参考素材。

---

# 28. Desired Viewer Response

记录：

```text
desired_emotion
desired_perception
desired_action
```

例如：

```text
emotion:
信任

perception:
认为园区成熟、有产业基础

action:
预约考察
```

---

# 29. Tone

可以定义：

```text
专业
可信
温暖
宏大
克制
年轻
活力
高端
亲和
庄重
理性
感性
```

允许多选，但需要判断主导 Tone。

---

# 30. Compliance

至少检查：

```text
legal
policy
brand
copyright
identity
fact_accuracy
privacy
approval_requirement
```

尤其政府项目：

> 政策、统计数据、人物身份、建筑信息必须优先以客户正式资料为依据。

---

# 31. Risk Classification

需求风险分：

### LOW

基本都可合理执行。

### MEDIUM

存在少量生成或事实风险。

### HIGH

可能涉及：

- 真实人物
- 政府领导
- 政策
- 精确数据
- 真实政府建筑
- 高一致性产品
- 复杂多人互动
- 高度敏感事实
- 客户明确要求模型完成高难动作

HIGH 不代表不能做。

含义是：

> 必须增加制作策略或人工确认。

---

# 32. Conflict Detection

必须检测以下冲突：

### Objective Conflict

例如：

> 同时要求“品牌高端”与“极低成本快速传播”。

### Audience Conflict

例如：

> 同时把政府领导、投资人、普通市民作为同等核心受众。

### Style Conflict

例如：

> “真实纪录片感” + “未来科幻大片”。

### Fact Conflict

例如：

> 两份客户资料中的数据不同。

### Constraint Conflict

例如：

> “所有建筑必须真实” + “未来城市必须完全虚构”。

### Time / Content Conflict

例如：

> 90 秒视频却要求完整讲 20 个产品。

发现冲突后：

> 不自行选择。

给出：

```text
冲突内容
冲突原因
影响
可能方案
建议
```

---

# 33. Assumption Protocol

允许 AI 在低风险情况下进行默认假设。

每个假设至少记录：

```yaml id="7u4j4c"
assumption_id:
content:
reason:
confidence:
impact:
status:
```

status：

```text
ACTIVE
CONFIRMED
REJECTED
```

用户一旦确认：

> 该假设转为项目已确认条件。

---

# 34. Question Protocol

向用户提问时：

不要一次提出大量问题。

问题按优先级：

### P0 Question

必须回答才能可靠继续。

### P1 Question

可以给默认值，但建议确认。

### P2 Question

不询问，AI 自动处理。

---

# 35. P0 Question 要求

P0 问题必须：

1. 清楚。
2. 尽量单一。
3. 说明为什么需要。
4. 如果有合理选项，提供选项。
5. 避免要求用户重复描述整个项目。

示例：

> 视频主要用于招商会还是品牌发布会？两者会直接影响叙事重点。

---

# 36. Question Bundling

多个互相独立的小问题：

> 尽量合并。

例如：

```text
为了进入脚本阶段，还缺 3 个关键信息：

1. 目标时长：
   A 60秒 / B 90秒 / C 120秒

2. 核心受众：
   A 政府领导 / B 潜在投资企业 / C 两者兼顾

3. 是否允许 AI 虚构园区建筑：
   A 可以 / B 不可以
```

但如果问题之间存在明显依赖关系：

> 分步询问。

---

# 37. Requirement Normalization

客户说法不统一时，标准化表达。

例如：

> “我们想做一个科技感宣传片。”

转换：

```text
requested_video_form:
宣传片

creative_intent:
科技感

video_type:
待 Strategy 判断
```

不要直接把：

> “宣传片”

当作最终视频类型。

---

# 38. Customer Language Preservation

重要客户原话应保留。

尤其：

- 核心口号
- 品牌用语
- 领导原话
- 产品定义
- 政策名称
- 已确认表述

这些内容可以记录：

```text
source_quote
```

后续如果进行“AI 友好改写”：

> 不得替换原文事实意义。

---

# 39. Requirement Compression

如果客户输入非常长：

> Brief 不应机械复述全部内容。

应压缩成：

```text
核心目标
核心受众
核心信息
关键约束
关键素材
关键事实
风险
待确认事项
```

并保留原始输入作为来源。

---

# 40. Requirement Traceability

每一个核心 Brief 字段，尽可能可以回答：

> **这个结论来自哪里？**

例如：

```text
core_message:
“突出园区产业集群优势”

source:
客户会议纪要 03，第三段

source_type:
客户明确要求
```

---

# 41. Brief Review Output

提交用户确认时，推荐使用以下结构：

```text
【项目理解】

项目目标：
……

核心受众：
……

核心信息：
……

视频形式判断：
……

必须出现：
……

禁止出现：
……

创作方向：
……

素材情况：
……

关键事实：
……

当前风险：
……

待确认：
……

AI 默认假设：
……
```

最后：

```text
状态：BRIEF V1 · REVIEW

【确认并继续】
【确认】
【修改】
```

---

# 42. Brief Approval Rule

用户确认后：

```text
BRIEF
→ LOCKED
```

后续 Strategy、Script、Storyboard、Prompt 必须以 LOCKED Brief 为上游事实源。

---

# 43. Brief 修改 Rule

如果 Brief 已锁定，但用户提出新需求：

必须判断：

```text
是否为普通局部修改？
还是 Change Request？
```

一般：

- 轻微表达调整 → MODIFY
- 新增传播目标 → CHANGE REQUEST
- 新增核心受众 → CHANGE REQUEST
- 改变视频目的 → CHANGE REQUEST
- 改变关键事实 → CHANGE REQUEST
- 改变时长/平台 → 根据影响程度判断

---

# 44. Brief Quality Gate

进入 REVIEW 前，必须检查：

```text
□ 视频目的是否明确
□ 目标受众是否明确
□ 核心信息是否明确
□ 视频用途是否明确
□ 时长是否足够明确
□ 关键事实是否有来源
□ 必须出现是否明确
□ 禁止出现是否明确
□ 重大合规风险是否发现
□ P0 问题是否处理
□ 冲突是否处理
□ 假设是否标记
□ 信息来源是否标记
```

---

# 45. Blocking Conditions

以下情况不得直接进入 Strategy：

```text
1. 视频目的完全不明。
2. 核心信息完全不明。
3. 目标受众完全不明且无法合理推导。
4. 关键事实存在不可消解冲突。
5. 客户要求依赖但未确认的关键政策/数据存在重大风险。
6. 项目用途与视频形式完全无法判断。
```

---

# 46. Warning Conditions

以下情况可以继续，但必须提示：

```text
1. 未提供参考片。
2. 未提供明确视觉风格。
3. 时长只有模糊范围。
4. AI 可行性存在中等风险。
5. 部分关键素材缺失。
6. 次级受众不明确。
```

---

# 47. Requirement-to-Creative Boundary

Brief 阶段允许：

> 提出创意方向建议。

但不应该提前制作完整：

- Script
- Storyboard
- Prompt

这样做是为了保持阶段边界。

例如可以：

> 建议采用“现实 → 问题 → 技术介入 → 城市变化”的叙事方向。

但不应该直接写：

> “0–5 秒航拍城市，镜头下降到……”

后者属于 Script / Storyboard。

---

# 48. Output Object

Brief 最终结构建议：

```yaml id="1r5t3w"
brief:
  project_info:
  business_objective:
  audience:
  core_message:
  content_hierarchy:
  must_include:
  optional_include:
  must_avoid:
  creative_direction:
  format:
  usage:
  assets:
  references:
  production_constraints:
  fact_constraints:
  compliance:
  desired_viewer_response:
  assumptions:
  open_questions:
  risks:
  source_annotations:
```

---

# 49. Requirement Interpretation Rule

如果客户说法存在多种合理解释：

不要自动选一个并当作事实。

使用：

```text
解释 A
解释 B
推荐方案
原因
```

除非某一种解释明显由客户上下文支持。

---

# 50. Final Requirement Principle

Requirement Intelligence 必须始终遵循：

> **先区分客户说了什么，再判断可以推导什么；先识别事实，再讨论创意；先处理真正影响结果的不确定性，再进入创作。**

最终目标不是制作一份漂亮的 Brief。

而是建立：

> **一个后续所有创作阶段都可以信任的项目事实源与创作输入源。**