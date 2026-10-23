# Stage281/282：最终几何在 wz=0.55 µm 名义照明下的验证

日期：2026-10-15。最终几何：周期328.75 nm、齿高237 nm、齿宽190 nm、top shift=-290 nm、光栅z宽0.75 µm；`wx=6 µm`。

## 执行

- Stage281a重建`wz=0.55 µm`导入源，并加载最终几何；入射功率`6.8075573954e-15 W`，数据边缘场幅1.8316%。
- Stage281b有齿模型03:59启动、05:27自然完成。
- 因旧Stage225c参考的z域/监视器与当前模型不匹配，没有错误复用；Stage281c在同一Stage281a设置下运行严格匹配的无齿参考，05:36启动、07:03自然完成。
- Stage282a/b/c完成相干扣背景、固定32模基底和纯散射场投影。

## 最终结果

- 净导模效率：7.1033243043%
- 正向/反向导模：7.1037361168% / 0.0004118124%
- TM/TE正向导模：7.0847096981% / 0.0187611797%
- mode1正向散射：4.6956345991%
- mode1占正向导模：66.10091538%
- 直接散射净功率：7.1039350684%
- 未展开散射净功率：0.0000513568%

## 数值闭合

- pattern/reference源功率逐位一致，源功率比1。
- y/z网格最大差0，参考插值与原生功率差0。
- 相干重构相对误差2.20e-16。
- 32模式/28导模；a/b线性误差5.55e-17/3.49e-17。
- 未展开残差仅0.0000514个百分点，结果有效。

## 与 wz=0.65 µm 比较

| 指标 | wz=0.55 µm | wz=0.65 µm | 变化 |
|---|---:|---:|---:|
| 净导模效率 | 7.103324% | 6.477015% | +0.626309 pp / +9.6697% |
| mode1效率 | 4.695635% | 4.279420% | +0.416214 pp / +9.7260% |
| 绝对净导模功率 | 4.83563e-16 W | 5.21095e-16 W | -7.2026% |

更窄光束在归一化效率上更高，但更宽光束因携带更多总功率，绝对耦合导模功率更高。因此系统端必须明确优化目标是“效率”还是“眼盒所需绝对功率”。

## 保存文件

- 有齿完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage281b_FINAL_GEOMETRY_wx6um_wz0p55um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp`
- 严格匹配无齿参考：`D:/FDTD_File/ar_incoupler_FDTD_stage281c_FINAL_GEOMETRY_wx6um_wz0p55um_zdomain2p8um_REFERENCE_COMPLETE_638nm.fsp`
- 场分解：`D:/FDTD_File/stage282a_final_geometry_wz0p55_coherent_field_decomposition.ldf`
- 固定模态基底：`D:/FDTD_File/stage282b_final_geometry_wz0p55_patterned_fixed_mode_basis32.ldf`
- 固定基底投影：`D:/FDTD_File/stage282c_final_geometry_wz0p55_fixed_basis32_projection.ldf`
