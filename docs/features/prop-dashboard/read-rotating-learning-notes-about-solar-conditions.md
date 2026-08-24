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

A "Rationale" section provides a plain-language explanation of today's forecast. The rationale field uses themed background and border colors that respect the current application theme.

### Solar And Lunar Panel

Displays a live solar image and the current Moon phase. By default, the solar image shows "Corona (193Å)". Click the solar image to cycle through available wavelengths:

- Corona (193Å)
- Chromosphere (304Å)
- Quiet Corona (171Å)
- Flaring (94Å)
- Visible (HMI)

### What To Look For

Below or beside the solar image, rotating plain-language learning notes describe what to observe in the currently displayed image. The notes rotate automatically; no action is required to advance them. The notes update to match the currently selected solar wavelength. The learning panel background is themed to match the current application theme.

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

Two learning notes explain the difference between auroral and sporadic-E propagation, helping you understand the current VHF conditions. The learning panel background is themed to match the current application theme.

## Theme Support

The Propagation Dashboard fully supports the active application theme. Panel backgrounds, separator lines, border colors, and the rationale field all use themed colors. When you change the application theme, the dashboard updates its appearance accordingly.

## Network Timeout

The dashboard applies a 15-second network timeout to all space-weather data fetches. If a fetch does not complete within this window, the request is cancelled, and the dashboard will not display stale or partial data. The data is retried on the next refresh cycle.

## Resizing and Positioning

The HF Propagation Dashboard remembers its window size and position. Resize the dialog by dragging its edges. The next time you open the dashboard, it will restore to its previous size and location. The geometry is saved under the key `PropDashboardDialogGeometry` in the application settings.

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