# Stage275/276：top shift = -280 nm 工程验证

日期：2026-10-15  
固定参数：波长638 nm；齿高237 nm；齿宽190 nm；光栅z宽0.75 µm；top shift=-280 nm。

## 结果

- Stage275a几何审计通过：24对象启用，顶点、y位置和z span误差均为0。
- Stage275b于2026-10-14 22:59启动，2026-10-15 00:27自然完成。
- Stage276a/b/c在同一个可见Lumerical窗口执行成功。
- 净导模效率：6.4639388644%
- 正向/反向导模：6.4643096181% / 0.0003707537%
- TM/TE正向导模：6.4481976770% / 0.0158828699%
- mode1正向散射：4.2806408796%
- mode1占正向导模：66.21961404%
- 直接散射净功率：6.4644534174%
- 未展开散射净功率：0.0000340583%

## 数值有效性

- 网格误差0、源功率比1、相干重构误差0。
- 32模式/28导模；a/b线性误差7.85e-17/5.85e-17。
- 未展开残差仅0.0000341个百分点，结果有效。

## 对比与决策

| top shift | 净导模效率 | mode1 |
|---:|---:|---:|
| -260 nm | 6.4004633991% | 4.2572617830% |
| -270 nm | 6.4366149072% | 4.2720749952% |
| -280 nm | 6.4639388644% | 4.2806408796% |

- 相对-270 nm，净导模效率绝对提高0.02732396个百分点、相对提高0.42451%；mode1相对提高0.20051%。
- 增益连续收窄，但-260/-270/-280 nm仍单调，尚未形成峰值包络。
- 若继续该变量，下一点为-290 nm；仍需保持其它参数冻结并重复同一闭合验证。

## 可复现文件

- `D:/FDTD_File/ar_incoupler_FDTD_stage275b_HEIGHT237nm_TOOTH190nm_TOPSHIFTm280nm_GRATINGWIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp`
- `D:/FDTD_File/stage276a_height237nm_tooth190nm_topshiftm280nm_width0p75um_coherent_field_decomposition.ldf`
- `D:/FDTD_File/stage276b_height237nm_tooth190nm_topshiftm280nm_width0p75um_patterned_fixed_mode_basis32.ldf`
- `D:/FDTD_File/stage276c_height237nm_tooth190nm_topshiftm280nm_width0p75um_fixed_basis32_projection.ldf`
