# Stage203a：2D/3D 源功率与 x-y 网格只读审计

完成时间：2026-09-30 19:55（Asia/Shanghai）

本步骤只加载 Stage201b 与 Stage203 已完成文件，没有重新运行 FDTD，也没有改变结构。

## 结果

| 指标 | 2D | 3D periodic | 判定 |
|---|---:|---:|---|
| status | 2 | 2 | 都由 auto-shutoff 正常结束 |
| 单位宽度源功率 | 2.18225315e-8 W/m | 2.17717148e-8 W/m | 3D/2D=0.997671，差-0.2329% |
| x 网格点数 | 3462 | 3462 | 相同 |
| y 网格点数 | 203 | 203 | 相同 |
| x 坐标最大差 | — | 0 nm | 完全相同 |
| y 坐标最大差 | — | 0 nm | 完全相同 |
| 最小/最大 dx | 3.499079 / 19.647696 nm | 3.499079 / 19.647696 nm | 相同 |
| 最小/最大 dy | 3.482824 / 34.750000 nm | 3.482824 / 34.750000 nm | 相同 |
| 3D z 网格 | — | 21 点，dz=20 nm | 与 Stage203 设置一致 |

## 结论

- Stage201b 与 Stage203 使用完全相同的 x-y Yee 网格，因此 2D/3D 右向功率差异不是 x-y 网格漂移造成的。
- 单位宽度源功率只相差 0.2329%，也不足以解释右向功率约 13.7% 的相对差异。
- 结合 Stage202 的 dz 收敛和 Stage203 的 z 单元宽度不变性，3D periodic direct-power baseline 已具备内部数值稳定性。
- 2D 与 3D 的绝对值必须分别报告，不能把 3D 数值包装成“复现 2D”；后续工程判断以 3D 基准内部的相对变化和能量闭合为主。

## 下一步

在 Stage203 基准上启用 mode expansion。扩展监视器与 `power_right` 必须同中心、同跨度；选择多个模式，比较全部前向模式和与 direct right power 的闭合误差。

官方网格读取接口参考：[Tips for getting the actual mesh size in FDTD](https://optics.ansys.com/hc/en-us/articles/360034382574-Tips-for-getting-the-actual-mesh-size-in-FDTD)。

## 文件

- 原始审计数据：`D:/FDTD_File/stage203a_2d_3d_sourcepower_xy_mesh_audit.ldf`
- 可读数据：`D:/Codex/Kai/stage203a_2d_3d_sourcepower_xy_mesh_audit.csv`
- 审计脚本：`D:/Codex/Kai/stage203a_audit_2d_3d_sourcepower_xy_mesh.lsf`
