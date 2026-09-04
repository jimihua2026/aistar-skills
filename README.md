# Aistar Agent Skills

面向 AI 视频创作的开放 Agent Skills 集合，包含创作策划与参考视频镜头解构两项能力。当前版本已在 Codex 验证，也可用于支持 Agent Skills 目录结构的其他 AI Agent；不支持该标准的平台可以手动加载 `SKILL.md` 及其引用资源。

## Skills

| Skill | 中文名称 | 当前版本 | 用途 |
| --- | --- | --- | --- |
| `aistar-director` | 星创导演 | 1.1.1 | 将文字、表格、文件、图片或语音需求转化为 Brief、创作策略、生产型脚本、AI Production Storyboard 和视频生成提示词。 |
| `shot-deconstruction` | 镜头解构 | 1.2.1 | 拆解参考 AI 视频镜头，并为每个镜头生成可独立使用的纯文字复刻提示词。 |

## 安装

### 支持 Agent Skills 的平台

1. 克隆或下载本仓库。
2. 将所需 Skill 的完整目录放入宿主 Agent 规定的 Skill 目录。
3. 保持 `SKILL.md`、`references/`、`templates/` 和其他引用资源的相对位置不变。
4. 按宿主 Agent 的方式重新加载 Skill；必要时重启 Agent。

不同 Agent 的安装目录和显式调用语法并不统一，应以对应平台的当前文档为准。

### Codex

仓库公开后，可在 Codex 中调用 `$skill-installer`，并要求安装：

```text
从 https://github.com/jimihua2026/aistar-skills 安装 aistar-director 和 shot-deconstruction
```

也可以手动克隆仓库，再把所需 Skill 目录复制或链接到：

```text
$HOME/.agents/skills/
```

### 不支持 Agent Skills 的平台

将目标 Skill 的 `SKILL.md` 作为项目指令或系统指令加载，并允许 Agent 按需读取同目录中的 `references/` 与 `templates/`。这种方式可以复用核心工作流，但自动触发、资源路由、长期个人层和工具调用能力取决于宿主平台。

## 使用

不同平台可以显式选择 Skill、让 Agent 按 `description` 自动匹配，或直接要求 Agent 遵循对应 `SKILL.md`。Codex 示例：

```text
$aistar-director 为这个企业宣传片项目整理 Brief 和生产型脚本
$shot-deconstruction 拆解这段参考视频并生成逐镜头复刻提示词
```

完整支持范围和降级行为见 [COMPATIBILITY.md](COMPATIBILITY.md)。

## 依赖与兼容性

- `aistar-director` 以说明、参考资料和模板为主，不要求额外运行时。
- `shot-deconstruction` 需要 FFmpeg 与 FFprobe，用于读取视频元数据、生成分析代理和抽取关键帧。
- 两个 Skill 都需要在工作区写入结果文件；实际可用能力受宿主 Agent 的文件、多模态、命令执行和权限机制影响。

## 个人数据

`aistar-director/personal/` 是每位使用者的本地个人层，用于保存偏好、规则、案例和进化记录：

- 该目录中的个性化文件默认由 Git 忽略，不会提交到本仓库。
- 首次需要个人层时，按照 `personal/README.md` 从 `templates/personal/` 初始化。
- 不要在 Issue、Pull Request 或示例中提交客户资料、未公开项目内容、访问凭据或个人敏感信息。

## 更新

```powershell
git pull --ff-only
```

更新 Base Skill 时，应保留本地 `personal/` 内容。提交自己的修改前，请先运行隐私与凭据检查。

## 版本与反馈

- 仓库级版本使用 `vX.Y.Z` 标签。
- 每个 Skill 的版本记录在其 `SKILL.md` frontmatter 中。
- 仓库更新记录见 [CHANGELOG.md](CHANGELOG.md)。
- 普通问题和功能建议可通过 GitHub Issues 提交。
- 安全问题请按照 [SECURITY.md](SECURITY.md) 处理。
- 贡献代码前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 第三方说明

文档中出现的 Seedance、即梦、FFmpeg 及其他产品或商标，仅用于说明适用工具和兼容场景。本项目与这些产品的权利人不存在隶属、授权、赞助或官方背书关系。

## 许可证

本项目使用 [MIT License](LICENSE)。
