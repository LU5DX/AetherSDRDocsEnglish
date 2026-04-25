# Switch to an External 10 MHz Reference

This page explains how to configure the FLEX-8600 to lock its internal oscillator to an external 10 MHz reference signal instead of the built-in reference. Use this when you have a GPS-disciplined oscillator, rubidium standard, or other precision 10 MHz source connected to the radio's rear-panel REF IN port.

## Before you start

- AetherSDR must be connected to the radio. The Radio Setup dialog is not available offline.
- Your external 10 MHz reference must be connected to the radio's rear-panel REF IN connector and must be active before you switch the source.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Locate the **10 MHz Reference Source:** combo box.
4. Select **External**.

The radio switches its reference lock immediately. No dialog close or Apply step is required.

To revert to the built-in oscillator, return to the same combo box and select **Internal**.

## What each control does

| Control | Kind | Valid values | Behavior |
|---|---|---|---|
| **10 MHz Reference Source:** | Combo box | `Internal` \| `External` | Selects whether the radio's ADC clock derives from the internal oscillator or an external 10 MHz signal present on the REF IN connector. |

## Tips

- While you are on the **RX** tab, the **Cal Frequency (MHz):** and **Freq Offset (ppb):** controls are also available. If your external reference has a known offset, you can enter it in **Freq Offset (ppb):** rather than re-running a full calibration sweep.

## Troubleshooting

- **Radio shows no lock or frequency drift after switching to External** — Confirm the reference signal is present at the REF IN port before switching. If the external source is not present or below the required level, the radio may free-run or behave erratically. Switch back to **Internal** and check the reference source and cabling.

## Related

- [Calibrate the GPSDO frequency offset](calibrate-the-gpsdo-frequency-offset.md)
- [Radio Setup overview](overview.md)
