# 项目数据与阶段交接

创建项目时复制`../assets/project-template.json`到交付目录的`project.json`，用已知事实填写。未知值使用null并列入`unknowns`，不编造默认的实际执行参数。

## 状态

`received → analyzed → designed → instructions_ready → frames_ready → tested → delivered`。

状态表示已完成的最远阶段，不能跳过证据。仅交付制作指令的项目可从instructions_ready直接进入delivered，且delivery_scope保持instructions，不能标为视频验证通过。部分测试通过也不能将未测试单元标为通过。

继续项目时先读project.json，继承已确认需求、已完成素材和失败记录，不重新收集相同问题。

## 字段约定

- `source`：视频文件路径、SHA-256、媒体时长与帧率；路径相对于项目目录，外部文件可用绝对路径。
- `source.duration_seconds`采用分析覆盖的时间基准，并在`duration_basis`写video或container。已知音视频轨时长不同时，优先按视觉轨建立视觉单元，另存container_duration_seconds，不将音轨尾部空余虚构为镜头。多轨时长尚不清楚时记录精度限制。
- `confirmed`：保留项、替换项、用途和声音范围。
- `units`：按时间连续覆盖参考视频的制作单元。字段为id、kind、start_seconds、end_seconds、boundary_precision、observation、replacement、dependencies。kind为shot或phase。phase可以是镜头内部阶段，不称为独立剪辑镜头。
- `transition_groups`：跨单元衔接，用unit_ids引用，不与units重复计入时长。
- `assets`：id、kind、path、status及derived_from。kind区分source_frame、generated_frame、video、report。未生成资产用planned，已写入且能读取才用ready。
- `tasks`：id、unit_ids、purpose、input_asset_ids、prompt、criteria、status；视频生成前增加planned_settings，执行后再增加actual_settings、output_asset_ids及review。status为planned、ready、submitted、generated、accepted、accepted_with_deviation或failed。
- `review`：reviewer、method、criteria_results、deviations和scope。用户认可、抽帧复核、逐帧检查和播放审阅分别记录。
- `attempts`：有真实执行后才记录任务id、输入版本、原样提示词、实际设置、费用、平台任务号与返回结果。不把建议设置写成执行事实。
- `next_action`：下一件具体工作及必要的缺失信息。

复杂项目可把分析与任务拆成引用文件；小项目不为每个字段创建文件。

## 分阶段输出

| 阶段 | 可审阅输出 | 进入下一阶段的依据 |
|---|---|---|
| analyzed | 带截图与时间的观察记录 | 源画面可见，事实和估计分开 |
| designed | 保留/替换表、跨镜头关联、风格规则 | 用户方向明确，替换动作可行 |
| instructions_ready | 每项任务的参考图选择、提示词、参数建议与验收 | 输入输出可指认，执行方式符合渠道能力 |
| frames_ready | 独立图片、原图对照与检查记录 | 数量、身份、位置及起止关系可接受 |
| tested | 生成结果、用户反馈与复核 | 验收范围明确，失败有处理方向 |
| delivered | 图文入口、可复制文本、project.json及成果文件 | 链接与引用有效，无虚假完成状态 |

## 网页生成任务卡

每张卡先写：本次验证什么、选哪个模式、哪个文件放首帧/尾帧或哪种参考角色。随后提供一段可复制提示词和最多三项主要检查。只有实际核实过的渠道能力写为可用；输入多张参考图片不意味着支持多关键帧控制。

生成能力未核实时，写“在界面可选时使用首尾帧；否则需按实际入口调整”，不要自动把普通参考图当作首尾帧。记录用户反馈后可复用同一成功配置，不反复索要截图。

帧号与高精度时间保留在证据记录。用户生成提示词使用可执行的动作顺序与合理时间分段，不把5.041667秒或人工估计的精确百分比机械写成平台能保证的控制参数。平台5秒设置输出121帧等差异按实际输出记录，不单凭毫秒差判为失败；严格节奏要求在剪辑阶段验收。

## 边界与来源镜头（1.1.0 技能扩展）

项目 Schema 仍为1.0，已有必填字段不变；以下为实际分析时填写的可选扩展，旧项目按下一步需要补充，不制造空证据。

- `units[].source_shot_id`：本项目内的源剪辑镜头标识。一个源镜头拆成多个phase时共享该标识；直接完整制作的shot也写其标识。报告镜头数按已确认源镜头统计，单位数和生成任务数另列。边界暂定时数量也标为暂定。
- `units[].boundary_review`：本单元起点的`status`（accepted/provisional）、`reason`、`method`、`evidence_times_seconds`；精度写入已有`boundary_precision`，新增记录使用frame_verified、estimated或unresolved。phase在镜内的起点method标为action_phase或production_split，不能声称是切镜；若phase恰从源镜头边界开始，继承该边界的实际依据；源片起点用source_start。方法名和精度必须符合实际证据。
- `transition_groups[]`可增加`start_seconds`、`end_seconds`、`split_seconds`、`split_reason`、`before_state`、`after_state`和有证据的`intermediate_states`。区间按参考片时间，引用已有unit_ids，不重复累计时长。不能确认的范围留null并记unknowns。
- 数值时间不先舍入；展示保留两位小数。unit采用左闭右开区间，共用邻接边界。精确帧号和时间戳可附在证据中，但需注明源视频和计数基准；可变帧率、代理映射与持续转场按本包[边界复核协议](boundary-review.md)处理。
- 边界理由与关键争议摘要随制作包保存；转场关键状态只有实际抽取并保留时才引用assets，不引用将被清理的临时图。复用按源哈希、分析范围与证据适用性判断。

检查上述扩展时，核对source_shot_id对应关系、转场范围是否位于参考片内、split是否属于转场区间以及与单元边界的一致性。现有结构检查脚本未校验这些扩展；通过脚本不代表它们或逐帧边界已经验证。严格剪辑时按源时间基准复核，不把脚本的时间容差当作精度保证。

## 检查脚本

运行`python scripts/validate_project.py /项目目录/project.json`检查时间覆盖、id、任务与素材引用、已就绪资产可读性、验收证据。该脚本不验证视觉质量，不能代替观察或用户验收。


完整影片可按需增加picture_lock、repairs、audio_cues和delivery字段；这些扩展不改变旧项目必填结构。具体落点、证据与归档约定见[全片返修与收尾](film-closeout.md)。


启动或环境变化时维护可选capability_check扩展，具体字段和判断规则见[启动能力检查](startup-capabilities.md)。其scope与本次delivery_scope一致，未知能力不记作已验证。
