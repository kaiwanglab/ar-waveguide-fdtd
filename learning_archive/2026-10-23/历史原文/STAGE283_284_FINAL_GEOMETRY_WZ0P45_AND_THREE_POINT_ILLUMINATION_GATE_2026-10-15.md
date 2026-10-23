# Stage283/284：最终几何 wz=0.45 µm 验证与三点照明门控

日期：2026-10-15。固定最终光栅几何：638 nm、周期328.75 nm、齿高237 nm、齿宽190 nm、top shift=-290 nm、光栅z宽0.75 µm、wx=6 µm。

## wz=0.45 µm 结果

- 净导模效率：7.6843735229%
- 正向/反向导模：7.6848214507% / 0.0004479278%
- TM/TE正向导模：7.6628358095% / 0.0216831770%
- mode1正向散射：5.0869913475%
- mode1占正向导模：66.19530955%
- 入射功率：5.570171652778e-15 W
- 绝对净导模功率：4.280327956680e-16 W
- 直接散射净功率：7.6852824190%
- 未展开散射净功率：0.0002647136%

## 数值与物理有效性

- PASS — `grid_match`
- PASS — `source_match`
- PASS — `coherent_reconstruction`
- PASS — `reference_interpolation`
- PASS — `fixed_basis`
- PASS — `projection_linearity`
- PASS — `efficiency_physical`
- PASS — `mode1_physical`
- PASS — `modal_residual_small`

总判定：**有效**。网格误差=0.000e+00/0.000e+00 m，源功率比=1，相干重构相对误差=1.236e-16，a/b线性误差=6.206e-17/7.068e-17。

## 三点照明宽度比较

| wz (µm) | 入射功率 (W) | 净导模效率 | mode1效率 | mode1占比 | 绝对净导模功率 (W) |
|---:|---:|---:|---:|---:|---:|
| 0.45 | 5.570172e-15 | 7.684374% | 5.086991% | 66.1953% | 4.280328e-16 |
| 0.55 | 6.807557e-15 | 7.103324% | 4.695635% | 66.1009% | 4.835629e-16 |
| 0.65 | 8.045297e-15 | 6.477015% | 4.279420% | 66.0671% | 5.210951e-16 |

- 归一化效率最优：wz=0.45 µm。
- 绝对净导模功率最优：wz=0.65 µm。
- 工程比较名义点：wz=0.55 µm，净导模效率=7.103324%。
- 最差照明端点：wz=0.65 µm，净导模效率=6.477015%。
- 三点跨度：1.207359个百分点，相对名义点=16.9971%。
- 端点相对名义点变化：0.45 µm=+8.1800%，0.65 µm=-8.8171%。
- 临时2%照明敏感性门槛：**未通过**。
- wz=0.55 µm 相对效率最优点差距：7.5614%。
- wz=0.55 µm 相对绝对功率最优点差距：7.2026%。

物理意义：缩小 `wz` 会改变入射高斯光束与有限光栅的空间重叠，同时降低总入射功率。因此“归一化耦合效率最高”和“实际耦入导模的绝对功率最高”可能落在不同光束宽度；两者必须同时报告，不能只挑一个百分比。

## 工程决策

结果在数值上有效，但未通过临时2%照明敏感性门槛。继续以wz=0.55 µm作为比较名义点，以0.45/0.65 µm作为容差端点，不优化wz本身。下一轮几何候选必须按名义效率、最差端效率和三点跨度排序，直到真实投影光机的光斑/瞳孔数据替换该临时门槛。

## 可复现文件

- patterned：`D:\FDTD_File\ar_incoupler_FDTD_stage283b_FINAL_GEOMETRY_wx6um_wz0p45um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp`
- matched reference：`D:\FDTD_File\ar_incoupler_FDTD_stage283c_FINAL_GEOMETRY_wx6um_wz0p45um_zdomain2p8um_REFERENCE_COMPLETE_638nm.fsp`
- coherent decomposition：`D:\FDTD_File\stage284a_final_geometry_wz0p45_coherent_field_decomposition.ldf`
- fixed modal basis：`D:\FDTD_File\stage284b_final_geometry_wz0p45_patterned_fixed_mode_basis32.ldf`
- fixed-basis projection：`D:\FDTD_File\stage284c_final_geometry_wz0p45_fixed_basis32_projection.ldf`
- machine-readable summary：`D:\Codex\Kai\stage283_284_final_geometry_wz0p45_three_point_results.json`
