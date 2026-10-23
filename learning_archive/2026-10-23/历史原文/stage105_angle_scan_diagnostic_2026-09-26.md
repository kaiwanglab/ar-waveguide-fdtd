# Stage105：入射角扫描诊断（当前未形成有效角度容差结论）

日期：2026-09-26

## 已确认的基准

- 目标波长：638 nm
- 几何：占空比62.5%、齿高290 nm、shift -280 nm
- 局部网格：5 nm
- 光源注入轴：y
- 光源方向：Backward
- 偏振角：90°
- 基准 `angle theta`：-12.5°
- 基准目标右行TM：58.5148%

## 首次扫描及异常

尝试角度：-17.5°、-15°、-12.5°、-10°、-7.5°。

所有结果均为58.5148%，完全相同。该结果不符合有限光栅的正常角度响应，因此不能作为角度容差结论。

## 发现的配置问题

1. FDTD区域四周边界均为PML。
2. 原光源 `plane wave type` 为 `Bloch/periodic`。
3. Ansys官方说明指出，Bloch/periodic斜入射通常应与周期/Bloch边界配合；有限结构并使用PML时，可使用Diffracting plane wave。
4. 已将源类型切换为Diffracting，并在-12.5°重新计算。
5. 修正后的基准仍为58.5148%，右向总功率0.58632，TM纯度99.8%，说明基准效率可复现。
6. 但改变Diffracting源的theta后，结果依旧完全一致，表明当前模型还存在角度源未真实改变或结果链未响应的问题。

## 明确排除

- 不是脚本没有改theta：`getnamed("source","angle theta")`能读出更新后的值。
- 不是波长采样错误：光源和全局监视器均锁定638 nm。
- 不是源类型切换失败：已打印确认 `plane wave type=Diffracting`。
- `getsourceangle()`不能用于当前Diffracting源，因此不能用该命令验证实际角度。

## 下一步验证方法

在继续读取耦合效率前，必须先验证入射波前：

1. 分别建立两个极端角度（例如0°与-20°）；
2. 在无结构或结构上方的场监视器中显示复电场相位；
3. 检查等相位线斜率是否随theta改变；
4. 只有波前方向确认改变后，才继续角度效率扫描；
5. 若Diffracting源仍不改变波前，则新建专用Gaussian/beam source角度验证副本，不改动主模型。

## 波前验证结果

- `field_xy`中当前偏振只有Ez分量非零：max|Ex|=0、max|Ey|=0、max|Ez|=2.71467。
- 使用Ez在光源下方约100 nm处计算相邻横向网格的平均复相位差。
- 取样y位置：650 nm；横向网格间距：19.6429 nm。
- theta属性设为0°时，平均相位步进为-0.606669°。
- theta属性设为-20°时，平均相位步进仍为-0.606669°。
- 按638 nm波长反算，两者实际横向相位对应角度均约-3.13765°。
- 因此已用场相位直接证明：当前PlaneSource的theta属性变化没有改变实际入射波前。
- 当前模型不得据此报告入射角容差。

## 后续修正路线

为有限12齿结构建立独立的Gaussian beam副本，明确束腰、焦点位置和入射角；先用0°与-20°相位图验证波前，再在相同束腰条件下进行角度效率扫描。该验证不得覆盖现有主模型。

## 当前状态

本阶段属于配置诊断，不能报告角度容差。已恢复并保留正确的-12.5°、638 nm、Diffracting基准结果模型：

- `D:/FDTD_File/ar_incoupler_FDTD_stage105_diffracting_thetaM12p5_638nm_mesh5nm_result_2D.fsp`
- `D:/FDTD_File/ar_incoupler_FDTD_stage105_diffracting_thetaM12p5_638nm_mesh5nm_result_2D.ldf`

## 官方参考

- https://optics.ansys.com/hc/en-us/articles/360034382894-Understanding-injection-angles-in-broadband-simulations
- https://optics.ansys.com/hc/en-us/articles/360034382854-Plane-wave-and-beam-source-Simulation-object
- https://optics.ansys.com/hc/en-us/articles/360034382714-Bloch-boundary-conditions-in-FDTD-and-MODE
