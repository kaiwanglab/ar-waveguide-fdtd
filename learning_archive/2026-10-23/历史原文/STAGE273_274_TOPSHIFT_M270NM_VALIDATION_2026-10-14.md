# Stage273/274：top shift = -270 nm 工程验证

日期：2026-10-14  
固定参数：波长638 nm；齿高237 nm；齿宽190 nm；光栅z宽0.75 µm；top shift=-270 nm。

## 执行与结果

- Stage273a几何审计通过：24个对象启用，顶点、y位置和z span误差均为0。
- Stage273b于21:06启动，22:42自然完成；完整FSP已保存。
- Stage274a/b/c在同一个可见Lumerical窗口执行成功。
- 净导模效率：6.4366149072%
- 正向/反向导模：6.4369826263% / 0.0003677191%
- TM/TE正向导模：6.4210574104% / 0.0156970387%
- mode1正向散射：4.2720749952%
- mode1占正向导模：66.36766391%
- 直接散射净功率：6.4372761550%
- 未展开散射净功率：0.0001846018%

## 数值有效性

- 网格误差0、源功率比1、相干重构误差约2.06e-16。
- 32模式/28导模；a/b线性误差1.12e-16/8.86e-17。
- 未展开残差0.0001846个百分点，结果有效。

## 对比与决策

| top shift | 净导模效率 | mode1 |
|---:|---:|---:|
| -250 nm | 6.3532603392% | 4.2344995398% |
| -260 nm | 6.4004633991% | 4.2572617830% |
| -270 nm | 6.4366149072% | 4.2720749952% |

- 相对-260 nm，净导模效率绝对提高0.03615151个百分点、相对提高0.56483%；mode1相对提高0.34795%。
- 增益继续收窄，但三点仍沿更负方向单调提升，峰值没有包住。
- 下一步保持其它参数不变，验证top shift=-280 nm。

## 可复现文件

- `D:/FDTD_File/ar_incoupler_FDTD_stage273b_HEIGHT237nm_TOOTH190nm_TOPSHIFTm270nm_GRATINGWIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp`
- `D:/FDTD_File/stage274a_height237nm_tooth190nm_topshiftm270nm_width0p75um_coherent_field_decomposition.ldf`
- `D:/FDTD_File/stage274b_height237nm_tooth190nm_topshiftm270nm_width0p75um_patterned_fixed_mode_basis32.ldf`
- `D:/FDTD_File/stage274c_height237nm_tooth190nm_topshiftm270nm_width0p75um_fixed_basis32_projection.ldf`
