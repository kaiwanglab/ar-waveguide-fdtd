# Stage207 有限宽 3D plane-wave pilot：功率监视器诊断

## 模型条件

- 波长：638 nm，单频。
- 光栅：24 齿，有限 z 宽 0.60 µm。
- FDTD z 域：1.20 µm，z 两端 PML。
- `power_right`：x-normal，z 范围约 -0.442637 至 +0.442637 µm，共 29 点。
- z 网格：40 nm pilot；实际运行约 54.68 min，仿真状态 `status=2`。

## 直接结果

- `power_right`：6.4357011%。
- `power_left`：1.0605666%。
- 表观方向性 `right/(right+left)`：85.8520713%。
- 这些数值目前只能叫“监视器净 Poynting 功率”，不能叫有限宽入耦效率。

## z 向功率截取检查

按照 Ansys 官方 Poynting 定义，在 `power_right` 面上计算

`Sx = 0.5*Re(Ey*conj(Hz) - Ez*conj(Hy))`

并沿 y、z 积分。手工积分得到 6.4357011%，与内置 `transmission("power_right")` 完全一致，说明后处理公式和归一化正确。

| z 积分区域 | 对源归一化功率 | 占当前监视器全宽功率 |
|---|---:|---:|
| `|z| <= 0.30 µm`（等于光栅宽度） | 4.2021198% | 65.2939% |
| `|z| <= 0.35 µm` | 5.1399373% | 79.8660% |
| `|z| <= 0.40 µm` | 5.7371362% | 89.1455% |
| 当前全宽，约 `|z| <= 0.442637 µm` | 6.4357011% | 100% |

- 最外侧约 42.6 nm × 2 仍携带当前监视器净功率的 10.8545%。
- z 分辨功率曲线在全宽内仅约 0.958–1.000，相当平坦，到两侧边界仍没有衰减完。
- x-z `|E|^2` 图同样显示右侧强场延伸到监视器上下边界。

## 物理判断

这不是一个“把监视器再放宽就能得到真正入耦效率”的结果。当前激励是横向无限的斜入射 plane wave，它本身带有 x 方向 Poynting 分量；`power_right` 又是 x-normal 面，因此监视器会把未由光栅耦合产生的斜入射背景也计入。z 曲线几乎均匀而不是在 0.60 µm 光栅附近集中，是这一污染的直接证据。

因此：

1. 6.4357% 不能作为有限宽光栅入耦效率。
2. 不能用它和 periodic 模型按面积比例直接比较。
3. 暂停几何参数优化和 z 域盲目加宽。
4. Stage208 使用完全相同设置、只关闭全部光栅齿，运行无光栅参考；它用于量化平面波背景。
5. 后续正式有限孔径验证应转向有限 3D 光束，并用导模投影/背景场扣除，而不是只读 `power_right`。

## 文件

- 完整仿真：`D:/FDTD_File/ar_incoupler_FDTD_stage207_FINITE_WIDTH_PLANE_WAVE_zPML_domain1p2um_grating0p6um_dz40nm_638nm_24teeth_COMPLETE.fsp`
- 原始直接功率：`D:/FDTD_File/stage207_finite_width_plane_wave_zPML_dz40nm_direct_power.ldf`
- z 向功率诊断：`D:/FDTD_File/stage207_power_right_z_capture_diagnostic.ldf`
- 可读数据：`D:/Codex/Kai/stage207_power_right_z_capture.csv`
- x-z 场图屏幕记录：`D:/Codex/Kai/stage207_xz_E2dB_screen.png`
- z 功率曲线屏幕记录：`D:/Codex/Kai/stage207_z_capture_screen.png`
