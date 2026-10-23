# Stage 117：最终结构角度容差验证

日期：2026-09-27  
固定条件：638 nm、周期 334 nm、占空比 62.5%、高度 290 nm、顶部偏移 -280 nm、模式面 x=5 um。

## 5 nm 粗扫与边界精扫

| 入射角 | TM效率/完整光源 |
|---:|---:|
| -30 deg | 13.9295% |
| -28.5 deg | 16.2654% |
| -28.0 deg | 17.0600% |
| -27.5 deg | 17.8538% |
| -24 deg | 22.1142% |
| -13.6 deg | 33.1954% |
| -8 deg | 18.6515% |
| -7 deg | 14.6701% |
| -6.5 deg | 12.8813% |
| -6 deg | 11.3103% |
| 0 deg | 7.3892% |

- 5 nm 峰值：33.1954%
- 半功率阈值：16.5977%
- 插值左边界：-28.2909 deg
- 插值右边界：-7.4842 deg
- 插值 3 dB 全角宽：20.8067 deg

## 3.5 nm 边界复核

最终峰值采用 Stage 116 的 3.5 nm 结果 33.2128%，半功率阈值为 16.6064%。

| 边界候选 | 3.5 nm TM效率 | 相对半高误差 |
|---:|---:|---:|
| -28.2909 deg | 16.6208% | +0.0144 pp |
| -7.4842 deg | 16.5100% | -0.0964 pp |

按局部斜率微调后的最终估计：

- 左侧 3 dB 边界：约 -28.30 deg
- 右侧 3 dB 边界：约 -7.51 deg
- 3 dB 全角宽：约 20.79 deg

## 物理解释

1. 峰值出现在 -13.6 deg，说明这个角度最接近当前光栅的目标相位匹配条件。
2. 3 dB 范围内，效率至少保持峰值的一半，而不是表示效率下降了 3 个百分点。
3. 左右容差不对称：相对峰值，左侧约 14.7 deg，右侧约 6.1 deg；正角度方向更敏感。
4. 该角宽属于当前二维有限高斯光束模型，不能直接等同于真实眼镜系统的视场角或 Eyebox。

## 已保存文件

- `D:/FDTD_File/stage117_final_design_angle_coarse_scan_mesh5nm.ldf`
- `D:/FDTD_File/stage117b_angle_3db_boundary_refine_mesh5nm.ldf`
- `D:/FDTD_File/stage117c_angle_3db_boundaries_mesh3p5nm_verify.ldf`
- `D:/FDTD_File/ar_incoupler_FDTD_stage117c_angle_bandwidth_verified_restored_thetaM13p6_period334nm_wl638nm_mesh3p5nm_2D.fsp`
- `D:/Codex/Kai/stage117_angle_plot.png`

## 下一步

Stage 118：固定入射角 -13.6 deg，扫描波长，得到最终结构的峰值波长、3 dB 光谱带宽以及 638 nm 工作点相对峰值的损失。
