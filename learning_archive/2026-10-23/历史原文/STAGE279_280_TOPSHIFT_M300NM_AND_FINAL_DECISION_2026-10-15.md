# Stage279/280：top shift = -300 nm 与局部优化终止判断

日期：2026-10-15。固定参数：638 nm，齿高237 nm，齿宽190 nm，z宽0.75 µm。

## -300 nm结果

- Stage279a审计通过；Stage279b于02:16启动、03:44自然完成；Stage280a/b/c执行成功。
- 净导模效率6.4738071244%；正向/反向6.4741817071%/0.0003745827%。
- TM/TE正向6.4580632589%/0.0158919115%。
- mode1=4.2672863300%，占正向导模65.91236581%。
- 网格误差0、源功率比1、重构误差0、32模式/28导模、a/b误差5.55e-17/1.78e-16。
- 直接散射净功率6.4740234163%，未展开残差-0.0002622599个百分点；数值闭合有效。

## 与-290 nm比较

- 总净导模效率下降0.00320776个百分点，相对下降0.04953%。
- mode1下降0.01213381个百分点，相对下降0.28354%。
- 因此-280/-290/-300 nm已包住总净导模局部峰值；-270/-280/-290 nm已包住mode1局部峰值。

## 双目标结论

| 目标 | 三点拟合顶点 | 已验证工程点 | 选择理由 |
|---|---:|---:|---|
| 总净导模效率 | -293.03 nm，预测6.477762% | **-290 nm，6.477015%** | 拟合相对增益仅约0.0115%，不值得再做3 nm细化 |
| mode1功率 | -283.75 nm，预测4.281330% | **-280 nm，4.280641%** | 拟合相对增益仅约0.0161%，不值得再做4 nm细化 |

- 以本阶段既定主目标“全部导模净功率”为准，冻结top shift=-290 nm。
- 若后续系统设计强调单一mode1纯度，则选-280 nm；它相对-290 nm仅损失约0.202%总净导模，却获得略高mode1并降低几何倾斜程度。
- 不再继续向更负方向外扩，也不进行亚10 nm细化；top shift一维局部优化在此停止。

## 可复现文件

- -300 nm完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage279b_HEIGHT237nm_TOOTH190nm_TOPSHIFTm300nm_GRATINGWIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp`
- -290 nm总功率最优工程点：`D:/FDTD_File/ar_incoupler_FDTD_stage277b_HEIGHT237nm_TOOTH190nm_TOPSHIFTm290nm_GRATINGWIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp`
- -280 nm mode1最优工程点：`D:/FDTD_File/ar_incoupler_FDTD_stage275b_HEIGHT237nm_TOOTH190nm_TOPSHIFTm280nm_GRATINGWIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp`
