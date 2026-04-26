# Change mode (USB, LSB, CW, AM, FM, etc.)

This page explains how to change the demodulation mode for a slice using the RX Controls applet. Changing the mode reshapes the filter presets and tuning step list to suit the new mode.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet is not functional without a radio connection.
- Identify which slice you want to change. If you have more than one slice active, select it first using the slice tabs (A..H) at the top of the RX Controls applet.

## Steps

1. Open the RX Controls applet. If it is not visible, click the **RX** tray button on the right sidebar.
2. If multiple slices are in use, click the tab labelled with the slice letter (A through H) that you want to change.
3. Locate the **Mode combo** box in the applet. Its current value is shown (default: **USB**).
4. Click the **Mode combo** to open the mode list.
5. Select the mode you want: **USB**, **LSB**, **CW**, **AM**, **SAM**, **FM**, **NFM**, **DFM**, **DIGU**, **DIGL**, or **RTTY**.
6. The slice switches to the selected mode. The filter preset buttons and tuning step list update automatically to match the new mode.

## What each control does

| Control | Default | Valid options | Notes |
|---|---|---|---|
| Mode combo | USB | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY | Changing mode reshapes filter presets and step sizes. |
| Filter width presets | (mode-dependent) | USB/LSB: 1800/2100/2400/2700/2900/3300 Hz; CW: 50/100/250/400 Hz; AM/SAM: 5600–14000 Hz; DIGU/DIGL: 100–2000 Hz; RTTY: 250–1000 Hz | Buttons are hidden in FM, NFM, and DFM modes. Presets are stored in `FilterPresets`. Right-click a preset button to save the current width as that preset. |
| STEP | 100 Hz (index 2) | USB/LSB: 1/10/50/100/500/1000/2000/3000 Hz; CW: 1/5/10/50/100/200/400 Hz; FM family: 50/250/500/2500/3000/5000/10000/12500 Hz | Step list is per-mode and updates automatically when the mode changes. |

## Tips

- FM, NFM, and DFM modes do not show filter width preset buttons. Use the filter passband widget to drag the lo/hi edges if you need to adjust the passband directly.
- After switching to FM or NFM, additional controls appear: **Tone mode**, **CTCSS tone value**, **Offset**, **−**, **Simplex**, **+**, and **REV** for repeater operation.
- Right-clicking a filter preset button saves the current filter width into that preset slot, which is persisted in `FilterPresets`.

## Troubleshooting

- **Mode combo is not responsive** — The applet requires an active radio connection. Check that AetherSDR is connected via `Settings > Connect to Radio...`.
- **RADE mode does not appear in the list** — RADE requires a build of AetherSDR compiled with the RADE option. Standard builds do not include it.

## Related

- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [RX Controls overview](overview.md)
