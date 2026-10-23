# Stage81-83 Bloch 单周期与局部色散检查点

日期：2026-09-23

## Stage81：单周期模型

- 周期：335.5 nm
- 光栅齿宽：167.75 nm（占空比50%）
- 光栅齿高度：210 nm
- x边界：Bloch
- y边界：PML
- 波长激励范围：620-656 nm
- 初始归一化Bloch波矢：-0.1186131
- TM激励：二维Electric dipole
- 时间监视器：3个非对称位置点监视器
- 局部网格：5 nm
- 仿真时间：500 fs

## Stage82：单k点共振验证

在归一化 kx=-0.1186131 时：

- 共振波长：638.193 nm
- Q：119.094
- amplitude：0.0268183
- error estimate：1.53903e-6

时间截断敏感性：

| 截断起点 | 波长 | Q |
|---:|---:|---:|
| 120 fs | 638.222 nm | 118.336 |
| 150 fs | 638.193 nm | 119.094 |
| 180 fs | 638.223 nm | 118.301 |

三次共振波长展宽仅0.030652 nm，峰位置稳定。

## Stage83：局部Bloch色散

| 归一化 kx | 共振波长/nm | Q |
|---:|---:|---:|
| -0.15 | 超出620-656 nm窗口 | - |
| -0.14 | 652.818 | 118.398 |
| -0.13 | 645.888 | 117.600 |
| -0.12 | 639.114 | 119.213 |
| -0.11 | 632.514 | 119.177 |
| -0.10 | 625.996 | 120.028 |
| -0.09 | 超出620-656 nm窗口 | - |

- 局部线性斜率：-670.173 nm / normalized-k
- 638 nm附近估算群折射率：1.81035
- 物理结论：此前由有限光栅峰值反推的有效相位匹配波矢，与独立Bloch单周期模型在638 nm附近的本征共振一致。

## 文件

- `D:/FDTD_File/ar_incoupler_FDTD_638nm_stage81_bloch_unit_cell_setup_2D.fsp`
- `D:/FDTD_File/ar_incoupler_FDTD_638nm_stage82_single_k_result_2D.fsp`
- `D:/FDTD_File/ar_incoupler_FDTD_638nm_stage83_local_bloch_dispersion_2D.fsp`
- `D:/FDTD_File/ar_incoupler_FDTD_stage82_single_k_resonances.ldf`
- `D:/FDTD_File/ar_incoupler_FDTD_stage82b_time_cut_stability.ldf`
- `D:/FDTD_File/ar_incoupler_FDTD_stage83_local_bloch_k_scan_results.ldf`
- `D:/Codex/Kai/fdtd_stage81_create_bloch_unit_cell_setup.lsf`
- `D:/Codex/Kai/fdtd_stage82_extract_single_k_resonances.lsf`
- `D:/Codex/Kai/fdtd_stage82b_time_cut_stability_check.lsf`
- `D:/Codex/Kai/fdtd_stage83_local_bloch_k_scan.lsf`

## 下一步

Stage84建议做638 nm目标点的模场分布验证，确认该共振的Ez能量主要位于波导芯层/光栅区，而不是PML或空气中的伪模；随后再扩展更宽的k和波长范围绘制完整局部能带。
