# Run a Two-Tone Tune

A two-tone tune lets you key the transmitter at a controlled power level so you can check linearity, adjust drive, or verify SWR before operating. You do this by setting a tune power level and activating the tune carrier using TUNE or MOX from the TX Controls applet.

## Before you start

- AetherSDR must be connected to the radio. Use `Settings > Connect to Radio...` if not already connected.
- The TX Controls applet must be visible. If it is not, click the TX tray button on the right sidebar.
- Confirm you are operating within a frequency and power level permitted by your license and local regulations.
- Notify others on the frequency before transmitting.

## Steps

1. In the TX Controls applet, locate the **Tune Pwr** slider.
2. Set **Tune Pwr** to the desired carrier power level. The default is 10; the valid range is 0–100.
3. Confirm the **RF Power** slider is at the level you want for full-power operation (default 100, range 0–100). This does not affect the tune carrier power, but verifying it now avoids surprises after tuning.
4. Watch the **SWR** gauge (range 1.0–3.0; red above 2.5) and the **RF Pwr** gauge (range 0–120 W barefoot, red above 100 W) — both update in real time while transmitting.
5. Click **TUNE**. The button label changes to **TUNING...** with a red background while the carrier is active.
6. Observe the **RF Pwr** and **SWR** gauges. When you have the readings you need, click **TUNE** again to stop. The button returns to **TUNE**.

Alternatively, to key the transmitter continuously at full RF power for a two-tone or IMD test using external audio:

1. Set **RF Power** to the desired drive level.
2. Click **MOX**. The button turns red while the transmitter is keyed.
3. Apply your two-tone audio source through the radio's audio input.
4. Click **MOX** again to return to receive. The button returns to its unlit state.

## What each control does

| Control | Kind | Default | Range | Behavior |
|---|---|---|---|---|
| **RF Pwr** | Meter | — | 0–120 W (barefoot); red above 100 W | Displays forward power at the exciter output. |
| **SWR** | Meter | — | 1.0–3.0; red above 2.5 | Displays standing wave ratio at the exciter. |
| **RF Power** | Slider | 100 | 0–100 | Sets transmit RF power level. |
| **Tune Pwr** | Slider | 10 | 0–100 | Sets the tune carrier power level. |
| **TUNE** | Button | — | TUNE / TUNING... | Starts or stops the tune carrier. Label changes to **TUNING...** with red background while active. |
| **MOX** | Toggle button | Off | Off (blue) / On (red) | Keys the transmitter manually. Button turns red while transmitting. |

## Tips

- Keep **Tune Pwr** low (10 or below) when using the tune carrier for antenna tuner operation to protect the final amplifier.
- If you need to run the internal ATU before the two-tone test, click **ATU** first. See [Run the internal ATU](run-the-internal-atu.md).
- The **SWR** gauge goes red above 2.5. If SWR is high during the tune carrier, stop transmission and check your antenna system before increasing power.

## Troubleshooting

- **TUNE button does nothing** — Confirm the radio is connected. The TX Controls applet requires an active radio connection.
- **RF Pwr gauge reads zero while TUNING...** — Check that **Tune Pwr** is above 0. If the slider is at 0, no carrier is transmitted.
- **SWR reads high immediately** — The antenna or feedline may have a fault. Reduce **Tune Pwr**, correct the antenna issue, then retry.
- **MOX keys but no audio transmits** — Verify your two-tone audio source is routed to the correct radio audio input. Audio routing is outside the TX Controls applet; see your system audio configuration.

## Related

- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Set RF output power](set-rf-output-power.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Enable APD to linearise the transmitter](enable-apd-to-linearise-the-transmitter.md)
