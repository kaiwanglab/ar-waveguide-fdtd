# Stage74–Stage76：638 nm 入射角95%带宽验证

日期：2026-09-23

## 固定结构与评价量

- 周期：335.5 nm
- 占空比：50%
- 高度：210 nm
- 波长：638 nm
- 启用光源：`gaussian_source`
- 设计入射角：−13°
- 评价量：右行导模 `TMsum = TM1_forward + TM3_forward`
- 角度带宽判据：`TMsum(angle) >= 0.95 × TMsum(−13°)`

## Stage74：Accuracy 3 边界细扫

| 入射角 (deg) | TMsum (%) | 相对 −13° 保留率 (%) |
|---:|---:|---:|
| −14.50 | 23.8026 | 93.8942 |
| −14.25 | 24.2778 | 95.7685 |
| −14.00 | 24.6783 | 97.3485 |
| −13.00 | 25.3505 | 100.0000 |
| −12.00 | 24.5119 | 96.6920 |
| −11.75 | 24.0723 | 94.9580 |
| −11.50 | 23.5486 | 92.8923 |

相邻点线性插值得到：

- 左95%边界：−14.3525°
- 右95%边界：−11.7561°
- 95%角宽：2.59644°

## Stage75：Accuracy 4 三点验证

Accuracy 4 下重新计算 −13°，得到同精度基准 `TMsum = 25.5208%`。

| 点位 | 入射角 (deg) | TMsum (%) | 保留率 (%) |
|---|---:|---:|---:|
| Stage74左边界 | −14.3525 | 24.2239 | 94.9185 |
| 峰值基准 | −13.0000 | 25.5208 | 100.0000 |
| Stage74右边界 | −11.7561 | 24.2739 | 95.1144 |

两个旧边界仅偏离95%约 0.08–0.11 个百分点，说明网格影响很小，但仍需要两个补点校正交点。

## Stage76：Accuracy 4 最终边界校正

补算结果：

- `−14.25° → TMsum 24.4123%，保留率 95.6566%`
- `−11.70° → TMsum 24.1642%，保留率 94.6845%`

把补点与 Stage75 的相邻点配对插值，得到最终 Accuracy 4 结果：

- **左95%边界：−14.3412°**
- **右95%边界：−11.7412°**
- **95%角宽：2.60001°**
- 角带中心：约 −13.0412°
- 设计角 −13° 到左边界余量：1.3412°
- 设计角 −13° 到右边界余量：1.2588°

Accuracy 3 与 Accuracy 4 的角宽仅相差约 0.00357°（约0.14%），因此该95%角宽对本次网格加密已经基本收敛。

## 如何理解物理意义

设计角附近满足最佳光栅相位匹配。改变入射角会改变入射光的面内波矢，偏离匹配条件后，耦入右行导模的功率下降。2.60°表示在当前单色、当前 Gaussian 光束、当前结构和当前监视器定义下，耦合效率保持峰值95%以上的入射角接受宽度。

这个数值不能直接当成整副AR眼镜的显示FOV。整机FOV还受光机角谱、波导传播、扩瞳、出耦结构、颜色以及眼盒位置影响。

## 保存文件

- `D:\Codex\Kai\fdtd_stage74_gaussian_angle_95pct_boundary_fine.lsf`
- `D:\Codex\Kai\fdtd_stage75_accuracy4_angle_boundary_verify.lsf`
- `D:\Codex\Kai\fdtd_stage76_accuracy4_angle_boundary_correction.lsf`
- `D:\FDTD_File\ar_incoupler_FDTD_stage74_angle_95pct_boundary_results.ldf`
- `D:\FDTD_File\ar_incoupler_FDTD_stage75_accuracy4_angle_boundary_results.ldf`
- `D:\FDTD_File\ar_incoupler_FDTD_stage76_accuracy4_angle_95pct_results.ldf`
- `D:\FDTD_File\ar_incoupler_FDTD_638nm_stage76_final_angle_95pct_2D.fsp`

最终模型已恢复到 `gaussian_source angle theta = −13°`，并保留 `mesh accuracy = 4`。

## 下一阶段

结构尺寸公差和单色角度接受范围已经完成。下一步应验证角度与波长的二维联合响应，回答“不同波长下最佳入射角是否漂移”，这是从单色入耦器走向AR显示色散分析的关键一步。
