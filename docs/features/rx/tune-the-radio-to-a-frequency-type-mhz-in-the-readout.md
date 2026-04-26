# Tune the radio to a frequency (type MHz in the readout)

Click the frequency readout in the RX Controls applet to open a text field, type a frequency in MHz, and press Enter to tune the slice to that frequency.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. If you are not connected, go to `Settings > Connect to Radio...`.
- The RX Controls applet must be visible. If it is not, click the RX tray button on the right sidebar.
- If the slice is locked, tuning is ignored. Unlock it first — see [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md).

## Steps

1. If you have more than one slice, click the appropriate tab (A through H) at the top of the RX Controls applet to select the slice you want to tune.
2. Click the frequency label — the dotted readout showing the current VFO frequency (for example, `14.225.000`). The readout switches to a text entry field.
3. Type the desired frequency in MHz (for example, `14.225`). The field accepts values from 0.001 to 54.000 MHz. If the slice is on a transverter antenna, values up to 450.000 MHz are accepted.
4. Press Enter. The slice tunes to the entered frequency and the panadapter recenters on it.

To cancel without tuning, press Escape. The previous frequency is restored and the editor closes.

## What each control does

| Control | Behavior | Default | Valid range |
|---|---|---|---|
| Frequency label | Displays the current VFO frequency with dotted grouping. Click to enter edit mode. | `0.000.000` | — |
| Frequency edit | Text field. Type a frequency in MHz and press Enter to tune and recenter. Press Escape to cancel. | — | 0.001–54.000 MHz (up to 450.000 MHz on a transverter antenna) |
| STEP | Sets the tuning step size used by the `<` / `>` buttons and the mouse wheel. Click `<` or `>`, or scroll the mouse wheel over the readout area, to step the frequency up or down. | 100 Hz | Per-mode list; for SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz |
| 🔓 / 🔒 | Locks or unlocks the slice. A locked slice ignores frequency changes from any source. | 🔓 (unlocked) | — |

## Tips

- You do not need to type leading zeros or trailing zeros. Typing `7.2` tunes to 7.200.000 MHz.
- If you tune by mouse wheel or the STEP `<` / `>` buttons instead of typing, the step size is determined by the STEP control. Change the step size first if you want coarser or finer steps.
- Filter presets are stored per mode in `FilterPresets`. Changing frequency does not alter the current filter width or mode.

## Troubleshooting

- **Clicking the frequency readout does nothing** — The slice may be locked. Check the 🔓 / 🔒 button in the header row; if it shows 🔒, click it to unlock.
- **The radio does not tune to the typed frequency** — Confirm the value is within the valid range (0.001–54.000 MHz, or up to 450.000 MHz on a transverter antenna). Values outside the range are rejected and the previous frequency is restored.
- **The panadapter does not follow the new frequency** — Check that `View > Pan Follows VFO` is enabled.

## Related

- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
