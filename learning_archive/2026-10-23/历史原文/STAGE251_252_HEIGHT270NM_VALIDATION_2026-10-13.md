# Stage251/252：270 nm 齿高验证

## 结论

270 nm 的有限光束三维净导模耦合效率为 **4.8594986977%**，相对 280 nm 的 **4.0189989512%** 提高 **20.9132%**。Mode 1 绝对效率为 **3.3085464129%**，相对 280 nm 提高 **20.5816%**。

因此齿高从 320 nm 依次减小到 270 nm 时，效率仍持续上升，峰值仍未包住。下一步只验证 **260 nm**；暂不同时修改 top shift、占空比或周期，避免把变量影响混在一起。

## 几何与运行

- 齿高：270 nm
- 齿底：-3.75 nm
- 齿顶：266.25 nm
- 齿宽：185 nm
- top shift：-240 nm
- z 向有限光栅宽度：0.75 um
- 结构对象：12 组 tooth + outer，参数一致性已在可见界面审计
- FDTD 完整模型：D:/FDTD_File/ar_incoupler_FDTD_stage251b_HEIGHT270nm_WIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp

## 模态投影结果

| 指标 | 270 nm |
|---|---:|
| 导模净效率 | 4.8594986977% |
| 导模前向 | 4.8597874241% |
| 导模后向 | 0.0002887263% |
| TM 前向 | 4.8418572402% |
| TE 前向 | 0.0176588170% |
| Mode 1 前向 | 3.3085464129% |
| Mode 1 / 导模前向 | 68.08006450% |
| 直接散射净值 | 4.8602147268% |
| 未展开净残差 | 0.0002644269% |

## 数值有效性

- 入射功率完全匹配：pattern/reference 均为 8.045297289070808e-15 W
- 网格插值误差：y=0、z=0
- 相干场重构相对误差：-1.4196e-16
- 固定基底：32 个模式，其中 28 个满足 Re(neff)>1
- a/b 线性误差：6.21e-17 / 2.48e-17
- 未展开净残差仅 0.0002644%

以上闭合指标说明 270 nm 的提升不是读取错误或模式投影伪差。

## 齿高趋势

| 齿高 | 净导模效率 |
|---:|---:|
| 270 nm | 4.859499% |
| 280 nm | 4.018999% |
| 290 nm | 3.108422% |
| 300 nm | 2.195387% |
| 310 nm | 1.308103% |
| 320 nm | 0.620073% |

270 nm 比 280 nm 的绝对提升为 **0.840500 percentage points**。趋势仍单调，所以下一步需要 260 nm 来判断峰值是否继续向更低齿高移动。

## 可复现文件

- D:/Codex/Kai/stage252a_height270nm_width0p75um_coherent_field_decomposition.lsf
- D:/Codex/Kai/stage252b_height270nm_width0p75um_patterned_fixed_mode_basis32.lsf
- D:/Codex/Kai/stage252c_height270nm_width0p75um_fixed_basis32_projection.lsf
- D:/FDTD_File/stage252a_height270nm_width0p75um_coherent_field_decomposition.ldf
- D:/FDTD_File/stage252b_height270nm_width0p75um_patterned_fixed_mode_basis32.ldf
- D:/FDTD_File/stage252c_height270nm_width0p75um_fixed_basis32_projection.ldf
- D:/Codex/Kai/stage251_252_height270nm_results.json
