# Switch to an external 10 MHz reference

This page explains how to select an external 10 MHz reference source on the FLEX-8600, which locks the radio's timebase to a high-stability external oscillator or GPSDO instead of the internal reference.

## Before you start

- AetherSDR must be connected to the radio. The Radio Setup dialog requires an active radio connection.
- A stable 10 MHz reference signal must be present on the radio's external reference input before you switch the source.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Locate the **10 MHz Reference Source:** combo box.
4. Select **External** from the combo box.

The radio applies the change immediately. To revert to the built-in oscillator, select **Internal**.

## What each control does

| Control | Description | Default | Valid values |
|---|---|---|---|
| **10 MHz Reference Source:** | Selects whether the radio locks to its internal oscillator or to a signal on the external 10 MHz reference input. | Internal | Internal, External |

## Tips

- If you are also correcting a measured frequency error, adjust **Freq Offset (ppb):** on the same **RX** tab before or after switching the reference source.

## Troubleshooting

- **Radio does not lock to the external reference** — Verify that the external signal is present, at 10 MHz, and within the radio's input level specification before selecting **External**. If the reference disappears after switching, the radio will lose lock; return the combo box to **Internal** until the signal is restored.

## Related

- [Calibrate the GPSDO frequency offset](calibrate-the-gpsdo-frequency-offset.md)
- [Radio Setup overview](overview.md)
