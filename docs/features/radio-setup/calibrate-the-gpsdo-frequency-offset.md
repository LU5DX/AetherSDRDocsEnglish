# Calibrate the GPSDO frequency offset

Use this page to correct frequency errors in the FLEX-8600's oscillator by setting a parts-per-billion offset or running an automatic calibration sweep. Accurate frequency calibration improves receive and transmit accuracy across all bands.

## Before you start

- AetherSDR must be connected to the radio. The RX tab is only accessible with an active radio connection.
- You need a known-accurate reference signal at a specific frequency to calibrate against (for example, a WWV carrier or GPSDO-disciplined signal).

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. To run an automatic calibration sweep:
   1. Enter the frequency of your reference signal in **Cal Frequency (MHz):**.
   2. Click **Start**. The radio performs a calibration sweep against that frequency.
4. To set a manual offset instead, enter the correction value directly in **Freq Offset (ppb):**.

## What each control does

| Control | Description | Default | Valid range |
|---|---|---|---|
| **Cal Frequency (MHz):** | The frequency used as the reference during the automatic calibration sweep. | — | — |
| **Start** | Begins the frequency calibration sweep using the value in **Cal Frequency (MHz):**. | — | — |
| **Freq Offset (ppb):** | Manual frequency offset applied to the oscillator, in parts per billion. | — | — |
| **10 MHz Reference Source:** | Selects whether the radio uses its internal oscillator or an external 10 MHz input as the frequency reference. | — | Internal \| External |

## Tips

- If you have a stable external 10 MHz reference connected to the radio's rear-panel input, switch **10 MHz Reference Source:** to External before calibrating. This makes the **Freq Offset (ppb):** adjustment unnecessary in most cases.

## Related

- [Switch to an external 10 MHz reference](switch-to-an-external-10-mhz-reference.md)
- [Radio Setup overview](overview.md)
