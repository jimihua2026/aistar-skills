# `references/terminology.md`

# Terminology & ID Protocol

本文档定义 `aistar-director` 全系统统一使用的术语、ID 命名规则、
状态定义与字段约定。

其他模块不得自行定义与本文冲突的术语或 ID 规则。
当各 reference 文件出现命名歧义时，以本文为准。

---

# 1. 核心对象术语

| 术语 | 英文 | 定义 |
| --- | --- | --- |
| 项目 | Project | 一次完整的视频制作任务 |
| 需求文档 | Brief | 客户需求的结构化产物 |
| 创作策略 | Creative Strategy | 视频类型、叙事、视觉与制作策略的总决策 |
| 脚本 | Script | 视频的叙事设计（讲什么、为什么这样讲） |
| 段落 | Section | 脚本中的完整传播阶段 |
| 节拍 | Beat | 脚本的最小叙事单元 |
| 视觉资产库 | Visual Asset Library | 项目全部稳定视觉元素的注册表 |
| 资产 | Asset | 人物 / 场景 / 产品 / 道具 / 参考素材 |
| 锚点 | Anchor | 决定"同一性"的关键视觉特征 |
| 分镜 | Storyboard | 镜头级的视觉执行设计 |
| 序列 | Sequence | 对应 Script Section 的镜头组 |
| 镜头 | Shot | 观众连续看到的一段画面 |
| 生成单元 | Generation Unit | 针对 AI 生成拆分后的最小执行单元 |
| 制作策略 | Production Strategy | 每个镜头的制作方式决策（AI/素材/后期） |
| 提示词 | Prompt | 可直接用于 Seedance / 即梦的生成指令 |
| 生产包 | Final Production Package | 项目最终交付物集合 |
| 复盘 | Retrospective | 项目完成后的经验提取 |
| 个人进化层 | Personal Layer | 属于当前创作者的规则、偏好、案例与风格 |

---

# 2. 阶段名称

项目阶段统一使用以下名称（与 `workflow.md` 一致）：

```text
INPUT          原始需求输入
BRIEF          需求结构化
STRATEGY       视频类型与创作策略
SCRIPT         生产型脚本
ASSETS         视觉资产规划
STORYBOARD     AI 生产分镜
PRODUCTION     制作策略
PROMPT         Seedance Prompt 工程
FINAL          最终生产包
RETROSPECTIVE  项目复盘
EVOLUTION      个人进化
```

---

# 3. ID 命名规则

## 3.1 叙事与镜头 ID

| 前缀 | 对象 | 格式 | 示例 |
| --- | --- | --- | --- |
| `SEC` | 脚本段落 | `SEC-NN` | SEC-04 |
| `BEAT` | 脚本节拍 | `BEAT-NN-NN` | BEAT-04-02 |
| `SEQ` | 分镜序列 | `SEQ-NN` | SEQ-04 |
| `SHOT` | 镜头 | `SHOT-NN-NN` | SHOT-04-02 |
| `PROMPT` | 生成提示词 | `PROMPT-NN-NN-VN` | PROMPT-04-02-V1 |

编号规则：

- `SEC` / `SEQ` 的第一段编号一一对应（SEQ-04 对应 SEC-04）。
- `SHOT-04-02` 表示第 4 序列的第 2 个镜头。
- `PROMPT-04-02-V1` 表示 SHOT-04-02 的 Prompt 第 1 版。
- 一个 Shot 拆成多个 Generation Unit 时，追加字母：`PROMPT-04-02A-V1`、`PROMPT-04-02B-V1`。

## 3.2 视觉资产 ID

| 前缀 | 类别 | 示例 |
| --- | --- | --- |
| `CHR` | 人物 | CHR-01 |
| `SC` | 场景 | SC-01 |
| `PRD` | 产品 | PRD-01 |
| `OBJ` | 道具 | OBJ-01 |
| `IMG` | 参考图片 | IMG-01 |
| `VID` | 参考视频 | VID-01 |
| `AUD` | 参考音频 | AUD-01 |

规则：

1. ID 项目内唯一，建立后不得复用、不得改指。
2. 资产废弃标记 `deprecated`，编号保留。
3. 在 Prompt 中以 `@资产ID` 形式引用（如 `@IMG-01`）。

## 3.3 变更与进化 ID

| 前缀 | 对象 | 示例 |
| --- | --- | --- |
| `CR` | 需求变更（Change Request） | CR-03 |
| `SUG` | 进化建议（Suggestion） | SUG-2026-08-03 |
| `P-RULE` | 个人规则 | P-RULE-018 |
| `P-CASE` | 个人案例 | P-CASE-007 |

---

# 4. 双向追踪链

所有对象保持追踪关系：

```text
SEC-04
↕
SEQ-04 → SHOT-04-02
↕
PROMPT-04-02-V1
↕
引用资产：CHR-01 / SC-02 / IMG-01
```

用户反馈某个镜头失败时，沿追踪链定位问题层：

```text
Prompt 问题
Storyboard 问题
Script 问题
Brief 问题
```

---

# 5. 状态机

## 5.1 阶段对象状态

```text
DRAFT       草稿，Skill 生成中
REVIEW      待用户确认
LOCKED      用户已确认，锁定
COMPLETED   项目整体完成
```

## 5.2 用户动作

```text
MODIFY                局部修改
BACK                  返回上一阶段
APPROVE               确认并锁定，不自动进入下一阶段
APPROVE_AND_CONTINUE  确认并锁定，立即进入下一阶段（默认主推）
```

## 5.3 工作模式

```text
A｜协作模式    每个关键节点等待用户确认
B｜极速模式    全自动，仅在 P0 / 严重冲突 / 高风险时暂停
```

新视频制作需求启动时，必须先询问用户选择 A｜协作模式或 B｜极速模式：

- 新的视频类型、首次制作或需求不清晰：建议 A｜协作模式。
- 已验证的同类型系列视频、需求结构稳定或沿用成熟模板：可选择 B｜极速模式。

## 5.4 个人规则状态

```text
CANDIDATE   候选（复盘提出）
ACTIVE      已采纳，直接生效
DEPRECATED  已删除 / 降级
```

---

# 6. 信息来源标签

重要信息必须标注来源：

| 标签 | 定义 |
| --- | --- |
| `客户明确要求` | 客户直接表达，应作为项目要求执行 |
| `基于客户信息推导` | 根据客户信息合理推导（不得伪装成客户明确要求） |
| `AI 建议` | 基于专业经验主动提出的方案 |
| `AI 默认假设` | 对 P1/P2 缺失信息采用的默认值 |
| `待确认` | 无法可靠判断，继续假设可能影响项目结果 |

---

# 7. 优先级体系

冲突时统一采用：

```text
客户明确要求 / Fact Lock
>
合规约束
>
已确认项目创意方向
>
Base Skill Rules
>
Personal Rules
>
Personal Preferences
>
AI 默认建议
```

流程与创作冲突时：

```text
Workflow Integrity
>
Fact Integrity
>
User Decision
>
Creative Optimization
```

---

# 8. 风格优先级链

风格字段（色彩、光线、质感、节奏等）发生冲突时：

```text
客户明确品牌 / 项目要求
>
项目创意方向（已锁定 Creative Strategy）
>
视频类型推荐策略
>
个人风格偏好（Personal Style Profile）
>
Prompt 默认表达
```

个人风格永远不能覆盖客户明确要求，
只在项目未明确指定时发挥作用。

---

# 9. 制作方式分类

| 分类 | 名称 | 定义 |
| --- | --- | --- |
| `A` | 直接 AI 生成 | 无需参考素材的纯 AI 镜头 |
| `B` | AI + 参考素材 | AI 生成，参考图/视频锁定外观或动作 |
| `C` | AI + 后期 | AI 生成主体，精确信息后期叠加 |
| `D` | 不建议 AI | 实拍 / 客户素材 / 素材库 / 纯后期 |

---

# 10. Prompt 模式

| 模式 | 名称 |
| --- | --- |
| `SINGLE_SHOT` | 单镜头生成 |
| `MULTI_SHOT` | 多镜头连续生成 |
| `IMAGE_TO_VIDEO` | 图生视频 |
| `MULTIMODAL_REFERENCE` | 多模态参考生成 |
| `VIDEO_EXTEND` | 视频延长 |
| `VIDEO_EDIT` | 视频编辑/修改 |

Prompt 复杂度分级：`L1`（简单单镜头）→ `L4`（高风险，建议拆镜）。

---

# 11. 视频类型

八大母类型（详见 `video-types.md`）：

```text
品牌认知型
产品/服务转化型
项目/成果证明型
招商/投资/政务说服型
人物/信任型
人才/组织型
知识/培训/政务服务型
活动/传播型
```

类型判断统一输出：

```text
主类型      决定"讲什么"
次类型      决定"强调什么"
表达形式    决定"怎么讲"
```

---

# 12. 完整性分级

Brief 信息缺口分级（详见 `requirement.md`）：

```text
P0  缺失则原则上不能继续
P1  建议确认，但可以继续
P2  由 AI 合理补全，标注"AI 默认假设"
```

---

# 13. 质量门问题分级

质量门发现的问题统一分级（详见 `quality.md`）：

```text
BLOCKING  必须处理，否则不得进入 REVIEW / 下一阶段
WARNING   记录但可以继续，需向用户明确提示
```

---

# 14. 锚点强度

```text
强锚点  不能轻易变化（人物面部、服装、产品外形、主要建筑）
弱锚点  允许自然变化（桌面小物件、远景人员、背景细节）
```

突破强锚点必须标记 `anchor_break` 并经用户确认。

---

# 15. Fact 与 Creative 的边界

项目内容分为两类，待遇完全不同：

## Fact（事实，进入 Fact Lock）

```text
公司名称 / 产品名称 / 人物姓名 / 人物身份 / 项目名称 /
项目数据 / 政策内容 / 地址 / 建筑 / 业务事实 /
技术参数 / 客户案例 / 品牌资产
```

Fact 不得由 AI 或 Personal Rule 自行修改、补造、美化。

## Creative（创意，可自由创作）

```text
叙事方式 / 镜头设计 / 运镜 / 光线 / 色彩 /
情绪 / 构图 / 视觉隐喻 / 场景氛围
```

Creative 可以由 AI 合理创作，受创作策略与个人风格影响。

---

# 16. Fact Lock

以下内容自动视为高优先级事实，AI 不得修改、补造或美化：

```text
公司 / 产品 / 人物 / 项目 / 数据 / 政策
建筑 / 地址 / 参数 / 案例 / 品牌资产
```

无法确认的事实标记 `待确认`，禁止凭空补造。

---

# 17. 版本规则

所有阶段对象采用版本号：

```text
brief_version: V1, V2, ...
strategy_version: V1, V2, ...
script_version: V1, V2, ...
storyboard_version: V1, V2, ...
prompt_version: PROMPT-NN-NN-VN
```

- 每次修改产生新版本，旧版本保留可回溯。
- 锁定的是特定版本，不是抽象对象。
- Personal Layer 独立版本化（如 Personal Profile v1.7）。
