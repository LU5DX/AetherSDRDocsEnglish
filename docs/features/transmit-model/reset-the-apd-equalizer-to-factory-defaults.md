# Reset the APD equalizer to factory defaults

The Transmit Model manages adaptive pre-distortion (APD) state for the connected radio. Use the steps below to turn APD off, which restores the equalizer to its factory default (disabled) state.

## Before you start

- Confirm your radio reports `apd configurable=1`. If the APD row is not visible in the TX applet, your radio does not support APD and no action is needed.

## Steps

1. Locate the **APD** toggle button in the TX applet.
2. If **APD** is lit (on), click it once to turn it off. The button returns to its default off state, disabling adaptive pre-distortion on the radio.

## What each control does

| Control | Behavior |
|---|---|
| **APD** | Enables or disables adaptive pre-distortion on the radio. Default is off. Hidden on radios that do not report `apd configurable=1`. |

## Tips

- The APD row does not appear on all radios. If you cannot see it, your hardware does not support adaptive pre-distortion and no reset is required.
- Turning APD off is the factory default state. There is no separate "reset" command — toggling the button off is equivalent to restoring factory defaults.

## Related

- [transmit-model.md](transmit-model.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
