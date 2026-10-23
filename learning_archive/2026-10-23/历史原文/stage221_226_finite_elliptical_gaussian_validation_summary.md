# Stage221–226 finite elliptical-Gaussian validation

## Outcome

Both finite-beam 3D points passed the matched-reference, coherent-field, and
fixed-mode numerical checks. The whole-beam net guided efficiency changes from
**1.0552834%** at `wz=0.45 um` to **0.9839211%** at `wz=0.55 um`.

The change is **-0.0713623 percentage point**, or **-6.7624% relative**. It
therefore fails the current local-insensitivity limits of `0.02 percentage
point` and `2%`. The result is physically waist-sensitive over the tested
range; this is not a numerical failure and is not evidence that the grating
geometry became worse.

## Comparison

| Metric | `wz=0.45 um` | `wz=0.55 um` | Change |
|---|---:|---:|---:|
| Directly integrated incident power (W) | `5.5701716528e-15` | `6.8075573954e-15` | `+22.2145%` |
| Coherent scattered direct power (%) | `1.0581986` | `0.9865539` | `-0.0716447 pp` |
| Guided forward power (%) | `1.0553890` | `0.9840182` | `-0.0713708 pp` |
| Guided backward power (%) | `0.00010566` | `0.00009718` | `-0.00000848 pp` |
| Net guided efficiency (%) | `1.0552834` | `0.9839211` | `-0.0713623 pp` |
| TM guided forward (%) | `1.0377793` | `0.9680050` | `-0.0697742 pp` |
| TE guided forward (%) | `0.0175988` | `0.0160043` | `-0.0015945 pp` |
| Mode 1 forward (%) | `0.8010840` | `0.7460080` | `-0.0550760 pp` |
| Mode 1 share of guided forward (%) | `75.9041` | `75.8124` | `-0.0917 pp` |
| Unexpanded scattered-net residual (%) | `0.0012860` | `0.0011415` | `-0.0001445 pp` |

The absolute net guided power is `5.8781096e-17 W` at `wz=0.45 um` and
`6.6980991e-17 W` at `wz=0.55 um`, an increase of **13.9499%**. The normalized
efficiency falls because total incident beam power increases faster
(`+22.2145%`) than the coupled guided power.

## Numerical validity of the `wz=0.55 um` point

- Stage225b and Stage225c both completed with `status=2`.
- Stage225c disabled exactly 24 grating objects.
- Patterned and reference incident powers are exactly equal:
  `6.807557395418483e-15 W`.
- The reference y-grid interpolation shift is `0.438266 nm`; the z grids are
  identical. Interpolation changes the normalized reference by only
  `0.0001855 percentage point`.
- Coherent reconstruction relative error is `-2.01e-16`.
- Stage226b and Stage226c both contain 32 modes and 22 guided modes.
- Forward/backward modal coefficient linearity errors are
  `4.16e-17 / 4.17e-17`.
- The fixed basis leaves only `0.0011415%` unexpanded scattered-net power.

All defined numerical gates pass. The `0.9839211%` value is therefore a valid
finite-beam result for this specific illumination definition.

## Physical interpretation

Increasing `wz` broadens the transverse illumination. More absolute optical
power reaches and couples through the finite grating, but still more power is
added outside the most useful coupling region. With normalization to the total
incident finite-beam power, the efficiency consequently decreases.

The waist is an input condition representing the projector/pupil field, not a
free grating parameter to maximize. Choosing whichever waist gives the largest
percentage would mix illumination overlap with structural performance.

## Next gate

Do not alter the grating geometry yet. Add one controlled `wz=0.65 um` point
only after checking source-data edge intensity, FDTD z-domain/monitor margins,
and memory cost. Repeat the same patterned/reference/coherent-field/fixed-basis
chain. This third point will distinguish a smooth physical overlap trend from a
two-point fluctuation. Final AR-system optimization must eventually use the
real illumination waist or pupil specification.

## Reproducible artifacts

- Machine-readable results and hashes:
  `D:/Codex/Kai/stage225_226_pipeline_results.json`
- Readable data table:
  `D:/Codex/Kai/stage221_226_finite_elliptical_gaussian_summary.csv`
- Decision gate:
  `D:/Codex/Kai/stage225_226_wz_sensitivity_gate.md`
- Stage225c raw data/model:
  `D:/FDTD_File/stage225c_elliptical_gaussian_wz0p55_reference_direct_power.ldf`
  and
  `D:/FDTD_File/ar_incoupler_FDTD_stage225c_ELLIPTICAL_GAUSSIAN_wx6um_wz0p55um_REFERENCE_COMPLETE_638nm.fsp`
- Stage226 analysis data:
  `D:/FDTD_File/stage226a_elliptical_gaussian_wz0p55_coherent_field_decomposition.ldf`,
  `D:/FDTD_File/stage226b_elliptical_gaussian_patterned_fixed_mode_basis32.ldf`,
  and
  `D:/FDTD_File/stage226c_elliptical_gaussian_fixed_basis32_projection.ldf`
