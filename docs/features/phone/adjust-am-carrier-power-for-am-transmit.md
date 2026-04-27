# Adjust AM carrier power for AM transmit

Use this page to set the AM carrier power level when transmitting in AM mode. Adjusting the carrier level controls how much power the radio outputs as the AM carrier before audio modulation is applied.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Set the slice to AM mode before transmitting.

## Steps

1. Open the Phone applet by clicking the **PHNE** tray button in the right sidebar. If the applet panel is not visible, click **View > Applet Panel** to show it.
2. Locate the **AM Carrier** row at the top of the Phone applet.
3. Drag the **AM Carrier** slider left to decrease or right to increase the carrier power level. The numeric label to the right of the slider updates immediately to show the current value (for example, `48`).

## What each control does

| Control | Description | Valid range | Default |
|---|---|---|---|
| **AM Carrier** slider | Sets the AM carrier power level sent to the radio. | 0–100 | None stored; reflects radio state |

## Tips

- The numeric label next to the slider shows the current value in real time. Use it to set a precise level without guessing the slider position.
- The AM Carrier slider has no persisted setting key. Its value is read from the radio on connect and reset if you reconnect.

## Related

- [Phone overview](overview.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
