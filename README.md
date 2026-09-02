# Aistar Skills

面向 AI 视频创作的 Codex Skill 集合，包含创作策划与参考视频镜头解构两项能力。

## Skills

| Skill | 中文名称 | 当前版本 | 用途 |
| --- | --- | --- | --- |
| `aistar-director` | 星创导演 | 1.1.0 | 将文字、表格、文件、图片或语音需求转化为 Brief、创作策略、生产型脚本、AI Production Storyboard 和视频生成提示词。 |
| `shot-deconstruction` | 镜头解构 | 1.2.0 | 拆解参考 AI 视频镜头，并为每个镜头生成可独立使用的纯文字复刻提示词。 |

## 安装

### 使用 Codex Skill Installer

仓库公开后，可在 Codex 中调用 `$skill-installer`，并要求安装：

```text
从 https://github.com/jimihua2026/aistar-skills 安装 aistar-director 和 shot-deconstruction
```

### 手动安装

1. 克隆仓库：

   ```powershell
   git clone https://github.com/jimihua2026/aistar-skills.git
   ```

2. 将需要的 Skill 目录复制或链接到个人 Skill 目录：

   ```text
   $HOME/.agents/skills/
   ```

3. 如果 Skill 没有立即出现，重启 Codex。

## 使用

在 Codex 中显式调用：

```text
$aistar-director 为这个企业宣传片项目整理 Brief 和生产型脚本
$shot-deconstruction 拆解这段参考视频并生成逐镜头复刻提示词
```

当请求与 Skill 的 `description` 匹配时，Codex 也可以自动选择相应 Skill。

## 依赖与兼容性

- `aistar-director` 以说明、参考资料和模板为主，不要求额外运行时。
- `shot-deconstruction` 需要 FFmpeg 与 FFprobe，用于读取视频元数据、生成分析代理和抽取关键帧。
- 两个 Skill 都需要在工作区写入结果文件；实际可用能力受 Codex 所在环境及权限配置影响。

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
- 普通问题和功能建议可通过 GitHub Issues 提交。
- 安全问题请按照 [SECURITY.md](SECURITY.md) 处理。
- 贡献代码前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 第三方说明

文档中出现的 Seedance、即梦、FFmpeg 及其他产品或商标，仅用于说明适用工具和兼容场景。本项目与这些产品的权利人不存在隶属、授权、赞助或官方背书关系。

## 许可证

本项目使用 [MIT License](LICENSE)。

