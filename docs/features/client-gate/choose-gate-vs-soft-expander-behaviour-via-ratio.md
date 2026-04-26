# Choose gate vs soft-expander behaviour via ratio

The Ratio knob controls how aggressively the gate attenuates audio below the threshold. Setting a high ratio produces a hard, near-total cut (classic gate behaviour); setting a low ratio produces a gentler, graduated reduction (soft downward expander). Choosing the right value prevents abrupt on/off switching while still cleaning up background noise.

## Before you start

- The gate must be enabled on the side you want to adjust (TX or RX). Enable it via the CHAIN widget or by double-clicking the GATE stage in the CHAIN widget to open the floating editor.
- The "Aetherial TX Gate" or "Aetherial AGC-T" sub-container must be visible in the Applet Panel.

## Steps

1. Locate the **Aetherial TX Gate** sub-container (TX side) or **Aetherial AGC-T** sub-container (RX side) in the Applet Panel.
2. Find the **Ratio** knob in the five-knob row at the bottom of the applet. Its label reads in the format `X.X:1`.
3. Turn **Ratio** toward `1.0:1` for a soft downward expander — audio below the threshold is attenuated gradually rather than cut hard.
4. Turn **Ratio** toward `10.0:1` for a harder, more gate-like cut — audio below the threshold is reduced steeply, approaching silence at the **Floor** value.
5. Watch the gain-reduction bar (the amber strip above the knob row) while the input is below threshold. A deeper amber fill confirms more attenuation is being applied.
6. Speak or play audio across the threshold and observe the transfer curve. The live input ball moves along the curve; the slope of the curve below the threshold steepens as Ratio increases.

## What each control does

| Control | Default | Valid range | Persisted key (TX / RX) | Behaviour |
|---|---|---|---|---|
| **Ratio** | `2.0` | `1.0` to `10.0` | `ClientGateTxRatio` / `ClientGateRxRatio` | Slope of the transfer curve below the threshold. `1.0:1` = no attenuation (expander off). `10.0:1` = near-total cut. Linear knob mapping. |
| **Thresh** | `-40.0 dB` | `-80.0` to `0.0 dB` | `ClientGateTxThresholdDb` / `ClientGateRxThresholdDb` | Level below which the gate begins attenuating. Ratio only has effect below this point. |
| **Floor** | `-15.0 dB` | `-80.0` to `0.0 dB` | `ClientGateTxFloorDb` / `ClientGateRxFloorDb` | Maximum attenuation the gate is allowed to apply, regardless of Ratio. A tick at −15 dB on the gain-reduction bar marks this default. |

## Tips

- A ratio of `2.0:1` (the default) behaves as a soft downward expander — a good starting point for TX voice gating where abrupt silence between words sounds unnatural.
- Raising Ratio above `5.0:1` approaches true gate behaviour. Pair this with a non-zero **Floor** value (for example, `-15.0 dB`) to prevent complete silence cutting in harshly.
- Changes made in the applet knobs and in the floating editor (opened by double-clicking the GATE stage in the CHAIN widget) stay in sync automatically.

## Troubleshooting

- **Ratio is at maximum but background noise is still audible between words** — The **Floor** setting is limiting attenuation before silence is reached. Lower **Floor** toward `-80.0 dB`, or lower **Thresh** so the gate engages at the actual noise level. See [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md) and [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md).
- **Audio cuts in and out too abruptly when Ratio is high** — Increase **Release** to let the gate close more slowly, or lower **Ratio** toward `2.0:1` to soften the transition. See [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).

## Related

- [Aetherial TX Gate / Aetherial AGC-T (RX) overview](overview.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
