# Lumerical AR 入耦光栅优化检查点（Stage 159–212b z-domain convergence running）

保存时间：2026-10-01（Asia/Shanghai）

## 1. 当前采用的结构基准

- 波长（单频基准）：638 nm
- 光栅齿数：24
- 周期：328.75 nm
- 入射角：-15.1°
- 齿宽：185 nm
- 齿高：310 nm
- 齿顶横向位移：-240 nm
- 齿底坐标：-3.75 nm（锁定齿底，避免“增高”与“向下刻蚀”混淆）
- 生产网格：3.5 nm
- mode_right / power_right 报告面：x=7 µm
- FDTD x 范围：-12 至 +12 µm
- 波导与基底 x 范围：-13 至 +13 µm（贯穿两侧 PML）

## 2. 重要纠错

Stage159 在扫描齿高时只改变局部多边形高度，没有同步改变对象中心 y。齿高增加会同时向下侵入波导，因此 W=180 nm、H=340 nm、TM=59.933% 只能作为诊断结果，不能当成有效的纯齿高优化。

Stage160 起锁定齿底为 -3.75 nm，只移动齿顶。物理约束正确后的粗扫最佳为 W=200 nm、H=300 nm、TM=57.2775%。

## 3. 几何优化结果

- Stage161（5 nm 局部 W-H）：W=190 nm、H=315 nm，TM=58.1345%。
- Stage162（3.5 nm W-H 验证）：W=190 nm、H=315 nm，TM=58.0348%，向右功率=60.2351%。
- Stage165（3.5 nm shift 验证）：shift=-250 nm，TM=58.1566%，向右功率=60.3905%。
- Stage168/169（3.5 nm 周期-角度验证与边界闭合）：P=328.50 nm、角度=-15.1°，mode1=59.8936%，向右功率=61.4542%。新增 P=328.75/329.00 nm 点均未超过该结果。
- Stage182 用显式 `span=0 nm`、638 nm 单点重新扫描 P=328.25/328.50/328.75 nm 与角度=-15.2/-15.1/-15.0°。raw 最高值位于 P=328.75 nm、角度=-15.0°，mode1=59.9327%，但只比名义点高 0.0086 pp，小于已知网格差 0.0119 pp，因此不视为真实提升，继续采用更居中的 P=328.50 nm、角度=-15.1°。
- Stage183/184 用锁定齿底的宽高单参数及 4×4 联合扫描找到 W=185 nm、H=310 nm；相对 W=190 nm、H=315 nm，mode1 从 59.9241% 提升到 60.4867%，mode3 从 1.7471% 降至 1.5720%，全前向模式和从 61.6712% 提升到 62.0586%，右侧功率从 61.4678% 提升到 61.8580%。
- Stage185 网格复核通过：3 nm 相对 3.5 nm 的 mode1/全前向/右侧功率差分别为 +0.0187/+0.0178/+0.0192 pp，显著小于新结构相对旧结构的 +0.5626 pp mode1 提升。
- Stage186 监视面复核通过：全前向模式和在 x=6/7/8 µm 的峰峰差为 0.5992 pp，直接右侧功率峰峰差为 0.1784 pp；mode1/mode3 的变化仍主要是模式分解对报告面的敏感性。
- Stage187/188 在新宽高结构上复核周期/角度。P=328.75 nm、角度=-15.1° 的 mode1=60.5613%，且三个角度点的变化约 0.092 pp；继续扩展到 P=329.25 nm 后最高仅 60.5681%，相对提升 0.0068 pp，低于停止线，因此不再扩展并采用更稳健的 P=328.75 nm、角度=-15.1°。
- Stage189/190 将 top shift 从 -250 nm 调整为 -240 nm。3 nm 网格直接对比确认 mode1/全前向/右侧功率分别提升 +0.0491/+0.0299/+0.0354 pp，mode3 降低 0.0193 pp；最终 3.5 nm 结果为 mode1=60.6064%、mode3=1.4706%、全前向=62.0770%、右侧功率=61.8808%，status=2。
- Stage191 完成制造公差角点验证：围绕 W=185 nm、H=310 nm、shift=-240 nm，同时组合 W±5 nm、H±5 nm、shift±10 nm，共 8 个角点，全部 status=2。mode1 范围为 59.8422%–60.6184%，全前向模式和为 61.4540%–61.9987%，右侧功率为 61.2625%–61.7976%。相对标称值，最差下降分别为 0.7642/0.6230/0.6183 pp；当前公差窗口通过，并停止几何微调。
- Stage192 完成最终结果验证：二维场图确认强场位于波导芯层 y=-0.30–0 µm，并沿 +x 连续传播；右侧/左侧功率绝对值为 61.8808%/1.0107%，左右方向性为 98.3929%。mode1/mode3 的 TE fraction 均约 0%，分别为 TM 基模与 TM 高阶模；mode2/mode4 的 TE fraction 为 100%，但耦合效率分别仅约 2.09e-30%/4.75e-29%。TM 前向总和为 62.0770%，其中 mode1 纯度为 97.6310%。
- Stage193 对最终结构进行 -25° 至 -5° 的工程角度粗扫，峰值仍位于 -15.1°，mode1=60.6064%，证明标称角没有漂移。半功率阈值为 30.3032%，粗扫将左右 3 dB 边界分别夹在 -20°至-17.5°和-15.1°至-12.5°之间。
- Stage194 在边界附近以 0.25°步长细扫并插值：左 3 dB 边界=-18.1043°，右边界=-12.6910°，3 dB 接受角宽=5.4133°。相对峰值 -15.1°，左/右容差约为 3.00°/2.41°；所有点 status=2，最终复跑恢复到 mode1=60.6064%。
- Stage195 使用彼此独立的 span=0 单色运行扫描 618/628/638/648/658 nm，并在每个波长重新更新 4 个波导模式。mode1/mode3 在全范围内保持 TM，mode1 有效折射率从 1.65201 平滑降至 1.63771；峰值仍为 638 nm、60.6064%。
- Stage196 在粗扫半功率交点附近细扫，得到固定 -15.1°入射时的左/右 3 dB 波长边界 621.035/648.573 nm，3 dB单色波长带宽 27.538 nm；最终恢复 638 nm复跑结果仍为 mode1=60.6064%、status=2。
- Stage197 完成 628/638/648 nm × -18/-16.5/-15.1/-13.5/-12° 的 3×5 独立单色联合扫描。最佳采样点分别为 628 nm/-13.5°/71.5229%，638 nm/-15.1°/60.6064%，648 nm/-16.5°/49.5431%；高效率脊线随波长增加向更负角度移动，所有15点 status=2，最终恢复638 nm、-15.1°。
- Stage198 围绕三行峰值各做3点局部扫描并抛物线拟合：628/638/648 nm的连续峰角为 -13.1710/-15.1616/-17.0915°，峰值mode1为72.2831/60.6295/51.4415%。色散斜率 `d(theta_peak)/d(lambda)=-0.196021°/nm`，即每增加10 nm最佳角约向负方向移动1.9602°；9点全部status=2，最终恢复638 nm、-15.1°。

## 4. 制造公差角点（Stage191）

| W (nm) | H (nm) | shift (nm) | status | mode1 (%) | mode3 (%) | 全前向模式和 (%) | 右侧功率 (%) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 180 | 305 | -250 | 2 | 60.6082 | 1.3033 | 61.9114 | 61.7094 |
| 180 | 305 | -230 | 2 | 60.2402 | 1.2137 | 61.4540 | 61.2625 |
| 180 | 315 | -250 | 2 | 60.6184 | 1.3803 | 61.9987 | 61.7976 |
| 180 | 315 | -230 | 2 | 60.3068 | 1.3449 | 61.6517 | 61.4624 |
| 190 | 305 | -250 | 2 | 60.0473 | 1.5972 | 61.6445 | 61.4385 |
| 190 | 305 | -230 | 2 | 60.2499 | 1.5587 | 61.8086 | 61.6139 |
| 190 | 315 | -250 | 2 | 59.8422 | 1.6618 | 61.5040 | 61.2998 |
| 190 | 315 | -230 | 2 | 60.1150 | 1.6833 | 61.7983 | 61.6074 |

标称结构复跑：mode1=60.6064%、mode3=1.4706%、全前向=62.0770%、右侧功率=61.8808%、status=2。

- 最低 mode1：59.8422%，出现在 W=190 nm、H=315 nm、shift=-250 nm。
- 最低全前向与最低右侧功率：61.4540% / 61.2625%，出现在 W=180 nm、H=305 nm、shift=-230 nm。
- 物理含义：三个指标在整个公差盒内只变化约 0.5–0.8 pp，标称点并非尖锐孤立峰，结构具备初步制造稳健性。

## 5. 监视器位置与模式分解

mode_right 实际返回 4 个模式。偶数模式几乎为 0；主要是 mode1 与 mode3 两个同偏振导模。

扩域后 x=6/7/8 µm：

| x (µm) | mode1 (%) | mode3 (%) | 全前向模式和 (%) | 直接向右功率 (%) |
|---:|---:|---:|---:|---:|
| 6 | 60.8423 | 1.1931 | 62.0354 | 61.6796 |
| 7 | 60.4867 | 1.5720 | 62.0586 | 61.8580 |
| 8 | 59.4011 | 2.0583 | 61.4594 | 61.7116 |

统计：

- mode1 均值 60.2434%，位置峰峰差 1.4413 个百分点。
- mode3 均值 1.6078%，位置峰峰差 0.8652 个百分点，和 mode1 反向变化。
- 全前向模式和均值 61.8512%，位置峰峰差 0.5992 个百分点。
- 直接向右功率均值 61.7497%，位置峰峰差 0.1784 个百分点。

结论：传输能量本身稳定；主要敏感性来自 mode1/mode3 的数值分解。最终报告必须区分“基模 mode1”“高阶 mode3”“全部前向导模”和“直接向右功率”。

### Stage192 最终模式与方向性验收

| 模式 | TE fraction (%) | neff | T_forward (%) | 判定 |
|---:|---:|---:|---:|---|
| 1 | ≈0 | 1.64489 | 60.6064 | TM 基模，目标模式 |
| 2 | 100 | 1.55913 | ≈0 | TE，未被明显激发 |
| 3 | ≈0 | 1.14188 | 1.47058 | TM 高阶模 |
| 4 | 100 | 1.07865 | ≈0 | TE，未被明显激发 |

- TM 前向模式和：62.0770%。
- mode1 在前向 TM 功率中的纯度：97.6310%。
- 直接右侧功率：61.8808%；与模式展开总和相差 0.1962 pp，量级很小。
- 左侧功率绝对值：1.0107%；左右方向性 = right/(right+left) = 98.3929%。
- `power_top=-88.2568%` 含入射场且符号由监视器法向决定，禁止与左右功率取绝对值后直接相加。
- 场图：`D:/Codex/Kai/stage192_E2dB.png`。

## 6. 网格收敛（x=7 µm）

| 网格 (nm) | mode1 (%) | mode3 (%) | 全前向模式和 (%) | 直接向右功率 (%) |
|---:|---:|---:|---:|---:|
| 5.0 | 60.5081 | 1.5476 | 62.0557 | 61.8582 |
| 4.0 | 60.5073 | 1.5741 | 62.0815 | 61.8833 |
| 3.5 | 60.4867 | 1.5720 | 62.0586 | 61.8580 |
| 3.0 | 60.5054 | 1.5710 | 62.0764 | 61.8772 |

3 nm 相对 3.5 nm 的差：mode1=+0.0187 pp，全前向模式=+0.0178 pp，向右功率=+0.0192 pp。因此继续采用 3.5 nm 作为成本/精度平衡点。

## 7. 光源带宽复核（Stage175b–181）

Stage175b 使用 628–648 nm、21 点、4 模式。代表点：

| 波长 (nm) | mode1 (%) | mode3 (%) | 全前向模式和 (%) | 向右功率 (%) |
|---:|---:|---:|---:|---:|
| 628.000 | 53.3879 | 0.7163 | 54.1042 | 53.9726 |
| 632.883 | 69.5527 | 1.3664 | 70.9191 | 70.7071 |
| 637.843 | 78.2784 | 2.2529 | 80.5312 | 80.3608 |
| 642.882 | 75.2614 | 3.0518 | 78.3132 | 78.2922 |
| 648.000 | 61.0985 | 3.4867 | 64.5851 | 64.6914 |

- mode1 峰值：78.6632%，波长 638.845 nm。
- 90% 峰值范围：约 633.869–643.899 nm，宽约 10.030 nm。

随后保持结构、网格、中心波长和仿真时间不变，只改变光源 `wavelength span`，得到：

| 光源 span (nm) | 读取波长 (nm) | mode1 (%) | mode3 (%) | 全前向模式和 (%) | 向右功率 (%) |
|---:|---:|---:|---:|---:|---:|
| 20（单点复现） | 638.000 | 78.3712 | 2.2817 | 80.6529 | 80.4860 |
| 20（21点光谱） | 637.843 | 78.2784 | 2.2529 | 80.5312 | 80.3608 |
| 10 | 637.961 | 69.5139 | 2.0237 | 71.5375 | 71.3653 |
| 5 | 637.990 | 64.7913 | 1.8915 | 66.6827 | 66.4885 |
| 2 | 637.998 | 61.8862 | 1.8077 | 63.6940 | 63.4919 |
| 0（真正单波长） | 638.000 | 59.9241 | 1.7471 | 61.6712 | 61.4678 |

关键结论：

- Stage180 用 20 nm 光源、638 nm 单点监视器重新运行，`status=2`，精确复现约 78.37%；宽带中心值本身可复现。
- Stage181 将源 span 明确设为 0 nm，`status=2`，精确复现旧 LDF 中的 59.9241%。
- 因此旧 LDF（span=0）和后来保存的 Stage174 FSP（span=20）对应不同光源定义；它们不能作为同一条件直接比较。
- 当前目标是 638 nm 单色设计，正式基准采用 span=0 nm 的 59.9241%；20 nm 结果属于另一种激励定义，不能记作几何优化提升。

## 8. Stage199 相位匹配反算

- 使用当前坐标和 `+1` 级定义：`n_phase = sin(theta_peak) + wavelength/period`。
- 628/638/648 nm 反算 `n_phase` 分别为 1.682408、1.679142、1.677204，均值 1.679585，极差仅 0.005204（约0.31%）。
- 相对裸波导 mode1 `neff` 的平均加载偏移为 0.034701，标准差 0.000852。
- 用裸波导色散加同一个平均偏移回代，三点峰角最大残差仅 0.0715°，显著小于扫描步长；联合响应斜脊线通过相位匹配物理校验。
- Stage199 只做数据反算，没有改变 FDTD 模型；当前可恢复模型仍为 Stage198 的已还原标称状态。

## 9. Stage200–201：3D资源与源坐标桥接

- Stage200确认本机为6核12线程、31.77 GB内存、RTX 2070 Max-Q 4 GB显存。完整24齿、三个方向3.5 nm的3D模型没有安全内存余量，因此先做z=0.2 µm周期桥接。
- 2D模型中z尺寸被忽略且彼此不一致；进入3D前必须显式统一结构、源、网格和监视器z跨度。
- Stage198正式源是2D Gaussian，不能直接缩窄z并当作等价3D Gaussian。桥接改用同源的2D/3D plane wave。
- 对y轴反向注入源，3D还必须设置 `phi`。实测 `phi=0°` 使主场变为Ex且倾斜落在y-z平面；`phi=+90°` 恢复Ez但kx左右镜像；`phi=-90°` 同时恢复x-y入射面、Ez偏振和正确kx符号。
- 2D plane-wave参考：right=38.5513%、left=1.5352%、方向性=96.1702%。
- Stage201e正确3D映射（phi=-90°、dz=20 nm）：right=33.2858%、left=1.5923%、方向性=95.4346%。相对2D的left只差+0.0571 pp、方向性差-0.7357 pp，但right仍低5.2655 pp。
- Stage202完成z网格收敛：dz=10 nm时right=33.285046%、left=1.592537%、方向性=95.433924%，status=2。相对dz=20 nm，right仅变化-0.000753 pp、方向性仅变化-0.000666 pp，远小于1 pp门槛；z网格已收敛，不再细化至5 nm。
- Stage202相对2D plane-wave参考的right仍低5.266244 pp；该差异没有随dz减半而缩小，因此不是z离散误差。下一步检查z周期单元宽度与源功率归一化。
- Stage203将z周期单元从0.2 µm扩大到0.4 µm，源功率比例为1.999562，单位宽度源功率只变化-0.021884%；right=33.293068%、left=1.592664%、方向性=95.434626%，相对0.2 µm单元只变化+0.007269/+0.000334/+0.000036 pp。3D周期结果对单元宽度不敏感，周期归一化通过。
- Stage203a只读审计确认2D/3D的x-y网格完全相同：均为3462×203，x/y坐标最大差均为0，dx/dy最小和最大值也完全一致。3D单位宽度源功率是2D的0.997671（只低0.2329%），不能解释right约13.7%的相对差异。3D periodic direct-power baseline已具备内部数值稳定性，但2D/3D绝对值仍必须分开报告。
- Stage204启用8模式3D mode expansion，扩展面与power_right中心和跨度差均为0，direct right保持33.293068%。目标TM mode1前向=34.802855%，TM高阶mode3前向=0.485764%，TE导模可忽略，mode1占导模前向功率98.622719%。
- Stage205/206不重跑FDTD，只在已保存场数据上把基底扩到16/32模式。mode1和mode3完全不变；全净模式和在16模式时从35.083859%收敛到34.451916%，32模式不再变化。剩余相对direct right的+1.158848 pp来自未离散展开的辐射/反向连续谱，停止增加模式。
- Stage207资源门槛：z-PML、1.2 µm域、0.6 µm有限光栅、0.9 µm功率面、dz=40 nm时，实际网格3462×203×45，节点代理量31,625,370，是Stage203的2.142857倍；估算运行99.3分钟、单进程峰值内存0.712 GiB，资源门槛通过。
- Stage207有限宽pilot已完成，实际运行约54.68分钟、status=2、单进程实际峰值约0.763 GiB。直接监视器得到right=6.435701%、left=1.060567%、表观方向性85.8521%，但该值不是可接受的有限宽入耦效率。
- Stage207对`power_right`的E/H做手工Poynting积分，完整面得到6.435701%，与内置`transmission`完全一致；但`|z|<=0.30/0.35/0.40 µm`分别只捕获当前全宽功率的65.2939%/79.8660%/89.1455%，最外侧约42.6 nm×2仍占10.8545%。z向功率曲线在全宽内约0.958–1.000，到边界没有衰减。
- 这说明横向无限、斜入射plane wave自身的x向Poynting分量被x-normal `power_right`计入，监视器背景污染显著；扩大z域/监视器会继续收集背景，不能把6.4357%或面积缩放值当作入耦效率。
- Stage208无光栅参考已完成，status=2。保持solver/source/mesh/monitors完全相同，只禁用全部24个光栅结构。源功率相对Stage207只差-0.0199%；无齿`power_right`带符号背景为-1.317210%，证明斜入射plane wave确实横穿x-normal输出面。
- Stage209b将无齿复场线性插值到有齿监视器网格。y网格最大错位0.438266 nm、z网格完全相同；插值只改变参考功率0.001811 pp。相干分解为：有齿总场+6.435701%、无齿背景-1.315137%、散射场+7.692612%、交叉项+0.058227%，四项重构相对误差1.18e-16。
- 结论：6.4357%被反向背景抵消，不能称耦合效率；7.6926%是光栅散射场穿过右面的净功率，但仍含目标导模和辐射连续谱，也不能称最终导模效率。下一验收必须做散射场到固定波导模式基底的投影。
- Stage210固定模式基底验证通过：复系数线性误差5.55e-16，手工展开与内置mode1只差0.001774 pp。16模下目标TM mode1前向=7.479729%、全部导模净功率=7.676693%、TM导模前向=7.671597%、TE导模前向=0.005570%，mode1占导模前向97.4282%。
- Stage211将模式数扩到32。目标mode1只变化+0.000452 pp，导模净功率只变化+0.000289 pp，`neff>1`导模数仍为10；导模子空间已收敛，停止增加模式。新增17–32属于PML离散辐射连续谱，不用其全模净和选择模态数。
- 有限宽平板的单个mode1受横向计算盒归一化影响；物理z域收敛指标改为全部导模净功率，并按入射到0.60 µm光栅宽度的功率归一化。
- Stage212a宽域资源门槛通过：z域1.6 µm、monitor 1.3 µm、光栅0.6 µm、mesh z span1.4 µm、dz40 nm；网格3462×203×50，仅为Stage207的1.111倍，预计61分钟、0.848 GiB/进程。
- Stage212b有齿宽域仿真已于2026-10-01启动。完成前禁止在Lumerical输入脚本、切换layout或停止进程；完成后运行匹配的无齿参考，再做复场扣除与导模投影。

## 10. 下次从这里继续

1. Stage198的2D Gaussian文件仍是正式设计基准，不得被3D诊断副本覆盖。
2. Stage202已经证明dz=20 nm足够；不得继续盲目细化dz。
3. Stage203a审计已完成，不再追查网格或周期单元。
4. Stage204–206模式验证完成；3D periodic基准已锁定。
5. Stage207–209b已经量化有限宽plane-wave的背景、纯散射场与相干交叉项；不得继续用direct power优化几何，也不得把简单功率差叫耦合效率。
6. Stage210–211固定模式基底与16→32模收敛已完成，不再增加模式数。
7. 当前等待Stage212b z域1.6 µm有齿仿真；完成后跑相同宽域的无齿参考，并用全部导模净功率比较Stage207的z域1.2 µm结果。
8. z域收敛后进入明确束腰与焦点的有限3D光束；周期桥接结果不能充当有限孔径结果。
8. 所有638 nm单色脚本继续显式设置 `source wavelength span=0`；低于已知数值不确定度的微小提升不再追逐。
9. `power_top` 含入射场且符号由监视器法向决定，不能与左右功率取绝对值后直接相加。

## 11. 关键文件

- 权威单波长基准（span=0、status=2）：`D:/FDTD_File/ar_incoupler_FDTD_stage181_AUTHORITATIVE_SINGLE_638nm_span0_status2_24teeth_mesh3p5nm_2D.fsp`
- 权威单波长数据：`D:/FDTD_File/stage181_true_single_wavelength_638nm.ldf`
- Stage174 旧文件（当前保存状态为 span=20，仅作历史文件）：`D:/FDTD_File/ar_incoupler_FDTD_stage174_MESH_CONVERGED_24teeth_638nm_x7um_mesh3p5nm_2D.fsp`
- 宽带检查点：`D:/FDTD_File/ar_incoupler_FDTD_stage175b_CHECKPOINT_broadband_unreconciled_20260929.fsp`
- 宽带原始数据：`D:/FDTD_File/stage175b_broadband_corrected_628_648nm_raw.ldf`
- 宽带处理数据：`D:/FDTD_File/stage175b_broadband_628_648nm_processed.ldf`
- 源带宽复核数据：`D:/FDTD_File/stage176_source_span10nm_638nm_center.ldf`、`stage177_source_span5nm_638nm_center.ldf`、`stage178_source_span2nm_time1000fs_638nm_center.ldf`
- 周期/角度复核数据：`D:/FDTD_File/stage182_period_angle_revalidation_span0_638nm.ldf`
- Stage182 raw 最高点文件（未正式采用）：`D:/FDTD_File/ar_incoupler_FDTD_stage182_ADOPTED_period_angle_span0_638nm_24teeth_mesh3p5nm_2D.fsp`
- 宽高联合扫描：`D:/FDTD_File/stage184_joint_width_height_candidate_span0_638nm.ldf`
- 新结构网格复核：`D:/FDTD_File/stage185_candidate_mesh_convergence_span0_638nm.ldf`
- 新结构监视面复核：`D:/FDTD_File/stage186_candidate_monitor_plane_validation_span0_638nm.ldf`
- 当前正式基准：`D:/FDTD_File/ar_incoupler_FDTD_stage186_VALIDATED_W185_H310_span0_638nm_x7um_mesh3p5nm_24teeth_2D.fsp`
- 周期/角度边界复核：`D:/FDTD_File/stage188_period_edge_extension_newWH_span0_638nm.ldf`
- shift 扫描：`D:/FDTD_File/stage189_top_shift_scan_final_geometry_span0_638nm.ldf`
- shift 3 nm 直接复核：`D:/FDTD_File/stage190_shift_3nm_direct_validation_span0_638nm.ldf`
- Stage191 制造公差原始数据：`D:/FDTD_File/stage191_manufacturing_corners_WHS_span0_638nm.ldf`
- Stage191 可读汇总：`D:/Codex/Kai/stage191_manufacturing_corners_summary.csv`
- 当前最新正式基准：`D:/FDTD_File/ar_incoupler_FDTD_stage191_ROBUSTNESS_VALIDATED_FINAL_span0_638nm_mesh3p5nm_24teeth_2D.fsp`
- Stage192 归一化场强图：`D:/Codex/Kai/stage192_E2dB.png`
- Stage192 最终验证摘要：`D:/Codex/Kai/stage192_final_validation_summary.md`
- Stage193 角度粗扫数据：`D:/FDTD_File/stage193_engineering_angle_coarse_span0_638nm.ldf`
- Stage194 3 dB 边界细扫数据：`D:/FDTD_File/stage194_engineering_angle_3dB_boundary_fine_span0_638nm.ldf`
- Stage194 可读角度数据：`D:/Codex/Kai/stage194_engineering_angle_response.csv`
- Stage194 角度响应图：`D:/Codex/Kai/stage194_engineering_angle_response.png`
- Stage194 角度验证摘要：`D:/Codex/Kai/stage194_engineering_angle_validation_summary.md`
- 当前工程验证基准：`D:/FDTD_File/ar_incoupler_FDTD_stage194_ENGINEERING_ANGLE_3DB_VALIDATED_RESTORED_NOMINAL_span0_638nm_mesh3p5nm_24teeth_2D.fsp`
- Stage195 单色粗扫：`D:/FDTD_File/stage195_engineering_single_wavelength_coarse_span0.ldf`
- Stage196 单色3 dB细扫：`D:/FDTD_File/stage196_engineering_single_wavelength_3dB_fine_span0.ldf`
- Stage196 可读光谱数据：`D:/Codex/Kai/stage196_engineering_spectral_response.csv`
- Stage196 单色光谱响应图：`D:/Codex/Kai/stage196_engineering_spectral_response.png`
- Stage196 光谱验证摘要：`D:/Codex/Kai/stage196_engineering_spectral_validation_summary.md`
- 当前最新工程验证基准：`D:/FDTD_File/ar_incoupler_FDTD_stage196_ENGINEERING_SINGLE_WAVELENGTH_3DB_VALIDATED_RESTORED_638nm_span0_mesh3p5nm_24teeth_2D.fsp`
- Stage197 联合响应原始数据：`D:/FDTD_File/stage197_engineering_wavelength_angle_joint_map_span0.ldf`
- Stage197 可读联合矩阵：`D:/Codex/Kai/stage197_wavelength_angle_joint_map.csv`
- Stage197 联合响应摘要：`D:/Codex/Kai/stage197_wavelength_angle_joint_summary.md`
- Stage197 联合响应热图：`D:/Codex/Kai/stage197_wavelength_angle_joint_heatmap.png`
- 当前最新工程验证基准：`D:/FDTD_File/ar_incoupler_FDTD_stage197_ENGINEERING_WAVELENGTH_ANGLE_JOINT_RESTORED_638nm_minus15p1_span0_mesh3p5nm_24teeth_2D.fsp`
- Stage198 色散峰值原始数据：`D:/FDTD_File/stage198_engineering_dispersion_peak_fine_3x3_span0.ldf`
- Stage198 可读峰值数据：`D:/Codex/Kai/stage198_dispersion_peaks.csv`
- Stage198 色散验证摘要：`D:/Codex/Kai/stage198_dispersion_peak_summary.md`
- Stage198 色散峰值图：`D:/Codex/Kai/stage198_dispersion_peaks.png`
- 当前最新工程验证基准：`D:/FDTD_File/ar_incoupler_FDTD_stage198_ENGINEERING_DISPERSION_PEAKS_RESTORED_638nm_minus15p1_span0_mesh3p5nm_24teeth_2D.fsp`
- Stage199 相位匹配反算数据：`D:/Codex/Kai/stage199_phase_matching_check.csv`
- Stage199 相位匹配验证图：`D:/Codex/Kai/stage199_phase_matching_verification.png`
- Stage199 相位匹配验证摘要：`D:/Codex/Kai/stage199_phase_matching_verification.md`
- Stage200 当前模型只读审计脚本：`D:/Codex/Kai/stage200_audit_current_2d_model.lsf`
- Stage200 3D资源预算与启动门槛：`D:/Codex/Kai/stage200_3d_resource_budget_and_gate.md`
- Stage201 2D/3D源映射数据：`D:/Codex/Kai/stage201_2d_to_3d_source_mapping.csv`
- Stage201 2D/3D源映射总结：`D:/Codex/Kai/stage201_2d_to_3d_source_mapping_summary.md`
- Stage201 2D/3D源映射图：`D:/Codex/Kai/stage201_2d_to_3d_source_mapping.png`
- Stage201b 2D plane-wave参考：`D:/FDTD_File/ar_incoupler_FDTD_stage201b_2D_PLANE_WAVE_REFERENCE_638nm_24teeth_COMPLETE.fsp`
- Stage201e正确3D源映射数据：`D:/FDTD_File/stage201e_3d_periodic_plane_wave_phiM90_dz20nm_direct_power.ldf`
- Stage201e正确3D源映射模型：`D:/FDTD_File/ar_incoupler_FDTD_stage201e_3D_PERIODIC_PLANE_WAVE_phiM90_dz20nm_638nm_24teeth_COMPLETE.fsp`
- Stage202运行脚本：`D:/Codex/Kai/stage202_run_3d_periodic_bridge_dz10nm.lsf`
- Stage202原始数据：`D:/FDTD_File/stage202_3d_periodic_plane_wave_phiM90_dz10nm_direct_power.ldf`
- Stage202完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage202_3D_PERIODIC_PLANE_WAVE_phiM90_dz10nm_638nm_24teeth_COMPLETE.fsp`
- Stage202可读收敛表：`D:/Codex/Kai/stage202_3d_periodic_bridge_convergence.csv`
- Stage202收敛总结：`D:/Codex/Kai/stage202_3d_periodic_bridge_convergence_summary.md`
- Stage202收敛图：`D:/Codex/Kai/stage202_3d_periodic_bridge_convergence.png`
- Stage203周期单元宽度测试脚本：`D:/Codex/Kai/stage203_run_3d_periodic_zcell0p4um_dz20nm.lsf`
- Stage203原始数据：`D:/FDTD_File/stage203_3d_periodic_zcell0p4um_phiM90_dz20nm_direct_power.ldf`
- Stage203完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage203_3D_PERIODIC_zcell0p4um_phiM90_dz20nm_638nm_24teeth_COMPLETE.fsp`
- Stage203可读不变性表：`D:/Codex/Kai/stage203_3d_periodic_zcell_invariance.csv`
- Stage203不变性总结：`D:/Codex/Kai/stage203_3d_periodic_zcell_invariance_summary.md`
- Stage203a只读审计脚本：`D:/Codex/Kai/stage203a_audit_2d_3d_sourcepower_xy_mesh.lsf`
- Stage203a原始审计数据：`D:/FDTD_File/stage203a_2d_3d_sourcepower_xy_mesh_audit.ldf`
- Stage203a可读审计表：`D:/Codex/Kai/stage203a_2d_3d_sourcepower_xy_mesh_audit.csv`
- Stage203a审计总结：`D:/Codex/Kai/stage203a_2d_3d_sourcepower_xy_mesh_audit_summary.md`
- Stage204 8模式验证脚本：`D:/Codex/Kai/stage204_run_3d_periodic_mode_expansion_8modes.lsf`
- Stage204–206模式验证总结：`D:/Codex/Kai/stage204_206_3d_periodic_mode_validation_summary.md`
- Stage204逐模可读表：`D:/Codex/Kai/stage204_mode_breakdown.csv`
- Stage204–206基底收敛表：`D:/Codex/Kai/stage204_206_mode_basis_convergence.csv`
- Stage205 16模式后处理脚本：`D:/Codex/Kai/stage205_postrun_expand_mode_basis_16.lsf`
- Stage206 32模式后处理脚本：`D:/Codex/Kai/stage206_postrun_expand_mode_basis_32.lsf`
- Stage207有限宽pilot资源门槛脚本：`D:/Codex/Kai/stage207_build_finite_width_plane_wave_pilot_gate.lsf`
- Stage207资源门槛总结：`D:/Codex/Kai/stage207_finite_width_resource_gate_summary.md`
- Stage207运行脚本：`D:/Codex/Kai/stage207_run_finite_width_plane_wave_pilot.lsf`
- Stage207功率截取诊断脚本：`D:/Codex/Kai/stage207_power_right_z_capture_diagnostic.lsf`
- Stage207功率截取可读表：`D:/Codex/Kai/stage207_power_right_z_capture.csv`
- Stage207有限宽结果诊断总结：`D:/Codex/Kai/stage207_finite_width_power_diagnostic_summary.md`
- Stage208无光栅参考运行脚本：`D:/Codex/Kai/stage208_run_finite_width_unpatterned_reference.lsf`
- Stage208完整无光栅参考：`D:/FDTD_File/ar_incoupler_FDTD_stage208_FINITE_WIDTH_UNPATTERNED_REFERENCE_zPML_domain1p2um_dz40nm_638nm_COMPLETE.fsp`
- Stage208原始参考数据：`D:/FDTD_File/stage208_finite_width_unpatterned_reference_direct_power.ldf`
- Stage209b插值复场分解脚本：`D:/Codex/Kai/stage209b_postprocess_interpolated_field_decomposition.lsf`
- Stage209b原始分解数据：`D:/FDTD_File/stage209b_interpolated_pattern_reference_field_decomposition.ldf`
- Stage207–209可读分解表：`D:/Codex/Kai/stage207_209_finite_width_background_decomposition.csv`
- Stage207–209验证总结：`D:/Codex/Kai/stage207_209_finite_width_background_validation_summary.md`
- Stage209b分解图记录：`D:/Codex/Kai/stage209b_interpolated_decomposition_screen.png`
- Stage210固定16模分解：`D:/FDTD_File/stage210d_fixed_basis_16mode_decomposition.ldf`
- Stage211 32模收敛分析：`D:/FDTD_File/stage211c_mode_basis32_convergence_analysis.ldf`
- Stage210–211可读总结：`D:/Codex/Kai/stage210_211_fixed_mode_validation_summary.md`
- Stage210逐模表：`D:/Codex/Kai/stage210d_fixed_basis_mode_table.csv`
- Stage211模式验证图：`D:/Codex/Kai/stage211_fixed_mode_validation.png`
- Stage212资源门槛：`D:/FDTD_File/stage212a_zdomain1p6_monitor1p3_resource_gate.ldf`
- Stage212有齿运行脚本：`D:/Codex/Kai/stage212b_run_zdomain1p6_monitor1p3_patterned.lsf`
- Stage212b原始直接功率数据：`D:/FDTD_File/stage212b_zdomain1p6_monitor1p3_patterned_direct_power.ldf`
- Stage212b完整有齿模型：`D:/FDTD_File/ar_incoupler_FDTD_stage212b_PATTERNED_zdomain1p6_monitor1p3_grating0p6_dz40nm_638nm_COMPLETE.fsp`
- Stage207/212初步直接结果表：`D:/Codex/Kai/stage207_212_preliminary_direct_domain_comparison.csv`
- Stage212b初读说明：`D:/Codex/Kai/stage212b_preliminary_direct_result.md`
- Stage212b已完成（2026-10-01）：status=2，Psrc=3.469050501e-14 W，right signed=5.006244%，left signed=-1.121449%，top signed=-69.953911%，按 1.6/0.6 宽度换算的直接右侧值=13.349984%。完整模型与LDF已写盘。该直接值仍含背景与干涉项，不能作为最终耦合效率。
- Stage213已完成：status=2，24个光栅对象均禁用，右侧背景=-1.416084%，约占有齿直接右侧功率绝对值的28.286%。
- Stage213匹配无齿参考脚本（已离线生成并校验对象名，待 Stage212b 完成后执行）：`D:/Codex/Kai/stage213_run_zdomain1p6_monitor1p3_unpatterned_reference.lsf`
- Stage214a宽域相干复场分解脚本（已离线生成，待 Stage213 完成后执行）：`D:/Codex/Kai/stage214a_zdomain1p6_coherent_field_decomposition.lsf`
- Stage214b宽域有齿32模固定基底脚本（已离线生成，待 Stage212b 完成后执行）：`D:/Codex/Kai/stage214b_patterned_wide_domain_fixed_mode_basis32.lsf`
- Stage214c宽域固定基底投影与域收敛脚本（已离线生成，待 Stage214a/214b 完成后执行）：`D:/Codex/Kai/stage214c_wide_domain_fixed_basis32_projection_and_convergence.lsf`
- Stage214a已完成：散射场6.351223%，交叉项0.068899%，重构相对误差约1.14e-16。
- Stage214b/c已完成：32模式、14导模；宽度归一化总导模净功率16.917800%，相对Stage207的15.353965%增加1.563835pp/10.1852%，未收敛。
- Stage207–214域收敛表：`D:/Codex/Kai/stage207_214_guided_domain_convergence.csv`
- Stage212–214验证总结：`D:/Codex/Kai/stage212_214_wide_domain_validation_summary.md`
- Stage215a资源门槛已通过：3462x203x60，Stage212节点量的1.20倍，预计69.6分钟，每引擎约0.516GiB。
- Stage215b已完成（2026-10-02）：status=2，Psrc=4.326393337008336e-14 W，right signed=4.056842509%，left signed=-1.188919894%，top signed=-71.939483822%，按 2.0/0.6 宽度换算的直接右侧值=13.522808365%。输出：`D:/FDTD_File/stage215b_zdomain2p0_monitor1p7_patterned_direct_power.ldf`；完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage215b_PATTERNED_zdomain2p0_monitor1p7_grating0p6_dz40nm_638nm_COMPLETE.fsp`。直接值仍含背景与相干交叉项，不作为最终耦合效率。
- Stage216匹配无齿参考已完成（2026-10-02）：status=2，24个光栅对象均禁用，Psrc=4.3255321337e-14 W，右侧背景=-1.515012%，left=-1.115493%，top=-67.401770%。运行脚本：`D:/Codex/Kai/stage216_run_zdomain2p0_monitor1p7_reference.lsf`；结果：`D:/FDTD_File/stage216_zdomain2p0_monitor1p7_unpatterned_reference_direct_power.ldf`；完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage216_REFERENCE_zdomain2p0_monitor1p7_grating0p6_dz40nm_638nm_COMPLETE.fsp`。
- Stage217a相干复场分解已完成：有齿总场4.056843%，背景-1.512662%，纯散射场5.509591%，交叉项0.059913%，重构相对误差约3.37e-16。结果：`D:/FDTD_File/stage217a_zdomain2p0_coherent_field_decomposition.ldf`。
- Stage217b/c固定32模投影已完成：18个导模，导模前向5.507225%，后向0.000660%，净值5.506565%；TM前向5.479902%，TE前向0.025800%；mode1前向4.837737%，占导模前向87.8435%；未展开散射净残差0.000653%。按0.6um光栅宽归一后为18.355217%，相对Stage214c的16.917800%增加1.437416pp/8.49647%，未通过<0.2pp或<1%的域收敛门槛。结果：`D:/FDTD_File/stage217c_zdomain2p0_fixed_basis32_projection_and_convergence.ldf`。
- Stage218a资源门已通过：z-domain=2.4um、monitor=2.1um、grating=0.6um、dz=40nm，网格3462x203x72，节点量为Stage212的1.44倍，预计83.52分钟，每引擎约0.6192GiB。结果：`D:/FDTD_File/stage218a_zdomain2p4_monitor2p1_resource_gate.ldf`。
- Stage218b已完成（2026-10-02）：status=2，Psrc=5.1781087059e-14 W，right signed=4.242899%，left=-1.218728%，top=-72.329581%，按2.4/0.6宽度换算的直接右侧值=16.971596%。结果：`D:/FDTD_File/stage218b_zdomain2p4_monitor2p1_patterned_direct_power.ldf`；完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage218b_PATTERNED_zdomain2p4_monitor2p1_grating0p6_dz40nm_638nm_COMPLETE.fsp`。直接值仍含背景与干涉项。
- Stage219已完成（2026-10-02）：status=2，24个光栅对象均禁用，Psrc=5.1770779952e-14 W，right=-1.573014%，left=-1.154533%，top=-68.923844%。结果：`D:/FDTD_File/stage219_zdomain2p4_monitor2p1_unpatterned_reference_direct_power.ldf`；完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage219_REFERENCE_zdomain2p4_monitor2p1_grating0p6_dz40nm_638nm_COMPLETE.fsp`。
- Stage220a相干场分解已完成：有齿总场4.242899%，参考背景-1.570577%，纯散射场5.747117%，交叉项0.066359%；重构误差为0，参考插值相对原生值差0.002123pp。结果：`D:/FDTD_File/stage220a_zdomain2p4_coherent_field_decomposition.ldf`。
- Stage220b/c固定32模投影已完成：22个导模，导模前向5.742414%，后向0.000534%，净值5.741881%；TM前向5.717402%，TE前向0.025012%；mode1前向4.476789%，占导模前向77.9600%；未展开散射净残差0.000568%。按0.6um光栅宽归一后为22.967523%，相对Stage217c的18.355217%增加4.612307pp/25.1280%，未通过<0.2pp或<1%的域收敛门槛。线性误差约2.22e-16，手工/内置模式投影最大差0.001608pp，证明读取与投影正确；不再盲目扩域，转为明确有限光束的物理3D验证。结果：`D:/FDTD_File/stage220c_zdomain2p4_fixed_basis32_projection_and_convergence.ldf`。
- Stage221a/b建立了有限椭圆Gaussian导入源：x向直接继承Stage198正式2D Gaussian的6um腰斑、-15.1°相位、TM偏振及E/H；z向乘以wz=0.45um的Gaussian包络，数据范围±1.10um、81点。旧平面波禁用，导入源唯一启用并沿y轴Backward注入。z数据边界场振幅0.2541%，0.6um光栅边缘场振幅64.1180%，E×H直接积分入射功率5.570171653e-15 W。设置文件：`D:/FDTD_File/ar_incoupler_FDTD_stage221b_ELLIPTICAL_IMPORT_SOURCE_wx6um_wz0p45um_SETUP_638nm.fsp`；审计：`D:/FDTD_File/stage221b_elliptical_import_source_wz0p45_setup_audit.ldf`。导入源不使用`sourcepower/transmission`归一化，后续一律使用直接Poynting积分。
- Stage222已完成（2026-10-02）：status=2，直接入射功率5.570171653e-15 W，右向直接功率2.875820049e-17 W，即0.5162893%；左向出射2.2317462%，上方监视面带符号功率-63.884931%。这些是直接监视器功率，不是最终导模耦合效率。原始数据：`D:/FDTD_File/stage222_elliptical_gaussian_wz0p45_patterned_direct_power.ldf`；完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage222_ELLIPTICAL_GAUSSIAN_wx6um_wz0p45um_PATTERNED_COMPLETE_638nm.fsp`。
- Stage223已完成（2026-10-10）：status=2，24个光栅对象全部禁用，直接入射功率`5.570171652777991e-15 W`，与Stage222逐位一致；右侧参考带符号功率`-0.5391689%`，左侧出射`1.9902776%`，上方带符号功率`-46.8659961%`。原始数据：`D:/FDTD_File/stage223_elliptical_gaussian_wz0p45_reference_direct_power.ldf`；完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage223_ELLIPTICAL_GAUSSIAN_wx6um_wz0p45um_REFERENCE_COMPLETE_638nm.fsp`。
- Stage224a相干场分解已完成：有齿总场右向`0.5162893%`，插值参考背景`-0.5389806%`，纯散射场`1.0581986%`，交叉项`-0.0029287%`；入射功率比为1，y网格最大差`4.38e-10 m`、z网格差0，重构误差严格为0。结果：`D:/FDTD_File/stage224a_elliptical_gaussian_wz0p45_coherent_field_decomposition.ldf`。
- Stage224b/c固定32模投影已完成：32个模式、22个导模；纯散射导模前向`1.0553890%`、后向`0.00010566%`、净值`1.0552834%`；TM前向`1.0377793%`、TE前向`0.0175988%`；mode1前向`0.8010840%`，占前向导模`75.9041%`。直接散射净值`1.0581986%`，未展开净残差仅`0.0012860%`；a/b线性误差分别约`2.86e-17/1.47e-17`。该`1.0552834%`是当前有限椭圆Gaussian物理3D净导模耦合效率，不再做平面波域宽归一。结果：`D:/FDTD_File/stage224b_elliptical_gaussian_patterned_fixed_mode_basis32.ldf`、`D:/FDTD_File/stage224c_elliptical_gaussian_fixed_basis32_projection.ldf`。
- 下一验证点：保持x向6um腰斑及全部光栅/网格设置不变，只将z向1/e场半径从`0.45um`改为`0.55um`，重新生成匹配的有齿与无齿参考并重复相干场/固定模态投影；比较有限光束净导模效率，判断光束腰灵敏度与边界截断误差。
- Stage225a已完成（2026-10-10）：建立`wz=0.55um`有限椭圆Gaussian导入源，数据范围仍为±1.10um、81点；直接入射功率`6.807557395418483e-15 W`，数据边缘场幅`1.8315639%`（边缘强度约`0.03355%`），光栅边缘场幅`74.265724%`。审计：`D:/FDTD_File/stage225a_elliptical_import_source_wz0p55_setup_audit.ldf`；设置模型：`D:/FDTD_File/ar_incoupler_FDTD_stage225a_ELLIPTICAL_IMPORT_SOURCE_wx6um_wz0p55um_SETUP_638nm.fsp`。
- Stage225b已完成（2026-10-10）：`status=2`，直接入射功率`6.807557395418483e-15 W`；有齿右侧直接功率`0.4509671%`，左侧出射`2.1664232%`，上方带符号功率`-42.5968981%`。这些仍是总场监视器结果，不是最终导模耦合效率。原始数据：`D:/FDTD_File/stage225b_elliptical_gaussian_wz0p55_patterned_direct_power.ldf`；完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage225b_ELLIPTICAL_GAUSSIAN_wx6um_wz0p55um_PATTERNED_COMPLETE_638nm.fsp`。
- Stage225c已完成（2026-10-10）：`status=2`，24个光栅对象全部禁用，入射功率`6.807557395418483e-15 W`与Stage225b逐位一致；右侧参考背景`-0.5340423%`，左侧出射`1.9733708%`，上方带符号功率`-27.9633558%`。原始数据：`D:/FDTD_File/stage225c_elliptical_gaussian_wz0p55_reference_direct_power.ldf`；完整模型：`D:/FDTD_File/ar_incoupler_FDTD_stage225c_ELLIPTICAL_GAUSSIAN_wx6um_wz0p55um_REFERENCE_COMPLETE_638nm.fsp`。
- Stage226a/b/c已完成并通过全部数值门槛：相干场重构相对误差`-2.01e-16`；32模式、22导模；a/b线性误差`4.16e-17/4.17e-17`。`wz=0.55um`的纯散射直接功率`0.9865539%`，导模前向`0.9840182%`、后向`0.00009718%`、净效率`0.9839211%`；TM前向`0.9680050%`、TE前向`0.0160043%`；mode1前向`0.7460080%`，占导模前向`75.8124%`；未展开净残差`0.0011415%`。
- 束腰敏感性结论：相对`wz=0.45um`的`1.0552834%`，`wz=0.55um`净效率下降`0.0713623pp`、相对下降`6.7624%`，未通过`0.02pp且2%`局部不敏感门槛。绝对导模功率反而从`5.8781096e-17 W`增至`6.6980991e-17 W`（`+13.9499%`），说明更宽光束增加了耦合功率，但总入射功率增加更快；这是照明重叠效应，不是光栅结构退化。
- 下一步不改光栅几何：先为`wz=0.65um`检查/扩展z域、源数据和监视器边界并做资源门槛，再重复匹配有齿/无齿、相干扣背景和固定32模投影。汇总：`D:/Codex/Kai/stage221_226_finite_elliptical_gaussian_validation_summary.md`；可读表：`D:/Codex/Kai/stage221_226_finite_elliptical_gaussian_summary.csv`；机器结果与哈希：`D:/Codex/Kai/stage225_226_pipeline_results.json`。
- Stage227a资源门槛与设置已完成（2026-10-10）：`wz=0.65um`，源数据±`1.30um`/97点/`27.0833nm`采样，FDTD z域`2.80um`，监视器`2.50um`，z网格覆盖`2.60um`且`dz=40nm`，光栅宽度保持`0.60um`。实际网格`3462x203x82`，节点量为Stage218的`1.138889`倍，预计单次约`96.07min`、每引擎约`0.589GiB`。源数据/监视器/FDTD边界强度分别为`0.03355%/0.06134%/0.009345%`，均低于`0.1%`；资源与边界门槛通过。审计：`D:/FDTD_File/stage227a_wz0p65_expanded_domain_resource_gate_and_setup_audit.ldf`；设置模型：`D:/FDTD_File/ar_incoupler_FDTD_stage227a_ELLIPTICAL_IMPORT_SOURCE_wx6um_wz0p65um_zdomain2p8um_SETUP_638nm.fsp`。
- Stage227b状态（2026-10-11复核）：`wz=0.65um`有齿仿真已完成，`status227b=2`，`Pin227b=8.045297289070808e-15 W`，与Stage227a完全一致；`eta_right=0.4195197959%`、`eta_left_out=2.1260786409%`、`eta_top_signed=-37.8252853831%`。原始LDF与完整FSP均已保存，stdout为`SCRIPT_COMPLETED`且stderr为空。
- Stage227c状态（2026-10-11）：严格匹配的`wz=0.65um`无齿参考仿真已启动，隐藏Python PID 37136；已确认`mpiexec -n 6`及6个`fdtd-engine-msmpi`进程运行，stderr为空。运行文件：`D:/FDTD_File/ar_incoupler_FDTD_stage227c_ELLIPTICAL_GAUSSIAN_wx6um_wz0p65um_zdomain2p8um_REFERENCE_RUNNING_638nm.fsp`。完成前不得执行Stage228分析或关闭求解器。
- Stage227c最终状态（2026-10-11）：参考仿真自然完成，stdout=`SCRIPT_COMPLETED`、stderr为空；`status227c=2`、`disabled227c=24`、`Pin227c=8.045297289070808e-15 W`，与Stage227b严格一致。完整FSP：`D:/FDTD_File/ar_incoupler_FDTD_stage227c_ELLIPTICAL_GAUSSIAN_wx6um_wz0p65um_zdomain2p8um_REFERENCE_COMPLETE_638nm.fsp`。
- Stage228相干场/固定32模投影已完成并通过闭合校验：右向导模净效率=`0.9493820228%`，前向=`0.9494544840%`，后向=`0.0000724612%`；前向TM=`0.9310203424%`，TE=`0.0180988098%`；mode1=`0.6070697595%`，占前向导模`63.93879535%`；未展开残差=`0.0008306901%`，场重构相对误差=`3.6519591e-16`。
- 三点束腰验证：`wz=0.45/0.55/0.65um`的净导模效率分别为`1.0552833771% / 0.9839210613% / 0.9493820228%`，呈单调下降；`0.55→0.65um`变化`-0.034539 pp`、相对`-3.5103%`，未通过2%局部不敏感门限。结论：停止盲目束腰扫描，先固定真实照明/瞳孔规格，再继续光栅几何优化。完整机器可读报告：`D:/Codex/Kai/stage227_228_pipeline_results.json`。
- 已在可见的Lumerical FDTD 2026 R1界面打开Stage227b有齿完成模型（GUI PID 13468），供后续逐项查看结构与结果。
- Stage229工程照明门槛已建立：`D:/Codex/Kai/STAGE229_ENGINEERING_ILLUMINATION_GATE_2026-10-11.md`。从此不再把`wz`作为单点效率最大化变量；暂以`wz=0.55um`为名义比较点、`0.45/0.65um`为照明容差端点，后续几何候选按名义效率、最差端效率和三点跨度共同排序，并在真实投影光机规格到位后替换该临时门槛。
- Stage230转入三维有限光栅宽度优化：二维标称几何（周期328.75nm、齿宽185nm、齿高310nm、top shift -240nm、入射角-15.1°）保持不变。Stage230a仅将12组`tooth+outer`对象的z span从0.60um扩大到1.20um；最初误将24个对象当成24个编号，设置门槛在运行前发现第13组不存在，已修正为12组且未启动错误仿真。设置校验通过：`status=1`、宽度1.20um、`wz=0.65um`、边缘场幅42.6531%、边缘强度18.1928%。可见Layout文件：`D:/FDTD_File/ar_incoupler_FDTD_stage230a_GRATING_WIDTH1p2um_wx6um_wz0p65um_zdomain2p8um_SETUP_638nm.fsp`（GUI PID 18352）。长仿真尚未启动。
- Stage230b状态（2026-10-11 16:53）：1.20um宽有齿模型已启动，隐藏Python PID 23052；预检确认无其它FDTD engine，启动后确认6个`fdtd-engine-msmpi`进程，stderr为空。运行文件：`D:/FDTD_File/ar_incoupler_FDTD_stage230b_GRATING_WIDTH1p2um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_RUNNING_638nm.fsp`。可见Stage230a Layout窗口继续保留；求解完成前不得修改运行文件或启动第二个宽度候选。
- Stage230b最终状态：自然完成，stdout=`SCRIPT_COMPLETED`、stderr为空，`status=2`，完整FSP与直接功率LDF已保存。
- Stage231相干扣除/固定32模投影已完成。Stage231c第一次执行因机械生成残留旧变量名`TS228a`失败，核对后修正为`TS231a`并成功重跑；未重跑FDTD。1.20um宽度的净导模效率=`0.8520408813%`，比0.60um基线`0.9493820228%`下降`0.097341 pp / 10.2531%`；Mode1效率下降2.0564%，但Mode1占比从63.9388%提高到69.7792%。结论：1.20um不是效率最优，但揭示效率—纯度折中；下一候选为中间点0.90um。详细记录：`D:/Codex/Kai/STAGE230_231_GRATING_WIDTH1P2UM_VALIDATION_2026-10-11.md`。
- Stage232a/b状态（2026-10-11 19:07）：0.90um中点设置已通过，宽度0.90um、半宽0.45um、`wz=0.65um`、边缘场幅61.9223%、边缘强度38.3437%；运行脚本静态确认恰好一个`run;`。Stage232b已启动，隐藏Python PID 21604，预检无其它engine，启动后6个`fdtd-engine-msmpi`进程正常，stderr为空。运行文件：`D:/FDTD_File/ar_incoupler_FDTD_stage232b_GRATING_WIDTH0p9um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_RUNNING_638nm.fsp`。
- Stage232b最终状态（2026-10-11）：原进程自然完成，stdout=`SCRIPT_COMPLETED`、stderr为空，`status=2`，完整FSP 175.44MB；直接右侧总场功率为`0.1072283791%`，该值含参考背景和相干交叉项，不作最终效率。
- Stage233a/b/c已完成：相干重构相对误差`-3.89e-16`，32模式中28个满足`Re(neff)>1`；0.90um宽度的净导模效率=`0.9856947781%`，前向=`0.9857582603%`，后向=`0.0000634822%`；TM前向=`0.9738220774%`，TE前向=`0.0117412363%`；mode1前向=`0.6922252398%`，占前向导模=`70.22261621%`；未展开净残差=`0.0004613078%`。与0.60um的`0.9493820228%`和1.20um的`0.8520408813%`相比，0.90um同时提高净效率与mode1纯度。三点二次插值仅用于选点，估计峰值约0.814um；下一次只验证0.80um。详细记录：`D:/Codex/Kai/STAGE232_233_WIDTH0P9UM_VALIDATION_2026-10-11.md`。
- Stage234a/b状态（2026-10-11）：0.80um细化点设置已通过，半宽0.40um、`wz=0.65um`，边缘场幅`68.4752%`、边缘强度`46.8886%`；设置脚本0次`run;`、正式脚本恰好1次`run;`且无Stage232残留。可见Layout已打开（GUI PID 36728）。Stage234b正式仿真已启动，隐藏Python PID 7612，确认6个`fdtd-engine-msmpi`、运行FSP已生成且stderr为空。完成前不得修改运行模型或启动第二个候选。
- Stage234b最终状态（2026-10-11）：自然完成，`status=2`，stdout=`SCRIPT_COMPLETED`、stderr为空，完整FSP 175.44MB；入射功率与基线逐位一致。Stage235a/b/c随后完成且通过数值闭合：相干重构误差`-1.21e-16`，a/b线性误差`5.55e-17/3.26e-17`，未展开净残差`0.0001356%`。
- 0.80um最终结果：净导模效率=`1.2199720446%`，前向=`1.2200421425%`，后向=`0.0000700978%`；TM前向=`1.2093806313%`，TE前向=`0.0104837035%`；mode1前向=`0.8365567450%`，占前向导模=`68.56785646%`。相对0.90um净效率提高`0.234277pp/23.7677%`，当前已验证点中效率和mode1绝对效率均最高。0.60/0.80/0.90um局部二次插值峰值约0.755um，下一步只验证0.75um；若相对0.80um提升小于1%，保留制造更稳健的0.80um并停止细化。详细记录：`D:/Codex/Kai/STAGE234_235_WIDTH0P8UM_VALIDATION_2026-10-11.md`。
- Stage236a/b状态（2026-10-11）：0.75um验证点设置已通过，半宽0.375um、`wz=0.65um`，边缘场幅`71.6885%`、边缘强度`51.3924%`；设置脚本0次`run;`、正式脚本恰好1次`run;`且无Stage234/235残留。可见Layout PID 34256。Stage236b正式仿真已启动，隐藏Python PID 29488，确认6个`fdtd-engine-msmpi`、运行FSP已生成且stderr为空。
- Stage236b最终状态（2026-10-12）：自然完成，`status=2`，stdout=`SCRIPT_COMPLETED`、stderr为空，完整FSP 175.44MB；Stage237a/b/c均成功，源功率比1，相干重构误差`-4.21e-16`，a/b线性误差`2.78e-17/1.91e-17`，未展开净残差`0.0001472%`。
- 0.75um最终结果：净导模效率=`1.3081025977%`，前向=`1.3081799415%`，后向=`0.0000773438%`；TM前向=`1.2950469051%`，TE前向=`0.0128862682%`；mode1前向=`0.8854150199%`，占前向导模=`67.68296866%`。相对0.80um净效率提高`7.2240%`，mode1绝对效率提高`5.8404%`，继续细化。0.60/0.75/0.80um局部拟合峰值约0.7326um，下一验证点0.73um。详细记录：`D:/Codex/Kai/STAGE236_237_WIDTH0P75UM_VALIDATION_2026-10-12.md`。
- Stage238a/b状态（2026-10-12）：0.73um局部峰值验证点设置已通过，半宽0.365um、`wz=0.65um`，边缘场幅`72.9551%`、边缘强度`53.2245%`；设置脚本0次`run;`、正式脚本恰好1次`run;`且无Stage236/237残留。可见Layout PID 25224。Stage238b正式仿真已启动，隐藏Python PID 38360，确认6个`fdtd-engine-msmpi`、运行FSP已生成且stderr为空。
- Stage238b最终状态（2026-10-12）：自然完成，`status=2`，stdout=`SCRIPT_COMPLETED`、stderr为空，完整FSP 175.44MB。Stage239a/b/c均成功，源功率比1，相干重构误差0，a/b线性误差`2.78e-17/2.26e-17`，未展开净残差`0.0002930%`。
- 0.73um最终结果：净导模效率=`1.3017639241%`，前向=`1.3018445477%`，后向=`0.0000806236%`；TM前向=`1.2868923449%`，TE前向=`0.0146550065%`；mode1前向=`0.8719638507%`，占前向导模=`66.97910686%`。相对0.75um净效率下降`0.48457%`，低于1%停止门槛且绝对值更低，故标称宽度确定为0.75um；停止峰值细化，转入±20nm制造容差，只需补0.77um端点。详细记录：`D:/Codex/Kai/STAGE238_239_WIDTH0P73UM_PEAK_CHECK_2026-10-12.md`。
- Stage240a/b状态（2026-10-12）：0.77um（标称+20nm）容差端点设置已通过，半宽0.385um、`wz=0.65um`，边缘场幅`70.4105%`、边缘强度`49.5763%`；设置脚本0次`run;`、正式脚本恰好1次`run;`且无Stage238/239残留。按用户反馈不再新增可见窗口。Stage240b后台仿真已启动，隐藏Python PID 33288，确认6个`fdtd-engine-msmpi`、运行FSP已生成且stderr为空。
- Stage227→228后续链已离线生成并校验：Stage227c匹配无齿脚本为`D:/Codex/Kai/stage227c_run_elliptical_gaussian_wz0p65_reference_zdomain2p8.lsf`；Stage228a/b/c分别为相干场分解、固定32模基底和导模投影，三个分析脚本均确认不含`run;`、无Stage225/226残留且关键路径与`zdomain2p8um`一致。自动接力为`D:/Codex/Kai/stage227_228_postprocess.py`，会在Stage227b/c完成后校验数值闭合并生成`D:/Codex/Kai/stage227_228_pipeline_results.json`及0.45/0.55/0.65um三点趋势判定；结果缺失时已验证会安全拒绝执行。
- 本检查点：`D:/Codex/Kai/LUMERICAL_CHECKPOINT_STAGE175B_2026-09-29.md`
## 2026-10-12 Stage240/241：宽度 +20 nm 容差端点完成

- Stage240b（grating width=0.77 um）正式 FDTD 已完成，FSP 175.44 MB，stdout=`SCRIPT_COMPLETED`，stderr 为空。
- Stage241a/b/c 后处理均完成；净导模效率=1.2734061518%，mode1=0.8667777004%，mode1 占比=68.06370526%。
- 与名义 0.75 um 相比，净导模效率下降 2.6525%；与 -20 nm 的 0.73 um 结果合并判断，±20 nm 两端均满足相对下降不超过 5% 的工程门槛。
- 结论：0.75 um 作为名义宽度，±20 nm 制造容差通过；停止继续加密宽度扫描，下一步转向新的工程变量。
- 详细报告：`D:/Codex/Kai/STAGE240_241_WIDTH_TOLERANCE_PLUS20NM_2026-10-12.md`

## 2026-10-12 Stage242/243：齿高制造容差启动

- 宽度变量已冻结为名义 0.75 um，下一工程变量为齿高制造误差。
- Stage242a 建立 -10 nm 端点：齿高 300 nm；齿底 -3.75 nm、齿宽 185 nm、顶面横移 -240 nm、z宽度 0.75 um保持不变。
- 24个多边形一致性审计通过：enabled=24，最大顶点误差 `3.84e-22 m`，y位置与z span误差均为0。
- Stage242b 正式仿真已在隐藏会话启动，Python PID 7568；确认6个 `fdtd-engine-msmpi` 正在运行，stderr为空，没有新增可见FDTD窗口。
- 运行模型：`D:/FDTD_File/ar_incoupler_FDTD_stage242b_HEIGHT300nm_WIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_RUNNING_638nm.fsp`
- 完成后执行Stage243a/b/c相干扣背景和固定32模投影，再与310 nm名义结果比较；之后只补+10 nm的320 nm端点。
- 自动接力脚本已启动（PID 22616）：等待Stage242b自然完成并严格检查FSP、`SCRIPT_COMPLETED`和空stderr；随后依次执行Stage243a/b/c、Stage244a设置与24对象审计、Stage244b 320nm长仿真、Stage245a/b/c，任一步失败立即停止。脚本：`D:/Codex/Kai/stage242_245_height_tolerance_pipeline.py`；状态：`D:/Codex/Kai/stage242_245_pipeline_status.log`；最终机器结果：`D:/Codex/Kai/stage242_245_height_tolerance_results.json`。
- Stage246下一工程变量门槛已建立：齿高验证完成且名义几何确认后，验证`top shift=-240±10 nm`；若端点相对净导模效率和mode1下降均不超过5%，冻结该变量，否则先回二维/RCWA筛选稳健中心。计划：`D:/Codex/Kai/STAGE246_NEXT_ENGINEERING_VARIABLE_GATE_2026-10-12.md`。
- Stage242b（300 nm）于2026-10-12 19:19自然完成：完整FSP 175.41 MB、直接功率LDF存在、stdout=`SCRIPT_COMPLETED`、stderr为空。Stage243a相干分解有效，源功率比1、网格差0、重构误差0、纯散射直接净值2.1953568%。
- 自动接力首次执行Stage243b时发现机械生成的输入路径重复为`HEIGHT300nm_HEIGHT300NM`；该会话未生成b/c结果，因此不采信其`SCRIPT_COMPLETED`。已修复Stage243b及生成器，待当前320 nm长仿真完成后补跑Stage243b/c，不重跑300 nm FDTD。
- 同类静态审计发现Stage245b路径存在`HEIGHT320nm_HEIGHT320NM`重复，已在执行前修复；Stage245尚未运行。
- Stage244a 320 nm设置及24对象一致性审计已通过，Stage244b长仿真于19:19:42自动启动，确认6个engine正常；当前不得并行补跑Stage243b/c。
- 安全收尾器已启动（PID 29192）：仅等待原接力PID 22616退出；确认Stage245c结果存在且engine为0后，补跑已修复的Stage243b/c并生成最终300/310/320nm对比JSON。若Stage245链不完整则停止，不会猜测或重跑FDTD。脚本：`D:/Codex/Kai/stage242_245_height_tolerance_finalizer.py`；状态：`D:/Codex/Kai/stage242_245_finalizer_status.log`。
- Stage244b于20:57:20自然完成，Stage245a/b/c随后完成；原接力按设计在缺失旧Stage243c时停止，安全收尾器成功补跑修复后的Stage243b/c并于20:58:17生成最终JSON。所有engine和两个后台进程均已退出。
- 齿高三点最终结果：300/310/320 nm净导模效率=`2.19538694% / 1.30810260% / 0.62007297%`；mode1=`1.49322779% / 0.88541502% / 0.41661068%`。300 nm相对310 nm净效率`+67.8299%`，320 nm`-52.5975%`；±10 nm容差失败。
- 数值闭合有效：两端源功率比1，32模式/28导模，a/b线性误差约1e-17，未展开残差绝对值<0.0005%。差异为物理趋势而非读取伪差。
- 结论：310 nm不是当前三维有限光束模型的稳健齿高；暂停Stage246 top-shift容差，下一步只验证290 nm。若290 nm继续上升，再逐步向280 nm寻找峰值，直到出现下降或相邻提升<1%。详细报告：`D:/Codex/Kai/STAGE242_245_HEIGHT_TOLERANCE_VALIDATION_2026-10-12.md`。
- Stage247a 290 nm设置与24对象审计通过：齿高290 nm、齿底-3.75 nm、齿顶286.25 nm、齿宽185 nm、top shift -240 nm、z宽0.75 um；enabled=24，最大顶点误差`3.84e-22 m`，y与z span误差0。
- Stage247b 290 nm正式FDTD已在隐藏会话启动（PID 12752），确认6个engine、运行FSP存在、stderr为空；Stage248自动后处理接力PID 23724正在等待。脚本：`D:/Codex/Kai/stage247_248_height290nm_pipeline.py`，状态：`D:/Codex/Kai/stage247_248_pipeline_status.log`。没有新增可见FDTD窗口。
- Stage247b于22:39:27自然完成，Stage248a/b/c于22:39:56全部完成；所有engine与接力进程均退出，stderr为空。
- 290 nm最终结果：净导模效率`3.10842214%`、正向`3.10860189%`、反向`0.00017975%`；TM`3.09170268%`、TE`0.01659218%`；mode1`2.12087863%`、占比`68.22612561%`。
- 相对300 nm，290 nm净效率提高`41.5888%`，mode1提高`42.0332%`。源功率比1，32模式/28导模，a/b线性误差约1e-16/1e-17，未展开残差`-0.0003661%`，结果有效。
- 结论：290/300/310/320 nm仍呈显著单调趋势，峰值未包住；下一点只验证280 nm。当前连续工作已接近5小时上限，不再启动下一次约100分钟长仿真，待后续额度恢复继续。详细报告：`D:/Codex/Kai/STAGE247_248_HEIGHT290NM_VALIDATION_2026-10-12.md`。
- 下一轮Stage249/250的280 nm设置、运行、相干分解和固定32模投影脚本已离线生成并完成静态审计：设置/分析脚本run次数分别为0/1/0，旧290 nm与Stage247/248可执行引用均为0，所有输入输出路径一致。尚未执行Stage249a，也未启动FDTD；额度恢复后先运行设置和24对象审计，再启动Stage249b。

## 2026-10-13 Stage249/250：280 nm 齿高验证完成

- Stage249a 几何与对象审计通过：齿高280 nm、齿底-3.75 nm、齿顶276.25 nm、齿宽185 nm、top shift -240 nm、z宽0.75 um；24对象启用，最大顶点误差`3.84e-22 m`，y与z span误差0。
- Stage249b 于2026-10-13 00:22自然完成，完整FSP 183,931,288 bytes，stdout=`SCRIPT_COMPLETED`、stderr为空；Stage250a/b/c随后全部完成，流水线状态为`PIPELINE_COMPLETED`。
- 280 nm最终结果：净导模效率`4.0189989512%`、前向`4.0192351467%`、后向`0.0002361955%`；TM`4.0015263259%`、TE`0.0174103014%`；mode1`2.7438237735%`、占前向导模`68.26731140%`。
- 相对290 nm，净导模效率提高`29.2939%`，mode1提高`29.3720%`；mode1占比基本不变，提升来自整体耦合增强。
- 数值闭合有效：源功率比1，32模式/28导模，a/b线性误差`2.78e-17/9.46e-17`，未展开残差`-0.0001921%`。
- 280/290/300/310/320 nm净效率为`4.018999/3.108422/2.195387/1.308103/0.620073%`，仍呈单调趋势，峰值未包住；下一步只验证270 nm。
- 按用户要求，从下一轮开始改为单个可见Lumerical窗口展示参数修改、几何校验、运行与结果读取；后台脚本仅复核和存档，不再隐藏完成全部优化过程。
- 详细报告：`D:/Codex/Kai/STAGE249_250_HEIGHT280NM_VALIDATION_2026-10-13.md`；机器结果：`D:/Codex/Kai/stage249_250_height280nm_results.json`。

## 2026-10-13 Stage251/252：270 nm 齿高验证完成

- Stage251a 在单个可见 Lumerical 窗口中完成参数修改与几何审计：齿高270 nm、齿底-3.75 nm、齿顶266.25 nm、齿宽185 nm、top shift -240 nm、z宽0.75 um。
- Stage251b 正式FDTD在该可见窗口自然完成，完整FSP为 D:/FDTD_File/ar_incoupler_FDTD_stage251b_HEIGHT270nm_WIDTH0p75um_wx6um_wz0p65um_zdomain2p8um_PATTERNED_COMPLETE_638nm.fsp，大小183,932,443 bytes。
- Stage252a/b/c在同一可见窗口用 feval() 依次执行；最初误用 run(path) 被Lumerical识别为求解器类型并立即报错，未改变结果，随后改正并成功。
- 270 nm净导模效率=4.8594986977%、前向=4.8597874241%、后向=0.0002887263%；TM=4.8418572402%、TE=0.0176588170%；mode1=3.3085464129%、占前向导模=68.08006450%。
- 相对280 nm，净效率提高20.9132%，mode1提高20.5816%；270/280/290/300/310/320 nm仍为单调趋势，峰值未包住。
- 数值闭合通过：源功率比1、网格差0、相干重构误差约1.42e-16、32模式/28导模、a/b线性误差6.21e-17/2.48e-17、未展开残差0.0002644%。
- 下一步只验证260 nm；在包住齿高峰值前不同时改变其它几何变量。
- 详细报告：D:/Codex/Kai/STAGE251_252_HEIGHT270NM_VALIDATION_2026-10-13.md；机器结果：D:/Codex/Kai/stage251_252_height270nm_results.json。

## 2026-10-13 Stage253/254：260 nm 齿高验证完成

- Stage253a 在同一个可见Lumerical窗口完成设置和审计：齿高260 nm、齿底-3.75 nm、齿顶256.25 nm、中心y=126.25 nm、齿宽185 nm、top shift -240 nm、z宽0.75 um。
- Stage253b 在可见窗口自然完成，完整FSP大小183,932,395 bytes；Stage254a/b/c随后均在同一窗口用feval()执行成功。
- 260 nm净导模效率=5.5641750063%、前向=5.5645015036%、后向=0.0003264972%；TM=5.5468628999%、TE=0.0173936065%；mode1=3.7704501273%、占前向导模=67.75899198%。
- 相对270 nm，净效率提高14.5010%，mode1提高13.9609%；增益较上一段缩小，但峰值仍未包住。
- 数值闭合通过：源功率比1、网格差0、相干重构误差约1.21e-16、32模式/28导模、a/b线性误差1.14e-16/5.69e-17、未展开残差0.0005379%。
- 下一步只验证250 nm；若下降则由250/260/270 nm包住峰值，若继续上升再验证240 nm。
- 详细报告：D:/Codex/Kai/STAGE253_254_HEIGHT260NM_VALIDATION_2026-10-13.md；机器结果：D:/Codex/Kai/stage253_254_height260nm_results.json。

## 2026-10-13 Stage255/256：250 nm 齿高验证完成

- Stage255a在同一可见窗口完成设置与审计：齿高250 nm、齿底-3.75 nm、齿顶246.25 nm、中心y=121.25 nm、齿宽185 nm、top shift -240 nm、z宽0.75 um。
- Stage255b自然完成，完整FSP大小183,932,395 bytes；Stage256a/b/c在同一可见窗口用feval()完成。
- 250 nm净导模效率=6.0539778363%、前向=6.0543228804%、后向=0.0003450442%；TM=6.0376705385%、TE=0.0164237692%；mode1=4.0851440842%、占前向导模=67.47483021%。
- 相对260 nm，净效率提高8.8028%，mode1提高8.3463%。增益继续收窄，但峰值尚未包住。
- 数值闭合通过：源功率比1、网格差0、重构误差2.20e-16、32模式/28导模、a/b误差1.96e-17/1.01e-16、未展开残差0.0004424%。
- 下一步只验证240 nm。
- 详细报告：D:/Codex/Kai/STAGE255_256_HEIGHT250NM_VALIDATION_2026-10-13.md；机器结果：D:/Codex/Kai/stage255_256_height250nm_results.json。

## 2026-10-13 Stage257/258：240 nm 齿高验证完成

- Stage257a在同一可见窗口完成设置与审计：齿高240 nm、齿底-3.75 nm、齿顶236.25 nm、中心y=116.25 nm、齿宽185 nm、top shift -240 nm、z宽0.75 um。
- Stage257b自然完成，完整FSP大小183,932,443 bytes；Stage258a/b/c在同一可见窗口用feval()完成。
- 240 nm净导模效率=6.2782981894%、前向=6.2786483101%、后向=0.0003501207%；TM=6.2636162642%、TE=0.0148148757%；mode1=4.2219370583%、占前向导模=67.24277026%。
- 相对250 nm，净效率提高3.7053%，mode1提高3.3485%；增益已连续收窄，但峰值仍未包住。
- 数值闭合通过：源功率比1、网格差0、重构误差0、32模式/28导模、a/b误差5.55e-17/6.63e-17、未展开残差0.0003800%。
- 下一步只验证230 nm；若下降，则以230/240/250 nm包住峰值并局部细化。
- 详细报告：D:/Codex/Kai/STAGE257_258_HEIGHT240NM_VALIDATION_2026-10-13.md；机器结果：D:/Codex/Kai/stage257_258_height240nm_results.json。

## 2026-10-13 Stage259/260：230 nm 齿高验证完成并包住峰值

- Stage259b 在同一可见 Lumerical 窗口自然完成，完整 FSP 大小 183,932,443 bytes；Stage260a/b/c 随后在该窗口用 `feval()` 完成。
- 230 nm 净导模效率=6.2143615914%、前向=6.2147086915%、后向=0.0003471001%；TM=6.2018279539%、TE=0.0126822480%；mode1=4.1598885634%、占前向导模=66.93617947%。
- 相对 240 nm，净效率下降约1.0184%，mode1下降约1.4697%；230/240/250 nm 已包住局部峰值。
- 三点二次拟合给出候选峰值齿高约237.22 nm、预测净效率约6.28945%；下一步只验证237 nm，不能把拟合值直接当最终结果。
- 数值闭合通过：源功率比1、网格差0、重构误差2.12e-16、32模式/28导模、a/b误差低于8.10e-17、未展开残差0.0005976%。
- 详细报告：D:/Codex/Kai/STAGE259_260_HEIGHT230NM_VALIDATION_2026-10-13.md；机器结果：D:/Codex/Kai/stage259_260_height230nm_results.json。

## 2026-10-13 Stage261/262：237 nm 局部峰值验证完成

- Stage261a 几何审计通过：237 nm 齿高、185 nm 齿宽、-240 nm top shift、0.75 um z宽，24个齿/外框对象全部启用且顶点、y、z span误差均为0。
- Stage261b 在同一可见Lumerical窗口自然完成，完整FSP大小183,932,395 bytes；Stage262a/b/c随后在该窗口用`feval()`完成。
- 237 nm净导模效率=6.2873608038%、前向=6.2877105730%、后向=0.0003497692%；TM=6.2734282494%、TE=0.0140743380%；mode1=4.2232571516%、占前向导模=67.16685036%。
- 相对240 nm，净效率提高0.14435%（绝对+0.009063个百分点），mode1提高0.03127%。
- 230/237/240 nm已包住峰值；细化拟合顶点237.38 nm、预测6.28755%，与237 nm实测差仅约0.000191个百分点，因此齿高一维优化停止于237 nm。
- 数值闭合通过：源功率比1、网格差0、重构误差约2.10e-16、32模式/28导模、a/b误差低于3.11e-17、未展开残差0.0004216%。
- 下一步固定237 nm，进行局部三点齿宽/占空比交互复核。
- 详细报告：D:/Codex/Kai/STAGE261_262_HEIGHT237NM_VALIDATION_2026-10-13.md；机器结果：D:/Codex/Kai/stage261_262_height237nm_results.json。

## 2026-10-14 Stage263/264：237 nm 齿高下的180 nm齿宽交互复核

- 几何审计通过：齿高237 nm、齿宽180 nm、top shift -240 nm、z宽0.75 um；24对象启用且顶点/y/z span误差为0。
- 净导模效率=6.2433237869%，mode1=4.2170720537%，mode1占比=67.54160185%。
- 相对185 nm齿宽基准，净效率下降0.70041%（绝对-0.044037个百分点），mode1下降0.14645%，但mode1占比提高0.37475个百分点。
- 数值闭合通过：源功率比1、网格差0、重构误差2.11e-16、32模式/28导模、a/b误差约1.14e-16/2.67e-17、未展开残差0.0002148%。
- 下一步只验证190 nm齿宽；若也低于185 nm，齿宽局部峰值完成包络。
- 详细报告：D:/Codex/Kai/STAGE263_264_HEIGHT237NM_TOOTH180NM_INTERACTION_2026-10-14.md；机器结果：D:/Codex/Kai/stage263_264_height237nm_tooth180nm_results.json。

## 2026-10-14 Stage265/266：237 nm 齿高下的190 nm齿宽交互验证完成

- 几何审计通过：齿高237 nm、齿宽190 nm、top shift -240 nm、z宽0.75 um；24对象启用且顶点/y/z span误差为0。
- 净导模效率=6.2999806868%，正向/反向=6.3003373492%/0.0003566623%；TM/TE正向=6.2857295019%/0.0143940220%；mode1=4.2069526344%，占正向导模66.77345039%。
- 数值闭合通过：源功率比1、网格差0、相干重构误差4.20e-16、32模式/28导模、a/b线性误差1.11e-16/9.05e-17、未展开残差0.0006253%。
- 180/185/190 nm总净导模效率依次为6.243324%/6.287361%/6.299981%；三点二次拟合顶点为189.508 nm、预测6.300133%。相对190 nm的理论余量只有0.000152个百分点，因此停止亚纳米细化并冻结齿宽190 nm。
- mode1在185 nm略高于190 nm，但190 nm总净导模效率更高；本阶段工程主目标继续采用全部导模净功率，mode1占比作为独立质量指标保留。
- 下一步固定237 nm齿高与190 nm齿宽，只验证top shift=-250/-240/-230 nm局部交互和制造容差。
- 详细报告：D:/Codex/Kai/STAGE265_266_HEIGHT237NM_TOOTH190NM_INTERACTION_2026-10-14.md；机器结果：D:/Codex/Kai/stage265_266_height237nm_tooth190nm_results.json。

## 2026-10-14 Stage267/268：top shift -250 nm 端点验证进行中

- Stage267a 已在单个可见Lumerical窗口完成设置与审计：齿高237 nm、齿宽190 nm、top shift -250 nm、齿底-3.75 nm、z宽0.75 um；24对象启用，顶点/y/z span最大误差均为0，`audit_pass=1`。
- Stage267b 已于2026-10-14 17:47在该可见窗口启动；6个`fdtd-engine-msmpi`进程均在运行，运行中FSP已生成。仿真完成前不切换Layout、不输入分析脚本、不终止求解。
- 完成后依次执行Stage268a/b/c：相干无齿背景扣除、固定32模基底、纯散射场投影；再与-240 nm名义点比较。只有数值闭合通过后才判断±10 nm容差。
- `-230 nm`另一端点的Stage269/270设置、运行和分析脚本已离线生成并完成静态审计：run命令数为0/1/0/0/0，旧`-250 nm`与Stage267/268引用均为0，输入输出路径一致；在Stage267/268结果有效前不提前启动。

## 2026-10-14 Stage267/268：top shift -250 nm 验证完成

- Stage267b 于19:16自然完成；Stage268a/b/c随后在同一个可见Lumerical窗口执行成功，三个LDF结果均已生成。
- -250 nm净导模效率=6.3532603392%，正向/反向=6.3536209112%/0.0003605720%；TM/TE正向=6.3384858647%/0.0149148706%；mode1=4.2344995398%，占正向导模66.64702851%。
- 相对-240 nm，净导模效率提高0.0532796524个百分点（相对+0.84571%），mode1提高0.0275469054个百分点（相对+0.65480%）；mode1占比下降0.12642个百分点。
- 数值闭合通过：源功率比1、网格差0、相干重构误差2.09e-16、32模式/28导模、a/b线性误差4.16e-17/4.82e-17、未展开残差0.0004803个百分点。
- 因-250 nm优于-240 nm，峰值尚未包住。下一步固定其它参数，只验证top shift=-260 nm；原先准备的-230 nm脚本暂不运行。
- 详细报告：D:/Codex/Kai/STAGE267_268_TOPSHIFT_M250NM_VALIDATION_2026-10-14.md；机器结果：D:/Codex/Kai/stage267_268_topshiftm250nm_results.json。

## 2026-10-14 Stage271/272：top shift -260 nm 验证进行中

- Stage271/272五个脚本由已验证的Stage267/268流水线机械派生并完成静态审计：run命令数为0/1/0/0/0，旧Stage267/268及-250 nm引用均为0，输入输出路径一致。
- Stage271a在同一可见Lumerical窗口执行；几何审计通过：top shift=-260 nm、齿高237 nm、齿宽190 nm、齿底-3.75 nm、z宽0.75 um，24对象启用，顶点/y/z span误差均为0。
- Stage271b于19:21启动；6个`fdtd-engine-msmpi`进程已确认运行，运行中FSP已生成。按上一轮约89分钟耗时估算，接近20:50再检查，不做分钟级轮询。
- 完成后依次执行Stage272a/b/c并与-250/-240 nm比较；若-260 nm下降则三点包峰，若继续上升则再沿负方向单变量扩展。
- 等待期间已离线准备Stage273/274的-270 nm备用流水线并完成静态审计：run命令数0/1/0/0/0，旧Stage271/272和-260 nm引用均为0；只有-260 nm继续提升时才执行，否则保留不用。
- 新增`D:/Codex/Kai/analyze_top_shift_scan.py`：从三份结果JSON自动兼容读取top shift、净导模效率和mode1；只有中点确实为局部最大值才做凹二次拟合，否则按单调方向推荐下一个点。脚本已通过语法检查和合成包峰算例。

## 2026-10-14 Stage271/272：top shift -260 nm 验证完成

- Stage271b于20:51自然完成；Stage272a/b/c随后在同一可见Lumerical窗口执行成功。
- -260 nm净导模效率=6.4004633991%，正向/反向=6.4008277657%/0.0003643665%；TM/TE正向=6.3852249103%/0.0153776010%；mode1=4.2572617830%，占正向导模66.51111292%。
- 相对-250 nm，净导模效率绝对提高0.04720306个百分点、相对提高0.74297%；mode1相对提高0.53754%。
- 数值闭合通过：源功率比1、网格差0、重构误差0、32模式/28导模、a/b线性误差7.85e-17/5.21e-17、未展开残差0.0003295个百分点。
- -240/-250/-260 nm仍沿更负方向单调提升，峰值未包住；下一步只验证-270 nm，使用已审计的Stage273/274脚本。
- 详细报告：D:/Codex/Kai/STAGE271_272_TOPSHIFT_M260NM_VALIDATION_2026-10-14.md；机器结果：D:/Codex/Kai/stage271_272_topshiftm260nm_results.json。

## 2026-10-14 Stage273/274：top shift -270 nm 验证进行中

- 自动三点工具读取-260/-250/-240 nm结果，确认未包峰并给出下一点-270 nm；判断文件：D:/Codex/Kai/top_shift_scan_m260_m250_m240_analysis.json。
- Stage273a几何审计通过：top shift=-270 nm、齿高237 nm、齿宽190 nm、齿底-3.75 nm、z宽0.75 um；24对象启用，顶点/y/z span误差均为0。
- Stage273b于21:06在同一可见Lumerical窗口启动；6个`fdtd-engine-msmpi`进程已确认运行，运行中FSP已生成。
- 按最近两轮约89–90分钟耗时，下一次约22:36只检查完整文件；期间不轮询FDTD。

## 2026-10-14 Stage273/274：top shift -270 nm 验证完成

- Stage273b于22:42自然完成；Stage274a/b/c随后在同一可见Lumerical窗口执行成功。
- -270 nm净导模效率=6.4366149072%，正向/反向=6.4369826263%/0.0003677191%；TM/TE正向=6.4210574104%/0.0156970387%；mode1=4.2720749952%，占正向导模66.36766391%。
- 相对-260 nm，净导模效率绝对提高0.03615151个百分点、相对提高0.56483%；mode1相对提高0.34795%。
- 数值闭合通过：源功率比1、网格差0、重构误差2.06e-16、32模式/28导模、a/b线性误差1.12e-16/8.86e-17、未展开残差0.0001846个百分点。
- -250/-260/-270 nm仍沿更负方向单调提升，增益继续收窄但峰值未包住；下一步只验证-280 nm。
- 详细报告：D:/Codex/Kai/STAGE273_274_TOPSHIFT_M270NM_VALIDATION_2026-10-14.md；机器结果：D:/Codex/Kai/stage273_274_topshiftm270nm_results.json。

## 2026-10-14 Stage275/276：top shift -280 nm 验证进行中

- Stage275/276五个脚本由已验证的-270 nm流水线机械派生并通过静态审计：run命令数0/1/0/0/0，旧Stage273/274和-270 nm引用均为0。
- Stage275a几何审计通过：top shift=-280 nm、齿高237 nm、齿宽190 nm、齿底-3.75 nm、z宽0.75 um；24对象启用，顶点/y/z span误差均为0。
- Stage275b于22:59在同一可见Lumerical窗口启动；6个`fdtd-engine-msmpi`进程确认运行，运行中FSP已生成。
- 按上一轮约96分钟耗时，下一次约2026-10-15 00:35只检查完整文件；期间不轮询FDTD。

## 2026-10-15 Stage275/276：top shift -280 nm 验证完成

- Stage275b于00:27自然完成；Stage276a/b/c随后在同一可见Lumerical窗口执行成功。
- -280 nm净导模效率=6.4639388644%，正向/反向=6.4643096181%/0.0003707537%；TM/TE正向=6.4481976770%/0.0158828699%；mode1=4.2806408796%，占正向导模66.21961404%。
- 相对-270 nm，净导模效率绝对提高0.02732396个百分点、相对提高0.42451%；mode1相对提高0.20051%。
- 数值闭合通过：源功率比1、网格差0、重构误差0、32模式/28导模、a/b线性误差7.85e-17/5.85e-17、未展开残差0.0000341个百分点。
- -260/-270/-280 nm仍单调，增益连续收窄但峰值未包住；继续该变量时下一点为-290 nm。
- 详细报告：D:/Codex/Kai/STAGE275_276_TOPSHIFT_M280NM_VALIDATION_2026-10-15.md；机器结果：D:/Codex/Kai/stage275_276_topshiftm280nm_results.json。

## 2026-10-15 Stage277/278：top shift -290 nm 验证进行中

- Stage277/278五个脚本由-280 nm验证流水线机械派生并通过静态审计：run命令数0/1/0/0/0，旧Stage275/276和-280 nm引用均为0。
- Stage277a几何审计通过：top shift=-290 nm、齿高237 nm、齿宽190 nm、齿底-3.75 nm、z宽0.75 um；24对象启用，顶点/y/z span误差均为0。
- Stage277b于00:38在同一可见Lumerical窗口启动；6个`fdtd-engine-msmpi`进程确认运行。
- 按上一轮约88分钟和近期最慢约96分钟估算，下一次约02:14只检查完整文件；期间不轮询FDTD。

## 2026-10-15 Stage277/278：top shift -290 nm 验证完成

- Stage277b于02:06自然完成；Stage278a/b/c随后执行成功。
- -290 nm净导模效率=6.4770148869%，mode1=4.2794201360%，mode1占比66.06706555%；数值闭合通过。
- 相对-280 nm，总净导模相对提高0.20229%，但mode1相对下降0.02852%，两个目标开始分化。
- 总净导模主目标尚未反转；再验证-300 nm作为最后一个外扩点，随后分别给出总功率最优与mode1最优。
- 详细报告：D:/Codex/Kai/STAGE277_278_TOPSHIFT_M290NM_VALIDATION_2026-10-15.md；机器结果：D:/Codex/Kai/stage277_278_topshiftm290nm_results.json。

## 2026-10-15 Stage279/280：top shift -300 nm 最后外扩点进行中

- Stage279/280脚本由-290 nm验证流水线机械派生并通过静态审计：run命令数0/1/0/0/0，旧Stage277/278和-290 nm引用均为0。
- Stage279a几何审计通过：top shift=-300 nm、齿高237 nm、齿宽190 nm、齿底-3.75 nm、z宽0.75 um；24对象启用且误差为0。
- Stage279b于02:16启动；6个`fdtd-engine-msmpi`进程确认运行。
- 此点作为最后一个外扩点：完成后分别判断总净导模最优与mode1最优，不再因微小单调增益无限外推。
- 下一次约03:53只检查完整文件；期间不轮询FDTD。

## 2026-10-15 Stage279/280：top shift局部优化完成并停止

- Stage279b于03:44自然完成；Stage280a/b/c随后执行成功。
- -300 nm净导模效率=6.4738071244%，mode1=4.2672863300%；数值闭合通过。
- 相对-290 nm，总净导模下降0.04953%，mode1下降0.28354%；因此-280/-290/-300 nm包住总净导模峰值，-270/-280/-290 nm包住mode1峰值。
- 三点拟合：总净导模顶点约-293.03 nm、预测6.477762%；mode1顶点约-283.75 nm、预测4.281330%。两者相对最近10 nm工程点的理论增益仅约0.0115%和0.0161%，低于继续细化价值。
- 主目标全部导模净功率选择-290 nm（6.477015%）；若优先mode1则选择-280 nm（4.280641%）。top shift一维优化停止，不再向更负方向外扩。
- 详细报告：D:/Codex/Kai/STAGE279_280_TOPSHIFT_M300NM_AND_FINAL_DECISION_2026-10-15.md；机器结果：D:/Codex/Kai/stage279_280_topshiftm300nm_results.json。

## 2026-10-15 Stage267–280：top shift制造容差结论

- 完整-240至-300 nm扫描已汇总。主目标标称top shift=-290 nm；±10 nm端点的总净导模最差下降约0.202%，mode1最差下降约0.284%，均通过5%制造容差门槛。
- 当前可见Lumerical窗口已恢复到-290 nm完整FSP，窗口标题和模型文件已目视确认。
- 汇总：D:/Codex/Kai/STAGE267_280_TOPSHIFT_OPTIMIZATION_AND_TOLERANCE_SUMMARY_2026-10-15.md。
- 下一阶段不再优化几何：固定最终几何，按Stage229照明门槛补做wz=0.55 um名义点和0.45 um端点；0.65 um当前结果作为另一端点。

## 2026-10-15 Stage281/282：最终几何的wz=0.55 um名义照明验证进行中

- 静态审计发现旧Stage225c无齿参考使用较窄z域/监视器，不能与当前zdomain=2.8 um模型严格匹配；已放弃直接复用，改为Stage281b有齿与Stage281c无齿在同一Stage281a设置下各运行一次。
- Stage281a从Stage198二维场重建wz=0.55 um导入源，并加载-290 nm最终几何；入射功率6.8075573954e-15 W，与历史wz=0.55逐位一致，数据边缘场幅1.8316%。
- Stage281b于03:59启动，6个`fdtd-engine-msmpi`进程确认运行；完成后才执行Stage281c匹配无齿参考，之后执行Stage282a/b/c。
- Stage281/282六个脚本已完成静态路径审计，run命令数0/1/1/0/0/0；已修正生成过程中发现的旧Stage227路径和`TS278a`残留，当前无旧可执行引用。
- Stage281b有齿模型于05:27自然完成；Stage281c严格匹配无齿参考于05:36启动，6个engine确认运行。下一次约07:13只检查完整参考文件；参考完成前不执行Stage282。

## 2026-10-15 Stage281/282：最终几何的wz=0.55 um名义照明验证完成

- Stage281c严格匹配参考于07:03自然完成；Stage282a/b/c随后全部成功。
- wz=0.55 um净导模效率=7.1033243043%，mode1=4.6956345991%，mode1占比66.10091538%；数值闭合全部通过。
- 相对wz=0.65 um，归一化净效率提高9.6697%，mode1效率提高9.7260%；但绝对净导模功率从5.21095e-16 W降至4.83563e-16 W，即下降7.2026%。
- 结论：效率与绝对功率对束腰的排序不同。暂保留Stage229的wz=0.55 um名义点；下一步只补最终几何的wz=0.45 um有齿/严格匹配无齿参考，完成三点照明门槛。
- 详细报告：D:/Codex/Kai/STAGE281_282_FINAL_GEOMETRY_WZ0P55_VALIDATION_2026-10-15.md；机器结果：D:/Codex/Kai/stage281_282_final_geometry_wz0p55_results.json。

## 2026-10-15 Stage283/284：最终几何三点照明门控完成

- Stage283b `wz=0.45 um` patterned模型于19:00自然完成；Stage283c严格匹配无齿参考于20:34自然完成，随后Stage284a/b/c相干场分解与固定32模投影成功。
- `wz=0.45 um`净导模效率=`7.6843735229%`，正向/反向=`7.6848214507% / 0.0004479278%`；TM/TE正向=`7.6628358095% / 0.0216831770%`；mode1=`5.0869913475%`，占正向导模=`66.19530955%`。
- 数值闭合全部通过：patterned/reference源功率一致，y/z网格误差0，重构相对误差`1.236e-16`，32模式/28导模，a/b线性误差`6.206e-17 / 7.068e-17`，未展开散射净残差仅`0.0002647136`个百分点。
- 最终三点净导模效率：`wz=0.45/0.55/0.65 um`分别为`7.6843735% / 7.1033243% / 6.4770149%`；名义点为0.55 um，最差端点为0.65 um。
- 两端相对名义点变化为`+8.1800% / -8.8171%`，三点相对跨度`16.9971%`，未通过临时2%照明敏感性门槛。
- 绝对净导模功率则随wz增大：`4.28033e-16 / 4.83563e-16 / 5.21095e-16 W`。mode1占比三点仅在`66.07%–66.20%`间变化，说明主要变化来自有限光束与有限光栅的空间重叠及归一化，而不是目标模式身份突变。
- 工程结论：结果数值有效，但当前几何不能称为通过照明鲁棒性的最终工程设计。继续固定0.55 um为比较名义点、0.45/0.65 um为端点，不优化wz本身；后续候选必须按名义效率、最差端效率和三点跨度排序。
- 自动接力首次因用户全屏视频触发Windows前台锁而未能将命令输入FDTD；patterned结果未丢失。已改用Alt激活+`AppActivate`并增加断点续跑，Stage283c及后处理均成功完成；原失败标记已归档保留。
- FDTD可见窗口已恢复到`wz=0.55 um`名义patterned完整模型，标题与恢复标记均验证。
- 详细报告：`D:/Codex/Kai/STAGE283_284_FINAL_GEOMETRY_WZ0P45_AND_THREE_POINT_ILLUMINATION_GATE_2026-10-15.md`；机器结果：`D:/Codex/Kai/stage283_284_final_geometry_wz0p45_three_point_results.json`。

## 2026-10-15 Stage285/286：1.50 um横向宽度候选名义筛选完成

- 基于0.75 um基线三点结果，净效率除以解析高斯覆盖率仅在`0.08496–0.08620`间变化，证明约17%的照明跨度主要由有限横向覆盖导致。
- 解析模型`erf[sqrt(2)*(W/2)/wz]`估计横向宽度约`1.409 um`才可能把两个端点相对名义点的变化压到2%；因此选择工程值`1.50 um`，先只验证`wz=0.55 um`名义点。
- Stage285a审计通过：宽度1.50 um、24个对象启用、中心与z span误差均为0；名义光束解析覆盖率99.3614%，光栅边缘场/强度为15.5750%/2.4258%。
- Stage285b于20:44启动、22:31自然完成；Stage286a/b/c后处理于23:05完成。
- 数值闭合有效：源功率比1、网格误差0、相干重构误差0、32模式/28导模、a/b线性误差`1.11e-16/3.78e-17`。未展开残差为`2.8214e-5`，仅占直接散射的约0.0365%，通过“绝对≤1e-4且相对≤0.1%”门槛。
- 1.50 um候选名义净导模效率=`7.7185615450%`，相对0.75 um基线`7.1033243043%`提高`8.6613%`；mode1=`6.2019714635%`，相对基线提高`32.0795%`；mode1占比从`66.1009%`提高到`80.3467%`；绝对净导模功率=`5.25446e-16 W`。
- 候选通过预先规定的90%名义性能保留门槛，不仅没有牺牲名义效率，反而同时提高总导模和mode1。因此下一步只补`wz=0.45/0.65 um`两个端点，验证解析模型预期的照明鲁棒性，不再扫描其它宽度。
- 自动后处理再次受用户浏览器前台竞争影响，命令未进入FDTD；主仿真结果未丢失。已手动激活同一窗口完成后处理，失败标记归档，完成标记与恢复标记均已生成。
- FDTD可见窗口已恢复到Stage285b的1.50 um候选完整模型。
- 报告：`D:/Codex/Kai/STAGE285_286_WIDTH1P5UM_WZ0P55_NOMINAL_SCREEN_2026-10-15.md`；机器结果：`D:/Codex/Kai/stage285_286_width1p5um_wz0p55_nominal_results.json`。

## 2026-10-15 Stage287–291：1.50 um候选三点照明验证进行中

- Stage287a已从最终几何的`wz=0.45 um`匹配模型建立宽度1.50 um端点设置；24个结构对象统一扩宽，解析高斯功率覆盖率为`99.9142%`。
- Stage287b于23:15在现有唯一FDTD窗口启动；6个`fdtd-engine-msmpi`计算引擎已确认运行。
- 已建立事件驱动自动链`D:/Codex/Kai/stage287_291_event_chain.ps1`：仅在完整FSP产生时触发，不进行一分钟高频轮询。
- 自动链顺序：Stage287b完成 -> Stage288a/b/c相干分解与固定32模投影 -> Stage289a/b运行`wz=0.65 um`端点 -> Stage290a/b/c后处理 -> Python汇总Stage291结论。
- 后续所有既有输入FSP/LDF已完成路径审计；目前缺少的依赖全部是本轮将生成的预期输出，没有断链。
- 数值有效性门槛：源功率一致、y/z网格一致、相干重构闭合、32模固定基底、投影线性、效率物理范围，以及未展开残差绝对值`<=1e-4`且相对直接散射`<=0.1%`。
- 工程判据：两个端点相对`wz=0.55 um`名义效率均在`±2%`内才冻结1.50 um宽度；否则保留完整机器结果并恢复0.75 um基线，不继续盲目扩大宽度。
- 自动产物：`stage287_291_width1p5um_three_point_results.json`和`STAGE287_291_WIDTH1P5UM_THREE_POINT_ILLUMINATION_VALIDATION.md`；完成或失败均生成明确标志文件。
- 本轮原理说明：`D:/Codex/Kai/STAGE287_291_LEARNING_NOTE.md`，记录束腰、解析覆盖率、三点门槛以及归一化效率与绝对功率的区别。
- 下一阶段分支规则：`D:/Codex/Kai/STAGE292_ENGINEERING_VALIDATION_DECISION_TREE.md`，结果出来后按“通过2% / 数值有效但未通过 / 数值失效”三条路径处理。

## 2026-10-16 Stage289–291：意外关机后的最小恢复

- 原自动链已于2026-10-16 01:02完成`wz=0.45 um`的Stage288a/b/c后处理并导出标量，随后自动启动`wz=0.65 um`的Stage289b。
- 夜间FDTD及自动链进程被系统关闭；Stage289b日志只到约`11.8924%`，没有完整FSP，故不得读取或用于比较。
- 中断的RUNNING FSP和p0日志已改名保留，文件名包含`INTERRUPTED_20261016_0130`；没有覆盖或伪装成有效结果。
- 2026-10-16 17:48重新打开Stage289a设置，仅重算未完成的`wz=0.65 um`；已完成的`wz=0.45 um`不重复运行。
- 新恢复链：`D:/Codex/Kai/stage289_291_recovery_event_chain.ps1`。它只等待Stage289b完整文件，再执行Stage290a/b/c、标量导出、三点finalizer和最终模型恢复。
- 恢复运行使用同一参数、同一参考LDF和同一6引擎配置；中断结果不参与任何数值结论。

## 2026-10-16 Stage287–291：1.50 um候选三点照明验证完成

- 重算的Stage289b完整结束，Stage290a/b/c相干分解与固定32模投影成功；两个端点的数值及物理有效性门槛全部通过。
- 三点净导模效率：`wz=0.45/0.55/0.65 um`分别为`7.5169802% / 7.7185615% / 7.6465338%`。
- 两端相对0.55 um名义点变化：`-2.6116% / -0.9332%`；三点相对跨度`2.6116%`，相比0.75 um宽度基线的`16.9971%`缩小`84.6348%`。
- 最差端从原0.75 um基线的`6.4770149%`提高到`7.5169802%`，相对提升`16.0562%`。
- mode1效率为`6.2377274% / 6.2019715% / 5.9747214%`，mode1占比为`82.9766% / 80.3467% / 78.1319%`；横向扩宽同时显著改善了目标模式纯度。
- 绝对净导模功率为`4.18709e-16 / 5.25446e-16 / 6.15186e-16 W`，仍随束腰增大，说明归一化效率与绝对功率必须继续分开报告。
- 结论：1.50 um候选显著改善照明鲁棒性，但0.45 um端点为`-2.6116%`，仍比临时`±2%`门槛超出`0.6116`个百分点，因此严格判定为**未通过**。
- 按预设规则不继续盲目扩大宽度；等待真实投影光斑/瞳孔规格。FDTD可见窗口已恢复到0.75 um、wz=0.55 um基线完整模型，恢复标记已验证。
- 自动链最后仅因Windows PowerShell 5.1按ANSI读取无BOM中文JSON而报“未终止字符串”；机器JSON本身经Python验证有效，编码读取已修正为`-Encoding UTF8`，该失败标志已归档为encoding-only。
- 报告：`D:/Codex/Kai/STAGE287_291_WIDTH1P5UM_THREE_POINT_ILLUMINATION_VALIDATION.md`；机器结果：`D:/Codex/Kai/stage287_291_width1p5um_three_point_results.json`；完成标志：`D:/Codex/Kai/STAGE287_291_EVENT_CHAIN_COMPLETE.flag`。

## Stage292入口：真实光机规格待确认

- 已建立工程输入模板：`D:/Codex/Kai/STAGE292_REAL_OPTICAL_INPUT_SPEC_TEMPLATE.md`。
- 在光谱宽度、出瞳/光斑定义、TE/TM权重、入射角范围及工程目标未确认前，不新增几何自由度，也不把临时2%门槛冒充产品要求。
- 规格确认后的第一轮只做7点最小验证：名义点、波长两端、极角两端、横向位置两端；全部数值有效后再决定是否做组合扫描或蒙特卡洛。

## 2026-10-17 Stage292–298：1.40 um平衡宽度验证进行中

- 用户明确要求继续优化，因此解除“等待真实规格”停点，但所有结论仍标记为当前仿真基准，不冒充产品验证。
- 1.40 um不是盲目扩宽：解析覆盖率阈值此前估计约1.409 um；同时0.75和1.50 um两组FDTD结果表明三点最优平衡宽度应落在二者之间。
- 1.40 um解析覆盖率：`wz=0.45/0.55/0.65 um`分别为`99.8136% / 98.9086% / 96.8748%`。
- 已生成Stage292–297共15个LSF脚本以及Stage292/293名义finalizer、Stage292–298三点finalizer。
- 静态审计发现并修复：后处理引用旧Stage285/287/289文件，以及机械替换误把top shift说明从-290 nm改成-297 nm。修复后run命令数按每组均为`0/1/0/0/0`，无旧宽度或旧Stage执行引用。
- Stage292a设置文件与审计LDF已生成；Stage292b名义点于13:55启动，6个FDTD引擎确认运行。
- 名义事件链`stage292_293_nominal_event_chain.ps1`已启动：名义性能门槛通过后才启动Stage294/295的0.45 um端点；随后`stage294_298_endpoint_event_chain.ps1`自动运行0.65 um端点并完成三点判断。
