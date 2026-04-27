# Tune VOX hang time

The VOX hang time controls how long the radio stays in transmit after your voice drops below the VOX trigger threshold. Adjusting it prevents choppy transmit drop-outs at the end of words while avoiding excessive dead air before returning to receive.

## Before you start

- AetherSDR must be connected to the radio. The Phone applet requires an active radio connection.
- VOX must be enabled. If VOX is not already on, enable it first — see [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md).

## Steps

1. Open the Phone applet by clicking the **PHNE** tray button in the right sidebar. If the applet panel is hidden, click the panel edge or use `View > Applet Panel` to show it.
2. Locate the **Delay:** row, directly below the VOX level row.
3. Drag the **Delay** slider left to shorten hang time or right to lengthen it. The numeric value to the right of the slider updates as you drag.

## What each control does

| Control | Description | Valid range | Default |
|---|---|---|---|
| **Delay** slider | Sets the VOX hang time — how long the radio remains in transmit after speech ends before returning to receive. | 0–100 | — |

No setting key is persisted for the Delay slider; the value is sent directly to the radio.

## Tips

- A Delay value that is too low causes the transmitter to drop in and out between words. Raise the value until tail drop-outs stop.
- A Delay value that is too high keeps the transmitter keyed well after you finish speaking, blocking other stations. Lower the value until the hang is just long enough to cover normal pauses.
- The VOX level threshold and Delay interact: a more sensitive (lower) VOX level may require a shorter Delay, and vice versa.

## Related

- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Phone overview](overview.md)
