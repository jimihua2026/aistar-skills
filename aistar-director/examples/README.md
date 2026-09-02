# Examples

> Examples 不作为硬规则，只作为参考示范。
> 分为 `good-cases/`（展示为什么成功）和 `failure-cases/`（展示为什么失败、应该避免什么）。

---

## 案例标注要求

每个案例必须标注：

```yaml
title:
video_type: 主类型 + 次类型
applicable_scope: 适用场景
outcome: success | failure
reason: 成功 / 失败原因
is_formal_rule: false   # 案例不是规则，只有经复盘机制确认后才可能升级
```

---

## 目录

```text
good-cases/       优秀案例（为什么有效）
failure-cases/    失败案例（为什么失败、如何避免）
```

建议每个案例包含：Brief 摘要 → 关键决策 → 最终 Prompt 片段 → 结果与教训。

案例数量不在多，在于每个案例都能回答："下次遇到类似项目，应该做什么 / 不做什么。"
