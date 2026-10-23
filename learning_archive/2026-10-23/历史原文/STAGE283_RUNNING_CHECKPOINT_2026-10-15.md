# Lumerical Stage283 运行检查点

- 保存时间：2026-10-15 17:25（Asia/Shanghai）
- 当前任务：最终几何在 `wz = 0.45 um` 条件下的工程化验证
- 当前阶段：Stage283b patterned 仿真运行中
- FDTD GUI：`fdtd-solutions` PID 7524，响应正常
- 计算引擎：6 个 `fdtd-engine-msmpi` 进程，均正常运行
- 启动时间：2026-10-15 17:24:38

## 已保存文件

- 设置工程：`D:/FDTD_File/ar_incoupler_FDTD_stage283a_FINAL_GEOMETRY_wx6um_wz0p45um_SETUP_638nm.fsp`
- 当前运行工程：`D:/FDTD_File/ar_incoupler_FDTD_stage283b_FINAL_GEOMETRY_wx6um_wz0p45um_zdomain2p8um_PATTERNED_RUNNING_638nm.fsp`
- 设置审计：`D:/FDTD_File/stage283a_final_geometry_wz0p45_setup_audit.ldf`

## Stage283a 已核验参数

- `wz = 0.45 um`
- `zmax = 1.1 um`
- `nz = 81`
- 直接积分入射功率：`5.570171652777991e-15 W`
- 数据集边缘场比：`0.0025407177935836693`
- 光栅边缘场比：`0.6411803884299546`

## 恢复顺序

1. 不要在 Stage283b 运行时关闭 FDTD 或强制结束进程。
2. patterned 完成后运行 `stage283c_run_final_geometry_wz0p45_reference_zdomain2p8.lsf`。
3. reference 完成后依次运行 Stage284a、284b、284c 后处理脚本。
4. 将 `wz = 0.45/0.55/0.65 um` 的归一化效率、绝对导模功率、mode1 效率及占比放在同一张表中比较。

