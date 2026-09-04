# 星创导演 Skill 更新记录

> 本文件记录正式版本演进。每次更新追加新条目，不覆盖历史记录；当前版本以 `SKILL.md` 的 `metadata.version` 为准。

## 版本定位

- 当前版本：`1.1.1`
- 版本规则：`主版本.次版本.修订版本`
- 历史基线：0822 定稿时点的 Base 工作流与通用方法
- Personal 层：`personal/`，属于创作者/团队的个人积累，更新 Base 时必须保留

## 1.1.1 · 2026-09-04 · 跨 Agent 兼容

### 更新内容

1. 增加宿主 Agent 兼容约定，以能力映射替代固定工具名。
2. 增加缺失模态、文件和自动 Skill 发现能力时的降级规则。
3. 明确外部访问、软件安装和文件覆盖仍需遵循宿主平台权限机制。
4. 核心业务工作流、模板结构和 Personal Layer 保持不变。

## 1.1.0 · 2026-09-02 · 使用说明与版本管理

### 更新背景

为团队成员提供统一的使用入口，并让已安装 Skill 能明确当前版本和判断候选更新。

### 更新内容

1. 在 `SKILL.md` 增加语义化版本号 `1.1.0`。
2. 增加简单版本比较与更新规则。
3. 明确更新 Base 层时保留 `personal/`。
4. 新增面向团队成员的 `使用说明.html`。

### 涉及文件

- `SKILL.md`
- `使用说明.html`
- `CHANGELOG.md`
- `更新说明.html`
- `AI-Agent-更新指南.md`

### 与 Base / Personal 的关系

- Base 层新增使用说明与版本规则。
- Personal 层未修改，后续更新继续保留。

### 检查结果

- 版本号、更新记录与用户说明统一为 `1.1.0`。
- 原有工作模式、阶段状态、模板和 Personal 内容保持不变。

### 是否需要团队确认

可作为团队当前稳定版本分发。

## 0822 · 首次发布定稿

### 本次更新

1. 建立独立发布目录，原始版保持不变。
2. 工作模式统一为：
   - `A｜协作模式`：Brief、Strategy、Script、Storyboard、Prompt 等关键节点逐步确认。
   - `B｜极速模式`：自动完成完整流程，仅在 P0、严重事实冲突、高风险方案或无法合理推断时暂停。
3. 新视频需求启动时必须先询问工作模式；新类型建议协作模式，同类型系列视频可选择极速模式。
4. 删除半自动模式及其相关描述。
5. 统一所有镜头必须输出 AI 生成提示词；即使主要制作路径不建议纯 AI，也要提供参考/兜底 Prompt，并附建议、风险和替代方案。
6. 连续叙事优先使用较完整的生成时长，补充起始状态、动作过程、结束状态和剪辑衔接设计；平台具体能力以当前页面和账号权限为准。
7. 强化环境、人物、物品的一致性管理：视觉资产锚点、参考素材职责、跨镜头状态交接和一致性质量检查。
8. 为介绍、说明、讲解、成果展示类视频增加旁白机制：资料检索、事实核验、逐段旁白、时长核算、画面接口和旁白质量门。
9. 增加最终生产包模板和批量 Prompt 交付表，便于团队执行和交付。
10. 弱化制作路径的字母编号，改以“主要制作路径”描述 AI、参考素材与后期的组合关系。
11. 清理固定的平台素材数量、时长和功能表述，改为以当前平台页面和账号权限为准。

### 涉及文件

- `SKILL.md`
- `references/terminology.md`
- `references/workflow.md`
- `references/seedance.md`
- `references/production-strategy.md`
- `references/quality.md`
- `references/visual-assets.md`
- `references/storyboard.md`
- `references/script.md`
- `references/voiceover.md`
- `references/creative-strategy.md`
- `templates/storyboard/storyboard-template.md`
- `templates/script/script-template.md`
- `templates/prompt/prompt-single-shot.md`
- `templates/prompt/prompt-multi-shot.md`
- `templates/prompt/prompt-delivery-table.md`
- `templates/final/final-package-template.md`
- 介绍页与文档关系图

### 定稿检查

- 正式执行文件中不存在半自动模式或旧的 C 极速编号。
- Personal 层目录完整保留。
- 原始版未修改。
- 新增模板已在 `SKILL.md` 的 Reference 文件地图中登记。
- 规则文件之间保持：工作模式、状态机、所有镜头 Prompt、旁白和主要制作路径的口径一致。

## 后续版本记录格式

新增版本时，按以下结构追加：

```markdown
## 版本号 · 日期 · 简短主题

### 更新背景

### 更新内容

### 涉及文件

### 与 Base / Personal 的关系

### 检查结果

### 是否需要团队确认
```
