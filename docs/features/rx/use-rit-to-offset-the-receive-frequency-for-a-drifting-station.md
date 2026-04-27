# Use RIT to offset the receive frequency for a drifting station

RIT (Receive Incremental Tuning) shifts the receive frequency by a small amount without moving the transmit frequency or the VFO readout. Use it when a station drifts slightly off your dial frequency and you want to track them without retuning the whole slice.

## Before you start

- AetherSDR must be connected to the radio. RIT controls are inactive without a radio connection.
- Open the RX Controls applet. Click the RX tray button on the right sidebar if the applet is not visible.
- Select the slice you want to adjust using the slice tabs (A..H) at the top of the applet, if more than one slice is active.

## Steps

1. In the RX Controls applet, locate the RIT row near the bottom of the applet.
2. Click RIT to enable Receive Incremental Tuning. The button lights when active.
3. Use the `<` and `>` buttons beside the RIT offset spinbox, or scroll the mousewheel over the spinbox, to adjust the offset. Each step moves the receive frequency by 10 Hz. The spinbox displays the current offset (default: `+0 Hz`).
4. Continue adjusting until the drifting station is centred in the passband.
5. To return to zero offset without disabling RIT, click RIT 0. The offset resets to `+0 Hz`.
6. To turn off RIT entirely, click RIT again. The receive frequency returns to the VFO frequency.

## What each control does

| Control | Kind | Default | Behavior |
|---|---|---|---|
| RIT | Toggle button | Off | Enables or disables Receive Incremental Tuning. |
| RIT offset | Spinbox | `+0 Hz` | Displays the current RIT offset. Use `<` / `>` or the mousewheel to adjust in 10 Hz steps. |
| RIT 0 | Push button | — | Zeroes the RIT offset without disabling RIT. |

## Tips

- RIT affects only the receive frequency. Your transmit frequency stays on the VFO. If you also need to offset your transmit frequency, use XIT instead of or alongside RIT.
- The 10 Hz minimum step suits SSB and CW work. For a station drifting slowly, a few presses of `>` or a short mousewheel scroll is usually enough.
- Clicking RIT 0 before turning RIT off is good practice. It means RIT is already zeroed if you re-enable it later.

## Related

- [Use XIT to offset the transmit frequency without changing RX](use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
