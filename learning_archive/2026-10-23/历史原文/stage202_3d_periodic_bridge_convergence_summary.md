# Stage202：3D 周期桥接 z 网格收敛

完成时间：2026-09-30 18:27（Asia/Shanghai）

## 对比结果

| 案例 | z 周期单元 | dz | 右向功率 | 左向功率 | 左右方向性 | status |
|---|---:|---:|---:|---:|---:|---:|
| Stage201b 2D plane-wave 参考 | — | — | 38.551290% | 1.535216% | 96.170243% | 2 |
| Stage201e 3D periodic | 0.2 µm | 20 nm | 33.285799% | 1.592330% | 95.434590% | 2 |
| Stage202 3D periodic | 0.2 µm | 10 nm | 33.285046% | 1.592537% | 95.433924% | 2 |

## 判断

- 20 nm → 10 nm 后，右向功率变化 **-0.000753 个百分点**，左向功率变化 **+0.000207 个百分点**，方向性变化 **-0.000666 个百分点**。
- 上述变化远小于预设的 1 pp 收敛门槛，因此 z 向网格已经收敛；不再继续到 5 nm。
- 3D 与 2D 的右向功率仍相差 **-5.266244 pp**。因为 dz 减半没有缩小该差异，所以它不是 z 网格离散误差。
- 下一步只改变 z 周期单元宽度（0.2 → 0.4 µm），保持 dz=20 nm、几何、源角度、偏振和监视器不变，检查周期边界与源功率归一化是否与单元宽度无关。

## 物理边界

- 这里验证的是“与 z 无关的周期桥接模型”，不是有限宽光栅或有限光束。
- 2D 正式 Gaussian 基准保持不变；本阶段使用同源 plane wave，仅用于隔离 2D→3D 的坐标、离散和归一化问题。
- `power_top` 包含入射场，且符号受监视器法向影响，不与左右功率绝对值直接求和。

## 文件

- Stage202 完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage202_3D_PERIODIC_PLANE_WAVE_phiM90_dz10nm_638nm_24teeth_COMPLETE.fsp`
- Stage202 原始数据：`D:/FDTD_File/stage202_3d_periodic_plane_wave_phiM90_dz10nm_direct_power.ldf`
- 可读数据：`D:/Codex/Kai/stage202_3d_periodic_bridge_convergence.csv`
- 收敛图：`D:/Codex/Kai/stage202_3d_periodic_bridge_convergence.png`
