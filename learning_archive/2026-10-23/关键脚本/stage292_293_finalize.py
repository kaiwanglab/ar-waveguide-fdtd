"""Validate the width=1.40 um nominal candidate and apply its stop rule."""

from __future__ import annotations

import json
import math
from datetime import datetime
from pathlib import Path


ROOT = Path(r"D:\Codex\Kai")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def value(data: dict, name: str) -> float:
    if name not in data:
        raise KeyError(name)
    result = float(data[name])
    if not math.isfinite(result):
        raise ValueError(f"{name} is not finite")
    return result


def main() -> None:
    a = load(ROOT / "stage293a_width1p4um_wz0p55_scalars.json")
    c = load(ROOT / "stage293c_width1p4um_wz0p55_scalars.json")
    baseline = load(ROOT / "stage281_282_final_geometry_wz0p55_results.json")

    validation = {
        "grid_y_max_error": value(a, "grid_y_max_error293a"),
        "grid_z_max_error": value(a, "grid_z_max_error293a"),
        "sourcepower_ratio": value(a, "sourcepower_ratio293a"),
        "reconstruction_relative_error": value(a, "reconstruction_relative_error293a"),
        "reference_interp_minus_native_pp": value(a, "reference_interp_minus_native_pp293a"),
        "nmodes": int(round(value(c, "nmodes293c"))),
        "guided_count": int(round(value(c, "guided_count293c"))),
        "a_linearity_error_max": value(c, "a_linearity_error_max293c"),
        "b_linearity_error_max": value(c, "b_linearity_error_max293c"),
    }
    result = {
        "incident_power_W": value(c, "PsrcP293c"),
        "reference_incident_power_W": value(c, "PsrcR293c"),
        "guided_scat_forward": value(c, "guided_scat_forward293c"),
        "guided_scat_backward": value(c, "guided_scat_backward293c"),
        "guided_scat_net": value(c, "guided_scat_net293c"),
        "tm_guided_scat_forward": value(c, "tm_guided_scat_forward293c"),
        "te_guided_scat_forward": value(c, "te_guided_scat_forward293c"),
        "mode1_scat_forward": value(c, "mode1_scat_forward293c"),
        "mode1_fraction_guided_forward": value(c, "mode1_fraction_guided_forward293c"),
        "scattered_direct_net": value(c, "scattered_direct_net293c"),
        "unexpanded_scattered_net": value(c, "unexpanded_scattered_net293c"),
    }
    result["absolute_guided_net_power_W"] = result["incident_power_W"] * result["guided_scat_net"]
    result["modal_residual_relative_to_direct"] = abs(result["unexpanded_scattered_net"]) / max(
        abs(result["scattered_direct_net"]), 1e-30
    )

    gates = {
        "grid_match": validation["grid_y_max_error"] <= 1e-15 and validation["grid_z_max_error"] <= 1e-15,
        "source_match": abs(validation["sourcepower_ratio"] - 1) <= 1e-12
        and abs(result["incident_power_W"] / result["reference_incident_power_W"] - 1) <= 1e-12,
        "coherent_reconstruction": abs(validation["reconstruction_relative_error"]) <= 1e-12,
        "reference_interpolation": abs(validation["reference_interp_minus_native_pp"]) <= 1e-9,
        "fixed_basis": validation["nmodes"] == 32 and validation["guided_count"] > 0,
        "projection_linearity": validation["a_linearity_error_max"] <= 1e-12
        and validation["b_linearity_error_max"] <= 1e-12,
        "efficiency_physical": 0 <= result["guided_scat_net"] <= 1
        and result["guided_scat_forward"] >= result["guided_scat_backward"] >= 0,
        "mode1_physical": 0 <= result["mode1_scat_forward"] <= result["guided_scat_forward"],
        "modal_residual_small": abs(result["unexpanded_scattered_net"]) <= 1e-4
        and result["modal_residual_relative_to_direct"] <= 1e-3,
    }
    valid = all(gates.values())

    base = baseline["results"]
    guided_retention = result["guided_scat_net"] / float(base["guided_scat_net"])
    mode1_retention = result["mode1_scat_forward"] / float(base["mode1_scat_forward"])
    mode1_share_change_pp = (
        result["mode1_fraction_guided_forward"] - float(base["mode1_fraction_guided_forward"])
    ) * 100
    nominal_screen_pass = valid and guided_retention >= 0.90 and mode1_retention >= 0.90

    if not valid:
        decision = "数值/物理有效性门控失败；不得比较宽度候选。"
    elif nominal_screen_pass:
        decision = (
            "1.40 µm候选通过名义点90%性能保留门槛，可进入wz=0.45/0.65 µm端点验证；"
            "当前单点结果尚不能证明照明鲁棒性。"
        )
    else:
        decision = (
            "1.40 µm候选未通过名义点90%性能保留门槛，停止该候选的端点长仿真；"
            "保留0.75 µm基线，并重新选择更接近的横向宽度或等待真实光机规格。"
        )

    output = {
        "stage": "292/293",
        "date": datetime.now().date().isoformat(),
        "candidate": {"grating_z_span_um": 1.40, "wz_um": 0.55, "analytic_power_overlap": 0.9890864428518845},
        "validation": validation,
        "validation_gates": gates,
        "all_validation_gates_pass": valid,
        "result": result,
        "baseline_width0p75_wz0p55": base,
        "comparison": {
            "guided_net_retention": guided_retention,
            "guided_net_change_percent": (guided_retention - 1) * 100,
            "mode1_retention": mode1_retention,
            "mode1_change_percent": (mode1_retention - 1) * 100,
            "mode1_share_change_pp": mode1_share_change_pp,
            "nominal_screen_pass": nominal_screen_pass,
        },
        "decision": decision,
    }
    out_json = ROOT / "stage292_293_width1p4um_wz0p55_nominal_results.json"
    out_json.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    gate_text = "\n".join(f"- {'PASS' if ok else 'FAIL'} — `{name}`" for name, ok in gates.items())
    report = f"""# Stage292/293：1.40 µm横向宽度候选的名义点筛选

日期：{datetime.now().date().isoformat()}。固定 `wz=0.55 µm`、周期328.75 nm、齿高237 nm、齿宽190 nm、top shift=-290 nm，仅将光栅z宽从0.75 µm改为1.40 µm。

## 选择原因与停止线

- 0.75 µm基线三点效率除以解析高斯覆盖率后仅变化约1.4%，说明照明敏感性主要来自有限横向覆盖。
- 解析覆盖模型预计约1.409 µm才可能达到2%端点变化，选择工程值1.40 µm做名义点候选。
- 本轮只跑0.55 µm名义点；总净导模与mode1必须分别保留基线的90%，否则停止两个端点长仿真。

## 数值有效性

{gate_text}

总判定：**{'有效' if valid else '无效'}**；重构相对误差={validation['reconstruction_relative_error']:.3e}，a/b线性误差={validation['a_linearity_error_max']:.3e}/{validation['b_linearity_error_max']:.3e}，未展开残差占直接散射={result['modal_residual_relative_to_direct']*100:.5f}%。

## 名义点比较

| 指标 | 1.40 µm候选 | 0.75 µm基线 | 变化/保留率 |
|---|---:|---:|---:|
| 净导模效率 | {result['guided_scat_net']*100:.6f}% | {float(base['guided_scat_net'])*100:.6f}% | {(guided_retention-1)*100:+.4f}% |
| mode1效率 | {result['mode1_scat_forward']*100:.6f}% | {float(base['mode1_scat_forward'])*100:.6f}% | {(mode1_retention-1)*100:+.4f}% |
| mode1占比 | {result['mode1_fraction_guided_forward']*100:.4f}% | {float(base['mode1_fraction_guided_forward'])*100:.4f}% | {mode1_share_change_pp:+.4f} pp |
| 绝对净导模功率 | {result['absolute_guided_net_power_W']:.6e} W | {float(base['absolute_guided_net_power_W']):.6e} W | {(guided_retention-1)*100:+.4f}% |

名义筛选：**{'通过' if nominal_screen_pass else '未通过'}**。

## 工程决策

{decision}
"""
    out_report = ROOT / "STAGE292_293_WIDTH1P4UM_WZ0P55_NOMINAL_SCREEN_2026-10-17.md"
    out_report.write_text(report, encoding="utf-8")
    print(json.dumps({"valid": valid, "screen_pass": nominal_screen_pass, "json": str(out_json), "report": str(out_report)}, ensure_ascii=True))


if __name__ == "__main__":
    main()

