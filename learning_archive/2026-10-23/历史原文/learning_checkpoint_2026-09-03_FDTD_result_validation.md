# Lumerical FDTD 学习检查点 — 2026-09-03

## 今天完成的内容

从结构参数优化转入结果验证，重点检查 `mode_right` 读取的 TM 前向效率是否随监视器位置收敛。

### 1. 确认原平面波结果不可信

- 复振幅背景扣除后的监视器间距结果：
  - 800 nm：前向 0.00478507%，后向 0.00138272%
  - 1000 nm：前向 0.045632%，后向 0.000849304%
  - 1200 nm：前向 0.0343783%，后向 0.000621354%
- 前向相对离散度：144.514%
- 结论：斜入射平面波和辐射场污染侧面模态监视器，不能把任一单点 `T_forward` 当作最终入耦效率。

### 2. 建立有限宽度 Gaussian 入射源

- 原 `source` 平面波已禁用但未删除，可逆。
- 新源名称：`gaussian_source`
- x=0，x span=9 µm，y=0.75 µm
- injection axis：y-axis；direction：Backward
- angle theta：-12.5°；polarization angle：90°（TM）
- waist radius w0：2.5 µm
- distance from waist：-0.75 µm，腰斑位于光栅表面
- 继承原工程宽带时间脉冲频谱；监视器在目标波长读取结果。

### 3. Gaussian 1000 nm 基准结果

- TM forward：0.0182883%
- TM backward：0.0000487968%
- right total：1.80204%
- left total：0.464786%
- top total：74.2768%
- 前后向比约 375；但单点效率仍不能作为最终效率。

### 4. Gaussian 监视器位置收敛验证

| 距最外侧光栅边缘 | TM forward | TM backward | right total |
|---:|---:|---:|---:|
| 800 nm | 0.0239297% | 0.000139668% | 1.66062% |
| 1000 nm | 0.0182883% | 0.0000487968% | 1.80204% |
| 1200 nm | 0.00852685% | 0.000160922% | 1.72182% |

- 前向相对离散度：91.0606%
- 判定：仍未通过 5%–10% 的收敛目标。
- 物理解释：800–1200 nm 仍处于光栅近场区，辐射场和倏逝场尚未与波导导模充分分离。

## 当前可靠结论

1. Gaussian 源确实降低了直接照明背景，离散度从 144.514% 降到 91.0606%。
2. 当前监视器仍太靠近光栅。
3. 目前任何单个 `T_forward` 都不能称为最终入耦效率。
4. 暂停周期、占空比、高度等结构参数扫描，先修复测量方法。

## 明天第一步

1. 从 Stage39 副本继续，不覆盖旧文件。
2. 将 FDTD 区域和 `waveguide_core` 的 x span 扩大到约 16 µm。
3. 将 `field_xy` x span 扩大到约 14 µm。
4. 保持 Gaussian、光栅结构、5 nm 网格和其他参数不变。
5. 将 `mode_right` / `power_right` 依次放在距最外侧光栅边缘 2、3、4 µm 处。
6. 比较 TM forward 的相对离散度：≤10% 初步通过，≤5% 为理想目标。
7. 若远距离仍不收敛，再转入端口/散射场分离方案，不继续盲目优化结构。

## 已核对存在的关键文件

- `D:/FDTD_File/ar_incoupler_FDTD_638nm_stage37_Gaussian_w0_2p5um_validation_setup_mesh5nm_2D.fsp`
- `D:/FDTD_File/ar_incoupler_FDTD_638nm_stage38_Gaussian_w0_2p5um_gap1000_complete_mesh5nm_2D.fsp`
- `D:/FDTD_File/ar_incoupler_FDTD_638nm_stage39_Gaussian_gap_convergence_data.ldf`
- `D:/FDTD_File/ar_incoupler_FDTD_638nm_stage39_Gaussian_gap_convergence_setup_mesh5nm_2D.fsp`
- `D:/Codex/Kai/fdtd_stage37_create_gaussian_validation_source.lsf`
- `D:/Codex/Kai/fdtd_stage38_gaussian_baseline_gap1000_run.lsf`
- `D:/Codex/Kai/fdtd_stage39_gaussian_gap_convergence_5nm.lsf`

## 明天恢复口令

“打开 Stage39 检查点，建立 16 µm 公共区域，做 2/3/4 µm Gaussian 远距离收敛验证。”
