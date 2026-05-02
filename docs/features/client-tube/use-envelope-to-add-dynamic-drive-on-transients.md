# Use Envelope to add dynamic drive on transients

The Envelope knob connects an envelope follower to the tube drive, so the amount of saturation changes in real time with the input signal level. Use it on TX to add harmonic grit on mic transients, or on RX to make received audio feel more present on peaks.

## Before you start

- The Tube stage must be enabled for the side you want to adjust (TX or RX). If the applet is not visible, enable the stage via the CHAIN widget first.
- Set Drive to a level where the transfer curve already shows some bend. Envelope modulates that drive; if Drive is at 0 dB the effect will be subtle.

## Steps

1. Double-click the TUBE stage in the CHAIN widget on the TX or RX side to open the floating editor titled "Aetherial Tube — TX" or "Aetherial Tube — RX".
2. Locate the Envelope knob in the right column of the editor.
3. Turn Envelope clockwise (positive) to increase drive on transients — the tube gets hotter as input levels rise. Turn it counter-clockwise (negative) to reduce drive on transients, compressing harmonics dynamically. Default is 0 %.
4. Adjust Attack to set how quickly the envelope follower responds when levels rise. Lower values (toward 0.1 ms) react faster; higher values (toward 30.0 ms) smooth out short spikes.
5. Adjust Release to set how quickly the follower recovers after levels drop. Lower values (toward 10.0 ms) recover faster; higher values (toward 500.0 ms) let the effect hang longer.
6. Watch the live input ball on the transfer curve — with Envelope active, the ball will move further along the curve on peaks than on quiet passages, confirming the follower is working.

## What each control does

| Control | Default | Valid range | Persisted setting (TX / RX) | Behavior |
|---|---|---|---|---|
| Envelope | 0 % | −1.0 to +1.0 | `ClientTubeTxEnvelope` / `ClientTubeRxEnvelope` | Positive: boosts drive on loud peaks. Negative: reduces drive on loud peaks. Zero: no dynamic modulation. |
| Attack | 5.00 ms | 0.1 to 30.0 ms | `ClientTubeTxAttackMs` / `ClientTubeRxAttackMs` | How quickly the follower responds to rising levels. Uses exponential scaling. Has no effect when Envelope is 0. |
| Release | 35.00 ms | 10.0 to 500.0 ms | `ClientTubeTxReleaseMs` / `ClientTubeRxReleaseMs` | How quickly the follower recovers after levels fall. Uses exponential scaling. Has no effect when Envelope is 0. |

## Tips

- After setting a positive Envelope value, check the OUT meter in the editor. Peaks may be louder than the static Drive setting alone would produce; use the Output knob to compensate.
- For natural-sounding TX mic grit, start with Envelope around +30 %, Attack at 5 ms, and Release at 50–80 ms, then adjust to taste.
- Negative Envelope values behave like a dynamic saturation reducer — useful on RX to tame harsh peaks without removing tube character from quieter passages.
- The Dry/Wet knob blends the fully processed signal (including envelope-modulated saturation) with the dry signal, so you can use high Envelope values without fully committing to the effect.

## Troubleshooting

- **Envelope knob has no audible effect** — Drive is likely at or near 0 dB. Set Drive to a value where the transfer curve visibly bends, then re-test Envelope.
- **Effect sounds erratic or pumping** — Attack or Release values are too short for the program material. Increase Release toward 100 ms or more; increase Attack above 10 ms to ignore short transients.
- **Output level spikes on transients** — Positive Envelope adds gain on peaks. Reduce Output to compensate, or reduce Envelope depth.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Tune Attack and Release for natural-sounding envelope following](tune-attack-and-release-for-natural-sounding-envelope-following.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Dry/Wet](parallel-blend-saturation-with-dry-wet.md)
- [Monitor output clipping with the level meter in the editor](monitor-output-clipping-with-the-level-meter-in-the-editor.md)
