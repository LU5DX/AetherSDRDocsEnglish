# Set Floor to avoid unnatural silence between words

A fully closed gate produces complete silence, which can sound unnatural during pauses in speech. The Floor knob limits how deep the gate can cut, so background audio is reduced rather than eliminated entirely.

## Before you start

- The TX Gate or RX gate stage must be enabled in the CHAIN widget. The ClientGateApplet is hidden until the Gate stage is active.
- Open the **Aetherial TX Gate** sub-container (TX side) inside the Aetherial Audio (TXDSP) parent container, or open the floating editor by double-clicking the GATE stage in the CHAIN widget.

## Steps

1. Locate the **Floor** knob in the five-knob row at the bottom of the **Aetherial TX Gate** applet.
2. Turn **Floor** clockwise to raise the floor (less attenuation, less silence) or counter-clockwise to lower it (more attenuation, deeper cut).
3. Watch the **Gain-reduction bar** while pausing speech. The amber fill should stop growing before it reaches the floor you set — the bar will not extend beyond the Floor value.
4. Speak normally and pause. Confirm that pauses sound like reduced background rather than dead silence.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Floor | -15.0 dB | -80.0 to 0.0 dB | `ClientGateTxFloorDb` | Maximum attenuation the gate is allowed to apply. Higher values (closer to 0 dB) preserve more audio during closure; lower values allow a deeper cut. |
| Gain-reduction bar | — | 0 to 40 dB GR | — | Horizontal amber strip, right-filled. Shows the current depth of attenuation. A tick mark at -15 dB indicates the default Floor position. |

For the RX side, the equivalent persisted key is `ClientGateRxFloorDb`. The Floor knob in the **Aetherial AGC-T** applet works identically.

## Tips

- The default Floor of -15.0 dB is marked by the tick on the gain-reduction bar. If attenuation at that value still sounds abrupt, try raising Floor to -10.0 dB or -6.0 dB.
- Floor only caps the attenuation ceiling — it does not change when or how fast the gate opens or closes. If the gate is opening and closing too sharply, also adjust Release. See [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).
- Setting Floor to 0.0 dB disables all attenuation, effectively bypassing the gate's effect without disabling it in the chain.

## Troubleshooting

- **The gain-reduction bar fills all the way regardless of Floor** — confirm you are adjusting the Floor knob on the correct side (TX or RX). The TX and RX applets have fully independent state and separate persisted keys.
- **Pauses still sound completely silent** — Floor may be set lower than -40.0 dB on the scale, or Ratio is very high (approaching 10:1), making the gate behave like a hard cut. Raise Floor toward -15.0 dB and consider lowering Ratio. See [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md).

## Related

- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
