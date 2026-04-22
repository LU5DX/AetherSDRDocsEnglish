# See the 3-day Kp forecast and blackout risk

The HF Propagation Dashboard includes a 3-day Kp forecast grid showing geomagnetic activity across 3-hour UTC periods, along with NOAA radio blackout and radiation storm risk rows for each day. Use this to plan operating sessions around disturbed conditions or aurora.

## Before you start

- AetherSDR must be running. A radio connection is not required for this feature.
- An active internet connection is needed to fetch forecast data.

## Steps

1. Click `View > Propagation Conditions` in the menu bar. This opens the HF Propagation Dashboard dialog.
2. Scroll to the **3-Day Forecast grid** section.
3. Read the Kp values across the 8 columns of 3-hour UTC periods for each of the three days. Cells are color-coded: green indicates quiet conditions (Kp below 3), yellow indicates unsettled conditions (Kp 3–4), and red indicates storm-level activity (Kp 5 or higher).
4. Check the **R1-R2**, **R3+**, and **S1+** rows below the Kp cells. These show NOAA radio blackout and radiation storm risk probability per day.
5. Read the **Rationale** text beneath the grid for a plain-language explanation of the current forecast.
6. Check the summary labels — **Geomagnetic field**, **Solar wind**, **Noise**, and **X-ray** — for additional context below the forecast grid.

## What each control does

| Control | Behavior |
|---|---|
| **3-Day Forecast grid** | Displays Kp per 3-hour UTC period across three days, plus Max Kp per day. Cells are color-coded by severity. |
| **R1-R2** row | NOAA HF radio blackout risk at the R1–R2 level, shown per day. |
| **R3+** row | NOAA HF radio blackout risk at the R3 level and above, shown per day. |
| **S1+** row | NOAA solar radiation storm risk at the S1 level and above, shown per day. |
| **Rationale** | Plain-language explanation of today's forecast. |
| **Geomagnetic field / Solar wind / Noise / X-ray** | Summary status labels below the forecast grid. Color-coded by severity. |

## Tips

- A Kp of 5 or higher signals storm-level geomagnetic activity. Polar and high-latitude paths are most affected. Lower HF bands (40m, 80m) tend to hold up better than upper bands during geomagnetic storms.
- The R1-R2 and R3+ rows reflect probability estimates per day, not certainty. Check the Kp cell colors across individual 3-hour periods to see when during the day risk is highest.
- Hover over the **Current Conditions cards** (SFI, SN, A-index, K-index, X-ray) for tooltip explanations of each index.

## Troubleshooting

- **Forecast grid shows no data or stale values** — AetherSDR fetches forecast data from the internet. Verify your network connection is active and reopen the dialog.

## Related

- [HF Propagation Dashboard overview](overview.md)
- [Check current solar flux, sunspot number and K-index](check-current-solar-flux-sunspot-number-and-k-index.md)
- [Decide which HF band is open for day or night work](decide-which-hf-band-is-open-for-day-or-night-work.md)
- [Watch for VHF sporadic-E or auroral openings](watch-for-vhf-sporadic-e-or-auroral-openings.md)
