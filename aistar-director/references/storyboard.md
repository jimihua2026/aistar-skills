# storyboard.md

# Storyboard Design Protocol

## 文件定位

`storyboard.md` 定义 `aistar-director` 如何将 Requirement、Video
Type、Creative Strategy 和 Script 转化为可执行的视频分镜。

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

Storyboard 的核心任务：

> 将脚本中的叙事单元转化为具体可视化镜头。

------------------------------------------------------------------------

## Storyboard 三层结构

``` text
Sequence
↓
Shot
↓
Generation Unit
```

### Sequence

对应 Script Section，描述完整叙事阶段。

### Shot

观众连续看到的一段画面。

### Generation Unit

针对 AI 视频生成拆分后的最小生成单元。

------------------------------------------------------------------------

## Shot 六要素模型

每个镜头必须回答：

``` text
WHO
WHERE
DO WHAT
HOW
WHY
FEEL
```

对应：

-   Subject
-   Environment
-   Action
-   Camera
-   Purpose
-   Emotion

------------------------------------------------------------------------

## Storyboard 标准结构

``` yaml
storyboard:
  project_title:
  total_duration:

  sequences:
    - sequence_id:
      purpose:
      emotion:
      visual_theme:

      shots:
        - shot_id:
          duration:
          script_reference:
          shot_purpose:
          visual_description:
          subject:
          environment:
          action:
          camera:
          composition:
          lighting:
          color:
          emotion:
          sound:
          transition:
          start_state:          # 生成开始时的主体、空间和摄影机状态
          action_timing:        # 动作触发 → 展开 → 完成
          end_state:            # 生成结束时的稳定画面状态
          edit_in_out:          # 可剪辑的入点、出点和与下一镜衔接方式
          ai_feasibility:
          generation_notes:
```

------------------------------------------------------------------------

## AI 视频分镜原则

### 一个镜头一个核心动作

避免一个镜头同时包含多个复杂事件。

### 动作优先

不要只描述静态对象，要描述主体正在发生什么。

### 控制复杂度

优先：

-   单主体
-   单动作
-   清晰环境

谨慎：

-   多人物互动
-   复杂机械操作
-   精确文字

------------------------------------------------------------------------

## Storyboard → Seedance Prompt

转换关系：

``` text
Storyboard
=
导演语言

Seedance Prompt
=
模型语言
```

Storyboard 提供：

-   内容
-   结构
-   视觉目标

Prompt 负责：

-   生成描述
-   风格控制
-   动作控制
-   一致性控制

------------------------------------------------------------------------

## Quality Gate

进入 Prompt 阶段前检查：

-   是否继承 Script
-   是否符合 Creative Strategy
-   每个镜头是否有目的
-   是否容易想象成片
-   是否符合 AI 能力
-   是否控制制作成本
-   是否具备视觉连续性

------------------------------------------------------------------------

## Final Principle

> 脚本决定为什么拍，分镜决定拍什么，Prompt 决定怎么生成。

优秀 Storyboard 的标准：

不是镜头数量最多，而是每一个镜头都有存在理由，并且能被导演、剪辑师和 AI
模型同时理解。
