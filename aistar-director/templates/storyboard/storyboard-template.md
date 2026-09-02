# Storyboard Template

> 本模板只定义 Storyboard 的输出结构；分镜规则、资产引用和制作路径判断分别见对应 reference 文件。
> 状态标记：`STORYBOARD V{N} · DRAFT / REVIEW / LOCKED`

---

## 《{项目名} · AI Production Storyboard》

### 0. 总览

| 字段 | 内容 |
| --- | --- |
| 项目（project_title） | |
| 总时长（total_duration） | |
| 序列数 / 镜头数 | |
| 引用的视觉资产 | CHR / SC / PRD / OBJ / IMG / VID / AUD 清单 |

---

### 1. 镜头规划表（先总后分）

| SHOT ID | 时长 | 段落 | 内容一句话 | 景别 | 主要制作路径 | AI 适配度 | 复杂度 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SHOT-01-01 | 4s | SEC-01 | | | | ★★★★☆ | ★★☆☆☆ |

---

### 2. 详细分镜

## SEQ-01｜{序列名}（对应 SEC-01）

| 字段 | 内容 |
| --- | --- |
| 序列目的（purpose） | |
| 情绪（emotion） | |
| 视觉主题（visual_theme） | |
| 时间轴节奏 | 如：0-4s 快速建立 / 4-9s 稍慢 / 9-14s 加速 / 14-18s 停顿落版 |

### SHOT-01-01

| 字段 | 内容 |
| --- | --- |
| 时间 | 0-4s |
| 脚本引用（script_reference） | BEAT-01-01 |
| 镜头目的（shot_purpose） | 这个镜头为什么存在 |
| 画面描述（visual_description） | 观众具体看到什么 |
| 主体（subject） | @CHR-01 |
| 主体动作（action） | 一个主动作 |
| 场景/空间（environment） | @SC-01，主体与空间的关系 |
| 景别/构图（composition） | 特写/近景/中景/全景/航拍 |
| 机位/视角 | |
| 运镜（camera） | 一个主要运镜，说明为什么这样动 |
| 旁白/台词 | 对应脚本文案 |
| 声音（sound） | 环境声 / 音效 / BGM / 人声 |
| 光线 / 色彩 | 继承视觉锚点 |
| 情绪（emotion） | |
| 参考资产 | @IMG-01（人物外观）等，每个注明职责 |
| 连续性/转场（transition） | 与前后镜头的关系 |
| 主要制作路径 | 直接 AI / AI + 参考素材 / AI + 后期修正 / 不建议纯 AI；无论路径如何均须输出提示词，并在必要时标注建议、风险、适用边界和替代方案 |
| AI 适配度（ai_feasibility） | ★～★★★★★ |
| AI 复杂度 | ★～★★★★★ + 原因 |
| AI 风险 | |
| 后期建议（generation_notes） | |
| fallback | AI 失败时的备用方案 |

### SHOT-01-02

（同上结构）

---

## SEQ-02｜{序列名}

（同上结构）

---

### 3. 质量门结论

> 叙事 / 冗余 / 连续性 / 可执行性 / 景别 / 节奏 / 复杂度
> （检查项见 `references/quality.md` Gate 5）

### 用户操作

```text
【确认】【确认并继续】【修改】【退回上一步】
```
