# RCWA 学习检查点｜2026-08-31

## 本阶段目标

在 638 nm 红光下，从周期、占空比和齿高三个层次优化 `n=+1` 双偏振效率，同时保持波导内传播角接近 48.4 deg。

## 固定评价方法

- 数据集：`RCWA -> grating_orders`
- TM：`Tp_grating`；TE：`Ts_grating`
- 目标级次：绝对标签 `n=+1`
- 双偏振分数：`min(TM n=+1, TE n=+1)`
- 偏振差值：`abs(TM n=+1 - TE n=+1)`

## 周期优化

- 粗扫描：380、390、400、410、420 nm。
- 效率随周期上升，但输出角同时下降，因此不能只选择最高效率。
- 教学角度约束：目标 48.4 deg，允许误差 +/-1 deg。
- 402 nm：输出角 48.357 deg，双偏振分数 19.9634%，属于精确角度候选。
- 407 nm：输出角 47.432 deg，误差 0.968 deg；TM 29.2667%，TE 22.6062%，双偏振分数 22.6062%，属于容差边界高效率候选。
- 408 nm 已超出 +/-1 deg 约束。

## 占空比优化（固定周期 407 nm、高度 290 nm）

- 粗扫描：35% 到 65%，步长 5%。
- 细扫描：48% 到 53%，步长 1%。
- 最佳占空比：51%；齿宽 = 407 nm * 0.51 = 207.57 nm。
- TM 随占空比增加持续增强；TE 在约 51% 达峰后下降，因此由 TE 决定双偏振上限。

## 高度优化（固定周期 407 nm、占空比 51%）

- 粗扫描：230 到 350 nm，步长 20 nm。
- 细扫描：235 到 260 nm，步长 5 nm。
- 最终扫描：243 到 247 nm，步长 1 nm。
- 最佳高度：243 nm。
- TM n=+1 = 25.305827%；TE n=+1 = 25.366581%。
- 双偏振分数 = 25.305827%；TM/TE 差值仅 0.060754 个百分点。
- 相比原始 407 nm / duty 51% / height 290 nm 的 22.606170%，双偏振分数提高约 11.94%。

## 当前红光候选结构

- 波长：638 nm
- theta = -14 deg；phi = 0 deg
- 周期：407 nm
- 占空比：51%；齿宽：207.57 nm
- 齿高：243 nm；齿中心 z = 121.5 nm
- RCWA 顶层绝对接口位置同步为 243 nm
- `n=+1` 输出角：47.432 deg
- TM n=+1：25.305827%
- TE n=+1：25.366581%
- 双偏振分数：25.305827%

## 当前求解器设置

- `k vectors domain = circular`
- `max number k vectors = 100`
- `mesh refinement = conformal variant 0`
- `use li factorization = 0`
- `use tangent vector field = 0`

## 关键文件

- 最终高度模型：`D:/FDTD_File/ar_incoupler_RCWA_638nm_period407nm_duty51_height_final_best_2D.fsp`
- 周期粗扫描：`D:/Codex/Kai/rcwa_638nm_period_coarse_sweep.csv`
- 周期角度约束细扫描：`D:/Codex/Kai/rcwa_638nm_period_fine_angle_constrained.csv`
- 占空比细扫描：`D:/Codex/Kai/rcwa_638nm_period407_duty_fine_sweep.csv`
- 高度最终扫描：`D:/Codex/Kai/rcwa_638nm_period407_duty51_height_final_sweep.csv`

## 下一步

固定当前结构，扫描 `max number k vectors = 40, 60, 80, 100, 120, 150`。以 150 为参考，检查 TM/TE 的绝对误差；教学判据暂定为两者误差均小于 0.1 个百分点。通过后再进行制造容差扫描，而不是继续追逐名义点的微小效率提升。

## k 向量收敛结果

以 `k=150` 为参考：TM = 25.330323%，TE = 25.366636%。

- k=40：TM 误差约 0.1635 个百分点，未通过。
- k=60：TM 误差约 0.0947 个百分点，TE 误差约 0.00013 个百分点；刚好通过 0.1 个百分点教学判据。
- k=80：TM 误差约 0.0536 个百分点。
- k=100：TM 误差约 0.0245 个百分点，TE 误差约 0.00006 个百分点；运行约 1.98 s。
- k=120：TM 误差约 0.0173 个百分点。
- k=150：参考运行约 3.76 s。

结论：k=60 是最低可用设置；考虑 k=100 相对 k=60 只增加约 0.45 s，却显著降低误差，后续正式验证推荐使用 k=100。结构名义结果可报告约 TM 25.31%、TE 25.37%，并注明 k=100 收敛设置。

新增文件：

- `D:/Codex/Kai/rcwa_638nm_kvector_convergence.csv`
- `D:/FDTD_File/ar_incoupler_RCWA_638nm_period407nm_duty51_height243nm_converged_k60_2D.fsp`
- `D:/FDTD_File/ar_incoupler_RCWA_638nm_period407nm_duty51_height243nm_converged_k100_2D.fsp`

## 模型边界

当前仍是 n=1.8 平面波 RCWA 周期单元筛选模型，不等于最终有限尺寸 AR 波导入耦效率。后续仍需材料色散、FDTD 模式展开、有限光栅和系统级验证。
