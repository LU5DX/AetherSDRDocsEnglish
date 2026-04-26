# Watch Live GR While Not Speaking

The gain-reduction bar in the GATE applet updates in real time, even while you are not transmitting. Use it to verify that the gate is silent when you are quiet and opens cleanly when you speak.

## Before you start

- The Gate stage must be enabled in the CHAIN widget. The GATE sub-container is hidden until the stage is active.
- The GATE sub-container must be visible inside the PooDoo Audio (TXDSP) parent container.

## Steps

1. Open the PooDoo Audio (TXDSP) container in the applet panel.
2. Locate the GATE sub-container. If it is not visible, enable the Gate stage via the CHAIN widget first.
3. Stay silent. Watch the amber **Gain-reduction bar** at the top of the applet. It fills from the right when the gate is applying attenuation.
4. Speak normally. The fill should collapse toward zero as your voice rises above the threshold and the gate opens.
5. Stop speaking. The bar should refill, showing attenuation returning. The speed of the refill reflects your **Release** setting.

## What each control does

| Control | Kind | Default | Valid range | Persisted key |
|---|---|---|---|---|
| Transfer curve | Indicator | — | — | — |
| Gain-reduction bar | Meter | — | 0 to 40 dB GR | — |
| Thresh | Knob | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` |
| Ratio | Knob | 2.0:1 | 1.0 to 10.0 | `ClientGateTxRatio` |
| Attack | Knob | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` |
| Release | Knob | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` |
| Floor | Knob | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` |

**Transfer curve** — plots the expander's static transfer curve. The live input ball moves along the curve and changes state to show whether the gate is currently open or closed.

**Gain-reduction bar** — horizontal amber strip, right-filled. Scale runs 0 to 40 dB. A tick mark at −15 dB indicates the soft-expander default floor. An empty bar means no attenuation is being applied. A full bar means the gate is applying maximum attenuation.

**Thresh** — level below which the gate starts attenuating. Set this just above your room noise floor. Linear mapping.

**Ratio** — attenuation steepness below the threshold. Higher values produce a harder gate; lower values produce a softer downward expansion. Linear mapping.

**Attack** — how quickly the gate opens when input rises above the threshold. Exponential mapping.

**Release** — how quickly the gate closes after input falls below the threshold. Exponential mapping.

**Floor** — maximum attenuation the gate is allowed to apply. Prevents the gate from cutting all the way to silence. Linear mapping.

## Tips

- Watch the input ball on the transfer curve alongside the gain-reduction bar. When the ball sits below the threshold marker, the bar should be filling. When the ball rises above it, the bar should be empty or nearly so.
- The knobs in the applet stay in sync with the floating Gate editor. Changes made in either place appear in both within one meter tick (approximately 33 ms).
- A tick mark at −15 dB on the gain-reduction bar corresponds to the default **Floor** value. If the bar never reaches that tick during silence, your **Thresh** may be set too low to catch background noise.

## Troubleshooting

- **Gain-reduction bar never moves** — The Gate stage may be bypassed. Check the CHAIN widget and confirm the stage is active. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).
- **Bar stays fully filled even when speaking loudly** — **Thresh** is likely set too high, so speech never rises above it. Lower **Thresh** or see [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md).
- **Bar empties and fills too abruptly, giving a choppy sound** — **Release** is too short. Increase the **Release** knob value. See [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).

## Related

- [Noise Gate / Expander overview](overview.md)
- [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
