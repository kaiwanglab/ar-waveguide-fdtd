# Stage86：Bloch共振网格收敛验证

日期：2026-09-23

固定条件：周期335.5 nm、归一化kx=-0.1186131、同一几何、同一620-656 nm激励与150 fs时间截断。

| 局部网格 | 共振波长 | Q | 芯层+光栅 `|E|^2`比例 |
|---:|---:|---:|---:|
| 7.5 nm | 638.270 nm | 118.552 | 89.6655% |
| 5.0 nm | 638.193 nm | 119.094 | 89.0717% |
| 3.5 nm | 638.101 nm | 119.099 | 88.4335% |
| 2.5 nm | 638.075 nm | 119.269 | 88.2025% |

相邻细化的峰位变化：

- 7.5 → 5.0 nm：0.0768 nm
- 5.0 → 3.5 nm：0.0919 nm
- 3.5 → 2.5 nm：0.0258 nm

## 结论

最后一次细化仅改变0.0258 nm，共振峰在约638.08 nm处实现良好收敛。5 nm结果相对2.5 nm仅偏移约0.118 nm，适合日常参数扫描；2.5-3.5 nm适合最终候选验证。场集中度随网格细化从89.07%变化到88.20%，差约0.87个百分点，模场归属结论不变。

## 文件

- `D:/FDTD_File/ar_incoupler_FDTD_stage86_mesh_convergence_results.ldf`
- `D:/FDTD_File/ar_incoupler_FDTD_stage86b_mesh2p5nm_result.ldf`
- `D:/FDTD_File/ar_incoupler_FDTD_638nm_stage86_mesh3p5nm_convergence_2D.fsp`
- `D:/FDTD_File/ar_incoupler_FDTD_638nm_stage86b_mesh2p5nm_2D.fsp`
- `D:/Codex/Kai/fdtd_stage86_bloch_mesh_convergence.lsf`
- `D:/Codex/Kai/fdtd_stage86b_mesh2p5nm_check.lsf`

## 推荐工作流

- 粗扫：7.5-10 nm
- 常规优化：5 nm
- 最终复核：2.5-3.5 nm

下一步Stage87应做仿真时间收敛，比较500 fs与更长时间下的峰位和Q。峰位已较稳定，但Q对时间长度更敏感，需独立验证后才可引用。
