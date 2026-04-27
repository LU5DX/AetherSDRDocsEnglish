# Tune the radio to a frequency (type MHz in the readout)

Type a frequency directly into the RX Controls applet to move the active slice's VFO to any frequency within the radio's tuning range.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. If not, go to `Settings > Connect to Radio...`.
- The RX Controls applet must be visible. If it is not, click the **RX** tray button on the right sidebar.
- Make sure the slice you want to tune is not locked. If the lock icon shows 🔒, click it to unlock before proceeding (see [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)).

## Steps

1. If you have more than one slice, click the appropriate slice tab (**A**, **B**, **C**, etc.) at the top of the RX Controls applet to select the slice you want to tune.
2. Click the **Frequency label** (the dotted readout, e.g. `0.000.000`). It switches into edit mode, becoming the **Frequency edit** field.
3. Type the desired frequency in MHz. For example, type `14.225` for 14.225 MHz.
4. Press **Enter**. The slice tunes to the entered frequency and the panadapter recenters on it.

To cancel without changing frequency, press **Escape**. The editor closes and the previous frequency is restored.

## What each control does

| Control | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Frequency label** | Displays the current VFO frequency with dotted grouping. Click to enter edit mode. | `0.000.000` | — | — |
| **Frequency edit** | Text field. Enter a frequency in MHz and press Enter to tune and recenter. Escape cancels. | — | 0.001–54.000 MHz (up to 450.000 MHz when the slice is on a transverter antenna) | — |
| **STEP** | Sets the step size used when nudging the frequency with the `<` / `>` buttons or the mouse wheel. | 100 Hz | Per-mode list (e.g. SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz) | — |
| **Filter width presets** | Click a preset button to apply that filter bandwidth for the current mode. Right-click a preset to save the current width into that slot. | — | USB/LSB: 1800–3300 Hz; AM/SAM: 5600–14000 Hz; CW: 50–400 Hz; DIG: 100–2000 Hz; RTTY: 250–1000 Hz | `FilterPresets` |

## Tips

- You do not need to type trailing zeros. `14.2` is interpreted as 14.200 MHz.
- To move frequency in small steps without retyping, use the `<` and `>` buttons next to **STEP**, or scroll the mouse wheel over the **Frequency label** after tuning.
- The step size list changes when you switch modes. Changing the **Mode combo** resets the step presets to values appropriate for that mode.

## Troubleshooting

- **The Frequency edit field does not appear when I click the readout** — The slice may be locked. Check whether the lock icon shows 🔒. If so, click it to unlock, then click the frequency readout again.
- **The frequency I typed was ignored** — You may have pressed Escape instead of Enter, or entered a value outside the valid range (0.001–54.000 MHz on a standard antenna, up to 450.000 MHz on a transverter antenna). Re-enter the value and press Enter.
- **The panadapter did not follow the new frequency** — Check that `View > Pan Follows VFO` is enabled.

## Related

- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
