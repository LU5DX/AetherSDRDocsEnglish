# Lock the slice to prevent accidental retuning

The tune-lock feature prevents a slice from responding to frequency changes. Use it when you want to monitor a fixed frequency without the risk of nudging the VFO by clicking the panadapter or scrolling the mouse wheel.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- The RX Controls applet must be visible. If it is not, click the RX tray button on the right sidebar to show it.

## Steps

1. In the RX Controls applet, identify the header row containing the slice badge, lock button, and antenna selectors.
2. If you have more than one slice, click the appropriate slice tab (A through H) to select the slice you want to lock.
3. Click the 🔓 button in the header row. The icon changes to 🔒 and turns blue, confirming the slice is locked.
4. To unlock, click 🔒 again. The icon returns to 🔓 and the slice resumes responding to frequency changes.

## What each control does

| Control | Default | Behavior |
|---|---|---|
| 🔓 / 🔒 | 🔓 (unlocked) | Toggles tune-lock on the active slice. When locked (🔒), the slice ignores all frequency changes. Click again to unlock. |

## Tips

- The lock state applies per slice. You can lock slice A while slice B remains freely tunable.
- The lock button is always visible in the header row regardless of the current mode.

## Related

- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
