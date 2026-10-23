# Stage257/258：240 nm 齿高验证

## 结论

240 nm 的净导模耦合效率为 **6.2782981894%**，相对 250 nm 的 **6.0539778363%** 提高 **3.7053%**。Mode 1 为 **4.2219370583%**，相对 250 nm 提高 **3.3485%**。

效率仍然上升，但相邻净效率增益已由 20.91% → 14.50% → 8.80% → 3.71% 连续收窄，峰值很可能位于当前附近。下一步只验证 **230 nm**；若下降，则用230/240/250 nm包住峰值。

## 结果

| 指标 | 240 nm |
|---|---:|
| 导模净效率 | 6.2782981894% |
| 导模前向 | 6.2786483101% |
| 导模后向 | 0.0003501207% |
| TM 前向 | 6.2636162642% |
| TE 前向 | 0.0148148757% |
| Mode 1 前向 | 4.2219370583% |
| Mode 1 / 导模前向 | 67.24277026% |
| 直接散射净值 | 6.2791146430% |
| 未展开净残差 | 0.0003799711% |

## 数值有效性

- pattern/reference 入射功率完全一致
- y/z 网格差均为0
- 相干场重构误差为0
- 32模式、28导模
- a/b线性误差：5.55e-17 / 6.63e-17
- 未展开净残差：0.0003800%

数值闭合正常。

## 决策

下一步保持其它参数不变，只验证230 nm。若230 nm下降，进行局部二次拟合并在240 nm附近选一个细化点；若继续上升，再验证220 nm。

## 可复现文件

- D:/FDTD_File/ar_incoupler_FDTD_stage257b_HEIGHT240nm_WIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp
- D:/FDTD_File/stage258a_height240nm_width0p75um_coherent_field_decomposition.ldf
- D:/FDTD_File/stage258b_height240nm_width0p75um_patterned_fixed_mode_basis32.ldf
- D:/FDTD_File/stage258c_height240nm_width0p75um_fixed_basis32_projection.ldf
- D:/Codex/Kai/stage257_258_height240nm_results.json
