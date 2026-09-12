# 镜头分析协议

本文件将 `inspection_record` 的候选区间变为最终镜头，负责镜头级决策与连续性，不写生成提示词。

## 判定原则

- 根据本包 [候选边界与连续性复核](boundary-review.md) 定稿。硬切或连接不同镜头的叠化/转场可建立新镜头；持续转场单独保存区间及分段选点依据。
- 人物移动、摄影机移动、景别/对焦/光线在连续拍摄内的变化通常仍是同一镜头；不要为描述动作而过度拆分。
- 长镜头内部不可逆的场景、主体或视觉结构重置先作为分析线索；只有证据支持剪辑断裂或跨镜连接时才增加剪辑镜头。连续形变仍用动作链表达。为生成而分段只写执行建议，保留原镜头编号和单镜头完整提示词。

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

展示时间保留两位小数，内部数值保留实际精度、采用左闭右开区间；边界证据按主文件 `boundary_review` 契约进入交付。首镜头从 `00.00秒` 开始，末镜头结束于实际时长。相邻镜头不得留空或重叠。用开始状态、动作链、结束状态和摄影机运动表达镜头内部变化，不另建运动时间轴。记录须继承的角色外观、服装、道具位置、场景、光线方向与运动方向；不得臆造未出现的细节。完成后交给 `prompt-reconstruction.md`。
