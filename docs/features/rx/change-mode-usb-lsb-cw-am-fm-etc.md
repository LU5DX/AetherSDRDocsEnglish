# Change mode (USB, LSB, CW, AM, FM, etc.)

Use this page to change the demodulation mode for a receive slice. Changing mode reshapes the filter presets and tuning step sizes to suit the new mode automatically.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet is only active when a radio connection is present.
- The RX Controls applet must be visible in the Applet Panel. If it is not, click the RX tray button on the right sidebar to show it.

## Steps

1. If you have more than one slice, click the appropriate slice tab (A through H) at the top of the RX Controls applet to select the slice you want to change.
2. Locate the **Mode combo** in the RX Controls applet. Its default value is USB.
3. Click the **Mode combo** to open the mode list.
4. Select the mode you want: USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, or RTTY.
5. The slice switches to the selected mode immediately. The filter preset buttons and tuning step sizes update to match the new mode.

## What each control does

| Control | Default | Valid values | Notes |
|---|---|---|---|
| Mode combo | USB | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY | Selecting a mode reshapes filter and step presets. |
| Filter width presets | mode-dependent | USB/LSB: 1800/2100/2400/2700/2900/3300 Hz; CW: 50/100/250/400 Hz; AM/SAM: 5600–14000 Hz; DIGU/DIGL: 100–2000 Hz; RTTY: 250–1000 Hz | Persisted as `FilterPresets`. Hidden for FM, NFM, and DFM modes. Right-click a preset button to save the current filter width as that preset. |
| STEP | 100 Hz (index 2) | Per-mode list; e.g. SSB: 1/10/50/100/500/1000/2000/3000 Hz; CW: 1/5/10/50/100/200/400 Hz; FM: 50/250/500/2500/3000/5000/10000/12500 Hz | Click `<` or `>`, or use the mouse wheel, to cycle through step sizes. |

## Tips

- FM, NFM, and DFM modes do not show filter preset buttons. Filter width is fixed for those modes.
- After switching to CW, the QSK indicator in the header row lights amber when CW break-in is active. That state is controlled from the CW applet, not here.
- Right-clicking a filter preset button saves the current passband width into that preset slot, stored as `FilterPresets`.

## Related

- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [RX Controls overview](overview.md)
