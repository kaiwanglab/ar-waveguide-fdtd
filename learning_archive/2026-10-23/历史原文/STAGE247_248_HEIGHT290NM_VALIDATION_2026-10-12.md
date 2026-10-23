# Stage247–248：三维有限光束齿高290 nm验证

日期：2026-10-12

## 验证目的

300/310/320 nm三点显示效率随齿高增加显著下降，尚未包住峰值。本轮保持其它参数不变，仅将齿高从300 nm降至290 nm，判断是否继续向更低齿高搜索。

固定参数：周期328.75 nm、齿宽185 nm、齿底-3.75 nm、top shift=-240 nm、光栅z宽0.75 um、wx=6 um、wz=0.65 um、入射角-15.1°。

## 数值完整性

- Stage247b自然完成，完整FSP、直接功率LDF均已保存
- Stage248a/b/c全部完成，stdout无错误、stderr为空
- 源功率比：1.000000
- 32个模式，其中28个满足`Re(neff)>1`
- a/b线性误差：`1.241e-16 / 1.164e-17`
- 未展开残差：`-0.0003661%`

上述误差远低于目标效率变化，结果物理有效。

## 290 nm结果

- 净导模效率：3.10842214%
- 正向导模效率：3.10860189%
- 反向导模效率：0.00017975%
- TM正向：3.09170268%
- TE正向：0.01659218%
- mode1正向：2.12087863%
- mode1占正向导模：68.22612561%
- 直接纯散射净值：3.10819670%

相对300 nm：

- 净导模效率提高41.5888%
- mode1绝对效率提高42.0332%

## 趋势与结论

| 齿高 | 净导模效率 | mode1效率 | mode1占比 |
|---|---:|---:|---:|
| 290 nm | 3.108422% | 2.120879% | 68.2261% |
| 300 nm | 2.195387% | 1.493228% | 68.0127% |
| 310 nm | 1.308103% | 0.885415% | 67.6830% |
| 320 nm | 0.620073% | 0.416611% | 67.1827% |

290→320 nm范围内净效率和mode1均随齿高降低而单调、显著上升，而mode1占比只小幅变化。峰值仍未被包住，不能将290 nm宣称为最优点。

下一点只验证280 nm。若280 nm继续提升，再向270 nm推进；若下降，则使用280/290/300 nm局部数据定位峰值并验证名义值及制造容差。每次只改一个齿高，不同时修改top shift。

## 可复现文件

- 设置与审计：`D:/FDTD_File/stage247a_height290nm_width0p75um_setup_gate.ldf`、`D:/FDTD_File/stage247a_height290nm_width0p75um_setup_consistency_audit.ldf`
- 完整FSP：`D:/FDTD_File/ar_incoupler_FDTD_stage247b_HEIGHT290nm_WIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp`
- Stage248结果：`D:/FDTD_File/stage248c_height290nm_width0p75um_fixed_basis32_projection.ldf`
- 机器可读汇总：`D:/Codex/Kai/stage247_248_height290nm_results.json`
