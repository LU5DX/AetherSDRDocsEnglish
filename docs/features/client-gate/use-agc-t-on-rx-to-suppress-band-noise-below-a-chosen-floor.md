# Use AGC-T on RX to suppress band noise below a chosen floor

The Aetherial AGC-T applet applies a client-side downward expander to received audio, attenuating signals that fall below a set threshold. Use it to reduce persistent band noise or hiss that sits beneath the audio you want to hear.

## Before you start

- AetherSDR must be running. A radio connection is not required to configure the controls, but you need audio flowing to see the live meters respond.
- The "Aetherial AGC-T" sub-container must be visible in the Applet Panel. It is hidden until the Gate stage is enabled on the RX side via the CHAIN widget or the floating editor.

## Steps

1. Enable the Gate stage on the RX side: single-click the Gate stage in the CHAIN widget on the RX side, or open the floating editor titled "Aetherial Gate — RX" by double-clicking the Gate stage in the CHAIN widget.
2. Locate the "Aetherial AGC-T" sub-container inside the Aetherial Audio (TXDSP) parent container in the Applet Panel.
3. Watch the transfer curve and the input ball while receiving. When the ball sits below the knee, the gate is attenuating.
4. Turn the Thresh knob to set the level below which attenuation begins. Start near your band noise floor — a typical starting point is around −40.0 dB — and raise it until band noise is reduced but wanted signals open the gate cleanly.
5. Turn the Ratio knob to control how aggressively signals below the threshold are cut. Lower values (closer to 1.0) give a gentle downward expansion; higher values give a harder cut.
6. Turn the Floor knob to set how deep the attenuation can go. The default −15.0 dB prevents complete silence while still reducing noise usefully.
7. Turn the Attack knob to set how quickly the gate opens when a signal rises above the threshold. Faster values let leading edges through cleanly.
8. Turn the Release knob to set how quickly the gate closes after a signal falls. Slower values avoid choppy cutoff on signal tails.
9. Watch the Gain-reduction bar. The amber fill shows current attenuation depth. Aim for steady fill during band noise and a drop to near-empty when a signal arrives.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| Thresh | −40.0 dB | −80.0 to 0.0 dB | `ClientGateRxThresholdDb` |
| Ratio | 2.0 | 1.0 to 10.0 | `ClientGateRxRatio` |
| Attack | 0.5 ms | 0.1 to 100.0 ms | `ClientGateRxAttackMs` |
| Release | 100 ms | 5 to 2000 ms | `ClientGateRxReleaseMs` |
| Floor | −15.0 dB | −80.0 to 0.0 dB | `ClientGateRxFloorDb` |
| Transfer curve | — | — | — |
| Gain-reduction bar | — | 0 to 40 dB GR | — |

**Transfer curve** — plots the expander's static input-to-output relationship. A live input ball moves along the curve to show whether the gate is currently open or closed.

**Gain-reduction bar** — horizontal amber strip, right-filled. Scale maxes at 40 dB. A tick mark at −15 dB indicates the default Floor position.

## Tips

- The knobs in the applet tile and the floating "Aetherial Gate — RX" editor stay in sync. Changes made in either location take effect immediately and are saved automatically.
- If wanted signals are being cut, lower Thresh or shorten Attack so the gate responds faster to rising audio.
- If band noise bleeds through between signals, raise Thresh or lower Floor to allow deeper attenuation.
- The −15 dB tick on the Gain-reduction bar is a useful reference: if the amber fill regularly exceeds that mark, band noise may be louder than the Floor setting can fully suppress.

## Troubleshooting

- **"Aetherial AGC-T" sub-container is not visible** — the Gate stage on the RX side has not been enabled. Enable it via the CHAIN widget or the floating "Aetherial Gate — RX" editor.
- **Gain-reduction bar shows no movement during band noise** — Thresh is set below the noise floor. Raise Thresh until the amber fill appears during noise-only periods.
- **Signals are being clipped or cut short** — Attack is too slow or Thresh is too high. Lower Thresh slightly, or reduce Attack to open the gate faster when a signal arrives.
- **Audio sounds choppy between words** — Release is too short. Increase Release so the gate closes more gradually after a signal falls.

## Related

- [Aetherial TX Gate / Aetherial AGC-T (RX) overview](overview.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
