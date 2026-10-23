# Stage207：有限宽 3D plane-wave pilot 资源门槛

完成时间：2026-09-30 21:13（Asia/Shanghai）

- z 边界从 periodic 改为 PML。
- z 仿真域 1.2 µm；波导/基底覆盖 1.6 µm；有限光栅宽度 0.6 µm。
- 右/左/top 功率监视器宽度 0.9 µm；局部 z 网格跨度 0.8 µm，dz=40 nm。
- x-y 网格保持 3462×203；实际 z 网格为 45 点，节点代理量 31,625,370。
- 相对 Stage203 的节点比例 2.142857；按 Stage203 实测墙钟时间线性估计约 99.3 分钟。
- 按 Stage203 峰值单进程内存线性估计约 0.712 GiB；6 进程总量远低于 24 GiB 安全停止线。

结论：资源门槛通过，可运行 coarse finite-width pilot。该案例仍是 plane wave，目标是隔离有限光栅边缘与 z-PML 效应；不是最终有限 3D Gaussian/显示系统效率。

文件：

- setup：`D:/FDTD_File/ar_incoupler_FDTD_stage207_SETUP_FINITE_WIDTH_PLANE_WAVE_zPML_domain1p2um_grating0p6um_dz40nm_638nm_24teeth.fsp`
- raw gate：`D:/FDTD_File/stage207_finite_width_plane_wave_resource_gate.ldf`
- 可读表：`D:/Codex/Kai/stage207_finite_width_resource_gate.csv`
