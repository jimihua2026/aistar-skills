# 镜头分析协议

本文件将 `inspection_record` 的候选区间变为最终镜头，负责镜头级决策与连续性，不写生成提示词。

## 判定原则

- 硬切、完成的叠化/转场或画面结构重置通常构成新镜头。
- 人物移动、摄影机移动、景别/对焦/光线在连续拍摄内的变化通常仍是同一镜头；不要为描述动作而过度拆分。
- 长镜头内部若有不可逆的场景、主体或视觉结构重置，可拆分并记录理由。

## 最终镜头记录

```yaml
shot_id:
start_seconds:
end_seconds:
boundary_reason:
observation: {subject:, environment:, start_state:, action_chain: [], end_state:, camera_motion:, composition:, lighting_color_style:}
continuity_notes:
uncertainties: []
```

时间保留两位小数；首镜头从 `00.00秒` 开始，末镜头结束于实际时长。相邻镜头不得留空或重叠。用开始状态、动作链、结束状态和摄影机运动表达镜头内部变化，不另建运动时间轴。记录须继承的角色外观、服装、道具位置、场景、光线方向与运动方向；不得臆造未出现的细节。完成后交给 `prompt-reconstruction.md`。
