# Stage267/268：top shift = -250 nm 工程验证

日期：2026-10-14  
固定参数：波长 638 nm；齿高 237 nm；齿宽 190 nm；光栅 z 宽 0.75 µm；top shift = -250 nm。

## 运行与几何审计

- Stage267a：24 个几何对象全部启用，顶点、y 位置和 z span 误差均为 0，`audit_pass=1`。
- Stage267b：17:47 启动，19:16 自然完成，完整 FSP 已保存。
- Stage268a/b/c：在同一可见 Lumerical 窗口依次执行，相干背景扣除、固定 32 模基底和纯散射场投影；三个 LDF 文件均成功生成。

## 主要结果

- 净导模效率：6.3532603392%
- 正向导模：6.3536209112%
- 反向导模：0.0003605720%
- TM 正向导模：6.3384858647%
- TE 正向导模：0.0149148706%
- mode 1 正向散射：4.2344995398%
- mode 1 / 正向导模：66.64702851%
- 直接散射净功率：6.3541963157%
- 未展开散射净功率：0.0004802916%

## 数值有效性

- 网格坐标误差：0
- 源功率比：1
- 相干重构相对误差：2.09e-16
- 固定基底：32 模，其中 28 个导模
- a/b 线性误差：4.16e-17 / 4.82e-17
- 直接散射净功率与固定模态展开结果接近，未展开残差仅 0.000480 个百分点；结果可用于趋势判断。

## 与 -240 nm 名义点比较

| top shift | 净导模效率 | mode 1 | mode 1 占正向导模 |
|---:|---:|---:|---:|
| -240 nm | 6.2999806868% | 4.2069526344% | 66.77345039% |
| -250 nm | 6.3532603392% | 4.2344995398% | 66.64702851% |

- 净导模效率绝对提高 0.0532796524 个百分点，相对提高约 0.84571%。
- mode 1 绝对提高 0.0275469054 个百分点，相对提高约 0.65480%。
- mode 1 占比下降约 0.12642 个百分点，说明总导模提升略快于 mode 1 提升。

## 决策

由于 -250 nm 优于 -240 nm，当前峰值尚未被 -250/-240 两点包住。下一步不应先跑 -230 nm；应保持其它参数不变，先验证 -260 nm。若 -260 nm 下降，则由 -260/-250/-240 nm 包住局部峰值；若继续上升，再沿负方向单变量扩展。

## 可复现文件

- 完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage267b_HEIGHT237nm_TOOTH190nm_TOPSHIFTm250nm_GRATINGWIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp`
- 场分解：`D:/FDTD_File/stage268a_height237nm_tooth190nm_topshiftm250nm_width0p75um_coherent_field_decomposition.ldf`
- 固定模态基底：`D:/FDTD_File/stage268b_height237nm_tooth190nm_topshiftm250nm_width0p75um_patterned_fixed_mode_basis32.ldf`
- 固定基底投影：`D:/FDTD_File/stage268c_height237nm_tooth190nm_topshiftm250nm_width0p75um_fixed_basis32_projection.ldf`
