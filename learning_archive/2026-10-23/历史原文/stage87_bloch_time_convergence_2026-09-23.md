# Stage87：Bloch共振仿真时间收敛

日期：2026-09-23

固定条件：5 nm局部网格、归一化kx=-0.1186131、620-656 nm激励、150 fs后开始谐波反演、自动停止阈值1e-9。

| 请求时间 | 实际t max | 共振波长 | Q | amplitude | error |
|---:|---:|---:|---:|---:|---:|
| 300 fs | 299.953 fs | 638.222 nm | 118.702 | 0.0270216 | 1.26622e-6 |
| 500 fs | 499.983 fs | 638.213 nm | 119.096 | 0.0267701 | 6.35377e-7 |
| 800 fs | 799.936 fs | 638.205 nm | 118.765 | 0.0268265 | 7.11541e-7 |

变化量：

- 波长300→500 fs：0.00872 nm
- 波长500→800 fs：0.00851 nm
- Q 300→500 fs：0.3946
- Q 500→800 fs：0.3309

## 结论

共振波长已经实现优于0.01 nm的时间收敛。Q值在118.7-119.1之间小幅波动，没有严格单调趋势，因此不应引用过多小数位；推荐报告为`Q≈119±0.3`。300 fs已经足以获得准确峰位，常规扫描可继续使用500 fs；800 fs适合最终Q值复核。

## 文件

- `D:/FDTD_File/ar_incoupler_FDTD_stage87_time_convergence_results.ldf`
- `D:/FDTD_File/ar_incoupler_FDTD_638nm_stage87_time800fs_mesh5nm_2D.fsp`
- `D:/Codex/Kai/fdtd_stage87_time_convergence.lsf`
- `D:/Codex/Kai/.ppt-build/recent_fdtd_optimization/stage87_complete_check.png`

## 下一步

Stage88建议验证激励与采样位置鲁棒性：改变偶极源位置或分别使用三个时间监视器独立提取共振，确认638.2 nm峰不依赖某一个特定采样点。
