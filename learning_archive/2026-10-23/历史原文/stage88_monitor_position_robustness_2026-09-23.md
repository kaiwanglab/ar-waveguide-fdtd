# Stage88：时间监视器采样位置鲁棒性

日期：2026-09-23

使用Stage87的800 fs仿真结果，不重新运行FDTD。三个时间监视器分别独立进行`findresonances`，并与三者归一化合成信号比较。

| 信号 | 共振波长 | Q | amplitude | error |
|---|---:|---:|---:|---:|
| monitor 1 | 638.211 nm | 118.514 | 0.0052139 | 1.34186e-8 |
| monitor 2 | 638.217 nm | 118.360 | 0.00330276 | 9.35477e-7 |
| monitor 3 | 638.212 nm | 118.870 | 0.0292008 | 6.01467e-7 |
| normalized sum | 638.205 nm | 118.765 | 0.0268265 | 7.11541e-7 |

- 共振波长最大差：0.0120919 nm
- Q最大差：0.510086

## 结论

三个空间位置和合成信号均识别到同一个约638.21 nm共振，峰位对监视器位置不敏感。振幅差异来自各监视器所处模场强弱位置，不影响本征频率判断。Q值位置间变化约0.51（约0.43%），推荐继续使用三个监视器的归一化合成结果，并将Q报告为约119而非保留过多小数。

## 文件

- `D:/FDTD_File/ar_incoupler_FDTD_stage88_monitor_position_robustness.ldf`
- `D:/Codex/Kai/fdtd_stage88_monitor_position_robustness.lsf`
- `D:/Codex/Kai/.ppt-build/recent_fdtd_optimization/stage88_monitor_robustness.png`

## 下一步

Stage89建议改变电偶极源位置并重复单点共振提取，验证638.2 nm峰不依赖特定激励位置。监视器鲁棒性验证了“怎么测”，源位置鲁棒性将验证“怎么激发”。
