# Contributing

## 提交问题

Issue 应包含复现步骤、期望结果、实际结果、Codex 使用环境以及相关 Skill 版本。请使用脱敏后的示例，不要上传客户素材或访问凭据。

## 提交修改

1. 从最新 `main` 分支创建独立分支。
2. 只修改与问题直接相关的 Skill 或文档。
3. 确认 `SKILL.md` frontmatter 中包含有效的 `name` 和 `description`。
4. 确认新增引用能从 `SKILL.md` 或相关文档中找到。
5. 运行 Skill 校验，并检查提交内容和 Git 历史中没有敏感信息。
6. 在 Pull Request 中说明行为变化、验证方式和兼容性影响。

每个 Skill 独立维护版本号。行为变化应更新对应的版本号和变更记录；仅修改仓库说明时不需要升级 Skill 版本。
