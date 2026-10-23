# Stage203：3D 周期单元宽度不变性验证

完成时间：2026-09-30 19:44（Asia/Shanghai）

## 单变量条件

- 从已完成的 Stage201e 3D 周期模型加载。
- 只把 z 周期单元从 0.2 µm 扩大到 0.4 µm。
- 结构覆盖跨度同步从 0.4 µm 扩大到 0.8 µm；源、功率监视器、mode monitor 和局部网格同步覆盖 0.4 µm 单元。
- 保持 dz=20 nm、638 nm、theta=-15.1°、phi=-90°、polarization=90°、plane-wave source、24 齿及所有 x-y 参数不变。

## 结果

| 案例 | z 单元 | 源功率 | 单位宽度源功率 | 右向功率 | 左向功率 | 方向性 |
|---|---:|---:|---:|---:|---:|---:|
| Stage201e | 0.2 µm | 4.355296e-15 W | 2.177648e-8 W/m | 33.285799% | 1.592330% | 95.434590% |
| Stage203 | 0.4 µm | 8.708686e-15 W | 2.177171e-8 W/m | 33.293068% | 1.592664% | 95.434626% |

- 单元宽度翻倍时，源功率比例为 **1.999562**；单位宽度源功率只变化 **-0.021884%**。
- 归一化右向功率变化 **+0.007269 pp**（相对 +0.021837%），左向功率变化 **+0.000334 pp**，方向性变化 **+0.000036 pp**。
- 这些变化远小于 1 pp 门槛，因此 3D 周期结果对 z 单元宽度不敏感，周期功率归一化通过。
- Stage203 相对 2D plane-wave 参考的右向功率仍低 **5.258222 pp**。结合 Stage202 的 dz 收敛，剩余差异属于 2D/3D 系统性差异，不能通过继续缩小 dz 或扩大 z 单元消除。

## 下一步

1. 只读比较 2D 与 3D 的源功率单位和实际 x-y 网格坐标，确认二者的数值基准。
2. 若 x-y 网格一致且 2D/3D 源功率定义已厘清，锁定 Stage203 作为“3D periodic direct-power baseline”。
3. 在该基准上启用 3D `mode_right`，校验模式边缘衰减、前向模式和与 direct power 的闭合。
4. 模式验证通过后，才进入 z-PML、有限宽光栅和物理 3D 有限光束。

## 文件

- 原始数据：`D:/FDTD_File/stage203_3d_periodic_zcell0p4um_phiM90_dz20nm_direct_power.ldf`
- 完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage203_3D_PERIODIC_zcell0p4um_phiM90_dz20nm_638nm_24teeth_COMPLETE.fsp`
- 可读数据：`D:/Codex/Kai/stage203_3d_periodic_zcell_invariance.csv`
- 运行脚本：`D:/Codex/Kai/stage203_run_3d_periodic_zcell0p4um_dz20nm.lsf`
