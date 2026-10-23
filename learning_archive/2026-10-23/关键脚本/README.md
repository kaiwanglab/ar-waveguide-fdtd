# 关键后处理脚本

这些文件从本地保存记录复制，用于学习和追溯，不在本次归档过程中执行。

| 文件 | 作用 |
|---|---|
| `stage293a_width1p4um_wz0p55_coherent_field_decomposition.lsf` | 总场与匹配无齿参考的复场分离 |
| `stage293b_width1p4um_wz0p55_patterned_fixed_mode_basis32.lsf` | 获取固定模式基底 |
| `stage293c_width1p4um_wz0p55_fixed_basis32_projection.lsf` | 对一致场数据进行固定基底投影 |
| `stage292_293_finalize.py` | 名义点后处理结果汇总 |
| `stage292_298_finalize.py` | 三光斑结果比较与有限检查范围 |

运行依赖相应 FSP / LDF、对象命名、源数据、Lumerical 环境和绝对路径；这些大文件不在本次文档包中。脚本可能包含加载、修改或保存动作，阅读前不要直接执行。

检查 `all_validation_gates_pass` 时，应逐项阅读判断条件。它不是对导入源、全部数值收敛、导模物理分类或产品规格的总保证。
