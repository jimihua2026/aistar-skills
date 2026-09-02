# script.md

# Script Design Protocol

## 1. 文件定位

`script.md` 定义 `aistar-director` 如何将已确认的 Requirement、Video
Type 和 Creative Strategy 转化为可执行的视频脚本。

流程：

``` text
Requirement
↓
Video Type
↓
Creative Strategy
↓
Script
↓
Storyboard
↓
Seedance Prompt
```

Script 的职责：

-   将传播策略转化为视频叙事
-   明确观众听什么、看什么、感受什么
-   为分镜设计提供结构基础

Script 不负责：

-   具体镜头编号
-   摄影参数
-   Seedance Prompt

------------------------------------------------------------------------

# 2. Script 核心原则

## 2.1 Script 不是文字稿

但对介绍、说明、讲解和成果展示类视频，Script 必须同时包含可配音的分段旁白。旁白不是把资料堆成文章，而是经过事实核验、信息取舍和时长控制后的声音轨道文本。

企业视频脚本不能只是旁白文章。

优秀 Script 必须回答：

-   观众听到什么？
-   观众看到什么？
-   观众理解什么？
-   观众感受到什么？

------------------------------------------------------------------------

# 3. 三层结构

## Macro Layer

定义整支视频：

-   总时长
-   叙事结构
-   情绪曲线
-   信息节奏

## Section Layer

定义完整传播阶段：

-   目标
-   核心信息
-   情绪
-   内容任务

## Beat Layer

最小叙事单元：

-   Purpose
-   Narration
-   Visual Intention
-   Information Type
-   Emotion
-   Sound Direction
-   AI Generation Note

------------------------------------------------------------------------

# 4. Script 标准结构

``` yaml
script:
  title:
  duration:
  creative_concept:
  narrative_structure:
  sections:
    - section_id:
      objective:
      emotion:
      key_message:
      beats:
        - beat_id:
          purpose:
          narration:
          visual_intention:
          information_type:
          emotion:
          sound_direction:
          ai_generation_note:
```

------------------------------------------------------------------------

# 5. Strategy 继承规则

Script 必须继承：

-   Core Proposition
-   Creative Concept
-   Narrative Strategy
-   Visual Anchor
-   Emotional Curve
-   Production Strategy

如果 Script 改变核心传播逻辑，需要重新确认 Creative Strategy。

------------------------------------------------------------------------

# 6. Beat 编写规则

每个 Beat 必须说明：

## Purpose

为什么存在。

## Narration

旁白或对白。

要求：

-   自然
-   简洁
-   避免 PPT 语言

## Visual Intention

描述画面目的，而不是简单列素材。

例如：

错误：

> 展示工厂

正确：

> 通过自动化生产线表现效率提升和技术价值。

------------------------------------------------------------------------

# 7. 介绍类内容与旁白

当需求属于介绍、说明、讲解或成果展示时：

1. 先从客户资料提取可确认事实。
2. 资料不足以支撑介绍时，检索官网、官方公告、官方报告及权威行业资料。
3. 将检索结果逐条标注来源、发布日期/检索日期和核验状态。
4. 每个段落生成旁白文字，并注明该段的主要信息任务。
5. 旁白与画面形成互补，避免逐字描述屏幕上已经出现的内容。
6. 未核验内容只能作为“待核验草案”，不能混入正式旁白。

详细的检索、核验、朗读时长和旁白交付字段见 `references/voiceover.md`。

# 8. 信息表达方式

信息可以通过：

-   Voice
-   Visual
-   Text
-   Graphic
-   Human

表达。

选择原则：

让最适合的媒介承担信息。

------------------------------------------------------------------------

# 9. AI Friendly Script 原则

## 一个 Beat 一个主要动作

避免一个镜头包含多个复杂事件。

## 抽象概念视觉化

不要写：

> 展示数字经济发展

应写：

> 展示企业、物流和数据系统之间形成连接。

## 精确信息交给后期

以下内容不要依赖 AI：

-   中文文字
-   Logo
-   UI
-   政策文件
-   精确数据

------------------------------------------------------------------------

# 10. 不同类型脚本重点

## 品牌认知型

重点：

价值、身份、愿景。

## 产品服务型

重点：

问题、解决方案、收益、行动。

## 招商投资型

重点：

机会、条件、证明、未来。

## 项目成果型

重点：

背景、过程、结果、证据。

## 人物信任型

重点：

人物、经历、选择、变化。

------------------------------------------------------------------------

# 11. Script Review

生成后进入：

`SCRIPT · REVIEW`

用户可以：

-   确认
-   确认并继续
-   修改
-   重新生成

------------------------------------------------------------------------

# 12. Script Quality Gate

检查：

-   是否符合 Creative Strategy
-   是否有明确核心命题
-   是否有完整叙事结构
-   是否存在情绪变化
-   是否有视觉方向
-   是否符合 AI 生成能力
-   是否考虑制作成本
-   是否没有提前锁死分镜

------------------------------------------------------------------------

# 13. Script → Storyboard Interface

输出：

``` yaml
script_output:
  core_proposition:
  creative_concept:
  emotional_curve:
  sections:
    - section_id:
      objective:
      beats:
        - beat_id:
          narration:
          visual_intention:
          emotion:
          information_type:
          required_assets:
```

------------------------------------------------------------------------

# 最终原则

> 策略决定方向，脚本决定叙事，分镜决定视觉，Prompt 决定生成。

好的 Script 不是文字最多，而是让导演、剪辑师和 AI
模型同时理解这支片为什么这样做。
