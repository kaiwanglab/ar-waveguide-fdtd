# Stage255/256：250 nm 齿高验证

## 结论

250 nm 的净导模耦合效率为 **6.0539778363%**，相对 260 nm 的 **5.5641750063%** 提高 **8.8028%**。Mode 1 为 **4.0851440842%**，相对 260 nm 提高 **8.3463%**。

效率仍在上升，但相邻增益由 20.91% → 14.50% → 8.80% 连续收窄，已明显接近峰值区域。峰值仍未包住，下一步只验证 **240 nm**。

## 结果

| 指标 | 250 nm |
|---|---:|
| 导模净效率 | 6.0539778363% |
| 导模前向 | 6.0543228804% |
| 导模后向 | 0.0003450442% |
| TM 前向 | 6.0376705385% |
| TE 前向 | 0.0164237692% |
| Mode 1 前向 | 4.0851440842% |
| Mode 1 / 导模前向 | 67.47483021% |
| 直接散射净值 | 6.0550007255% |
| 未展开净残差 | 0.0004424313% |

## 数值有效性

- pattern/reference 入射功率完全一致
- y/z 网格差均为0
- 相干场重构相对误差：2.20e-16
- 32模式、28导模
- a/b线性误差：1.96e-17 / 1.01e-16
- 未展开净残差：0.0004424%

数值闭合正常。

## 决策

下一步保持其它参数不变，只验证240 nm。若240 nm下降，则以240/250/260 nm包住峰值；若继续上升，则再向230 nm推进。

## 可复现文件

- D:/FDTD_File/ar_incoupler_FDTD_stage255b_HEIGHT250nm_WIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp
- D:/FDTD_File/stage256a_height250nm_width0p75um_coherent_field_decomposition.ldf
- D:/FDTD_File/stage256b_height250nm_width0p75um_patterned_fixed_mode_basis32.ldf
- D:/FDTD_File/stage256c_height250nm_width0p75um_fixed_basis32_projection.ldf
- D:/Codex/Kai/stage255_256_height250nm_results.json
