# Stage123：高度 × 顶部横移联合鲁棒性

日期：2026-09-28  
软件：Ansys Lumerical FDTD 2026 R1  
粗筛网格：5 nm

## 目的

比较候选名义shift=-260 nm与旧名义shift=-280 nm。两者采用相同的高度误差（265/290/315 nm）和相同的shift误差（名义值±20 nm），按中心效率、9点平均效率和9点最差效率作公平判断。

## 联合矩阵：TM forward (%)

| 高度 (nm) \ shift (nm) | -240 | -260 | -280 | -300 |
|---:|---:|---:|---:|---:|
| 265 | 32.2193 | 32.3865 | 32.2072 | 31.6417 |
| 290 | 33.2949 | **33.4393** | 33.1954 | 32.5928 |
| 315 | 32.6142 | 32.9109 | 32.8316 | 32.4165 |

## 公平鲁棒性比较

候选-260 nm使用shift=-240/-260/-280的9个点；旧名义-280 nm使用shift=-260/-280/-300的9个点。

| 名义shift | 中心效率 | 9点平均 | 9点最差 |
|---:|---:|---:|---:|
| -260 nm | **33.4393%** | **32.7888%** | **32.2072%** |
| -280 nm | 33.1954% | 32.6246% | 31.6417% |

相对旧名义，-260 nm带来：

- 中心效率：+0.2439个百分点
- 9点平均：+0.1642个百分点
- 9点最差：+0.5655个百分点

## 决策

1. -260 nm不只是单点峰值更高，在联合高度/shift误差下的平均值和最差值也更好。
2. 将-260 nm升级为新的“鲁棒名义shift”。
3. 旧的-280 nm模型保留为可回退基准，不覆盖。
4. 下一步以height=290 nm、shift=-260 nm、period=334 nm、duty=62.5%执行3.5 nm完整能量守恒和模式纯度验证。
5. 只有Stage124通过后，才重新检查新名义结构的角度峰值、光谱峰值及关键制造窗口。

## 文件

- `D:/FDTD_File/stage123_height_shift_joint_robustness_mesh5nm.ldf`
- `D:/FDTD_File/stage123_joint_robustness_metrics.ldf`
- `D:/FDTD_File/ar_incoupler_FDTD_stage123_joint_matrix_complete_restored_h290_shiftM280_period334nm_mesh3p5nm_2D.fsp`
- `D:/Codex/Kai/stage123_height_shift_joint_robustness_mesh5nm.lsf`
- `D:/Codex/Kai/stage123_analyze_joint_robustness.lsf`
