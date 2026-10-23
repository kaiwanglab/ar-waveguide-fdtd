# Stage225–226 transverse beam-waist sensitivity gate

## Purpose

Compare the finite 3D elliptical-Gaussian results at `wz=0.45 um` and
`wz=0.55 um` while keeping the grating, `wx=6 um`, wavelength, incidence,
mesh, monitors, reference subtraction, mode basis, and normalization method
unchanged.

This is a **beam-definition sensitivity check**, not a geometry optimization.
The beam waist describes the incident optical field. A higher efficiency at a
different waist is not automatically a better grating because the illuminated
fraction of the finite grating has also changed.

## Fixed baseline

- `wz=0.45 um`
- directly integrated incident power: `5.570171652777991e-15 W`
- fixed-basis net guided efficiency: `1.0552833771102107%`
- 32 solved modes, 22 guided modes
- unexpanded scattered-net residual: `0.0012859828750811514%`

## Required numerical gates for `wz=0.55 um`

1. Patterned and matched-reference runs both finish with `status=2`.
2. Exactly 24 grating objects are disabled in the reference model.
3. Patterned/reference directly integrated incident powers agree to
   `1e-13` relative tolerance.
4. Coherent field reconstruction relative error is below `1e-10`.
5. Fixed basis contains 32 modes and the guided-mode count is identical in
   Stage226b and Stage226c.
6. Maximum forward/backward modal coefficient linearity errors are below
   `1e-12`.
7. Stage226c's direct scattered power equals Stage226a's `TS` within numerical
   precision. The unexpanded residual is reported rather than hidden.

## Local sensitivity calculation

Let

- `eta045 = 1.0552833771102107%`
- `eta055 = 100 * eta_finite_beam_guided_net226c`

Then calculate

- absolute change: `delta_pp = eta055 - eta045` percentage points
- relative change: `delta_rel = eta055 / eta045 - 1`

For this validation campaign, call the two tested waists **locally
insensitive** only if both conditions hold:

- `abs(delta_pp) <= 0.02 percentage point`
- `abs(delta_rel) <= 2%`

These are project decision thresholds, not universal optical laws.

## Decision after Stage226c

- If all numerical gates pass and both sensitivity limits pass: record local
  waist insensitivity over `0.45–0.55 um`; do not optimize the waist further
  until the real projector/pupil illumination is specified.
- If numerical gates pass but sensitivity limits fail: do not claim geometry
  improvement. Add one controlled physical point (normally `wz=0.65 um`) with
  sufficient z-domain margin and repeat the same matched-reference/fixed-basis
  chain to reveal the trend.
- If a numerical gate fails: repair that validation issue first. Do not change
  grating geometry or compare efficiencies.

## Physical interpretation rule

The accepted efficiency is always normalized to the total incident finite-beam
power obtained by direct `E x H` integration. No plane-wave domain-width or
grating-width scaling is allowed. Final AR-system optimization must eventually
use the actual illumination waist/pupil rather than whichever simulated waist
gives the largest number.
