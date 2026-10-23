# Stage85：Bloch色散与有限光栅最佳角闭环

日期：2026-09-23

## 输入

- 周期：335.5 nm
- 目标波长：638 nm
- Stage83局部色散拟合斜率：-670.173 nm / normalized-k
- Stage79有限12齿FDTD最佳角：-13.0358°

## Bloch色散插值

Stage83线性拟合在638 nm处得到：

- 归一化Bloch波矢：kx = -0.118111

归一化波矢与自由空间入射角的关系：

`sin(theta) = kx * lambda / period`

代入后：

- Bloch模型预测角：-12.9796°
- 有限12齿FDTD最佳角：-13.0358°
- 两者差值：0.0562°

## 结论

独立单周期Bloch本征分析与有限12齿Gaussian入耦仿真的最佳角仅相差约0.056°，相位匹配关系实现定量闭环。剩余小差异可由有限齿数、Gaussian光束角谱、局部色散非严格线性以及峰值拟合误差解释。

## 文件

- `D:/FDTD_File/ar_incoupler_FDTD_stage85_bloch_finite_angle_closure.ldf`
- `D:/Codex/Kai/.ppt-build/recent_fdtd_optimization/stage85_angle_closure.png`
