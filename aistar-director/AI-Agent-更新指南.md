# 星创导演 Skill 更新指南（供 AI Agent 使用）

## 目的

在未来更新星创导演 Skill 时，保持版本可追溯、Base 与 Personal 分层清晰，并确保更新后整体可运行。本文是给 AI Agent 的执行指南，不是团队阅读版更新说明。

当前版本以 `SKILL.md` frontmatter 中的 `metadata.version` 为准，本版为 `1.1.0`。版本号采用 `主版本.次版本.修订版本`：不兼容变化升级主版本，向后兼容的新能力升级次版本，修复与文字澄清升级修订版本。

## 一、目录与分层

```text
基础版（禁止修改）：原始目录 / aistar-director/
当前发布版（允许更新）：发布目录 / aistar-director-0822/
```

目录名可由团队成员放置在各自工作区；以当前会话中实际打开的发布目录为准，不要写死本机盘符或用户目录。

发布版内部：

- Base 层：`SKILL.md`、`references/`、`templates/`、`examples/` 及公共说明文件。
- Personal 层：`personal/`。包含个人规则、偏好、案例、风格画像和进化记录。
- 版本判断：`SKILL.md` 的 `metadata.version`。
- 版本记录：`CHANGELOG.md`、`更新说明.html`、本文件。

默认只更新发布版 Base 层。除非用户明确要求，不修改基础版，不删除文件，不覆盖 Personal 层。

检查候选新版时，按数值逐段比较双方 `metadata.version`。只有候选版本更高才更新；候选版本相同、较低或缺少版本号时停止并报告。更新完成后重新读取已安装版版本号，确认更新成功。

## 二、收到更新需求后的标准流程

### 1. 读取上下文

先读取：

```text
SKILL.md
references/terminology.md
references/workflow.md
CHANGELOG.md
personal/personal-rules.md
personal/personal-preferences.md
```

再按需求读取相关 reference 和 template，不要一次加载全部文件。

### 2. 判断更新范围

将需求归入：

- Base 规则：更新 `SKILL.md` 或 `references/`。
- 输出结构：更新 `templates/`。
- 团队示例：更新 `examples/`。
- Personal 经验：只有用户明确采纳或明确要求时，才更新 `personal/`。
- 版本记录：每次正式更新都更新 `CHANGELOG.md` 和 `更新说明.html`。

若需求同时影响 Base 和 Personal，先修改 Base，再检查 Personal 是否仍兼容；不要为了融合而擅自重写 Personal 内容。

### 3. 建立变更计划

在修改前列出：

```text
更新目标：
涉及 Base 文件：
涉及 Template 文件：
涉及 Examples / 展示文件：
Personal 层是否修改：默认否
不应改变的既有规则：
可能影响的下游：
```

只实施用户确认的范围，不顺便加入未确认的新功能。

### 4. 修改并保持融合

遵守以下优先级：

```text
用户明确要求 / Fact Lock
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

检查重点：

- Base 的新规则不能与 `workflow.md` 的状态机、确认、锁定、回退、版本机制冲突。
- 新字段必须能接入现有的 Brief → Strategy → Script → Assets → Storyboard → Production → Prompt → Final 链路。
- 新规则不能绕过用户确认、Fact Lock 或已锁定内容保护。
- 新模板字段必须有对应的生成规则或质量门；不要只增加空字段。
- Personal 层内容保持原样，并检查新 Base 规则是否会覆盖其合法偏好。
- 如果 Base 与 Personal 出现冲突，按优先级处理并在更新记录中说明，不直接删除 Personal 内容。
- 保持所有镜头都输出 Prompt 的团队硬性要求。
- 保持 A｜协作模式、B｜极速模式的工作模式编号；不要恢复半自动模式或旧编号。
- 制作路径是镜头执行建议，不要与工作模式混淆，也不要擅自恢复字母化强调。

### 5. 更新记录

在 `CHANGELOG.md` 末尾追加，不覆盖历史：

```markdown
## 版本号 · 日期 · 简短主题

### 更新背景

### 更新内容

### 涉及文件

### 与 Base / Personal 的关系

### 检查结果

### 是否需要团队确认
```

同步更新 `更新说明.html`，面向团队只写：背景、主要变化、使用影响、定稿边界；不要把内部推理和长篇规则复制进去。

## 三、更新后的合理性检查

### 结构检查

- `SKILL.md` 的 Reference 文件地图是否包含新增文件。
- 所有被引用的路径是否实际存在。
- 新增模板是否位于正确目录。
- YAML、Markdown、HTML 是否无明显格式破坏。
- Personal 目录及文件数量、内容是否被意外修改。

### 规则检查

- 工作模式是否只有 A 协作、B 极速。
- 协作模式是否在关键阶段等待确认。
- 极速模式是否自动推进并只在关键问题暂停。
- 状态是否遵循 `DRAFT → REVIEW → LOCKED → COMPLETED`。
- 修改、回退、需求变更是否保留版本历史。
- 是否存在下游擅改已锁定内容的描述。
- 所有镜头是否仍须输出 Prompt。
- 旁白、资产一致性、起止状态、转场和后期分工是否能与现有链路衔接。
- 平台动态能力是否被错误写成永久固定限制。

### 冗余与冲突检查

搜索并处理：

```text
半自动
Mode C
C｜极速
A/B/C/D（若指工作模式或制作路径编号）
```

注意：视频类型自身的 A/B/C/D 等分类不属于工作模式，不要误删。检查“制作路径”相关内容是否已采用自然语言表述。

### 交付检查

- `CHANGELOG.md` 有本次更新条目。
- `更新说明.html` 与 Markdown 口径一致。
- 当前版本目录可作为完整发布目录使用。
- 原始版未修改。
- Personal 层保留且未被 Base 更新覆盖。

## 四、禁止事项

1. 不修改 `aistar-director` 基础版。
2. 不删除旧版本记录或 Personal 内容。
3. 不把 AI 推断写成客户事实。
4. 不把新增建议伪装成用户已确认规则。
5. 不因局部修改重写整个 Skill。
6. 不恢复已删除的半自动工作模式。
7. 不把镜头制作路径编号误当成工作模式编号。
8. 不以“整体优化”为理由加入未确认的新功能。
9. 不在检查未完成前宣布版本可发布。

## 五、最终报告格式

更新完成后，向用户报告：

```text
版本：
已更新文件：
Base 层变化：
Personal 层：保留 / 经明确要求修改
原始版：未修改
检查结果：
仍待确认的问题：
```
