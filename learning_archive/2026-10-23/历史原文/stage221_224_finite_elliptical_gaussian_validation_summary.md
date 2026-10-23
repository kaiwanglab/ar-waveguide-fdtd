# Stage221-224 finite elliptical Gaussian validation

## Outcome

The finite-beam 3D workflow is now numerically self-consistent. For `wx=6 um` and `wz=0.45 um`, the net guided-mode coupling efficiency is **1.0552834%** of the directly integrated incident power.

## Evidence

- Patterned and matched-reference runs use exactly the same directly integrated incident power: `5.570171652777991e-15 W`.
- Stage223 finished normally (`status=2`) with all 24 grating objects disabled.
- Coherent field subtraction reconstructs the patterned field power with zero numerical residual.
- The fixed basis contains 32 solved modes, of which 22 satisfy the guided-mode criterion.
- Guided forward power: `1.0553890%`; guided backward power: `0.00010566%`; net guided power: `1.0552834%`.
- TM guided forward: `1.0377793%`; TE guided forward: `0.0175988%`.
- Mode 1 contributes `0.8010840%`, or `75.9041%` of forward guided power.
- Unexpanded scattered net residual is `0.0012860%`, showing that the 32-mode basis captures essentially all right-going scattered power relevant to this monitor.

## Physical interpretation

The earlier plane-wave finite-domain values grew with z-domain width and therefore were not a physical finite-aperture efficiency. The present finite elliptical Gaussian source fixes the physical illumination width. No domain-width scaling is applied. The reported `1.0552834%` is therefore the current physically meaningful finite-beam guided-coupling result, subject to beam-waist and mesh convergence checks.

## Next gate

Repeat the matched patterned/reference workflow at `wz=0.55 um` with all other geometry, source-x profile, mesh, monitors, and modal criteria unchanged. Compare the net guided efficiency against `1.0552834%`. This isolates beam-waist sensitivity and provides a check that the `wz=0.45 um` result is not dominated by an arbitrary transverse illumination choice.
