# Check current solar flux, sunspot number and K-index

The HF Propagation Dashboard shows live solar indices — Solar Flux Index (SFI), sunspot number, K-index, A-index, and X-ray class — in a set of metric cards. Use this page to get a quick read on current ionospheric conditions before calling CQ or chasing DX.

## Before you start

- AetherSDR must be running. A radio connection is not required for this feature.
- An active internet connection is needed to fetch live solar data.

## Steps

1. Click `View > Propagation Conditions` to open the HF Propagation Dashboard.
2. Read the **Current Conditions cards** at the top of the dialog. Five metric tiles are displayed: **SFI**, **SN**, **A-index**, **K-index**, and **X-ray**.
3. Hover over any tile to read its tooltip. Each tooltip explains what the index measures and what the current value means for HF propagation.

## What each control does

| Control | What it shows |
|---|---|
| **SFI** tile | Solar Flux Index. Higher values (120 and above) favor upper HF bands; values below 120 suggest lower bands will lead. |
| **SN** tile | Sunspot number. More sunspots generally mean stronger ionization and better support for higher-frequency HF propagation. |
| **K-index** tile | Short-term geomagnetic disturbance on a scale of 0–9. Values of 5 or above indicate storm-level activity and noisy polar paths. |
| **A-index** tile | All-day average of geomagnetic activity. Elevated values mean conditions may stay unsettled even if the latest K-index looks quiet. |
| **X-ray** tile | Latest solar flare class (A/B/C/M/X). C, M, and X class flares can trigger daylight radio blackouts on sunlit paths. |

None of these controls have persisted settings keys — they are read-only indicators updated from live data.

## Tips

- The color of each tile value changes with severity: green indicates favorable or quiet conditions, yellow indicates elevated or unsettled conditions, and red indicates storm-level or major flare activity.
- If a tile shows no value, the dashboard is still waiting for data from the network.

## Related

- [HF Propagation Dashboard overview](overview.md)
- [See the 3-day Kp forecast and blackout risk](see-the-3-day-kp-forecast-and-blackout-risk.md)
- [Decide which HF band is open for day or night work](decide-which-hf-band-is-open-for-day-or-night-work.md)
