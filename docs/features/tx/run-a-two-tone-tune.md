# Run a Two-Tone Tune

A two-tone tune lets you check transmitter linearity and drive levels by keying the radio manually with MOX while monitoring forward power and SWR. Use this procedure when your rig is in SSB mode and you want to verify output without transmitting audio.

## Before you start

- AetherSDR is connected to the FLEX-8600 (radio indicator shows connected).
- The TX Controls applet is visible. If it is not, click the TX tray button on the right sidebar.
- Your transceiver is set to SSB mode and is on a clear frequency.
- A two-tone audio source (external generator or software) is ready to feed the radio's microphone or line input.

## Steps

1. In the TX Controls applet, set the **Tune Pwr** slider to the power level you want to use for the test. Default is 10; valid range is 0–100.
2. Set the **RF Power** slider to the desired output level. Default is 100; valid range is 0–100.
3. If you want to use a specific transmit profile (for example, a clean SSB profile without processing), select it from the **TX Profile** drop-down.
4. Start the two-tone audio signal from your external source so it is feeding the radio's input.
5. Click **MOX**. The button turns red and the radio keys up.
6. Watch the **RF Pwr** meter (0–120 W, red above 100 W) and the **SWR** meter (1.0–3.0, red above 2.5). Adjust the **RF Power** slider while transmitting to reach your target output.
7. When the test is complete, click **MOX** again to unkey the transmitter. The button returns to its unlit state.
8. Stop the two-tone audio source.

## What each control does

| Control | Kind | Default | Valid range | Behavior |
|---|---|---|---|---|
| RF Power | Slider | 100 | 0–100 | Sets transmit RF power level. |
| Tune Pwr | Slider | 10 | 0–100 | Sets tune-carrier power level (not used during MOX, but set it before switching modes). |
| TX Profile | Drop-down | — | Populated from radio | Loads the selected transmit profile. |
| MOX | Toggle button | Off | Off / On (red) | Keys the transmitter manually. Button turns red while TX is active. |
| RF Pwr | Meter | — | 0–120 W; red > 100 W | Displays forward power at the exciter output. |
| SWR | Meter | — | 1.0–3.0; red > 2.5 | Displays standing wave ratio at the exciter. |

## Tips

- Keep SWR below 2.5 during the test. The SWR meter turns red above 2.5 as a visual warning.
- Select a TX profile that has microphone processing disabled before running a two-tone test. Processing can distort the two-tone envelope and produce misleading IMD readings.
- If you have ATU memories available, consider recalling a known-good memory before keying to ensure the antenna is matched. See [Recall an ATU memory](recall-an-atu-memory.md).

## Troubleshooting

- **MOX keys but RF Pwr reads zero** — The two-tone audio source may not be reaching the radio's input, or the mode is not SSB. Confirm the audio routing and mode selection before re-keying.
- **SWR immediately goes red when MOX is pressed** — The antenna is unmatched. Click MOX to unkey, then run the ATU or check the feedline before continuing. See [Run the internal ATU](run-the-internal-atu.md).
- **RF Pwr meter pegs at full scale** — RF Power slider is set too high for the connected antenna and amplifier. Click MOX to unkey, then reduce the RF Power slider before re-keying.

## Related

- [Set RF output power](set-rf-output-power.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Switch TX profiles (e.g. SSB, Digital)](switch-tx-profiles-e-g-ssb-digital.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Recall an ATU memory](recall-an-atu-memory.md)
