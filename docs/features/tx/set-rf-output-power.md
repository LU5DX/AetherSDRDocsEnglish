# Set RF output power

Use the RF Power slider in the TX Controls applet to set how much power the FLEX-8600 transmits. Adjusting this before transmitting prevents overdrive and protects your amplifier or antenna system.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. If not, go to `Settings > Connect to Radio...`.
- The TX Controls applet must be visible. If it is not, click the TX tray button in the right sidebar.

## Steps

1. Locate the **RF Power** slider in the TX Controls applet. It is the first slider below the **RF Pwr** and **SWR** meters.
2. Drag the slider left to decrease power or right to increase power. The numeric value to the right of the slider updates immediately.
3. Confirm the value shown next to the slider matches your intended power level (0–100).

## What each control does

| Control | Description | Default | Valid range |
|---|---|---|---|
| **RF Pwr** meter | Displays forward power at the exciter output. | — | 0–120 W; red above 100 W (barefoot). Scale changes to 0–600 W on Aurora 500W models, red above 500 W. |
| **SWR** meter | Displays standing wave ratio at the exciter. | — | 1.0–3.0; red above 2.5. |
| **RF Power** slider | Sets the transmit RF power level sent to the radio. | 100 | 0–100 |

## Tips

- The **RF Pwr** meter shows actual forward power only while transmitting. Set the slider before keying up, then verify the meter reading during a transmission.
- If you are using a linear amplifier, set **RF Power** to the drive level your amplifier requires rather than maximum.
- To set power for the tune carrier separately from the operating power level, use the **Tune Pwr** slider. See [Set tune-carrier power](set-tune-carrier-power.md).

## Troubleshooting

- **Slider moves but forward power does not change** — The radio may not be transmitting. The **RF Pwr** meter only reads while keyed. Key the radio with MOX or by transmitting normally, then recheck.
- **RF Pwr meter pegs into the red** — Reduce the **RF Power** slider. On barefoot FLEX-8600 operation the red zone begins above 100 W; exceeding it risks overdrive.

## Related

- [TX Controls overview](overview.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Switch TX profiles (e.g. SSB, Digital)](switch-tx-profiles-e-g-ssb-digital.md)
