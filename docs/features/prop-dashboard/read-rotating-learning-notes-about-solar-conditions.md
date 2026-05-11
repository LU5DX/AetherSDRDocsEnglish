# HF Propagation Dashboard

The HF Propagation Dashboard provides an at-a-glance view of HF and VHF propagation conditions, including current solar indices, a 3-day Kp forecast with blackout and radiation risk, HF day/night band conditions, solar and lunar imagery, and sporadic-E/aurora hints.

## Opening the Dashboard

- Open the HF Propagation Dashboard via `View > Propagation Conditions`.

## Dashboard Layout

The dashboard is organized into several panels that display current conditions, forecasts, and learning material.

### Current Conditions Cards

Five metric tiles display current solar and geomagnetic indices. Hover over any tile to see a plain-language explanation of what the value means.

| Metric | Description |
|---|---|
| SFI | Solar Flux Index |
| SN | Sunspot Number |
| A-index | Geomagnetic A-index |
| K-index | Geomagnetic K-index |
| X-ray | Current X-ray flux level |

### 3-Day Forecast Grid

A color-coded grid showing Kp forecasts for each 3-hour UTC period across three days. Below the grid, additional risk rows display:

- Max Kp per day
- R1-R2: Radio blackout risk (minor to moderate)
- R3+: Radio blackout risk (strong to extreme)
- S1+: Solar radiation storm risk

At the bottom of the forecast section, summary labels show:
- Geomagnetic field status
- Solar wind conditions
- Noise levels
- X-ray conditions

A "Rationale" section provides a plain-language explanation of today's forecast.

### Solar And Lunar Panel

Displays a live solar image and the current Moon phase. By default, the solar image shows "Corona (193Å)". Click the solar image to cycle through available wavelengths:

- Corona (193Å)
- Chromosphere (304Å)
- Quiet Corona (171Å)
- Flaring (94Å)
- Visible (HMI)

### What To Look For

Below or beside the solar image, rotating plain-language learning notes describe what to observe in the currently displayed image. The notes rotate automatically; no action is required to advance them. The notes update to match the currently selected solar wavelength.

### HF Band Conditions

A table showing day and night conditions for each HF band. Four band rows are displayed with condition indicators for both day and night.

### VHF Conditions

Shows the current state of VHF propagation openings:

| Condition | States | Meaning |
|---|---|---|
| Aurora | Closed / Open | Current auroral propagation |
| E-Skip NA | Closed / Open | Sporadic-E propagation over North America |
| E-Skip EU | Closed / Open | Sporadic-E propagation over Europe |

### What These Mean (VHF)

Two learning notes explain the difference between auroral and sporadic-E propagation, helping you understand the current VHF conditions.

## Adjusting Dialog Appearance

The HF Propagation Dashboard supports frameless window mode. When frameless mode is enabled, the dialog displays a custom title bar instead of the system window decoration.

This mode is controlled by the `FramelessWindow` setting in the application settings. When set to "True" (the default), the dialog uses frameless mode. If the setting is "False", the dialog uses the system window frame.

When frameless mode is active:
- A custom title bar labeled "HF Propagation Dashboard" is shown at the top.
- The dialog can be resized by dragging its edges.
- Internal content margins adjust slightly to account for the custom title bar.

## What each control does

| Control | Behavior |
|---|---|
| Current Conditions cards | Five metric tiles (SFI, SN, A-index, K-index, X-ray) with hover tooltips providing plain-language explanations. |
| 3-Day Forecast grid | Color-coded Kp per 3-hour UTC period for each of three days, plus Max Kp, R1-R2, R3+, and S1+ risk rows. |
| Solar And Lunar panel | Displays live solar image (click to cycle wavelengths) and current Moon phase. Default label: "Corona (193Å)". |
| What To Look For | Rotating plain-language learning notes about the current solar image. Updates automatically as the image cycles. |
| HF Band Conditions | Day and night condition per band row (4 band rows). |
| VHF Conditions | Aurora, E-Skip NA, E-Skip EU states (Closed/Open). |
| What These Mean (VHF) | Two learning notes explaining aurora vs sporadic-E propagation. |

## Related

- [Cycle solar imagery wavelengths to build intuition](cycle-solar-imagery-wavelengths-to-build-intuition.md)
- [Check current solar flux, sunspot number and K-index](check-current-solar-flux-sunspot-number-and-k-index.md)