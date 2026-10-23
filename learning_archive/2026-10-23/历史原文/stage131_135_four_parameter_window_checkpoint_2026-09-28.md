# Stage131–135：四参数联合制造窗口与数值验证

日期：2026-09-28  
软件：Ansys Lumerical FDTD 2026 R1

## 候选三参数联合窗口

- period=334 +/-1.25 nm
- tooth width=208.75 +/-7.5 nm
- height=290 +/-12.5 nm
- top shift名义值=-260 nm

## Stage131：加入shift +/-20 nm的5 nm筛选

对P/W/H八个角点再叠加shift=-280/-240 nm，共16点。

- 15/16点达到95%保持率。
- 唯一失败点：P=335.25 nm、W=216.25 nm、H=302.5 nm、shift=-240 nm。
- 该点TM=31.6061%，保持率94.5177%。
- 同一P/W/H在shift=-280 nm时保持率95.2989%。

结论：shift +/-20 nm与其他三项联合极限同时发生时不能保证95%。

## Stage132：限制角点的shift边界

5 nm网格结果：

| shift | TM | 保持率 |
|---:|---:|---:|
| -275 nm | 31.9129% | 95.4353% |
| -265 nm | 31.9427% | 95.5243% |
| -255 nm | 31.8851% | 95.3521% |
| -250 nm | 31.8156% | 95.1441% |
| -245 nm | 31.7237% | 94.8696% |

正向95%边界约为-247.4 nm。为保持对称并留余量，候选shift规格收紧为-260 +/-10 nm。

## Stage133：最终3.5 nm四参数全角点验证

完整候选窗口：

- period=334 +/-1.25 nm
- width=208.75 +/-7.5 nm
- height=290 +/-12.5 nm
- shift=-260 +/-10 nm

结果：16/16点全部通过95%。

- 最差点：P=335.25 nm、W=216.25 nm、H=302.5 nm、shift=-250 nm
- 最差TM：31.8500%
- 相对名义33.4535%的保持率：95.2067%
- 第二低点为相同P/W/H、shift=-270 nm：95.5951%

## Stage134：3.0 nm差分网格复核

| 网格 | 名义TM | 最差TM | 保持率 |
|---:|---:|---:|---:|
| 3.5 nm | 33.4535% | 31.8500% | 95.2067% |
| 3.0 nm | 33.4805% | 31.8974% | 95.2716% |

保持率只变化+0.0649个百分点，且余量增加，说明95%通过不是3.5 nm网格偶然误差。

## Stage135：最差角点能量守恒

- TM前向/完整光源：31.8500%
- 同位置右行总功率：31.7411%
- 模式与局部总功率差：0.108835个百分点
- 封闭盒截获输入：81.0390%
- 右侧输出：32.4597%
- 左侧输出：0.215889%
- 底部输出：48.4378%
- 相对能量闭合误差：0.0918574%
- TM/封闭盒输入：39.3020%

结论：最差角点的能量闭合仍小于0.1%，模式功率与同位置总功率差约0.34%相对量，数值结果可接受。

## 当前冻结候选

四参数联合制造窗口暂冻结为：

`period 334 +/-1.25 nm; width 208.75 +/-7.5 nm; height 290 +/-12.5 nm; shift -260 +/-10 nm`

该窗口的最差保持率仅有0.2067个百分点余量，因此下一项必须验证名义点与最差点的测量面位置敏感性；若保持率随测量面变化超过余量，应进一步收紧窗口或改进模式提取方法。

## 文件

- `D:/FDTD_File/stage131_four_parameter_joint_corners_shift20_mesh5nm.ldf`
- `D:/FDTD_File/stage132_critical_corner_shift_refine_mesh5nm.ldf`
- `D:/FDTD_File/stage133_four_parameter_joint_corners_shift10_mesh3p5nm_verify.ldf`
- `D:/FDTD_File/stage134_nominal_worst_mesh3nm_convergence.ldf`
- `D:/FDTD_File/stage135_worst_corner_energy_validation_mesh3p5nm.ldf`
- `D:/FDTD_File/ar_incoupler_FDTD_stage135_worst_corner_energy_validated_restored_nominal_mesh3p5nm_2D.fsp`
- `D:/Codex/Kai/stage133_results_worst.png`
- `D:/Codex/Kai/stage134_results.png`
- `D:/Codex/Kai/stage135_results.png`
