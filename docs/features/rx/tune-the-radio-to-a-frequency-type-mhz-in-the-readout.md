# Tune the radio to a frequency (type MHz in the readout)

Type a frequency directly into the VFO readout to retune the active slice. Use this when you know the exact frequency and want to go there immediately without clicking the panadapter.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet will be blank if there is no connection.
- The RX Controls applet must be visible. If it is not, click the **RX** tray button on the right sidebar to show it.
- The slice must not be tune-locked. If the 🔒 icon is shown, the slice will ignore frequency changes. See [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md).

## Steps

1. In the RX Controls applet, confirm the correct slice tab is selected (A through H). If you have more than one slice, click the appropriate tab to make it active.
2. Click the **Frequency label** — the dotted frequency readout (e.g. `14.225.000`). Clicking it switches it into edit mode, replacing the label with a text field.
3. Type the desired frequency in MHz. For example, type `14.225` for 14.225 MHz. The field accepts values from 0.001 to 54.000 MHz. If the slice is on a transverter antenna, values up to 450.000 MHz are accepted.
4. Press **Enter**. The radio tunes to the entered frequency and the panadapter recenters on it.

## What each control does

| Control | Behavior | Default | Valid range |
|---|---|---|---|
| **Frequency label** | Displays the current VFO frequency with dotted grouping. Click to enter edit mode. | `0.000.000` | — |
| **Frequency edit** | Text field that appears after clicking the label. Enter MHz and press Enter to tune and recenter. Supports kHz/Hz auto-scaling. | — | 0.001–54.000 MHz (up to 450.000 MHz on a transverter antenna) |
| **STEP** | Sets the tuning step size used by the `<` / `>` buttons and mousewheel. Step list depends on the current mode. | 100 Hz | SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz; other modes vary |

## Tips

- After entering a frequency, the panadapter recenters automatically to keep the VFO visible. If you prefer the panadapter not to follow, uncheck **View > Pan Follows VFO**.
- For small adjustments after typing a frequency, use the mousewheel over the **Frequency label** or click the `<` / `>` buttons next to **STEP** to nudge by the current step size.
- To avoid accidentally retuning a slice while adjusting other controls, enable tune-lock by clicking the 🔓 icon so it shows 🔒.

## Troubleshooting

- **Pressing Enter has no effect** — The slice may be tune-locked (🔒 is shown in the header row). Click 🔒 to unlock it, then re-enter the frequency.
- **Frequency entry field does not appear** — The radio connection may have dropped. Check the connection status and reconnect via **Settings > Connect to Radio...** if needed.
- **Entered frequency is not accepted** — The value may be out of range. Valid input is 0.001–54.000 MHz (or up to 450.000 MHz on a transverter antenna). Confirm the slice antenna is correct.

## Related

- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
