"""Close the width=1.40 um three-point illumination robustness gate."""

from __future__ import annotations

import json
import math
from datetime import datetime
from pathlib import Path


ROOT = Path(r"D:\Codex\Kai")


def load(name: str) -> dict:
    return json.loads((ROOT / name).read_text(encoding="utf-8-sig"))


def num(data: dict, name: str) -> float:
    if name not in data:
        raise KeyError(name)
    result = float(data[name])
    if not math.isfinite(result):
        raise ValueError(name)
    return result


def endpoint(stage: int, width: float) -> tuple[dict, dict, dict]:
    a = load(f"stage{stage}a_width1p4um_wz0p{int(width*100):02d}_scalars.json")
    c = load(f"stage{stage}c_width1p4um_wz0p{int(width*100):02d}_scalars.json")
    suffix = str(stage)
    validation = {
        "grid_y_max_error": num(a, f"grid_y_max_error{suffix}a"),
        "grid_z_max_error": num(a, f"grid_z_max_error{suffix}a"),
        "sourcepower_ratio": num(a, f"sourcepower_ratio{suffix}a"),
        "reconstruction_relative_error": num(a, f"reconstruction_relative_error{suffix}a"),
        "reference_interp_minus_native_pp": num(a, f"reference_interp_minus_native_pp{suffix}a"),
        "nmodes": int(round(num(c, f"nmodes{suffix}c"))),
        "guided_count": int(round(num(c, f"guided_count{suffix}c"))),
        "a_linearity_error_max": num(c, f"a_linearity_error_max{suffix}c"),
        "b_linearity_error_max": num(c, f"b_linearity_error_max{suffix}c"),
    }
    result = {
        "wz_um": width,
        "incident_power_W": num(c, f"PsrcP{suffix}c"),
        "reference_incident_power_W": num(c, f"PsrcR{suffix}c"),
        "guided_forward": num(c, f"guided_scat_forward{suffix}c"),
        "guided_backward": num(c, f"guided_scat_backward{suffix}c"),
        "guided_net": num(c, f"guided_scat_net{suffix}c"),
        "tm_forward": num(c, f"tm_guided_scat_forward{suffix}c"),
        "te_forward": num(c, f"te_guided_scat_forward{suffix}c"),
        "mode1": num(c, f"mode1_scat_forward{suffix}c"),
        "mode1_share": num(c, f"mode1_fraction_guided_forward{suffix}c"),
        "direct_scattered_net": num(c, f"scattered_direct_net{suffix}c"),
        "unexpanded_net": num(c, f"unexpanded_scattered_net{suffix}c"),
    }
    result["absolute_guided_net_power_W"] = result["incident_power_W"] * result["guided_net"]
    result["residual_relative_to_direct"] = abs(result["unexpanded_net"]) / max(abs(result["direct_scattered_net"]), 1e-30)
    gates = {
        "grid_match": validation["grid_y_max_error"] <= 1e-15 and validation["grid_z_max_error"] <= 1e-15,
        "source_match": abs(validation["sourcepower_ratio"] - 1) <= 1e-12
        and abs(result["incident_power_W"] / result["reference_incident_power_W"] - 1) <= 1e-12,
        "coherent_reconstruction": abs(validation["reconstruction_relative_error"]) <= 1e-12,
        "reference_interpolation": abs(validation["reference_interp_minus_native_pp"]) <= 1e-9,
        "fixed_basis": validation["nmodes"] == 32 and validation["guided_count"] > 0,
        "projection_linearity": validation["a_linearity_error_max"] <= 1e-12 and validation["b_linearity_error_max"] <= 1e-12,
        "efficiency_physical": 0 <= result["guided_net"] <= 1 and result["guided_forward"] >= result["guided_backward"] >= 0,
        "mode1_physical": 0 <= result["mode1"] <= result["guided_forward"],
        "modal_residual_small": abs(result["unexpanded_net"]) <= 1e-4 and result["residual_relative_to_direct"] <= 1e-3,
    }
    return result, validation, gates


def main() -> None:
    nominal = load("stage292_293_width1p4um_wz0p55_nominal_results.json")
    baseline = load("stage283_284_final_geometry_wz0p45_three_point_results.json")
    p45, v45, g45 = endpoint(295, 0.45)
    p65, v65, g65 = endpoint(297, 0.65)
    n = nominal["result"]
    p55 = {
        "wz_um": 0.55,
        "incident_power_W": n["incident_power_W"],
        "guided_net": n["guided_scat_net"],
        "mode1": n["mode1_scat_forward"],
        "mode1_share": n["mode1_fraction_guided_forward"],
        "absolute_guided_net_power_W": n["absolute_guided_net_power_W"],
    }
    points = [p45, p55, p65]
    valid = bool(nominal["all_validation_gates_pass"]) and all(g45.values()) and all(g65.values())
    maximum = max(p["guided_net"] for p in points)
    minimum = min(p["guided_net"] for p in points)
    relative_changes = {f"wz{p['wz_um']:.2f}": (p["guided_net"] / p55["guided_net"] - 1) * 100 for p in (p45, p65)}
    span_pp = (maximum - minimum) * 100
    span_relative = (maximum - minimum) / p55["guided_net"] * 100
    two_percent_pass = valid and max(abs(x) for x in relative_changes.values()) <= 2
    base_gate = baseline["three_point_illumination_gate"]
    span_reduction = (1 - span_relative / float(base_gate["three_point_relative_span_percent"])) * 100
    worst_end = min((p45, p65), key=lambda p: p["guided_net"])
    worst_end_gain = (worst_end["guided_net"] / float(base_gate["worst_endpoint_guided_net"]) - 1) * 100

    if not valid:
        decision = "至少一个端点数值/物理有效性门控失败；不得做三点鲁棒性结论。"
    elif two_percent_pass:
        decision = "1.40 µm候选通过三点2%照明敏感性门槛；冻结该横向宽度并转入真实投影光机规格验证。"
    else:
        decision = (
            "1.40 µm候选改善了有限光束覆盖，但仍未通过2%照明敏感性门槛。"
            "保留机器结果和最差端提升，不再盲目放大宽度；等待真实光斑/瞳孔规格后再决定是否继续。"
        )

    output = {
        "stage": "292-298",
        "date": datetime.now().date().isoformat(),
        "candidate_grating_z_span_um": 1.40,
        "points": points,
        "endpoint_validation": {"wz0p45": v45, "wz0p65": v65},
        "endpoint_gates": {"wz0p45": g45, "wz0p65": g65},
        "all_validation_gates_pass": valid,
        "metrics": {
            "nominal_guided_net": p55["guided_net"],
            "worst_endpoint_wz_um": worst_end["wz_um"],
            "worst_endpoint_guided_net": worst_end["guided_net"],
            "three_point_span_pp": span_pp,
            "three_point_relative_span_percent": span_relative,
            "endpoint_relative_changes_from_nominal_percent": relative_changes,
            "illumination_local_2pct_pass": two_percent_pass,
            "span_reduction_vs_width0p75_percent": span_reduction,
            "worst_endpoint_gain_vs_width0p75_percent": worst_end_gain,
        },
        "decision": decision,
    }
    out_json = ROOT / "stage292_298_width1p4um_three_point_results.json"
    out_json.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    rows = "\n".join(
        f"| {p['wz_um']:.2f} | {p['guided_net']*100:.6f}% | {p['mode1']*100:.6f}% | {p['mode1_share']*100:.4f}% | {p['absolute_guided_net_power_W']:.6e} |"
        for p in points
    )
    report = f"""# Stage292–298：1.40 µm横向宽度候选三点照明验证

日期：{datetime.now().date().isoformat()}。

## 三点结果

| wz (µm) | 净导模效率 | mode1效率 | mode1占比 | 绝对净导模功率 (W) |
|---:|---:|---:|---:|---:|
{rows}

- 数值有效性：**{'全部通过' if valid else '未全部通过'}**。
- 两端相对名义点变化：0.45 µm={relative_changes['wz0.45']:+.4f}%，0.65 µm={relative_changes['wz0.65']:+.4f}%。
- 三点跨度：{span_pp:.6f}个百分点，相对名义点={span_relative:.4f}%。
- 相对0.75 µm基线，跨度缩小={span_reduction:.4f}%，最差端效率变化={worst_end_gain:+.4f}%。
- 临时2%照明敏感性门槛：**{'通过' if two_percent_pass else '未通过'}**。

## 工程结论

{decision}

机器结果：`{out_json}`
"""
    out_report = ROOT / "STAGE292_298_WIDTH1P4UM_THREE_POINT_ILLUMINATION_VALIDATION.md"
    out_report.write_text(report, encoding="utf-8")
    print(json.dumps({"valid": valid, "two_percent_pass": two_percent_pass, "json": str(out_json), "report": str(out_report)}, ensure_ascii=True))


if __name__ == "__main__":
    main()

