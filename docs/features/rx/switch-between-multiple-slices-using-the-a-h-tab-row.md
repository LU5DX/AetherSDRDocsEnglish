# Switch between multiple slices using the A..H tab row

The FLEX-8600 supports up to eight simultaneous receive slices. The A..H tab row at the top of the RX Controls applet lets you switch which slice the applet is bound to, so you can view and adjust each slice's mode, frequency, filter, and other settings independently.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The RX Controls applet requires an active radio connection.
- The radio must have more than one slice active. The tab row is hidden when only one slice exists.
- The RX Controls applet must be visible. If it is not, click the RX tray button on the right sidebar to show it.

## Steps

1. Look at the top of the RX Controls applet for the horizontal row of lettered tabs (A, B, C, and so on, up to H).
2. Click the tab letter that corresponds to the slice you want to inspect or control.
3. Confirm the switch: the **Slice badge** in the header row updates to show the letter of the newly selected slice, coloured by its slice identity.
4. All controls below the tab row — mode, frequency, filter, AGC, AF gain, and others — now reflect and control the selected slice.

## What each control does

| Control | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|
| Slice tabs (A..H) | Selects which slice the RX Controls applet is bound to. | — | 1–8 tabs, capped by the radio's maximum slice count | — |
| Slice badge | Displays the letter of the currently bound slice, coloured by slice identity. | A | A / B / C / D / E / F / G / H | — |

## Tips

- The tab row is hidden entirely when the radio reports a maximum slice count of 1. If you do not see any tabs, only one slice is configured on the radio.
- Each slice retains its own mode, frequency, filter presets, AGC settings, and antenna selection. Switching tabs does not alter any slice's settings; it only changes which slice the applet displays.
- Filter width presets are saved per mode via the `FilterPresets` setting. Presets you save on slice A in USB mode apply to USB mode on all slices.

## Related

- [RX Controls overview](overview.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
