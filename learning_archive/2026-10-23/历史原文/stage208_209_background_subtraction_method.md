# Stage208–209：为什么不能直接用“有齿功率 − 无齿功率”当入耦效率

## 1. 当前问题

Stage207 使用 z-PML、有限宽光栅，但激励仍是横向均匀的斜入射 plane wave。`power_right` 是 x-normal 面，因此它不仅会看到光栅激发的向右导波，也会看到斜入射背景本身的 x 向能流。

Stage208 保持 source、FDTD、mesh、monitor 全部相同，只关闭光栅齿。它给出无光栅时的背景场 `E0,H0`。Stage207 有齿时的场记为 `E,H`，定义光栅散射场：

`Es = E - E0`

`Hs = H - H0`

## 2. 相干功率的正确展开

有齿模型的时间平均 Poynting 矢量为：

`P = 0.5*Re[(E0+Es) × conj(H0+Hs)]`

展开后有四部分：

1. 无光栅参考背景：`0.5*Re[E0 × conj(H0)]`
2. 纯散射场：`0.5*Re[Es × conj(Hs)]`
3. 交叉项 A：`0.5*Re[E0 × conj(Hs)]`
4. 交叉项 B：`0.5*Re[Es × conj(H0)]`

因此：

`Ppattern = Preference + Pscattered + Pcross`

而简单的 `Ppattern - Preference` 实际等于 `Pscattered + Pcross`。交叉项可以为正也可以为负，所以这个差值不能一般性地解释成“光栅耦合功率”。

## 3. Stage209 的验收条件

- Stage207 与 Stage208 的 y/z 监视器网格坐标必须完全相同。
- 两次仿真的 source power 应相同；目标差异小于 0.1%。
- 四项重构必须满足 `Ppattern = Preference + Pscattered + Pcross`，相对误差接近机器精度。
- 若无光栅参考占有齿 `power_right` 的大部分，则确认直接功率指标被背景主导。
- 即使散射场功率可算出，它仍包含导波与辐射；最终入耦效率还需要对散射场做目标导模投影，或改用不会横穿输出面的有限光束。

## 4. 工程决策

- Stage207/208/209的作用是验证测量方法，不是继续追逐结构百分数。
- 背景问题关闭前，不再扫描周期、占空比、齿高或z宽度。
- 正式模型层级应分开：周期RCWA/周期FDTD负责局部衍射；2D有限齿FDTD负责沿传播方向的耦合；毫米级孔径与眼盒不使用全尺寸FDTD硬算。
