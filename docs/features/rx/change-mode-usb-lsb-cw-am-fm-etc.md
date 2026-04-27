# Change mode (USB, LSB, CW, AM, FM, etc.)

This page explains how to select a receive mode for a slice. Changing the mode reshapes the filter presets and tuning step sizes to suit the new modulation.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- If you have more than one slice, select the correct slice first using the A..H tab row at the top of the RX Controls applet.

## Steps

1. If the RX Controls applet is not visible, click the **RX** tray button on the right sidebar to show it.
2. If your radio has more than one slice active, click the appropriate slice tab (**A** through **H**) to bind the applet to the slice you want to change.
3. Click the **Mode combo** drop-down. The current mode is shown (default: **USB**).
4. Select the desired mode from the list:
   - **USB**, **LSB**, **CW**, **AM**, **SAM**, **FM**, **NFM**, **DFM**, **DIGU**, **DIGL**, **RTTY**
   - (RADE appears only in builds with RADE support enabled.)
5. The slice switches to the selected mode. The filter width presets and tuning step sizes update automatically to suit the new mode.

## What each control does

| Control | Default | Valid values | Notes |
|---|---|---|---|
| **Mode combo** | USB | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY (+ RADE if available) | Changing mode reshapes filter presets and step sizes. |
| **Filter width presets** | Mode-dependent | USB/LSB: 1800/2100/2400/2700/2900/3300 Hz; CW: 50/100/250/400 Hz; AM/SAM: 5600–14000 Hz; DIGU/DIGL: 100–2000 Hz; RTTY: 250–1000 Hz | Buttons are hidden for FM, NFM, and DFM modes. Right-click a preset button to save the current filter width to that slot. Persisted in `FilterPresets`. |
| **STEP** | 100 Hz (index 2) | Per-mode list (e.g. SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz; CW: 1, 5, 10, 50, 100, 200, 400 Hz; FM family: 50–12500 Hz) | Use the **<** / **>** buttons or the scroll wheel to cycle through available step sizes. |
| **Filter passband widget** | — | Drag lo/hi edges | Fine-tune the passband independently of the presets. |

## Tips

- FM, NFM, and DFM modes do not show filter width preset buttons. The filter is fixed for those modes.
- After switching to FM or NFM, the CTCSS tone and repeater offset controls (Tone mode, Offset, −, Simplex, +, REV) become visible. See [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md) for details.
- After switching to CW, the **QSK** indicator in the header becomes relevant. Its state is controlled from the CW applet, not from RX Controls.
- AGC mode controls are hidden when an FM family mode is active.

## Troubleshooting

- **Mode combo is missing or grayed out** — The applet is not connected to the radio. Check the connection via `Settings > Connect to Radio...`.
- **Filter preset buttons disappeared after changing mode** — This is expected when switching to FM, NFM, or DFM. Those modes do not use filter presets.

## Related

- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
