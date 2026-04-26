# Set TX threshold just above room noise floor

Setting the Thresh knob to just above your ambient noise level tells the TX gate to pass speech while silencing the background hiss, fan noise, or mains hum that sits below that level between words.

## Before you start

- The Aetherial TX Gate must be enabled via the CHAIN widget on the TX side. The applet is hidden until the Gate stage is active.
- Open the "Aetherial TX Gate" sub-container inside the Aetherial Audio (TXDSP) parent container, or double-click the GATE stage in the CHAIN widget to open the floating "Aetherial Gate — TX" editor.

## Steps

1. Put your shack in its normal operating condition — background noise present, radio on, but do not transmit.
2. Watch the transfer curve's live input ball. The ball shows where your room noise currently sits on the input scale.
3. Watch the Gain-reduction bar. While you are silent, the bar should show amber fill, confirming the gate is actively attenuating.
4. Turn the Thresh knob slowly counterclockwise (lower) until the Gain-reduction bar just begins to fill amber when you stop speaking. This is the point where the gate catches room noise.
5. Turn Thresh clockwise (higher) by 2–3 dB past that point so the threshold sits comfortably above the noise floor.
6. Speak normally. The Gain-reduction bar should clear immediately when your voice begins and refill within the Release time after you stop. If the gate clips the start of words, see [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Thresh | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` | Level below which the gate begins attenuating. Set this just above your noise floor. |
| Ratio | 2.0 | 1.0 to 10.0 | `ClientGateTxRatio` | How aggressively the gate cuts below threshold. Higher values cut harder. |
| Attack | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` | How quickly the gate opens when input rises above threshold. |
| Release | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` | How quickly the gate closes after input falls below threshold. |
| Floor | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` | Maximum attenuation the gate is allowed to apply. Prevents complete silence between words. |

The **Transfer curve** plots the static input/output relationship and shows a live ball at the current input level. The **Gain-reduction bar** is an amber horizontal strip, right-filled, scaled 0 to 40 dB; a tick marks the −15 dB default floor.

## Tips

- Set Thresh by ear with the Gain-reduction bar as your guide: the bar should be fully lit during silence and clear the moment you speak.
- Leave Floor at −15.0 dB initially. A floor this shallow prevents the audio from dropping to an unnatural dead silence between words. Deepen it only if your noise floor is high enough to be audible at that level.
- If the input ball never rises above threshold when you speak, Thresh is set too high. Lower it until the ball crosses the threshold line on voice peaks.
- Changes to any knob take effect immediately and are saved automatically. No separate apply step is needed.

## Troubleshooting

- **Gate cuts into the beginning of words** — Attack is too slow, or Thresh is set too close to your voice level. Lower Thresh by 3–5 dB or reduce Attack. See [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).
- **Gain-reduction bar stays empty even during silence** — Thresh is set below the noise floor. Raise Thresh until the bar shows amber fill when the room is quiet.
- **Gate chops rapidly (chattering)** — Thresh is set right at the noise floor boundary. Raise Thresh 2–3 dB to create separation between the noise level and the threshold.
- **Applet is not visible** — The Gate stage is not enabled on the TX chain. Enable it via the CHAIN widget. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).

## Related

- [Aetherial TX Gate / Aetherial AGC-T (RX) overview](overview.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
