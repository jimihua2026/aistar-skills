# `references/creative-strategy.md`

# Creative Strategy Protocol

本文档定义 `aistar-director` 如何根据已经确认的 Structured Brief 和 Video Type Routing，形成项目级的 **Creative Strategy**。

本文件回答的问题是：

> **这支视频应该“怎么打”，才能用合适的叙事、创意、视觉和制作方式，完成客户真正的传播目标？**

本文件位于：

```text id="1xq8zn"
BRIEF
↓
VIDEO TYPE
↓
CREATIVE STRATEGY
↓
SCRIPT
```

本文件不负责最终脚本、详细分镜或 Seedance Prompt。

---

# 1. Creative Strategy 的职责

Creative Strategy 负责把：

```text id="teik0g"
客户需求
+
项目事实
+
视频类型
+
受众
+
传播目标
+
客户素材
+
Personal Style
```

转化为：

```text id="c9p7my"
传播打法
+
创意命题
+
叙事方向
+
视觉方向
+
情绪方向
+
声音方向
+
制作策略
+
成本策略
```

目标：

> 在写 Script 之前，先回答“这支片到底应该怎么做”。

---

# 2. Creative Strategy 与其他阶段的边界

## Brief

回答：

> 客户要什么？

## Video Type

回答：

> 这是什么类型、承担什么传播任务？

## Creative Strategy

回答：

> **这支片采用什么创作打法？**

## Script

回答：

> 具体讲什么？

## Storyboard

回答：

> 具体看到什么？

因此：

> Creative Strategy 不应该直接写成完整脚本。

---

# 3. Strategy 的核心原则

## 3.1 需求驱动

所有策略首先服务：

> Primary Objective

其次服务：

> Primary Audience

再次服务：

> Desired Action

不要为了“好看”而牺牲传播目标。

---

## 3.2 先确定传播命题，再确定视觉

不要一开始决定：

> “做一个很科技的片子。”

而应该先回答：

> “我们想让谁相信什么？”

例如：

```text id="fz10xj"
目标：
吸引企业投资园区

传播命题：
“这里不是一个普通园区，而是一套已经具备完整产业生态的投资载体。”
```

然后再决定：

> 用什么视觉证明这个命题。

---

## 3.3 一个项目只能有一个主导传播命题

允许多个支撑信息。

但必须有：

```text id="l4hrg9"
Core Proposition
```

最多建议：

> 1 个核心命题 + 3～5 个支撑命题。

---

# 4. Creative Strategy 标准对象

建议输出：

```yaml id="x4f03c"
creative_strategy:
  strategic_objective:
  primary_audience:
  desired_action:
  core_proposition:

  creative_concept:
  one_line_idea:

  narrative_strategy:
  narrative_structure:

  emotional_strategy:
  emotional_curve:

  visual_strategy:
  visual_anchor:
  visual_language:
  color_direction:
  lighting_direction:
  camera_language:

  sound_strategy:

  asset_strategy:

  ai_strategy:
  live_action_strategy:
  postproduction_strategy:

  production_economics:
  complexity_strategy:

  risks:
  assumptions:
  alternatives:

  rationale:
```

---

# 5. Strategic Objective

首先把 Brief 中的 Business Objective 转化成一个更具体的：

> **传播任务。**

例如：

### Brief

> 招商。

### Strategy

> 让潜在投资企业在短时间内形成“这里具备产业基础、配套能力和发展机会”的判断，并愿意进一步了解项目。

Strategy 不应简单重复：

> “目标：招商。”

而应说明：

> **视频最终希望在受众脑中建立什么判断。**

---

# 6. Core Proposition

定义整个视频最重要的一句话。

标准：

> 看完整支片后，观众最应该记住什么？

例如：

```text id="aetqfz"
“我们不是在建设一个园区，而是在建设一套完整的产业生态。”
```

Core Proposition 不能：

- 太长
- 包含大量事实
- 同时包含多个完全独立观点

---

# 7. One-Line Idea

将 Core Proposition 进一步转化成：

> 一句话创意。

它不是广告口号，而是：

> **贯穿整支视频的创作逻辑。**

例如：

```text id="xopq32"
Core Proposition：
让城市治理更加主动。

One-Line Idea：
“让城市开始自己发现问题。”
```

---

# 8. Creative Concept

Creative Concept 是：

> **整支片子的创意母体。**

它决定：

- 开场怎么进入
- 中间怎么推进
- 视觉母题是什么
- 结尾如何升华

一个好的 Creative Concept 应满足：

```text id="j0t4ub"
相关
可视觉化
可持续
可复用
可控制成本
```

不能只是一句漂亮口号。

---

# 9. Creative Concept 的质量检查

一个概念如果无法回答下面四个问题，则不应采用：

### Q1

能否自然进入开场？

### Q2

能否贯穿中段？

### Q3

能否形成视觉母题？

### Q4

能否自然落到结尾？

---

# 10. 视觉母题

Creative Strategy 必须确定：

> **什么视觉元素能够贯穿全片，把不同场景统一起来？**

例如：

```text id="kzqqlt"
数据流
光线
道路
门
手
地图
连接线
时间
人群
机器
水
生长
```

视觉母题不是装饰。

应该能够承担：

> 叙事连接 / 转场 / 情绪推进 / 品牌识别

中的至少一种作用。

---

# 11. Narrative Strategy

Narrative Strategy 描述：

> **观众将以怎样的心理路径理解视频。**

常见模式：

```text id="ykx3qb"
问题驱动
机会驱动
人物驱动
产品驱动
结果驱动
时间线驱动
空间漫游
对比驱动
数据驱动
事件驱动
愿景驱动
```

可以混合，但必须有一个主导模式。

---

# 12. 常见叙事模式

## 12.1 Problem → Solution

适用于：

- 产品
- 服务
- 数字化
- 政务服务
- 技术项目

结构：

```text id="2abv2y"
问题
→ 放大问题
→ 解决方案
→ 应用
→ 结果
```

---

## 12.2 Opportunity → Action

适用于：

- 招商
- 投资
- 城市发展
- 新项目

结构：

```text id="qt4j3p"
机会
→ 为什么现在
→ 为什么是这里
→ 为什么是你
→ 行动
```

---

## 12.3 Person → Story → Meaning

适用于：

- 人物
- 品牌故事
- 招聘
- 企业文化

结构：

```text id="px7j9n"
人物
→ 经历
→ 冲突
→ 选择
→ 变化
→ 价值
```

---

## 12.4 Evidence → Proof → Impact

适用于：

- 项目成果
- 工程
- 客户案例
- 政府成果

结构：

```text id="9a5dmv"
事实
→ 过程
→ 证据
→ 结果
→ 价值
```

---

## 12.5 World → Business → Future

适用于：

- 品牌片
- 城市片
- 企业形象
- 未来战略

结构：

```text id="34mh3n"
时代 / 环境
→ 品牌 / 项目
→ 当前行动
→ 未来
```

---

# 13. Strategy 必须根据 Video Type 调整叙事

例如：

### 招商型

默认优先：

> Opportunity → Proof → Action

### 产品型

默认优先：

> Problem → Solution → Benefit → Action

### 项目成果型

默认优先：

> Evidence → Proof → Impact

### 人物型

默认优先：

> Person → Story → Meaning

但这些只是：

> **推荐起点**

不能强制模板化。

---

# 14. Narrative Structure 的选择原则

选择结构时优先考虑：

```text id="1m9w9k"
传播目标
>
受众
>
核心信息
>
现有素材
>
时间长度
>
个人风格
```

而不是：

> “这个类型以前都这样做。”

---

# 15. Emotional Strategy

必须定义：

> 观众在整个过程中应该经历怎样的情绪变化？

常见情绪：

```text id="xhlzty"
好奇
压迫
紧张
探索
惊喜
信任
自豪
兴奋
温暖
振奋
希望
坚定
```

情绪不是越强越好。

必须服务传播目标。

---

# 16. Emotional Curve

至少输出：

```text id="n5h0u0"
开场情绪
中段情绪
高潮情绪
结尾情绪
```

例如：

```text id="c2nsu9"
开场：
问题感 / 好奇

中段：
探索 / 信任

高潮：
震撼 / 确信

结尾：
愿景 / 行动
```

---

# 17. Visual Strategy

Visual Strategy 回答：

> **这支视频整体应该“长什么样”？**

至少包括：

```text id="1trp15"
visual_language
visual_anchor
color_direction
lighting_direction
camera_language
composition_preference
editing_rhythm
```

---

# 18. Visual Language

不要写：

> “高级、震撼、电影感。”

应转换成：

```text id="x0k2e5"
真实商业摄影
现代建筑空间
低饱和
克制镜头运动
浅景深人物特写
大尺度空间
真实自然光
```

Visual Language 必须尽可能可执行。

---

# 19. Visual Anchor

Visual Anchor 是：

> **整支片子的视觉识别核心。**

例如：

```text id="7gwd7q"
数据流穿梭在真实城市空间
```

或者：

```text id="6dtxw6"
“门”作为从传统业务进入数字未来的视觉隐喻
```

每个项目建议：

> 1 个主要视觉锚点。

必要时：

> 1 个主要 + 1 个辅助。

---

# 20. Color Direction

颜色策略必须服务：

> 品牌 + 情绪 + 场景真实性。

例如：

```text id="u5tzds"
品牌蓝为主
中性灰辅助
少量高亮绿色表示系统成功
```

不要仅仅写：

> “蓝色科技感。”

---

# 21. Lighting Direction

根据：

- 类型
- 场景
- 情绪
- 品牌

确定：

```text id="l4b10p"
自然光
硬光
柔光
高反差
低反差
冷光
暖光
混合光
```

对于写实企业/政府项目：

> 默认避免无必要的过度霓虹和赛博朋克风。

---

# 22. Camera Language

Camera Language 描述：

> 观众会如何观察这个世界？

例如：

### 品牌片

> 稳定、克制、大尺度。

### 招商片

> 城市大景 + 空间推进 + 稳定运动。

### 人物片

> 中近景 + 跟拍 + 呼吸感。

### 产品片

> 精确构图 + 稳定产品镜头 + 功能跟随。

这里只定义：

> **镜头语言方向**

具体镜号留给 Storyboard。

---

# 23. Editing Rhythm

建议定义：

```text id="2ln0cx"
slow_build
steady
medium
fast
accelerating
variable
```

以及：

> 开场 / 中段 / 高潮 / 结尾

分别采用什么节奏。

---

# 24. Sound Strategy

至少确定：

```text id="jyio7k"
BGM
ambient_sound
sound_effects
voice
silence
```

以及：

> 声音在叙事中承担什么职责。

例如：

> 招商片：BGM 建立信心，环境声提供真实感。

> 人物片：人物原声优先，BGM 辅助。

---

# 25. Asset Strategy

根据 Brief 中已有素材决定：

```text id="9uubt3"
客户真实素材
素材库
AI生成
实拍
后期图形
```

重点判断：

> 哪些内容必须真实？

> 哪些内容适合 AI？

> 哪些内容应该交给后期？

---

# 26. AI Strategy

不要回答：

> “这个视频用 AI 做。”

要回答：

> **AI 在这个项目中最应该承担什么工作？**

例如：

```text id="9xu7js"
AI负责：
宏观环境
概念场景
B-roll
过渡镜头
未来愿景
产品使用场景模拟

真实素材负责：
项目证据
领导
客户
真实建筑
真实生产线

后期负责：
数据
中文文字
Logo
UI
政策文本
```

---

# 27. AI Production Ratio

不要求精确百分比。

可以采用：

```text id="xn08m4"
AI 主导
AI 辅助
混合制作
真实素材主导
后期主导
```

如果有项目级比例需求：

> 可以给出估算。

但不把比例作为质量指标。

---

# 28. Production Economics

每个策略必须判断：

```text id="9rbbfa"
效果
时间
成本
```

考虑：

### AI Cost

生成难度、迭代次数。

### Post Cost

剪辑、字幕、数据包装、修图等。

### Asset Cost

素材获取、实拍、客户整理成本。

### Review Cost

客户审核和返工成本。

---

# 29. Cost Optimization

如果两种方案观感接近：

> 优先选择成本更低、稳定性更高的方案。

例如：

```text id="vrifd4"
方案 A：
一个较长的复杂多人物 AI 镜头。

方案 B：
多个简单完整动作段落 + 动作、视线、运动方向和声音连接，必要时再用剪辑完成精细衔接。

如果 B：
生成成功率更高
成本更低
视觉效果接近

则推荐 B。
```

---

# 30. Complexity Budget

每个项目都有：

> **复杂度预算。**

默认根据：

- 视频时长
- 项目价值
- AI 生成比例
- 交付周期
- 可用素材

决定。

并避免：

> 每个镜头都成为“视觉高潮”。

---

# 31. Visual Novelty Budget

创意视频需要新鲜感，但：

> 每个镜头都创新会造成视觉失控。

因此 Strategy 应区分：

```text id="fk7kpc"
核心视觉创新
辅助视觉变化
稳定重复元素
```

建议：

> 至少有稳定的视觉锚点贯穿。

---

# 32. Creative Constraint

一个好的 Strategy 不只是：

> “可以做什么。”

也要明确：

> “不要做什么。”

例如：

```text id="p9jfgv"
避免：
赛博朋克
过度霓虹
虚假建筑
复杂 CG
过度快速剪辑
AI 长文字
```

这样后续 Script/Storyboard/Prompt 都有统一方向。

---

# 33. AI Feasibility Strategy

对整个项目判断：

```text id="xq4f7k"
HIGH
MEDIUM
LOW
```

### HIGH

AI 可承担大部分视觉生成。

### MEDIUM

需要：

> AI + 真实素材 + 后期。

### LOW

核心价值高度依赖真实人物、真实事件、精确事实。

不能因为 LOW 就否定 AI。

而应：

> 调整 AI 的角色。

---

# 34. Strategy Alternatives

如果当前项目存在两个以上合理打法：

可以给：

```text id="up9f9n"
方案 A
方案 B
```

每个方案说明：

- 核心创意
- 优势
- 风险
- 成本
- AI 难度

默认提供：

> 1 个主推荐方案。

只有当不同方案差异足够大时，才展示多方案。

---

# 35. Strategy Recommendation

推荐方案必须说明：

```text id="w82pc8"
为什么适合这个客户
为什么适合这个受众
为什么适合这个目标
为什么适合当前素材
为什么适合当前制作条件
```

避免只说：

> “我推荐 A，因为更高级。”

---

# 36. Creative Challenge

如果客户原始方案明显不是最优：

允许提出：

```text id="8g1x0m"
Creative Challenge
```

格式：

```text id="u3yr8y"
客户要求：
……

问题：
……

为什么：
……

替代方案：
……

预计影响：
……

是否采纳：
待用户决定
```

Creative Challenge 永远属于：

> AI 建议。

---

# 37. Strategy Review

提交 Creative Strategy 时：

```text id="9qt7f5"
【创作策略】

核心传播任务：
……

Primary Type：
……

Creative Concept：
……

One-Line Idea：
……

Narrative Strategy：
……

Visual Anchor：
……

Emotional Curve：
……

AI / 实拍 / 素材 / 后期策略：
……

成本策略：
……

主要风险：
……

AI 建议：
……
```

状态：

```text id="rjrq7w"
STRATEGY · REVIEW
```

---

# 38. Strategy Quality Gate

进入 REVIEW 前必须检查：

```text id="veq7b3"
□ 是否服务 Primary Objective
□ 是否服务 Primary Audience
□ 是否有唯一 Core Proposition
□ 是否有清晰 Creative Concept
□ 是否可以视觉化
□ 是否能贯穿全片
□ 是否符合 Video Type
□ 是否与客户 Fact 冲突
□ 是否考虑已有素材
□ 是否考虑 AI 可行性
□ 是否考虑制作成本
□ 是否明确主要视觉锚点
□ 是否明确情绪路径
□ 是否存在不必要复杂度
```

---

# 39. Strategy Lock

用户确认后：

```text id="ebayp3"
CREATIVE_STRATEGY
→ LOCKED
```

Script 必须继承：

```text id="q0siw8"
Core Proposition
Creative Concept
Narrative Strategy
Visual Anchor
Emotional Strategy
Production Strategy
```

不得擅自改变。

---

# 40. Strategy → Script Interface

交给 `script.md` 的标准输入：

```yaml id="3jl6pt"
strategy_input:
  primary_type:
  secondary_type:

  strategic_objective:
  primary_audience:
  desired_action:
  core_proposition:

  creative_concept:
  one_line_idea:

  narrative_strategy:
  narrative_structure:

  emotional_strategy:
  emotional_curve:

  visual_strategy:
  visual_anchor:
  visual_language:
  camera_language:

  sound_strategy:

  asset_strategy:
  ai_strategy:
  production_strategy:

  constraints:
  risks:
```

Script 可以：

> 在此基础上继续创作。

Script 不可以：

> 无理由推翻已确认 Strategy。

---

# 41. Personal Style Integration

Personal Skill 可以影响：

```text id="zwq9vu"
Creative Concept 的表达方式
Expression Form
Visual Language
Camera Language
Emotional Tone
Sound Direction
AI / Postproduction Preference
```

但是：

> Personal Style 只能作为策略优化因素。

不得覆盖：

- 客户明确要求
- Fact Lock
- 合规约束
- 已确认核心传播目标

---

# 42. Personal Style 权重

如果项目没有明确风格：

> Personal Style 权重提高。

如果客户有明确视觉标准：

> Personal Style 权重下降。

如果客户明确要求与 Personal Style 冲突：

> 客户要求优先。

---

# 43. Strategy Change Trigger

以下变化需要重新审视 Creative Strategy：

```text id="2tb1lo"
Primary Objective 改变
Primary Audience 改变
Desired Action 改变
Core Proposition 改变
Video Type 改变
重大事实约束改变
视频时长大幅变化
主要平台改变
```

以下通常不需要重新制定 Strategy：

```text id="y4xy2j"
单个镜头修改
颜色微调
BGM变化
单句旁白修改
单个 Prompt 修改
```

---

# 44. Strategy Failure Diagnosis

当最终成片效果不好时，复盘时先判断：

```text id="4gm1hs"
Strategy Failure
Script Failure
Storyboard Failure
Prompt Failure
Production Failure
```

如果多个镜头都表现出同一问题：

> 优先怀疑 Strategy / Script。

如果只有个别镜头失败：

> 优先怀疑 Storyboard / Prompt。

---

# 45. Strategy Principle

最终遵循：

> **先确定为什么做，再确定怎么讲；先确定怎么讲，再确定看什么；先确定看什么，再决定怎么生成。**

Creative Strategy 的价值不是让 AI “想得更多”，而是：

> **让后续每一个创作决定，都围绕同一个传播目标和创意核心展开。**