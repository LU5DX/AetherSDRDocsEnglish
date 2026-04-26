# Calibrate the GPSDO frequency offset

Use this page to adjust the frequency reference calibration on your FLEX-8600. Correcting the offset improves receive and transmit frequency accuracy across all bands.

## Before you start

- AetherSDR must be connected to the radio. The RX tab is not accessible while disconnected.
- Identify a known-accurate reference signal to calibrate against (for example, a WWV carrier or GPS-disciplined standard).

## Steps

1. Go to `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. In **Cal Frequency (MHz):**, enter the frequency of your reference signal.
4. Click **Start** to begin the calibration sweep.
5. When the sweep completes, review the result. If you need to apply a manual correction instead, enter the desired value directly in **Freq Offset (ppb):**.

## What each control does

| Control | Description | Default | Valid range |
|---|---|---|---|
| **Cal Frequency (MHz):** | Frequency used for the calibration sweep. Set this to your reference signal's frequency. | — | — |
| **Start** | Begins the frequency calibration sweep against the entered cal frequency. | — | — |
| **Freq Offset (ppb):** | Manual frequency offset applied to the reference oscillator, in parts per billion. Adjust this if automatic calibration is not available. | — | — |
| **10 MHz Reference Source:** | Selects whether the radio uses its internal oscillator or an external 10 MHz input as the frequency reference. | — | Internal \| External |

## Tips

- If you have an external 10 MHz reference connected to the radio's rear-panel input, switch **10 MHz Reference Source:** to External before calibrating. This may make manual offset correction unnecessary.

## Related

- [Switch to an external 10 MHz reference](switch-to-an-external-10-mhz-reference.md)
- [Radio Setup overview](overview.md)
