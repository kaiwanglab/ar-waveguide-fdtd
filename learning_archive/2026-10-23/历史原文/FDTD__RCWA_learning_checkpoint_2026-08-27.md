# RCWA 学习检查点｜2026-08-27

## 今日目标

在已优化的 532 nm 单周期 RCWA 入耦器上，学习用固定衍射级次标签比较蓝、绿、红三色响应，并手动验证红光周期相位匹配。

## 固定评价规则

- 读取对象：`RCWA -> grating_orders`
- `Tp_grating`：TM（p 偏振）
- `Ts_grating`：TE（s 偏振）
- 目标级次：绝对标签 `n=+1`
- 双偏振分数：`min(TM n=+1, TE n=+1)`
- `grating_power` 用于查看能量流向；不要与 `grating_orders` 的数值混合做扫描比较。

## 532 nm 基准结构

- 波长：532 nm；入射角：theta = -14 deg，phi = 0 deg
- 波导芯层折射率：1.8
- 周期：335 nm
- 占空比：51%；齿宽：170.85 nm
- 齿高：290 nm；齿中心 z = 145 nm
- 绿光 `n=+1`：TM 43.2420%，TE 43.4901%，双偏振分数 43.2420%。

## RGB 固定几何验证（335 nm 周期）

| 波长 | TM n=+1 | TE n=+1 | 双偏振分数 | 结论 |
|---|---:|---:|---:|---|
| 450 nm | 59.7657% | 57.9004% | 57.9004% | 目标级强，但 TM 的 n=-1 有约 5.98% 泄漏 |
| 532 nm | 43.2420% | 43.4901% | 43.2420% | 当前基准点 |
| 638 nm | 3.1385% | 10.5295% | 3.1385% | 主要停留在 n=0，红光周期失配 |

## 红光相位匹配与手动验证

为了保持 532 nm 的近似波导内传播方向，用：

`n_core*sin(theta_out) = sin(theta_in) + lambda/period`

由 532 nm / 335 nm / -14 deg 得到目标内角约 48.4 deg；638 nm 对应的估算周期约 402 nm。

已手动验证 400 nm：

- 实际波长：638 nm（`6.38e-7 m`）
- 周期：400 nm（`4e-7 m`）
- 齿宽：204 nm（`2.04e-7 m`），保持 51% 占空比
- 齿高：290 nm，中心 z=145 nm；theta=-14 deg
- 结果：TM n=+1 = 22.4186%，TE n=+1 = 18.7748%，双偏振分数 = 18.7748%
- 对比红光 335 nm：双偏振分数从 3.1385% 提升到 18.7748%。
- 但 n=0 仍占主导（TM 68.9067%，TE 72.2297%），400 nm 仅证明方向正确，不是最终最优值。

## 重要文件

- `D:/FDTD_File/ar_incoupler_RCWA_532nm_dualpol_best_theta_m14deg_2D.fsp`
- `D:/FDTD_File/ar_incoupler_RCWA_450nm_dualpol_geometry_theta_m14deg_2D.fsp`
- `D:/FDTD_File/ar_incoupler_RCWA_638nm_dualpol_geometry_theta_m14deg_2D.fsp`
- `D:/FDTD_File/ar_incoupler_RCWA_635nm_period400nm_dualpol_theta_m14deg_2D.fsp`
  - 注意：该文件名中的 `635nm` 是保存时的命名笔误；模型内部波长已核对为 638 nm。
- `D:/Codex/Kai/rcwa_RGB_532nm_geometry_summary.csv`
- `D:/Codex/Kai/rcwa_638nm_period400nm_result_card.csv`

## 明天的下一步

在 638 nm、theta=-14 deg、占空比 51%、高度 290 nm 条件下，对周期做粗扫描：380、390、400、410、420 nm；每个周期同步设置齿宽为 `period * 0.51`。比较各点的 `min(TM n=+1, TE n=+1)`，找到红光目标级次的峰值附近，再进行细扫描。

## 边界

当前结果是 n=1.8 平面波 RCWA 的周期单元筛选结果，不等同于最终 AR 波导的真实入耦效率。后续需用 FDTD 模式展开、材料色散、有限光栅与系统级模型验证。
