# Lock the slice to prevent accidental retuning

The tune-lock feature prevents a slice from responding to frequency changes. Use it when you want to monitor a fixed frequency while operating other slices or clicking around the panadapter.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- Identify which slice you want to lock. If you have more than one slice, select it using the A..H tab row at the top of the RX Controls applet.

## Steps

1. Open the RX Controls applet. If it is not visible, click the **RX** tray button on the right sidebar.
2. Locate the 🔓 button in the header row, immediately to the right of the slice badge (A, B, C, etc.).
3. Click 🔓 to lock the slice. The icon changes to 🔒 and the button highlights in blue. The slice will now ignore frequency changes.
4. To unlock, click 🔒 again. The icon returns to 🔓 and the slice resumes normal tuning.

## What each control does

| Control | Default | Behavior |
|---------|---------|----------|
| 🔓 / 🔒 | 🔓 (unlocked) | Toggles tune-lock on the active slice. When locked (🔒), the slice ignores all frequency changes. Icon flips between open and closed padlock. No persisted setting key. |

## Tips

- The lock applies only to the slice currently shown in the RX Controls applet. Other slices are unaffected.
- If you have multiple slices, use the slice tabs (A..H) to switch to a different slice and lock or unlock it independently.

## Troubleshooting

- **Clicking the panadapter or typing a frequency still tunes the slice** — Confirm the 🔒 icon is showing and highlighted blue. If the applet is showing a different slice than the one you intend to lock, select the correct slice tab first.
- **The 🔓 / 🔒 button is not visible** — The header row may be scrolled out of view if the applet panel is very short. Resize the panel or scroll up within the applet.

## Related

- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
