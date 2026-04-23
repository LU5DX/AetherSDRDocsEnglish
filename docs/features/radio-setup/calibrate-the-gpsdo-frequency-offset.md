# Calibrate the GPSDO frequency offset

Use this page to trim the Flex radio's internal oscillator frequency by entering a known-good calibration frequency and applying a parts-per-billion offset. Accurate frequency calibration improves receive accuracy and on-air frequency precision.

## Before you start

- AetherSDR must be connected to the radio. The RX tab is not accessible without a live radio connection.
- Have a known-accuracy reference signal available at a specific frequency, or know the offset you want to apply directly.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. In **Cal Frequency (MHz):**, enter the frequency of your reference signal in MHz.
4. Click **Start** to begin the calibration sweep.
5. If you prefer to set the offset manually without running a sweep, enter the desired value directly in **Freq Offset (ppb):**.

## What each control does

| Control | Description | Default | Valid range |
|---|---|---|---|
| **Cal Frequency (MHz):** | The frequency used as the reference during the calibration sweep. | — | — |
| **Start** | Starts the frequency calibration sweep using the value in **Cal Frequency (MHz):**. | — | — |
| **Freq Offset (ppb):** | Manual frequency offset applied to the receiver's oscillator, in parts per billion. | — | — |
| **10 MHz Reference Source:** | Selects whether the radio uses its internal oscillator or an external 10 MHz reference signal. | — | Internal \| External |

## Tips

- If you have a stable external 10 MHz reference, switching **10 MHz Reference Source:** to External and connecting the signal to the radio's rear-panel input may give better long-term stability than offset calibration alone.

## Related

- [Switch to an external 10 MHz reference](switch-to-an-external-10-mhz-reference.md)
- [Radio Setup overview](overview.md)
