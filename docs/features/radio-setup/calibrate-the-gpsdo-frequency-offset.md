# Calibrate the GPSDO frequency offset

Use this page to trim the frequency reference of your FLEX-8600 by setting a calibration frequency or entering a manual offset in parts-per-billion. Accurate frequency calibration improves receive and transmit accuracy across all bands.

## Before you start

- AetherSDR must be connected to the radio. The RX tab is only accessible when a radio connection is active.
- Your radio must have a GPSDO fitted, or an accurate external reference signal available for comparison.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. To run an automatic calibration sweep, set the known-accurate reference frequency in **Cal Frequency (MHz):**, then click **Start**.
4. To enter an offset manually, type the desired value directly into **Freq Offset (ppb):**.
5. Close the dialog. The offset is applied to the radio immediately.

## What each control does

| Control | Description | Default | Valid range |
|---|---|---|---|
| **Cal Frequency (MHz):** | The frequency used as the reference during a calibration sweep. Set this to a known-accurate signal (for example, a time standard or GPSDO-disciplined beacon). | — | — |
| **Start** | Initiates the frequency calibration sweep using the value in **Cal Frequency (MHz):**. | — | — |
| **Freq Offset (ppb):** | Manual frequency offset applied to the radio's reference oscillator, in parts per billion. | — | — |
| **10 MHz Reference Source:** | Selects whether the radio uses its internal oscillator or an external 10 MHz reference input. | — | Internal \| External |

## Tips

- If you have a known-good 10 MHz external reference, switch **10 MHz Reference Source:** to External before calibrating to get the best baseline accuracy.
- The **Freq Offset (ppb):** field lets you make fine corrections without running a full sweep, useful when you already know the approximate error from a previous calibration.

## Related

- [Switch to an external 10 MHz reference](switch-to-an-external-10-mhz-reference.md)
- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
