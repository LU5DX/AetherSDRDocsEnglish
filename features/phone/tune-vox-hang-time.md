# Tune VOX hang time

VOX hang time controls how long the radio stays in transmit after your voice drops below the VOX threshold. Adjusting it prevents the radio from chopping off the end of your transmission or staying in TX too long between words.

## Before you start

- AetherSDR must be connected to the radio. The Phone applet is unavailable without a radio connection.
- VOX must be enabled. See [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md).

## Steps

1. Click the **PHNE** tray button on the right sidebar to open the Phone applet.
2. Locate the **Delay** slider in the Phone applet.
3. Drag the **Delay** slider left to shorten hang time or right to lengthen it. The numeric readout to the right of the slider updates as you drag.

## What each control does

| Control | Description | Valid range | Default | Setting key |
|---|---|---|---|---|
| **Delay** | Sets VOX hang time — how long the radio remains in transmit after audio falls below the VOX threshold. | 0–100 | — | — |

## Tips

- If the radio drops back to receive between words, increase **Delay**.
- If the radio lingers in transmit too long after you stop speaking, decrease **Delay**.

## Related

- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Phone overview](overview.md)
