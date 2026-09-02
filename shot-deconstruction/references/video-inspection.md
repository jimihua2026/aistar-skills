# 视频观察协议

本阶段只把视频转为带时间锚点的观察事实，不判定最终镜头，不生成提示词。

## 输入与产出

输入为已通过预检的视频及必要元数据，以及满足阈值时创建的分析代理。产出内部 `inspection_record`：

```yaml
video: {duration_seconds:, resolution:, fps:}
global_observation:
  scenes:
  subjects:
  rhythm:
  transitions:
candidate_segments:
  - start_seconds:
    end_seconds:
    boundary_evidence:
    keyframes: []
    observation: {subject:, environment:, start_state:, action_chain: [], end_state:, camera_motion:, composition:, lighting_color_style:, visual_effects: [], uncertainties: []}
```

只有用户明确要求声音、音乐或旁白分析时，才在 `global_observation` 中增加 `audio_observation`，提取并分析相应音轨。未要求时不转写、不识别音乐，也不生成占位式音频结论。

## 执行

1. 使用分析代理（无代理时使用原视频）完整浏览一次，记录场景、主体、显著剪辑/转场、主动作、摄影机运动与节奏。
2. 建立秒级时间轴。硬切、淡入淡出、叠化、遮挡/物体转场及显著画面结构改变均标为候选边界。
3. 每个候选区间优先采集起始、中部和结束关键帧；仅在动作、构图、镜头速度/方向、特效阶段或焦点变化时增加关键帧。静帧无法判断动态关系时，按动态复杂度追加连续帧，不做全片固定高密度采样。
4. 代理不足以判断小文字、细微道具/互动、纹理或边界证据时，才从原视频补取少量对应帧。
5. 分别记录主体、环境和摄影机的视觉结果。无法区分推进和变焦等机制时，记录可观察结果与可能性，并加入 `uncertainties`。
6. 区分有意视觉效果和明显生成瑕疵；将平台水印、生成声明、播放器界面、账号标识和非场景字幕标为非内容叠层，不把它们写入观察字段。

若用户要求音频分析：背景音乐记录风格、节奏、情绪、变化点和剪辑关系；旁白按时间转写，并记录语言、文字风格、表达节奏和声画关系。无法确认时保留时间范围并写入不确定项，不伪造内容。

每个候选区间应有足以支持主体、动作、摄影机和风格判断的证据，随后交给 `shot-analysis.md`。
