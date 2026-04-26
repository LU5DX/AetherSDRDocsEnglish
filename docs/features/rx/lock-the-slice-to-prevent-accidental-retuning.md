# Lock the slice to prevent accidental retuning

Use the tune-lock toggle in the RX Controls applet to freeze a slice's frequency so that clicks, scroll-wheel events, and tuning commands cannot retune it.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- Identify which slice you want to lock. If you have more than one slice active, select it first using the slice tab row (A..H).

## Steps

1. Open the RX Controls applet. If it is not visible, click the **RX** tray button on the right sidebar.
2. If multiple slices are in use, click the lettered tab (A through H) for the slice you want to lock.
3. Locate the **🔓** button in the header row, immediately to the right of the slice badge.
4. Click **🔓**. The icon changes to **🔒** and turns blue. The slice is now locked and will ignore frequency changes.
5. To unlock, click **🔒**. The icon returns to **🔓** and the slice accepts tuning again.

## What each control does

| Control | Default | Behavior |
|---|---|---|
| **🔓 / 🔒** | 🔓 (unlocked) | Toggles tune-lock on the active slice. When locked (🔒), the slice ignores frequency changes from any source. When unlocked (🔓), normal tuning resumes. |

## Tips

- The lock state applies only to the slice it is set on. Other slices are unaffected.
- The slice badge letter (A, B, C, etc.) and the lock button are both in the header row. Confirm the badge shows the correct slice letter before locking.

## Related

- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
