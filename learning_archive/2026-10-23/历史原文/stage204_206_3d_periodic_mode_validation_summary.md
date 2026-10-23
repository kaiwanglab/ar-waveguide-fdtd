# Stage204–206：3D 周期模式展开与基底收敛

完成时间：2026-09-30 21:06（Asia/Shanghai）

## 配置与完整性

- 基准：Stage203，3D periodic，z 单元 0.4 µm，dz=20 nm，638 nm，plane wave，theta=-15.1°，phi=-90°，polarization=90°。
- `mode_right` 与 `power_right` 的 x/y/z 中心差、y/z span 差均为 0。
- eigensolver 更新状态为 1；FDTD status=2。
- 启用模式展开后，direct right/left/方向性仍为 33.293068% / 1.592664% / 95.434626%，与 Stage203 完全一致，说明监视器没有扰动仿真。

## 主要模式

| 模式 | neff | TE fraction | 前向 | 反向 | 净值 | 解释 |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 1.644886 | ≈0 | 34.802855% | 0.003775% | 34.799080% | 目标 TM 基模 |
| 2 | 1.559134 | 1 | 0.000235% | ≈0 | 0.000235% | TE 导模，几乎未激发 |
| 3 | 1.141883 | ≈0 | 0.485764% | 0.082753% | 0.403010% | TM 高阶模 |
| 4 | 1.078647 | 1 | 0.000028% | ≈0 | 0.000028% | TE 导模，几乎未激发 |
| 6 | 0.873908 | ≈0 | 0.024522% | 0.143036% | -0.118514% | 辐射/泄漏型反向净通量 |

- mode1 占 neff>1 的全部导模前向功率 **98.622719%**。
- TE 导模耦合可忽略；主要非目标导模是 mode3。

## 模式基底收敛

| 模式数 | 全前向和 | 全反向和 | 全净和 | 全净和 - direct right |
|---:|---:|---:|---:|---:|
| 8 | 35.313423% | 0.229564% | 35.083859% | +1.790791 pp |
| 16 | 35.343425% | 0.891509% | 34.451916% | +1.158848 pp |
| 32 | 35.343425% | 0.891509% | 34.451916% | +1.158848 pp |

- 16→32 模式所有聚合结果不再变化，离散模式基底已经收敛；继续增加模式没有收益。
- `T_forward` 表示所选前向模态的功率，direct right 是监视面上的总净 Poynting 通量。存在反向波与未离散展开的辐射连续谱时，单个前向导模可以大于净通量，二者不应强行相等。
- 因此 3D periodic plane-wave 结果应同时报告：目标 mode1 前向 **34.802855%**、mode3 前向 **0.485764%**、direct right **33.293068%**、左右方向性 **95.434626%**。
- 这套数值不替代正式 2D Gaussian 设计基准；它是后续有限宽 3D 验证的独立周期基准。

模式定义参考：[Using and understanding Mode Expansion Monitors](https://optics.ansys.com/hc/en-us/articles/360034902433-Using-and-understanding-Mode-Expansion-Monitors)。

## 文件

- Stage204 原始结果：`D:/FDTD_File/stage204_3d_periodic_mode_expansion_8modes.ldf`
- Stage204 完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage204_3D_PERIODIC_MODE8_zcell0p4um_dz20nm_638nm_24teeth_COMPLETE.fsp`
- Stage205 16 模式后处理：`D:/FDTD_File/stage205_postrun_mode_basis_16.ldf`
- Stage206 32 模式后处理：`D:/FDTD_File/stage206_postrun_mode_basis_32.ldf`
- 逐模可读表：`D:/Codex/Kai/stage204_mode_breakdown.csv`
- 基底收敛表：`D:/Codex/Kai/stage204_206_mode_basis_convergence.csv`
