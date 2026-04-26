# Tune VOX hang time

VOX hang time controls how long the radio stays in transmit after your voice drops below the VOX threshold. Adjusting it prevents the radio from cutting back to receive too quickly between words.

## Before you start

- AetherSDR must be connected to the radio. The Phone applet is unavailable when disconnected.
- VOX must be enabled. See [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md).

## Steps

1. Open the Phone applet in the Applet Panel. If it is not visible, click the **PHNE** tray button on the right sidebar.
2. Locate the **Delay** row beneath the VOX level row.
3. Drag the **Delay** slider left to shorten hang time or right to lengthen it. The numeric readout to the right of the slider updates as you drag.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Delay** | Sets VOX hang time — how long the radio remains in transmit after audio drops below the VOX threshold. | — | 0–100 | — |

No value for the default is available in the catalog. The range is 0 to 100 (unitless scale sent to the radio).

## Tips

- If the radio drops to receive in the middle of a sentence, increase **Delay**.
- If the radio stays in transmit too long after you stop speaking, decrease **Delay**.
- The **Delay** slider has no effect unless **VOX** is enabled.

## Related

- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)
- [Phone overview](overview.md)
