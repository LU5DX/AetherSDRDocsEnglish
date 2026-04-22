# Switch to an External 10 MHz Reference

Use this page to select an external 10 MHz reference signal as the FLEX-8600's frequency standard. This is useful when you have a GPS-disciplined oscillator, rubidium standard, or other precision reference connected to the radio's rear-panel REF IN port.

## Before you start

- AetherSDR must be connected to the radio. The Radio Setup dialog requires an active radio connection.
- Your external 10 MHz reference source must be connected to the radio's rear-panel REF IN connector and must be active before you switch the setting.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **RX** tab.
3. Locate the **10 MHz Reference Source:** combo box.
4. Select **External** from the drop-down list.
5. Click **Close** to dismiss the dialog.

To revert to the built-in oscillator, repeat the steps and select **Internal**.

## What each control does

| Control | Kind | Valid values | Behavior |
|---|---|---|---|
| **10 MHz Reference Source:** | Combo box | `Internal`, `External` | Selects whether the radio locks its sample clock to the internal oscillator or to a 10 MHz signal present on the REF IN connector. |

## Tips

- The **RX** tab also contains the GPSDO calibration controls (**Cal Frequency (MHz):**, **Start**, and **Freq Offset (ppb):**). If you are using a GPS-disciplined oscillator as your external reference, you do not also need to apply a manual frequency offset — the GPSDO holds the frequency.

## Troubleshooting

- **Frequency display becomes unstable or the radio stops receiving after switching to External** — The external reference is absent, too low in level, or not exactly 10 MHz. Verify the source is running and properly cabled, then switch back to **Internal** to restore normal operation.

## Related

- [Calibrate the GPSDO frequency offset](calibrate-the-gpsdo-frequency-offset.md)
- [Radio Setup overview](overview.md)
