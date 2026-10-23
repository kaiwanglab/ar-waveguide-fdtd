# Stage121：最终结构齿高制造公差

日期：2026-09-28  
软件：Ansys Lumerical FDTD 2026 R1  
模型：二维有限长度高斯光束入耦模型

## 固定参数

- 波长：638 nm
- 周期：334 nm
- 占空比：62.5%，齿宽208.75 nm
- 入射角：-13.6 deg
- 顶部横向偏移：-280 nm
- 模式/功率测量面：x = 5 um
- 标称齿高：290 nm
- 扫描时只改变齿高，顶部横移保持不变

## 5 nm网格粗扫

| 齿高 (nm) | TM forward (%) | 相对标称保持率 (%) |
|---:|---:|---:|
| 230 | 26.7745 | 80.6575 |
| 240 | 28.6713 | 86.3714 |
| 250 | 30.3064 | 91.2970 |
| 260 | 31.6670 | 95.3960 |
| 270 | 32.6518 | 98.3625 |
| 280 | 33.0554 | 99.5784 |
| 290 | 33.1954 | 100.0000 |
| 300 | 33.1663 | 99.9125 |
| 310 | 32.9839 | 99.3628 |
| 320 | 32.6619 | 98.3930 |
| 330 | 32.2196 | 97.0605 |
| 340 | 31.6733 | 95.4149 |
| 350 | 31.0409 | 93.5098 |

粗扫线性插值得到95%候选边界：259.034 nm与342.178 nm。

## 3.5 nm边界验证

第一轮：

| 齿高 (nm) | TM forward (%) | 保持率 (%) |
|---:|---:|---:|
| 259.034 | 31.5380 | 94.9573 |
| 290.000 | 33.2128 | 100.0000 |
| 342.178 | 31.6051 | 95.1596 |

斜率修正后的第二轮：

| 齿高 (nm) | TM forward (%) | 保持率 (%) |
|---:|---:|---:|
| 259.138 | 31.5508 | 94.9960 |
| 343.016 | 31.5444 | 94.9768 |

## 结论

1. 290 nm是当前曲线峰值附近，280–310 nm形成平坦平台，不是尖锐偶然峰。
2. 以“目标TM不低于标称值95%”定义，最终齿高窗口约为259.15–342.9 nm。
3. 相对290 nm标称值，非对称容差约为-30.85/+52.9 nm。
4. 若必须写成对称尺寸规范，理论上限取较小侧约±30.8 nm；考虑数值误差和联合参数耦合，当前工程建议暂取±25 nm。
5. 本结果是保持shift=-280 nm不变的单变量灵敏度，不等同于真实工艺中高度与侧壁角的联合分布。

## 已保存文件

- `D:/FDTD_File/ar_incoupler_FDTD_stage121c_height_final_edges_verified_restored290nm_period334nm_duty62p5_thetaM13p6_wl638nm_mesh3p5nm_2D.fsp`
- `D:/FDTD_File/stage121_height_manufacturing_tolerance_mesh5nm.ldf`
- `D:/FDTD_File/stage121b_height_95pct_edges_mesh3p5nm_verify.ldf`
- `D:/FDTD_File/stage121c_height_final_edges_mesh3p5nm_verify.ldf`
- `D:/Codex/Kai/stage121_height_manufacturing_tolerance_mesh5nm.lsf`
- `D:/Codex/Kai/stage121b_height_95pct_edges_mesh3p5nm_verify.lsf`
- `D:/Codex/Kai/stage121c_height_final_edges_mesh3p5nm_verify.lsf`

## 下一步

Stage122固定高度290 nm，只扫描顶部横移shift，评价侧壁倾斜量制造公差；之后再做高度与shift的联合角点验证。
