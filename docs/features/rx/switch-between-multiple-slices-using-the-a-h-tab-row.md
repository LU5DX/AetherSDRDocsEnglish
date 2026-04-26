# Switch between multiple slices using the A..H tab row

The FLEX-8600 supports up to eight simultaneous receive slices. The A..H tab row in the RX Controls applet lets you move between those slices so the applet's controls apply to the one you want.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The tab row is not visible otherwise.
- The radio must have more than one slice active. The tab row is hidden when only one slice exists.
- The RX Controls applet must be open in the Applet Panel. If it is not visible, click the **RX** tray button on the right sidebar.

## Steps

1. Look at the top of the RX Controls applet for a row of lettered buttons (A, B, C, and so on).
2. Click the letter of the slice you want to work with (for example, **B**).
3. Confirm the change: the **Slice badge** (the small coloured square at the left of the header row) updates to show the selected letter, and all controls below — frequency, mode, filter, AGC, and so on — now reflect that slice.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Slice tabs (A..H) | Selects which slice the RX applet is bound to. | 1–8 buttons, capped by the radio's maximum slice count. Row is hidden when only one slice is present. |
| Slice badge | Displays the letter of the currently bound slice. | Coloured by slice identity. Updates immediately when you click a tab. |

## Tips

- The tab row shows only as many buttons as the radio has slices available, up to a maximum of eight (A through H).
- After switching slices, check the **Slice badge** to confirm which slice is active before changing mode, frequency, or filter settings.
- Filter width presets are stored per-mode under the `FilterPresets` setting. Switching slices does not change your saved presets, but the displayed preset buttons will reflect the mode and filter of the newly selected slice.

## Related

- [RX Controls overview](overview.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
