# FDTD 学习检查点｜2026-09-01

## 今天完成的内容

从 RCWA 的周期单元结果进入有限长度 FDTD 验证，完成了一个可见、可继续编辑的 2D 入耦光栅模型。

当前结构参数：

- 波长：638 nm
- 入射角：-13°
- 偏振：TM，polarization angle = 0°
- 周期：407 nm
- 齿宽：210 nm
- 间隙：197 nm
- 齿高：175 nm
- 齿数：8
- 光栅总长度：3.256 µm
- FDTD x span：5.256 µm
- FDTD z 范围：-0.8 µm 至 1.175 µm
- 仿真时间：1000 fs
- 局部网格：dx = dz = 10 nm
- 局部网格范围：x span = 3.8 µm，z = -0.15 至 0.30 µm

## 已建立的对象

- `source`：从上向下传播的 638 nm、-13°、TM 平面波
- `power_right`：右侧 X-normal 功率监视器
- `power_left`：左侧 X-normal 功率监视器
- `power_top`：上方 Z-normal 功率监视器
- `field_xz`：XZ 电场监视器
- `mode_right`：右侧 TM 模式展开监视器
- `mesh_grating_10nm`：覆盖光栅附近的局部网格

## 今天实际运行结果

第一次 8 周期、10 nm 网格、TM 的 2D FDTD 主仿真已经正常结束。运行很快是因为模型是 2D、周期数少、且只有光栅附近使用 10 nm 局部网格；它不是完整 AR 眼镜尺寸模型。

模型已保存在：

`D:/FDTD_File/ar_incoupler_FDTD_638nm_finite8_stage6_TM_mesh10nm_2D.fsp`

## 今天发现并确认的问题

### 1. power_top 读取失败

`transmission("power_top")` 当前不可用。右、左监视器的读取语句可执行，但脚本在读取 `power_top` 时停止。明天需要检查 `power_top` 的监视器类型、位置以及是否真正保存了 `T` 结果。

### 2. mode_right 模式展开计算失败

`Result View - mode_right` 中能看到：

`expansion for right_field`

但右键执行 `Calculate` 后出现：

`Failed to calculate results!`

因此当前问题不是 FDTD 主仿真失败，也不是光栅几何错误，而是 `mode_right` 的模式求解或与 `power_right` 的关联设置尚未正确完成。

## 明天从这里继续

1. 打开上述 stage6 `.fsp` 文件。
2. 关闭当前警告框，点击顶部 `Layout`。
3. 检查 `mode_right`：X-normal、x = 2.1 µm、z = 0、z span = 0.9 µm。
4. 检查截面是否完整覆盖波导芯层及必要包层。
5. 重新计算 fundamental TM mode，并确认模式剖面确实位于波导芯层。
6. 重新关联 `right_field` 与 `power_right`。
7. 再运行 FDTD，执行模式展开 Calculate，读取 `T_forward` 与 `T_backward`。
8. 单独修复 `power_top`，再读取向上泄漏功率。
9. 完成 10 nm 基准后，使用 5 nm 网格做收敛性对照；此时再判断数值是否可信。

## 相关脚本与截图

- `D:/Codex/Kai/fdtd_visible_finite8_stage6_mesh10nm.lsf`
- `D:/Codex/Kai/fdtd_visible_read_first_run_results.lsf`
- `D:/Codex/Kai/fdtd_first_run_status.png`
- `D:/Codex/Kai/fdtd_mode_right_result_view.png`
- `D:/Codex/Kai/fdtd_send_to_script.png`

## 本阶段必须记住的概念

- `Run` 负责求解时域电磁场。
- 模式展开是后处理分析；主仿真结束不代表模式展开一定成功。
- 看到结果名称不等于该分析结果已经成功计算。
- 右键 `Calculate` 报错时，应先检查模式截面、模式选择和关联监视器，而不是继续优化光栅几何。
- 当前 10 nm 网格结果只能作为快速基准；最终结论需要与 5 nm 网格比较。
