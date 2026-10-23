# Stage277/278：top shift = -290 nm 工程验证

日期：2026-10-15。固定参数：638 nm，齿高237 nm，齿宽190 nm，z宽0.75 µm。

## 结果与有效性

- Stage277a审计通过；Stage277b于00:38启动、02:06自然完成；Stage278a/b/c执行成功。
- 净导模效率6.4770148869%；正向/反向6.4773879398%/0.0003730529%。
- TM/TE正向6.4612227729%/0.0159373398%。
- mode1=4.2794201360%，占正向导模66.06706555%。
- 网格误差0、源功率比1、重构误差2.06e-16、32模式/28导模、a/b误差1.11e-16/5.83e-17。
- 直接散射净功率6.4773825250%，未展开残差-0.0001151279个百分点；闭合有效。

## 对比与决策

- 相对-280 nm，总净导模效率绝对提高0.01307602个百分点、相对提高0.20229%。
- mode1反而下降0.00122074个百分点（相对-0.02852%），mode1占比下降0.15255个百分点。
- 若目标是总导模净功率，趋势尚未反转；再验证-300 nm作为最后一个外扩点。
- 若目标是mode1，-280 nm已经优于-290 nm；后续需将两个目标分开报告。

## 文件

- `D:/FDTD_File/ar_incoupler_FDTD_stage277b_HEIGHT237nm_TOOTH190nm_TOPSHIFTm290nm_GRATINGWIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp`
- `D:/FDTD_File/stage278a_height237nm_tooth190nm_topshiftm290nm_width0p75um_coherent_field_decomposition.ldf`
- `D:/FDTD_File/stage278b_height237nm_tooth190nm_topshiftm290nm_width0p75um_patterned_fixed_mode_basis32.ldf`
- `D:/FDTD_File/stage278c_height237nm_tooth190nm_topshiftm290nm_width0p75um_fixed_basis32_projection.ldf`
