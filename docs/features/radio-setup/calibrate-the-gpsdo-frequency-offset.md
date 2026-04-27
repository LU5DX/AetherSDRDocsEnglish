# Calibrate the GPSDO frequency offset

Use this page to correct the frequency reference of your FLEX-8600 using the built-in GPSDO calibration controls. Accurate frequency calibration reduces dial error across all bands.

## Before you start

- AetherSDR must be connected to the radio. The RX tab in Radio Setup is only available when a radio connection is active.
- Your radio must have a GPSDO installed and locked before calibration results will be meaningful.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. In **Cal Frequency (MHz):**, enter the frequency of a known-accurate reference signal.
4. Click **Start** to begin the calibration sweep.
5. When the sweep completes, review the measured offset shown in **Freq Offset (ppb):**.
6. If you prefer to set the offset manually rather than using the sweep result, edit **Freq Offset (ppb):** directly.

## What each control does

| Control | Kind | Description |
|---|---|---|
| **Cal Frequency (MHz):** | Spinbox | The reference frequency used during the calibration sweep. Set this to a known-accurate signal — for example, a broadcast standard-frequency station. |
| **Start** | Push button | Initiates the calibration sweep at the frequency entered in **Cal Frequency (MHz):**. |
| **Freq Offset (ppb):** | Spinbox | The frequency offset applied to the radio's reference oscillator, in parts per billion. Can be set by the sweep or entered manually. |
| **10 MHz Reference Source:** | Combo box | Selects whether the radio uses its **Internal** or an **External** 10 MHz reference. Valid values: `Internal` \| `External`. |

## Tips

- If you intend to use an external 10 MHz reference instead of the GPSDO, set **10 MHz Reference Source:** to `External` before calibrating, so the offset applies to the correct source.

## Related

- [Switch to an external 10 MHz reference](switch-to-an-external-10-mhz-reference.md)
- [Radio Setup overview](overview.md)
