# Stage 118：最终结构光谱带宽验证

日期：2026-09-27  
固定条件：入射角 -13.6 deg、周期 334 nm、占空比 62.5%、高度 290 nm、顶部偏移 -280 nm、模式面 x=5 um。

## 5 nm 粗扫

| 波长 | TM效率/完整光源 |
|---:|---:|
| 580 nm | 6.60897% |
| 600 nm | 19.7751% |
| 620 nm | 35.2292% |
| 627 nm | 37.8066% |
| 638 nm | 33.1954% |
| 650 nm | 20.3824% |
| 660 nm | 10.3704% |
| 680 nm | 1.16686% |

## 峰值精扫

| 波长 | 5 nm TM效率 |
|---:|---:|
| 624 nm | 37.2103% |
| 625 nm | 37.4660% |
| 626 nm | 37.6699% |
| 627 nm | 37.8066% |
| 628 nm | 37.8140% |
| 629 nm | 37.7429% |
| 630 nm | 37.5873% |

5 nm三点抛物线拟合峰值约为 627.594 nm、37.8205%。

## 5 nm 边界精扫

| 波长 | TM效率 |
|---:|---:|
| 597 nm | 17.5725% |
| 598 nm | 18.2713% |
| 599 nm | 19.0084% |
| 600 nm | 19.7751% |
| 650 nm | 20.3824% |
| 651 nm | 19.2619% |
| 652 nm | 18.1601% |
| 653 nm | 17.0736% |

插值边界为 598.867 nm 和 651.319 nm，带宽 52.452 nm。

## 3.5 nm 最终复核

- 626.594 nm：37.8662%
- 627.594 nm：37.9084%
- 628.594 nm：37.8539%
- 三点拟合峰值：627.531 nm
- 拟合峰值效率：37.9086%
- 半功率阈值：18.9543%
- 598.867 nm：19.0040%，高于半高 0.0498 pp
- 651.319 nm：18.8803%，低于半高 0.0739 pp
- 斜率修正后的短波边界：约 598.80 nm
- 斜率修正后的长波边界：约 651.25 nm
- 最终 3 dB 光谱带宽：约 52.45 nm
- 相对带宽：约 8.36%
- 等效 Q 值：约 11.96

## 638 nm 工作点

- 638 nm、3.5 nm网格效率：33.2128%
- 达到峰值效率的 87.61%
- 相对峰值低 4.6958 个百分点
- 功率比损失约 0.57 dB
- 638 nm仍位于3 dB工作带宽内，但天然峰值约在627.5 nm。

## 读图方法

1. 横轴是波长，纵轴是目标TM导模效率。
2. 曲线最高点给出峰值波长和峰值效率。
3. 峰值的一半约为18.95%；水平线与曲线的两个交点就是3 dB/FWHM边界。
4. 两边界之差是3 dB光谱带宽。
5. 本阶段跨波长对比统一采用相对于完整FDTD光源的 `TM_source`；不混用随波长变化的封闭盒截获归一化值。

## 保存文件

- `D:/FDTD_File/stage118_final_design_wavelength_coarse_scan_mesh5nm.ldf`
- `D:/FDTD_File/stage118b_wavelength_peak_refine_mesh5nm.ldf`
- `D:/FDTD_File/stage118c_wavelength_3db_boundary_refine_mesh5nm.ldf`
- `D:/FDTD_File/stage118d_spectral_peak_and_boundaries_mesh3p5nm_verify.ldf`
- `D:/FDTD_File/stage118e_spectral_peak_location_mesh3p5nm_verify.ldf`
- `D:/FDTD_File/ar_incoupler_FDTD_stage118e_spectral_peak_location_verified_restored_638nm_thetaM13p6_period334nm_mesh3p5nm_2D.fsp`
- `D:/Codex/Kai/stage118_spectral_plot.png`

## 下一步

Stage 119：制造容差验证。保持638 nm与-13.6 deg不变，分别扰动周期、占空比、刻蚀高度和顶部横向偏移，输出最差效率和敏感度排序，而不是继续追求单点峰值。
