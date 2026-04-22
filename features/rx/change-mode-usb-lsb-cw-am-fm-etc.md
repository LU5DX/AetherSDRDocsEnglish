# Change mode (USB, LSB, CW, AM, FM, etc.)

This page explains how to change the demodulation mode for a slice. Changing the mode reshapes the filter presets and tuning step sizes for the new mode automatically.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- Open the RX Controls applet if it is not already visible. Click the RX tray button on the right sidebar, or confirm the applet panel is shown via `View > Applet Panel`.

## Steps

1. If you have more than one slice, click the correct slice tab (A through H) at the top of the RX Controls applet to select the slice you want to change.
2. Locate the **Mode combo** in the RX Controls applet. It shows the current mode (default: **USB**).
3. Click the **Mode combo** to open the mode list.
4. Select the desired mode from the list.

The slice mode changes immediately. Filter preset buttons update to show widths appropriate for the new mode, and the tuning step list resets to the per-mode defaults.

## What each control does

| Control | Default | Valid values | Behavior |
|---|---|---|---|
| Mode combo | USB | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY | Sets the slice demodulation mode. Reshapes filter presets and step sizes for the selected mode. |
| Filter width presets | — | USB/LSB: 1800/2100/2400/2700/2900/3300 Hz; AM/SAM: 5600–14000 Hz; CW: 50/100/250/400 Hz; DIGU/DIGL: 100–2000 Hz; RTTY: 250–1000 Hz | Preset buttons update automatically when mode changes. Not shown for FM, NFM, or DFM. Persisted as `FilterPresets`. |
| STEP | 100 Hz (index 2) | SSB: 1/10/50/100/500/1000/2000/3000 Hz; CW: 1/5/10/50/100/200/400 Hz; FM: 50/250/500/2500/3000/5000/10000/12500 Hz (others vary) | Step list resets to per-mode values when mode changes. Use the **<** / **>** buttons or the mouse wheel to cycle through steps. |

## Tips

- FM family modes (FM, NFM, DFM) do not show filter preset buttons. CTCSS tone and repeater offset controls appear instead when one of these modes is selected.
- AGC mode controls are hidden in FM family modes.
- After switching to CW, check the QSK indicator. It lights amber when CW break-in is active, reflecting the state set in the CW applet.

## Troubleshooting

- **RADE mode is not in the list** — RADE requires a special build of AetherSDR. Your installed build does not include it.
- **Filter preset buttons are missing after switching mode** — This is expected for FM, NFM, and DFM. Those modes do not use variable filter presets.
- **Step sizes do not look right after a mode change** — The STEP control resets to per-mode defaults on a mode change. Use the **<** / **>** buttons to select the step size you want.

## Related

- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [RX Controls overview](overview.md)
