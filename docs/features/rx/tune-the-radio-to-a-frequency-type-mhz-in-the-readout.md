# Tune the radio to a frequency (type MHz in the readout)

Type a frequency directly into the VFO readout to retune the active slice. Use this method when you want to jump to a specific frequency rather than clicking the panadapter or scrolling the step control.

## Before you start

- AetherSDR must be connected to the radio. If not, go to `Settings > Connect to Radio...` and establish a connection.
- The RX Controls applet must be visible. If it is not, click the **RX** tray button on the right sidebar to show it.
- The slice you want to tune must not be locked. A closed padlock (🔒) in the applet header means the slice is locked and will ignore frequency changes. See [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md).

## Steps

1. If you have more than one slice, click the correct slice tab (**A**, **B**, **C**, etc.) in the RX Controls applet to make it active.
2. Click the **Frequency label** (the dotted readout, e.g. `14.225.000`). The label switches to an editable text field.
3. Type the frequency in MHz, for example `14.225` or `7.074`. The field accepts values from 0.001 to 54.000 MHz. If the slice is on a transverter antenna, the field accepts up to 450.000 MHz.
4. Press **Enter**. The slice tunes to the entered frequency and the panadapter recenters on it.

## What each control does

| Control | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Frequency label** | Displays the current VFO frequency with dotted grouping. Click to enter edit mode. | `0.000.000` | — | — |
| **Frequency edit** | Text field that appears after clicking the label. Enter MHz and press Enter to tune and recenter. Supports kHz/Hz auto-scaling. | — | 0.001–54.000 MHz (up to 450.000 MHz on XVTR) | — |
| **STEP** | Sets the tuning step size used when scrolling or using the **<** / **>** buttons. Cycles through a per-mode list. | 100 Hz (index 2) | SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz; CW: 1, 5, 10, 50, 100, 200, 400 Hz; FM: 50–12500 Hz (see mode list) | — |
| **Filter width presets** | Buttons that apply a preset filter width for the current mode. Right-click a button to save the current width as that preset. Hidden in FM, NFM, and DFM modes. | — | USB/LSB: 1800–3300 Hz; CW: 50–400 Hz; AM/SAM: 5600–14000 Hz; DIG: 100–2000 Hz; RTTY: 250–1000 Hz | `FilterPresets` |

## Tips

- If you enter a value without a decimal point, AetherSDR applies kHz/Hz auto-scaling. For example, entering `14225` is interpreted as 14.225 MHz.
- After tuning, the panadapter recenters automatically. To disable this, uncheck `View > Pan Follows VFO`.
- To fine-tune after entering a frequency, use the **STEP** control's **<** / **>** buttons or the mouse wheel over the frequency display.

## Troubleshooting

- **Clicking the frequency label does nothing** — The slice may be locked. Check whether the padlock icon in the applet header shows 🔒. If so, click it to unlock the slice.
- **Frequency reverts immediately after pressing Enter** — The entered value may be outside the valid range (0.001–54.000 MHz on a standard antenna port). Verify the frequency and try again. If the slice is on a transverter antenna, values up to 450.000 MHz are accepted.
- **The Frequency label is not visible** — The RX Controls applet may be collapsed or hidden. Click the **RX** tray button on the right sidebar to toggle it.

## Related

- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
