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

| Control | Default      | Behavior                                                                                                                |
|---------|--------------|-------------------------------------------------------------------------------------------------------------------------|
| 🔓 / 🔒   | 🔓 (unlocked) | Toggles tune-lock on the active slice. When locked (🔒), the slice ignores all frequency changes. Click again to unlock. |

## Tips

- The lock state applies per slice. You can lock slice A while slice B remains freely tunable.
- The lock button is always visible in the header row regardless of the current mode.
- From v0.9.3, the slice tab buttons and the slice badge both use per-slice colors managed by SliceColorManager. Colors are customizable per slice and persist across sessions. The same color is reflected in the slice tab buttons, the slice badge, VFO widgets, and meter strips.

## NT mode

Version 0.9.3 adds the `NT` mode alongside the existing digital modes (`DIGU`, `DIGL`). It behaves identically to other digital modes in the following ways:

- **Filter presets** — NT shares the DIG filter preset set (100–2000 Hz). The filter width label updates accordingly.
- **Filter width calculation** — The filter width display measures the high-edge offset, the same as USB and DIGU.
- **Squelch** — The SQL button and squelch slider are disabled in NT mode. Because audio is routed via DAX in digital modes, squelch is not meaningful. If squelch was active when you switched into NT mode, AetherSDR turns it off automatically and restores it when you leave NT mode.

## Related

- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)