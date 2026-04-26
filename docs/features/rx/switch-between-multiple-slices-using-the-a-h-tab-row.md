# Switch between multiple slices using the A..H tab row

The RX Controls applet shows a row of lettered tabs — A through H — when the radio has more than one slice active. Clicking a tab binds the entire RX Controls applet to that slice, letting you adjust its frequency, mode, filter, and other settings independently.

## Before you start

- AetherSDR must be connected to the radio. The tab row requires a live radio connection.
- At least two slices must exist on the radio. The tab row is hidden when only one slice is active.

## Steps

1. Open the RX Controls applet in the Applet Panel. If it is not visible, click the RX tray button on the right sidebar.
2. Locate the slice tab row at the top of the RX Controls applet. Tabs are labelled A, B, C, and so on, up to H, with one tab per active slice.
3. Click the tab letter for the slice you want to control (for example, B to switch to slice B).
4. Confirm the switch: the slice badge below the tab row updates to the letter of the selected slice, and all controls in the applet — mode, frequency, filter width, antenna, and so on — reflect that slice's current state.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Slice tabs (A..H) | Selects which slice the RX Controls applet is bound to. | Row is hidden when the radio reports only one slice. Between 1 and 8 tabs appear, capped by the radio's maximum slice count. |
| Slice badge | Displays the letter of the currently bound slice (A/B/C/D/E/F/G/H). | Coloured by slice identity. Updates immediately when you click a tab. |

No persisted setting key is associated with the slice tab selection itself. Filter width presets are stored per-mode under `FilterPresets`.

## Tips

- The tab row only appears when `maxSlices` is greater than 1. If you see no tabs, the radio currently has only a single slice configured.
- Switching tabs does not change anything on the radio; it only changes which slice the local RX Controls applet is viewing and editing.
- Each slice retains its own mode, frequency, filter, antenna, AGC, and RIT/XIT settings. Switching tabs lets you inspect or adjust a slice without disturbing the others.

## Related

- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
- [RX Controls overview](overview.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
