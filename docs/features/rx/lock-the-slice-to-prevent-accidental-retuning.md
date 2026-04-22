# Lock the slice to prevent accidental retuning

The tune-lock feature prevents a slice from responding to frequency changes, such as accidental panadapter clicks or scroll-wheel movement. Use it to hold a monitoring frequency steady while you work another slice.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet is not functional without a radio connection.
- The RX applet must be visible. If it is not, click the RX tray button on the right sidebar to show it.

## Steps

1. In the RX applet header row, locate the padlock icon. When the slice is unlocked, the icon shows 🔓.
2. Click 🔓. The icon changes to 🔒 and turns blue. The slice now ignores frequency changes.
3. To unlock, click 🔒 again. The icon returns to 🔓 and normal tuning resumes.

## What each control does

| Control | Default | Behavior |
|---|---|---|
| 🔓 / 🔒 | 🔓 (unlocked) | Toggles tune-lock on the active slice. When locked (🔒), the slice ignores all frequency change commands. Click again to unlock. |

## Tips

- The lock applies to the slice currently shown in the RX applet. If you have multiple slices, check the slice badge (A, B, C, …) in the header row to confirm which slice you are locking before clicking.
- Locking a slice does not affect its audio, filter, mode, or AGC settings — only tuning is blocked.

## Related

- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
