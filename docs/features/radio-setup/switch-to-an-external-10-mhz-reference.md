# Switch to an external 10 MHz reference

Use this page to change the Flex radio's frequency reference from its internal oscillator to an external 10 MHz signal connected to the rear-panel REF IN connector. An external reference improves frequency accuracy and stability, which matters for weak-signal work, digital modes, and operating with GPS-disciplined or rubidium standards.

## Before you start

- AetherSDR must be connected to the radio. The RX tab in Radio Setup is not accessible without an active connection.
- A stable 10 MHz signal must be present on the radio's rear-panel external reference input before switching the source.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Locate the **10 MHz Reference Source:** combo box.
4. Select **External**.

The radio switches to the external reference immediately. To revert, select **Internal** from the same combo box.

## What each control does

| Control | Kind | Valid values | Behavior |
|---|---|---|---|
| **10 MHz Reference Source:** | Combo box | `Internal` \| `External` | Selects whether the radio clocks from its internal oscillator or an external 10 MHz signal on the rear-panel input. |

## Tips

- If you are also correcting a frequency offset, adjust **Freq Offset (ppb):** on the same RX tab after switching to the external reference. See [Calibrate the GPSDO frequency offset](calibrate-the-gpsdo-frequency-offset.md) for that procedure.
- Switching back to **Internal** while the external reference is still connected is safe; the radio will use its internal oscillator and ignore the rear-panel signal.

## Troubleshooting

- **Frequency display jumps or becomes unstable after selecting External** — The external 10 MHz signal is absent, too weak, or out of specification. Verify the signal is present and within the radio's input level requirement before selecting External. Switch back to **Internal** to restore normal operation.

## Related

- [Calibrate the GPSDO frequency offset](calibrate-the-gpsdo-frequency-offset.md)
