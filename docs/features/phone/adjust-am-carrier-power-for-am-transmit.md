# Adjust AM carrier power for AM transmit

Use this page to set the AM carrier power level when transmitting in AM mode. The carrier level controls how much of the transmitter power is devoted to the unmodulated carrier.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The radio must be set to AM mode before the AM Carrier level has any effect on transmit.
- The Phone applet must be visible in the Applet Panel.

## Steps

1. If the Phone applet is not visible, click the **PHNE** tray button on the right sidebar to show it.
2. Locate the **AM Carrier** slider in the Phone applet.
3. Drag the **AM Carrier** slider left or right to set the desired carrier level. The numeric value (0–100) updates next to the slider as you drag.

## What each control does

| Control | Type | Range | Default | Persisted key |
|---|---|---|---|---|
| AM Carrier | Slider | 0–100 | — | — |

The numeric label to the right of the **AM Carrier** slider shows the current value (for example, `48`). This value is sent directly to the radio and is not saved by AetherSDR between sessions; the radio restores it from its own state on reconnect.

## Tips

- The AM Carrier level applies only while the radio is in AM mode. Adjusting it in other modes has no audible effect but the value is still sent to the radio.
- A carrier level of 0 suppresses the carrier entirely; a level of 100 sets full carrier power as allowed by the radio's TX band settings.

## Related

- [Phone overview](overview.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
