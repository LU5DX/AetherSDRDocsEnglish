# Calibrate the GPSDO frequency offset

Use this page to correct any frequency error in the FLEX-8600's internal oscillator by applying a measured offset in parts per billion (ppb), or by running an automatic calibration sweep against a known reference frequency.

## Before you start

- AetherSDR must be connected to the radio. The RX tab controls are only active with a live radio connection.
- Have a known, accurate frequency reference available if you intend to use the calibration sweep — for example, a WWV carrier, a GPS-disciplined beacon, or a calibrated signal generator.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. To run an automatic sweep: enter the reference frequency in MHz in the **Cal Frequency (MHz):** spinbox, then click **Start**. The radio sweeps around that frequency and computes the offset.
4. To set the offset manually: enter the desired correction directly into the **Freq Offset (ppb):** spinbox. Positive values shift the indicated frequency upward; negative values shift it downward.
5. Close the dialog. The offset is applied immediately to the radio.

## What each control does

| Control | Kind | Behavior | Default | Range |
|---|---|---|---|---|
| **Cal Frequency (MHz):** | Spinbox | Frequency used as the reference for the automatic calibration sweep. | — | — |
| **Start** | Button | Starts the frequency calibration sweep using the value in **Cal Frequency (MHz):**. | — | — |
| **Freq Offset (ppb):** | Spinbox | Manual frequency correction applied to the oscillator, in parts per billion. | — | — |
| **10 MHz Reference Source:** | Combo box | Selects whether the radio locks to its internal oscillator or an external 10 MHz reference input. | — | Internal \| External |

## Tips

- If you have a GPS-disciplined 10 MHz source connected to the rear-panel reference input, switch **10 MHz Reference Source:** to External instead of applying a manual offset. See [Switch to an external 10 MHz reference](switch-to-an-external-10-mhz-reference.md).
- Run the calibration sweep on a frequency where propagation effects are negligible — a local reference is more reliable than a distant shortwave standard.

## Troubleshooting

- **Start button has no effect** — Confirm AetherSDR is connected to the radio. The RX tab controls require an active radio connection.
- **Freq Offset (ppb): value resets after reconnect** — The offset is stored on the radio, not in AetherSDR's local settings. If the radio loses power before saving its state, the value may revert to the last persisted radio configuration.

## Related

- [Switch to an external 10 MHz reference](switch-to-an-external-10-mhz-reference.md)
- [Radio Setup overview](overview.md)
