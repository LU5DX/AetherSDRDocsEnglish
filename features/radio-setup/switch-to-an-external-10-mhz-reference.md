# Switch to an External 10 MHz Reference

This page explains how to select an external 10 MHz reference clock on your FLEX-8600. Use an external reference when you need to lock the radio to a GPS-disciplined oscillator, rubidium standard, or other precision frequency source.

## Before you start

- AetherSDR must be connected to the radio. The Radio Setup dialog is not available without an active radio connection.
- A stable 10 MHz signal must be physically connected to the FLEX-8600's rear-panel 10 MHz reference input before switching the source.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Locate the **10 MHz Reference Source:** combo box.
4. Select **External**.

The radio immediately switches its reference oscillator input. No additional apply step is required.

To revert to the internal oscillator, return to the **RX** tab and select **Internal** from **10 MHz Reference Source:**.

## What each control does

| Control | Kind | Valid values | Behavior |
|---|---|---|---|
| **10 MHz Reference Source:** | Combo box | Internal \| External | Selects whether the radio locks to its internal oscillator or to a signal present on the rear-panel 10 MHz input. |

## Tips

- If you also need to correct a residual frequency error after locking to an external reference, use the **Freq Offset (ppb):** spinbox on the same **RX** tab.

## Troubleshooting

- **Radio frequency is unstable or drifts after selecting External** — The external 10 MHz signal may be absent, too weak, or out of specification. Verify the signal is present and within the FLEX-8600's input level requirements, then toggle back to **Internal** and retry.
- **10 MHz Reference Source: combo box is greyed out or missing** — AetherSDR requires an active radio connection to display RX tab controls. Confirm the radio is connected before opening Radio Setup.

## Related

- [Calibrate the GPSDO frequency offset](calibrate-the-gpsdo-frequency-offset.md)
