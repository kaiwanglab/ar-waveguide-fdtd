# AR 波导 RCWA 学习检查点

日期：2026-08-25  
软件：Ansys Lumerical FDTD / RCWA 2026 R1  
阶段：532 nm 单周期光栅的双偏振、定向入耦局部优化完成；尚未进行波长带宽、材料色散、收敛与真实导模验证。

## 今日完成

1. 手动查看并理解了双偏振候选模型的几何、RCWA分层界面和入射条件。
2. 学会了为什么光栅高度改变时，需要同步修改 RCWA 的 `interface absolute positions`。
3. 建立了结果卡工作流：从 `grating_orders` 中按固定标签读取 `n=-1,0,+1`，不再依赖肉眼读 Visualizer 曲线。
4. 完成 TM/TE 双偏振粗扫与细扫，目标函数为：

   `dualpol_score = min(TM n=+1, TE n=+1)`

5. 理解了：`2D Y-normal` 模式中 `n` 是 x 方向的衍射级次，`m=0`；此处目标为 `n=+1`。

## 当前最佳双偏振候选

| 参数 | 数值 |
| --- | ---: |
| 波长 | 532 nm |
| 周期 | 335 nm |
| 占空比 | 51% |
| 齿宽 x span | 170.85 nm = 0.17085 µm |
| 光栅高度 z span | 290 nm = 0.29 µm |
| 齿中心 z | 145 nm = 0.145 µm |
| RCWA 模式 | 2D Y-normal |
| 传播方向 | backward，空气向波导 |
| 入射角 theta | -14° |
| phi | 0° |
| 上方介质 | n=1.0 |
| 下方 core-proxy | n=1.8 |
| RCWA 界面位置 | -0.30、0、0.29 µm |

## 最终结果卡

| 级次 | TM | TE |
| ---: | ---: | ---: |
| n=-1 | 0% | 0% |
| n=0 | 52.4978% | 49.1268% |
| n=+1 | 43.2420% | 43.4901% |

双偏振评分：`min(43.2420%, 43.4901%) = 43.2420%`。

这不是最终 AR 波导效率；它是空气到 `n=1.8` 平面波代理结构中的 RCWA 周期单元筛选结果。最终需回到FDTD模式展开监视器验证真实导模耦合。

## 优化过程

### 1. 单目标 TM 优化

- 参数：占空比59%、高度290 nm、theta=-14°。
- 结果：TM n=+1 = 44.1182%，TE n=+1 = 34.4098%。
- 缺点：TM与TE不平衡。

### 2. 双偏振粗扫

- 固定：周期335 nm、theta=-14°。
- 扫描：占空比45–65%，步长5%；高度220–340 nm，步长30 nm。
- 粗扫最佳：占空比50%、高度310 nm；TM=45.44%、TE=40.81%、评分40.81%。

### 3. 双偏振细扫

- 扫描：占空比48–52%，步长1%；高度290–330 nm，步长10 nm。
- 最优：占空比51%、高度290 nm；TM=43.24%、TE=43.49%、评分43.24%。

## 已掌握的结果读取逻辑

```text
.fsp 模型
  → lumapi 打开模型
  → getresult("RCWA", "grating_orders")
  → 固定取 n=-1、0、+1
  → 读取 Tp_grating（TM）和 Ts_grating（TE）
  → 写入 CSV 结果卡
```

不要用 `grating_power` 图的左右位置来替代固定级次标签；斜入射时可传播级次会改变，必须按 `grating_orders` 中的 n 标签读取。

## 明天从这里开始

1. 打开 `ar_incoupler_RCWA_532nm_dualpol_best_theta_m14deg_2D.fsp`。
2. 手动复查：占空比51%、高度290 nm、界面位置0.29 µm、theta=-14°。
3. 使用 `rcwa_polarization_result_card.py` 生成一次结果卡，确认可独立读取 TM/TE 的 n=-1、0、+1。
4. 再学习并执行波长扫描：先比较 450 nm、532 nm、638 nm 的 n=+1 效率和方向性。
5. 波长扫描后，再讨论是否需要独立RGB周期、色散补偿或多层/非对称光栅。

## 关键文件

- `D:/FDTD_File/ar_incoupler_RCWA_532nm_dualpol_best_theta_m14deg_2D.fsp`
- `D:/Codex/Kai/rcwa_dualpol_best_result_card.csv`
- `D:/Codex/Kai/rcwa_dualpol_fine_sweep_532nm_theta_m14.csv`
- `D:/Codex/Kai/rcwa_dualpol_coarse_sweep_532nm_theta_m14.csv`
- `D:/Codex/Kai/rcwa_polarization_result_card.py`
- `D:/Codex/Kai/RCWA_result_card_template.py`

