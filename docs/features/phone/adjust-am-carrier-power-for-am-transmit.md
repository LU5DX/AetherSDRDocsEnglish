# Adjust AM carrier power for AM transmit

Use the AM Carrier slider in the Phone applet to set the carrier power level when transmitting in AM mode. Lowering this value reduces the unmodulated carrier power; raising it increases it.

## Before you start

- AetherSDR must be connected to the radio. The Phone applet is unavailable without an active radio connection.
- Your slice must be set to AM mode before the AM carrier level has any effect on transmit.

## Steps

1. If the Phone applet is not visible in the right sidebar, click the **PHNE** tray button to show it.
2. Locate the **AM Carrier** row at the top of the Phone applet.
3. Drag the **AM Carrier** slider left to decrease carrier power or right to increase it. The numeric value to the right of the slider updates as you drag (for example, **48**).

## What each control does

| Control | Type | Valid range | Default | Persisted key |
|---|---|---|---|---|
| AM Carrier | Slider | 0–100 | — | — |

The numeric label next to the slider shows the current value. There is no persisted setting for AM Carrier level; the value is read from the radio on each connection.

## Tips

- The current level is displayed as a number to the right of the slider (for example, **48**). Use this to return to a known setting after experimenting.
- The AM Carrier slider has no effect when the slice is in a non-AM mode such as SSB or CW.

## Related

- [Phone overview](overview.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
