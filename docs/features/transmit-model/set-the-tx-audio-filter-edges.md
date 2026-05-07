# Set the TX audio filter edges

The TX audio filter edges define the low and high frequency boundaries of the transmitted audio signal. Adjust these two controls to shape the audio bandwidth sent to the radio.

## Steps

1. In the TX applet, locate the **Low Cut** spinbox and enter the desired low-frequency cutoff in Hz, or use the step buttons to snap to the nearest 50 Hz multiple. The default is **50 Hz**.
2. Locate the **High Cut** spinbox and enter the desired high-frequency cutoff in Hz, or use the step buttons to snap to the nearest 50 Hz multiple. The default is **3300 Hz**.

> Both values are sent to the radio together in a single command whenever either control changes.

## What each control does

| Control | Behavior |
|---|---|
| **Low Cut** | Sets the TX audio low-frequency cutoff in Hz. Step buttons snap to the nearest 50 Hz multiple. Valid range: 0–10000 Hz. Default: 50 Hz. |
| **High Cut** | Sets the TX audio high-frequency cutoff in Hz. Step buttons snap to the nearest 50 Hz multiple. Valid range: 0–10000 Hz. Default: 3300 Hz. |

## Tips

- Both `filter_low` and `filter_high` are always sent together; changing one control updates the radio with both current values.
- Narrowing the high cut (for example, to 2800 Hz) reduces transmitted bandwidth on crowded bands. Raising the low cut (for example, to 100–200 Hz) can reduce low-frequency rumble from the microphone.
- Values snap to 50 Hz multiples when using step buttons; you can type an arbitrary value directly into the spinbox.

## Related

- [transmit-model.md](transmit-model.md)
- [tx-profile.md](tx-profile.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
