# Set threshold just above room noise floor

Set the **Thresh** knob so the gate starts attenuating just above your room's ambient noise level. This keeps background noise silenced between transmissions while letting your voice through cleanly.

## Before you start

- The Gate stage must be enabled in the CHAIN widget. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if the GATE applet is not visible.
- Be in a quiet room at your normal operating position so the noise floor reading is representative.

## Steps

1. Open the GATE sub-container inside the PooDoo Audio (TXDSP) parent container. If it is not visible, double-click the Gate stage in the CHAIN widget to open the floating Gate editor, or right-click the GATE sub-container titlebar and choose to show it.
2. Watch the **Transfer curve** display. The live input ball shows your current input level in real time. With no speech, the ball should sit at your room noise floor.
3. Speak nothing. Note where the ball rests on the curve — that is your noise floor.
4. Turn the **Thresh** knob up (toward 0 dB) until it sits 2–6 dB above the resting ball position. The gate will now begin attenuating whenever you are not speaking.
5. Confirm by watching the **Gain-reduction bar**: it should show amber fill during silence and return to empty when you speak at normal level.
6. Speak into the microphone. Verify that the ball crosses the threshold, the gain-reduction strip drops to empty, and your audio passes through without chopping.
7. If the gate opens too late or clips the start of words, lower **Thresh** slightly or adjust **Attack**. See [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Thresh | -40.0 dB | -80.0 to 0.0 dB | `ClientGateTxThresholdDb` | Level below which the gate starts attenuating. Set this just above the noise floor. |
| Ratio | 2.0 | 1.0 to 10.0 | `ClientGateTxRatio` | Higher values give a harder cut; lower values act as a soft downward expander. |
| Attack | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` | How quickly the gate opens when input rises above threshold. |
| Release | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` | How quickly the gate closes after input falls below threshold. |
| Floor | -15.0 dB | -80.0 to 0.0 dB | `ClientGateTxFloorDb` | Maximum attenuation the gate is allowed to apply. |

`ClientGateTxEnabled` controls whether the gate stage is active at all.

## Tips

- The **Gain-reduction bar** scale runs from 0 to 40 dB. The tick mark at -15 dB corresponds to the default **Floor** value — a useful reference point for soft-expander operation.
- The knobs in the GATE applet and the floating Gate editor stay in sync. Changes made in either location take effect immediately and are saved automatically.
- Set **Thresh** conservatively low rather than too high. An overly high threshold will chop the beginnings of words.

## Troubleshooting

- **Ball never crosses the threshold during speech** — Thresh is set too high. Turn the **Thresh** knob toward -80 dB until normal speech pushes the ball above the threshold line.
- **Gate does not silence room noise between words** — Thresh is set too low. Raise **Thresh** until it sits above the resting ball position during silence.
- **Gate chops the start of words** — **Attack** is too slow or **Thresh** is too close to the speech level. Lower **Thresh** slightly or reduce the **Attack** value. See [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).
- **Unnatural silence between words** — **Floor** is applying too much attenuation. Raise **Floor** toward 0 dB. See [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md).

## Related

- [Noise Gate / Expander overview](overview.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
