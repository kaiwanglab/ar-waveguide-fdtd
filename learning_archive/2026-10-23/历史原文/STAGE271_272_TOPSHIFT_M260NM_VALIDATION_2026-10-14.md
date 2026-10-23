# Stage271/272：top shift = -260 nm 工程验证

日期：2026-10-14  
固定参数：波长638 nm；齿高237 nm；齿宽190 nm；光栅z宽0.75 µm；top shift=-260 nm。

## 执行与结果

- Stage271a几何审计通过：24个对象启用，顶点、y位置和z span误差均为0。
- Stage271b于19:21启动，20:51自然完成；完整FSP已保存。
- Stage272a/b/c在同一个可见Lumerical窗口执行成功，三份LDF结果均已生成。
- 净导模效率：6.4004633991%
- 正向/反向导模：6.4008277657% / 0.0003643665%
- TM/TE正向导模：6.3852249103% / 0.0153776010%
- mode1正向散射：4.2572617830%
- mode1占正向导模：66.51111292%
- 直接散射净功率：6.4012596460%
- 未展开散射净功率：0.0003295099%

## 数值有效性

- 网格坐标误差0，源功率比1，相干重构误差0。
- 固定32模基底，其中28个导模。
- a/b线性误差7.85e-17 / 5.21e-17。
- 未展开残差仅0.0003295个百分点，结果可用于工程趋势判断。

## 对比与决策

| top shift | 净导模效率 | mode1 |
|---:|---:|---:|
| -240 nm | 6.2999806868% | 4.2069526344% |
| -250 nm | 6.3532603392% | 4.2344995398% |
| -260 nm | 6.4004633991% | 4.2572617830% |

- 相对-250 nm，净导模效率绝对提高0.04720306个百分点、相对提高0.74297%；mode1相对提高0.53754%。
- -240/-250/-260 nm仍沿更负top shift方向单调提升，峰值未包住。
- 下一步保持其余参数不变，验证top shift=-270 nm；不能对未包峰数据直接做峰值外推。

## 可复现文件

- `D:/FDTD_File/ar_incoupler_FDTD_stage271b_HEIGHT237nm_TOOTH190nm_TOPSHIFTm260nm_GRATINGWIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp`
- `D:/FDTD_File/stage272a_height237nm_tooth190nm_topshiftm260nm_width0p75um_coherent_field_decomposition.ldf`
- `D:/FDTD_File/stage272b_height237nm_tooth190nm_topshiftm260nm_width0p75um_patterned_fixed_mode_basis32.ldf`
- `D:/FDTD_File/stage272c_height237nm_tooth190nm_topshiftm260nm_width0p75um_fixed_basis32_projection.ldf`
