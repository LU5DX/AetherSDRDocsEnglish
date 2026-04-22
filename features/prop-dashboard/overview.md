# HF Propagation Dashboard overview

The HF Propagation Dashboard gives you an at-a-glance view of current solar conditions, a 3-day geomagnetic forecast, HF band conditions by day and night, solar and lunar imagery, and VHF propagation hints. Use it to decide which bands are likely open before you transmit, or to understand why conditions are behaving unexpectedly.

## Before you start

- No radio connection is required. The dashboard fetches data independently.
- An active internet connection is needed to retrieve solar indices, forecast data, and solar imagery.

## How it works

Open the dashboard from `View > Propagation Conditions`. The dialog retrieves current solar data and presents it in seven distinct areas described below.

### Current Conditions cards

Five metric tiles display the most important solar and geomagnetic indices at a glance: **SFI** (Solar Flux Index), **SN** (Sunspot Number), **A-index**, **K-index**, and **X-ray** class. Each card is color-coded to reflect the quality of conditions — green indicates favorable conditions, yellow indicates unsettled or moderate conditions, and red indicates storm-level or degraded conditions. Hover over any card to read a plain-language tooltip explaining what that metric means for HF propagation.

### 3-Day Forecast grid

Displays Kp values for each 3-hour UTC period across three days — 24 cells in total. Each cell is color-coded by Kp level. Below the Kp grid, three risk rows show the probability of NOAA-scale radio blackout and radiation storm events per day: **R1-R2**, **R3+**, and **S1+**. Summary labels for geomagnetic field state, solar wind speed, atmospheric noise, and X-ray flux appear beneath the forecast grid.

### Solar And Lunar panel

Shows a live solar image and the current Moon phase. Clicking the solar image cycles through five wavelength views:

| Label | Code |
|---|---|
| Corona (193Å) | 0193 |
| Chromosphere (304Å) | 0304 |
| Quiet Corona (171Å) | 0171 |
| Flaring (94Å) | 0094 |
| Visible (HMI) | HMIIC |

The default view is **Corona (193Å)**.

### What To Look For

Displays rotating plain-language notes that explain what to observe in the currently selected solar image. The notes change automatically as you cycle wavelengths, helping you build intuition about solar activity.

### HF Band Conditions

Shows day and night propagation conditions across four HF band rows. Each row is color-coded: **Good**, **Fair**, or **Poor**. Use this panel to identify which bands are most likely productive for your operating time and location.

### VHF Conditions

Reports the current state of three VHF propagation paths: **Aurora**, **E-Skip NA** (North America), and **E-Skip EU** (Europe). Each indicator shows either **Open** or **Closed**.

### What These Mean (VHF)

Two fixed learning notes explain the difference between auroral propagation and sporadic-E, giving context for the VHF Conditions indicators above.

## Tips

- The **Rationale** text below the forecast grid provides a plain-language explanation of why today's forecast looks the way it does — read it for a quick summary before checking individual metrics.
- Hovering over a **Current Conditions** card shows a detailed tooltip explaining the metric's significance for HF propagation, including which bands are most affected.
- The dashboard does not require a connected FLEX-8600 radio. You can consult it before powering up your station.

## Related

- [Check current solar flux, sunspot number and K-index](check-current-solar-flux-sunspot-number-and-k-index.md)
- [See the 3-day Kp forecast and blackout risk](see-the-3-day-kp-forecast-and-blackout-risk.md)
- [Decide which HF band is open for day or night work](decide-which-hf-band-is-open-for-day-or-night-work.md)
- [Watch for VHF sporadic-E or auroral openings](watch-for-vhf-sporadic-e-or-auroral-openings.md)
- [Cycle solar imagery wavelengths to build intuition](cycle-solar-imagery-wavelengths-to-build-intuition.md)
- [Read rotating learning notes about solar conditions](read-rotating-learning-notes-about-solar-conditions.md)
