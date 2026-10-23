# Stage70 收紧联合公差窗口验证

## 候选窗口

- period = 335.5 ± 2.0 nm，即 333.5/337.5 nm
- duty = 50 ± 5 个百分点，即 45/55%
- height = 210 ± 20 nm，即 190/230 nm
- 基准：TMsum = 25.3505%，mesh accuracy = 3

## 8 角点结果

| Case | Period (nm) | Duty (%) | Height (nm) | TMsum (%) | Retention (%) | 判定 |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 333.5 | 45 | 190 | 23.9650 | 94.5345 | 不通过 |
| 2 | 333.5 | 45 | 230 | 24.2302 | 95.5807 | 通过 |
| 3 | 333.5 | 55 | 190 | 24.8574 | 98.0548 | 通过 |
| 4 | 333.5 | 55 | 230 | 24.2258 | 95.5633 | 通过 |
| 5 | 337.5 | 45 | 190 | 24.8108 | 97.8710 | 通过 |
| 6 | 337.5 | 45 | 230 | 25.1096 | 99.0499 | 通过 |
| 7 | 337.5 | 55 | 190 | 24.1064 | 95.0924 | 临界通过 |
| 8 | 337.5 | 55 | 230 | 23.5206 | 92.7817 | 不通过，最差角点 |

## 与 Stage69 对比

- Stage69 最差保持率：77.5782%
- Stage70 最差保持率：92.7817%
- 提升：15.2035 个百分点
- Stage69 严格通过角点：2/8
- Stage70 严格通过角点：6/8

收紧窗口明显有效，但还不能把 Stage70 的范围作为最终联合制造规格。

## Stage70 的 2^3 因子效应

| 项目 | 效应（百分点） |
|---|---:|
| Period | +0.265 |
| Duty | -1.386 |
| Height | -0.644 |
| Period × Duty | -3.137 |
| Period × Height | +0.078 |
| Duty × Height | -1.757 |
| Period × Duty × Height | +0.012 |

最强项仍是 Period × Duty，其次是 Duty × Height。因此下一轮应优先收紧占空比，并适度收紧周期和高度，而不是继续大范围单因素扫描。

## 下一轮候选值

根据 Stage70 最差角点相对 95% 阈值的缺口，将三项半范围缩小到大约 Stage70 的 70%：

- period = 335.5 ± 1.5 nm，即 334.0/337.0 nm
- duty = 50 ± 3.5 个百分点，即 46.5/53.5%
- height = 210 ± 15 nm，即 195/225 nm

这将作为 Stage71 的最终候选联合规格验证；若 8 个角点全部达到 95%，停止继续收紧并转入更高网格精度复核。

## 文件

- 脚本：`D:/Codex/Kai/fdtd_stage70_reduced_joint_tolerance_8corners.lsf`
- 结果：`D:/FDTD_File/ar_incoupler_FDTD_stage70_reduced_joint_tolerance_8corners_results.ldf`
- 模型：`D:/FDTD_File/ar_incoupler_FDTD_638nm_stage70_post_reduced_joint_tolerance_accuracy3_2D.fsp`
