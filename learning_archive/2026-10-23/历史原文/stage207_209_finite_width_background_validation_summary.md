# Stage207–209：有限宽 3D plane-wave 背景验证结论

## 最终数值

Stage207 有齿模型：

- `power_right` 带符号净功率：+6.4357011%。
- `power_left` 带符号净功率：-1.0605666%。
- `power_top`：-64.1588530%，含入射场，不能与左右绝对值直接相加。

Stage208 无齿参考：

- `power_right` 带符号净功率：-1.3172103%。
- `power_left` 带符号净功率：-0.9789170%。
- `power_top`：-59.4383588%。
- 两次 source power 比值：0.99980093，差异约 -0.0199%，归一化一致。

Stage209b 将无齿参考复场插值到有齿监视器网格后，得到精确相干分解：

| 分量 | 对有齿源功率归一化 |
|---|---:|
| 有齿总场 | +6.4357011% |
| 无齿参考背景 | -1.3151372% |
| 光栅散射场 | +7.6926116% |
| 背景–散射干涉交叉项 | +0.0582266% |
| 三项重构 | +6.4357011% |

重构相对误差为 `-1.18e-16`。参考与有齿模型的 z 网格完全相同；y 网格最大错位 0.438266 nm。线性插值修正仅改变参考功率 0.001811 个百分点，因此结论不依赖该微小网格差异。

## 怎么理解

1. `power_right=6.4357%` 是总场净功率，不是纯光栅入耦功率。
2. 斜入射 plane wave 在 x-normal 面上产生 -1.3151% 的反向背景；它抵消了部分光栅散射的正向能流。
3. 光栅散射场自身穿过右监视面的净向右功率是 7.6926%。
4. 但散射场里仍同时包含目标波导导模和向右传播的辐射/连续谱，因此 7.6926% 仍不能直接命名为最终导模入耦效率。
5. z 分辨曲线在当前 ±0.4426 µm 监视器边界处仍不衰减；有限横向 pilot 的功率口径尚未收敛。

## 下一阶段（Stage210）

- 使用同一组波导模式作为固定参考基底。
- 把 Stage207 与 Stage208 的复场分别投影到该基底；利用展开系数的线性关系得到散射场的 `a_scattered = a_patterned - a_reference`。
- 报告目标 TM 基模、TM 高阶模、辐射连续谱和背景项，禁止只报一个 `power_right`。
- 先完成模式投影方法验证，再决定是否扩大 z 域/监视器；目前不扫描光栅几何。
- 最终物理有限孔径要使用明确束腰和焦点的 3D beam。0.60 µm 横向光栅只是一项资源和方法 pilot，不代表毫米级 AR 入耦孔径。

## 方法依据

- Ansys Poynting 积分：`P = 0.5*Re(E × H*)`，部分监视器功率必须对局部 Poynting 矢量积分。
- Ansys 模式展开说明：模式展开给出任意监视器场到波导本征模的前向/后向系数。
- 2026 R1 支持把 rectilinear field dataset 直接传给 `overlap` / `expand` / `expand2`，可用于插值后的散射场。

官方资料：

- https://optics.ansys.com/hc/en-us/articles/1500007397442-Integrating-the-Poynting-Vector
- https://optics.ansys.com/hc/en-us/articles/360034902433-Using-and-understanding-Mode-Expansion-Monitors
- https://optics.ansys.com/hc/en-us/articles/360034406414-expand2-Script-command

## 文件

- Stage207 完整有齿模型：`D:/FDTD_File/ar_incoupler_FDTD_stage207_FINITE_WIDTH_PLANE_WAVE_zPML_domain1p2um_grating0p6um_dz40nm_638nm_24teeth_COMPLETE.fsp`
- Stage208 完整无齿参考：`D:/FDTD_File/ar_incoupler_FDTD_stage208_FINITE_WIDTH_UNPATTERNED_REFERENCE_zPML_domain1p2um_dz40nm_638nm_COMPLETE.fsp`
- Stage208 原始数据：`D:/FDTD_File/stage208_finite_width_unpatterned_reference_direct_power.ldf`
- Stage209b 插值复场分解：`D:/FDTD_File/stage209b_interpolated_pattern_reference_field_decomposition.ldf`
- 可读汇总：`D:/Codex/Kai/stage207_209_finite_width_background_decomposition.csv`
- 分解图屏幕记录：`D:/Codex/Kai/stage209b_interpolated_decomposition_screen.png`
