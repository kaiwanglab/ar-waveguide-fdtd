# Stage89：电偶极源位置鲁棒性

日期：2026-09-23

固定结构、5 nm网格、500 fs、归一化kx=-0.1186131，仅改变二维TM电偶极源的位置。

| 源位置 | x | y | 共振波长 | Q | amplitude | error |
|---|---:|---:|---:|---:|---:|---:|
| 光栅上方空气区 | -90.585 nm | 255 nm | 638.213 nm | 119.096 | 0.0267701 | 6.35377e-7 |
| 波导芯层内部 | 73.81 nm | -150 nm | 638.234 nm | 119.066 | 0.0676579 | 9.25251e-7 |
| 高折射率光栅齿内部 | -60.39 nm | 105 nm | 638.201 nm | 118.714 | 0.0175602 | 1.08964e-6 |

- 共振波长最大差：0.0331018 nm
- Q最大差：0.382529

## 结论

三个物理区域中的激励都得到同一个约638.2 nm共振，证明峰位不依赖特定光源位置。芯层内源的拟合振幅最大，说明其与目标Bloch导模的空间重叠最好；光源位置主要改变模式被激发的强弱，而不改变结构本征频率。

## 文件

- `D:/FDTD_File/ar_incoupler_FDTD_stage89_dipole_position_robustness.ldf`
- `D:/FDTD_File/ar_incoupler_FDTD_638nm_stage89_dipole_position_robustness_2D.fsp`
- `D:/Codex/Kai/fdtd_stage89_dipole_position_robustness.lsf`
- `D:/Codex/Kai/.ppt-build/recent_fdtd_optimization/stage89_complete_check.png`

## 下一步

Stage90建议完成Bloch验证阶段的最终汇总：统一给出峰位、Q、群折射率、角度闭环、模场集中度、网格/时间/采样/激励鲁棒性，并明确哪些数值可作为最终结论，哪些仅作为辅助指标。
