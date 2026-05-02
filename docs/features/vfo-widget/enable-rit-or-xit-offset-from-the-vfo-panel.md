# Enable RIT or XIT offset from the VFO panel

RIT (Receiver Incremental Tuning) and XIT (Transmitter Incremental Tuning) let you shift the receive or transmit frequency by a small offset without moving the main VFO. This is useful for working split-frequency contacts or compensating for a station that is slightly off your dial frequency.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires a live radio connection.
- The VFO panel for the target slice must be open and expanded. If it is collapsed to the frequency-only strip, click anywhere on it to expand it.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel appears anchored to the marker.
2. Click the **X/RIT** tab inside the VFO panel.
3. To enable receiver offset, click the **RIT** button. The button activates and the label shows the current RIT offset.
4. To enable transmitter offset, click the **XIT** button. The button activates and the label shows the current XIT offset.
5. With RIT or XIT active, place the mouse pointer over the corresponding button and scroll the mouse wheel to adjust the offset. Each scroll step changes the offset by 10 Hz.
6. To disable RIT or XIT, click the active button again.

## What each control does

| Control | Kind | Default | Valid range | Persisted setting |
|---|---|---|---|---|
| RIT button + label | Toggle button | off | — | — |
| XIT button + label | Toggle button | off | — | — |

**RIT / XIT buttons + labels** — Enable receiver (RIT) or transmitter (XIT) incremental tuning for this slice. When active, the label next to each button shows the current offset value. Scroll the mouse wheel over the button to adjust the offset in 10 Hz steps. Neither setting is persisted; state reflects live radio state.

## Tips

- RIT and XIT offsets are independent. You can enable both at the same time to offset receive and transmit independently.
- Scroll-wheel adjustment is 10 Hz per step. For larger offsets, scroll multiple notches.

## Related

- [VFO Panel overview](overview.md)
- [Change mode from the VFO panel](change-mode-from-the-vfo-panel.md)
- [Tune the radio by typing a frequency into the VFO panel](tune-the-radio-by-typing-a-frequency-into-the-vfo-panel.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
