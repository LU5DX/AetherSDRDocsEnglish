# Switch to an External 10 MHz Reference

This page explains how to select an external 10 MHz reference clock on a connected FLEX-8600. Use an external reference when you have a GPS-disciplined oscillator or other precision 10 MHz source and want the radio to lock to it instead of its internal oscillator.

## Before you start

- AetherSDR must be connected to the radio. The Radio Setup dialog requires an active radio connection.
- Your external 10 MHz reference signal must be connected to the rear-panel REF IN port on the FLEX-8600 before switching the source.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the `RX` tab.
3. Locate the `10 MHz Reference Source:` combo box.
4. Select `External` from the combo box. To return to the built-in oscillator, select `Internal`.

## What each control does

| Control | Kind | Valid range | Behavior |
|---|---|---|---|
| `10 MHz Reference Source:` | Combo box | `Internal` \| `External` | Tells the radio which 10 MHz source to lock its ADC clocks to. `Internal` uses the radio's onboard oscillator. `External` locks to the signal present on the rear-panel REF IN connector. |

## Tips

- The `RX` tab also contains the `Cal Frequency (MHz):` spinbox and `Freq Offset (ppb):` spinbox used for GPSDO calibration. If you are using a GPS-disciplined oscillator as your external reference, see [Calibrate the GPSDO frequency offset](calibrate-the-gpsdo-frequency-offset.md) for the calibration procedure.

## Troubleshooting

- **Radio frequency appears unstable or offset after switching to External** — The REF IN signal may be absent, too low in level, or not exactly 10 MHz. Verify the external source is running and properly connected before selecting `External`. Switch back to `Internal` while diagnosing.

## Related

- [Calibrate the GPSDO frequency offset](calibrate-the-gpsdo-frequency-offset.md)
