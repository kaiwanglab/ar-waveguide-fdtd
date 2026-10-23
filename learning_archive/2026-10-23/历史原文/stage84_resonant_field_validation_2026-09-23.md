# Stage84：638.193 nm Bloch 共振模场验证

日期：2026-09-23

## 目标

验证Stage82-83找到的638.193 nm共振是否为波导/光栅区域中的物理Bloch导模，而不是空气、衬底或PML中的伪模。

## 当前真实y方向几何

- substrate：-850 nm到-300 nm
- waveguide core：-300 nm到0 nm
- grating tooth：0 nm到210 nm

因此光栅齿位于波导芯层的上表面，并非嵌入芯层内部。

## 方法

- kx（bandstructure归一化单位）：-0.1186131
- 监视波长：638.193 nm
- 使用二维z-normal DFT场监视器记录E数据
- 显示量：`E.E2`，即总电场强度 `|E|^2`
- 采用实际x、y坐标间距进行梯形权重积分，避免非均匀网格造成简单像素求和偏差

## 结果

| 区域 | 坐标范围 | 加权 `|E|^2` 比例 |
|---|---:|---:|
| 波导芯层 | -300到0 nm | 77.8596% |
| 光栅齿高度范围 | 0到210 nm | 11.2122% |
| 芯层+光栅齿 | -300到210 nm | 89.0717% |
| 其余区域 | - | 10.9283% |

## 结论

638.193 nm峰的场主要限制在波导芯层，并有约11.2%的电场强度分布在表面光栅齿高度范围。该峰是与表面光栅相互作用的Bloch导模，不是PML或空气伪模。这里的比例是坐标加权的`|E|^2`比例，不是包含介电常数和磁场项的严格总电磁能量比例。

## 文件

- `D:/FDTD_File/ar_incoupler_FDTD_638nm_stage84_resonant_field_2D.fsp`
- `D:/FDTD_File/ar_incoupler_FDTD_stage84_resonant_field_localization.ldf`
- `D:/Codex/Kai/fdtd_stage84_resonant_field_localization.lsf`
- `D:/Codex/Kai/.ppt-build/recent_fdtd_optimization/stage84_corrected_status_35s.png`

## 下一步

Stage85建议将Bloch模型预测与有限12齿FDTD结果定量闭环：用Stage83色散曲线在638 nm处插值得到Bloch kx，再换算为自由空间入射角，与Stage79有限光栅最佳角-13.0358°比较。
