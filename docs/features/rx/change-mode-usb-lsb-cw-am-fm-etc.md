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

| Control                    | Default          | Valid values                                                                                                                       |
|----------------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------|
| **Mode combo**             | USB              | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY (+ RADE if available)                                                        |
| **Filter width presets**   | Mode-dependent   | USB/LSB: 1800/2100/2400/2700/2900/3300 Hz; CW: 50/100/250/400 Hz; AM/SAM: 5600–14000 Hz; DIGU/DIGL: 100–2000 Hz; RTTY: 250–1000 Hz |
| **STEP**                   | 100 Hz (index 2) | Per-mode list (e.g. SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz; CW: 1, 5, 10, 50, 100, 200, 400 Hz; FM family: 50–12500 Hz)     |
| **Filter passband widget** | —                | Drag lo/hi edges                                                                                                                   |
## Tips

- FM, NFM, and DFM modes do not show filter width preset buttons. The filter is fixed for those modes.
- After switching to FM or NFM, the CTCSS tone and repeater offset controls (**Tone mode**, **Offset**, **−**, **Simplex**, **+**, **REV**) become visible. See [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md) for details.
- After switching to CW, the **QSK** indicator in the header becomes relevant. Its state is controlled from the CW applet, not from RX Controls.
- AGC mode controls are hidden when an FM family mode is active.
- Filter presets are now stored in a `lo:hi` format (e.g. `300:3000`) as well as the older plain-width format. Both formats are read correctly. If you have saved custom presets from an earlier version, they continue to work without any action on your part.
- The `stepFilterWidth()` method walks the per-mode preset list so widen/narrow shortcuts produce mode-correct edge geometry. This ensures that when you widen or narrow the filter using keyboard shortcuts, the filter stays within the appropriate preset boundaries for the current mode.

## Slice tab behaviour (v0.9.5.1)

When the radio reports a change in the number of available slices, the A..H tab row is now rebuilt correctly instead of being skipped. The previous behaviour kept the old buttons if any were already present; v0.9.5.1 tears down and recreates the buttons whenever the slice count changes (`clearSliceButtons()`, #2254). On disconnect the tab row is hidden and the static **Slice badge** is restored automatically.

Signal connections for slice button clicks are also guarded so that reconnecting to the radio does not attach duplicate handlers.

## Filter width formatting (v0.9.8)

The filter width readout in the RX Controls applet now uses mode-specific logic to display the correct labelled width. This readout is shared with the VFO panel for consistent formatting (#2197). The `formatFilterWidth()` static method applies mode-aware rules so that SSB and digital modes display the expected bandwidth label (e.g., "2.7K" for 2700 Hz USB, "500" for 500 Hz CW).

## Troubleshooting

- **Mode combo is missing or grayed out** — The applet is not connected to the radio. Check the connection via `Settings > Connect to Radio...`.
- **Filter preset buttons disappeared after changing mode** — This is expected when switching to FM, NFM, or DFM. Those modes do not use filter presets.
- **Slice tabs show the wrong number of buttons after reconnecting** — This was a known issue fixed in v0.9.5.1 (#2254). Update to the current release if you see stale tab buttons.

## Related

- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)