# Set Threshold Just Above Room Noise Floor

Set the Thresh knob so the gate opens for your voice but stays closed during background noise between words. A threshold set too low lets room noise through; set too high, it clips the leading edges of speech.

## Before you start

- The Gate stage must be enabled in the CHAIN widget. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if the GATE applet is not visible.
- Have a typical noise source present in your shack (fans, air conditioning, nearby equipment) so the noise floor reading is representative.
- The GATE sub-container must be visible inside the PooDoo Audio (TXDSP) parent container.

## Steps

1. Open the GATE applet. If it is not visible, double-click the Gate stage in the CHAIN widget to open the floating Gate editor, or right-click the GATE sub-container titlebar and select the option to show it.
2. Observe the transfer curve. The live input ball moves along the curve in real time, showing the current input level relative to the threshold.
3. Watch the Gain-reduction bar while you are **not speaking**. If it shows no amber fill, the threshold is already above the noise floor — skip to step 6.
4. Turn the Thresh knob slowly clockwise (toward 0 dB) while watching the Gain-reduction bar. Stop when the amber fill appears consistently while the room is quiet and you are not speaking. This point is your noise floor.
5. Continue turning Thresh clockwise by 2–3 dB past that point. This gives a small margin so that borderline noise does not cause the gate to flutter.
6. Speak at your normal microphone level. Confirm the input ball rises above the threshold line on the transfer curve and the Gain-reduction bar drops to near zero while you are talking.
7. Return to silence. Confirm the Gain-reduction bar fills amber, indicating the gate is closed and attenuating background noise.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Thresh | -40.0 dB | -80.0 to 0.0 dB | `ClientGateTxThresholdDb` | Level below which the gate starts attenuating. Raise this above the noise floor. |
| Ratio | 2.0 | 1.0 to 10.0 | `ClientGateTxRatio` | Steepness of attenuation below threshold. Higher values give a harder cut. |
| Attack | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` | How quickly the gate opens when input rises above threshold. |
| Release | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` | How quickly the gate closes after input falls below threshold. |
| Floor | -15.0 dB | -80.0 to 0.0 dB | `ClientGateTxFloorDb` | Maximum attenuation the gate is allowed to apply. |
| Transfer curve | — | — | — | Plots the static transfer curve. The live ball shows current input level and whether the gate is open or closed. |
| Gain-reduction bar | — | 0 to 40 dB GR | — | Amber horizontal strip, right-filled. The tick at -15 dB marks the default Floor value. |

## Tips

- Set the threshold while the radio is in a typical operating session, not in an unusually quiet room. The noise floor that matters is the one present during actual use.
- The Gain-reduction bar scale maxes at 40 dB. If the bar fills completely during noise, the gate is applying maximum attenuation; lower `ClientGateTxFloorDb` (more negative) only if you need deeper cuts.
- Changes to Thresh take effect immediately and are saved automatically. No apply step is required.
- If the floating Gate editor and the GATE applet are both open, knob changes in either view sync to the other within approximately 33 ms.

## Troubleshooting

- **Input ball never rises above the threshold line while speaking** — Thresh is set too high. Turn the Thresh knob counter-clockwise (toward -80 dB) until the ball crosses the threshold during normal speech.
- **Gain-reduction bar shows no fill even during silence** — Thresh is below the noise floor. Raise Thresh clockwise until the bar shows amber fill when the room is quiet.
- **Gate flutters rapidly between open and closed** — The threshold is sitting exactly on the noise floor. Raise Thresh by a further 2–3 dB, or increase Release to slow the close time. See [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).
- **GATE applet is not visible** — The Gate stage may be bypassed or hidden. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).

## Related

- [Noise Gate / Expander overview](overview.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
