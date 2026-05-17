# HF Propagation Dashboard

The HF Propagation Dashboard provides an at-a-glance view of current HF/VHF propagation conditions, including solar indices, a 3-day Kp forecast with blackout and radiation risk assessments, HF day/night band conditions, solar and lunar imagery, and sporadic-E/aurora hints.

## Before you start

- AetherSDR must be running. A radio connection is not required for this feature.
- An active internet connection is needed to fetch live solar data.

## Opening the dashboard

1. Click `View > Propagation Conditions` to open the HF Propagation Dashboard.

The dialog title and geometry are persisted across sessions using the `PropDashboardDialogGeometry` setting key.

## What each control does

### Current Conditions cards

Five metric tiles are displayed at the top of the dialog. Hover over any tile to read its tooltip explaining what the index measures and what the current value means for HF propagation.

| Control | What it shows |
|---|---|
| **SFI** tile | Solar Flux Index. Higher values (120 and above) favor upper HF bands; values below 120 suggest lower bands will lead. |
| **SN** tile | Sunspot number. More sunspots generally mean stronger ionization and better support for higher-frequency HF propagation. |
| **K-index** tile | Short-term geomagnetic disturbance on a scale of 0–9. Values of 5 or above indicate storm-level activity and noisy polar paths. |
| **A-index** tile | All-day average of geomagnetic activity. Elevated values mean conditions may stay unsettled even if the latest K-index looks quiet. |
| **X-ray** tile | Latest solar flare class (A/B/C/M/X). C, M, and X class flares can trigger daylight radio blackouts on sunlit paths. |

None of these controls have persisted settings keys — they are read-only indicators updated from live data.

### 3-Day Forecast grid

Shows the Kp forecast for each 3-hour UTC period across three days. Below the grid, summary rows display:

- **Max Kp** - Highest predicted Kp value per day
- **R1-R2** - Risk of minor-to-moderate radio blackouts
- **R3+** - Risk of strong-to-extreme radio blackouts
- **S1+** - Risk of solar radiation storms

Additional summary labels under the forecast grid show:
- **Geomagnetic field** status
- **Solar wind** conditions
- **Noise** levels
- **X-ray** activity

### Solar And Lunar panel

Displays a live solar image. Click on the image to cycle through available wavelengths. The default label shows **Corona (193A)**. Below the solar image, the current Moon phase is displayed.

### What To Look For

Rotating plain-language learning notes about the current solar image appear in this section.

### HF Band Conditions

Shows day and night condition per band row. Four band rows are displayed with color-coded indicators showing propagation quality.

### VHF Conditions

Shows current VHF propagation openings with three states per indicator: **Closed** or **Open**.

| Indicator | What it shows |
|---|---|
| **Aurora** | Current auroral propagation opening status |
| **E-Skip NA** | Current sporadic-E opening status for North America |
| **E-Skip EU** | Current sporadic-E opening status for Europe |

### What These Mean (VHF)

Two learning notes explain the difference between aurora and sporadic-E propagation modes.

### Rationale

A plain-language explanation of today's forecast appears at the bottom of the dashboard.

## Tips

- The color of each tile value changes with severity: green indicates favorable or quiet conditions, yellow indicates elevated or unsettled conditions, and red indicates storm-level or major flare activity.
- If a tile shows no value, the dashboard is still waiting for data from the network.
- The dashboard window size and position are remembered between sessions. Resize or move the dialog and it will reopen in the same location.
- Kp cells in the forecast grid are color-coded according to their severity level.

## Related

- [Check current solar flux, sunspot number and K-index](check-current-solar-flux-sunspot-number-and-k-index.md)
- [See the 3-day Kp forecast and blackout risk](see-the-3-day-kp-forecast-and-blackout-risk.md)
- [Decide which HF band is open for day or night work](decide-which-hf-band-is-open-for-day-or-night-work.md)