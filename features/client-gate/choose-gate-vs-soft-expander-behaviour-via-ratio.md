# Choose gate vs soft-expander behaviour via ratio

The Ratio knob controls whether the Noise Gate / Expander acts as a gentle downward expander or a hard noise gate. Adjusting it lets you match the processing character to your microphone and operating environment.

## Before you start

- The GATE applet must be visible in the applet panel. If it is hidden, enable the Gate stage via the CHAIN widget or double-click the Gate stage in the CHAIN widget to open the floating Gate editor.
- The Gate stage must be enabled. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if you need to turn it on first.
- Transmit audio must be flowing so the transfer curve and gain-reduction bar reflect live behaviour while you adjust.

## Steps

1. Locate the Ratio knob in the GATE applet. It is the second knob from the left in the five-knob row, labelled "Ratio".
2. Watch the transfer curve. The curve steepens as you increase Ratio, showing how aggressively the processor attenuates signal below the threshold.
3. Turn Ratio toward **1.0:1** for soft-expander behaviour. At low ratios, audio below the threshold is reduced gently rather than cut hard — pauses between words remain audible but quieter.
4. Turn Ratio toward **10.0:1** for hard gate behaviour. At high ratios, audio below the threshold is cut sharply, producing near-silence between words.
5. Speak normally and watch the gain-reduction bar. The amber fill shows the current attenuation depth. The tick at −15 dB on the bar marks the default Floor value; if your amber fill regularly reaches or exceeds that tick at your chosen ratio, consider adjusting Floor. See [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md).

## What each control does

| Control | Default | Valid range | Persisted key | Behaviour |
|---|---|---|---|---|
| Ratio | 2.0 | 1.0 to 10.0 | `ClientGateTxRatio` | Linear mapping. Displayed as X.X:1. Lower values give soft downward expansion; higher values give a harder, more gate-like cut. |
| Thresh | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` | Level below which the gate begins attenuating. Sets the point at which Ratio takes effect. |
| Floor | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` | Maximum attenuation the gate is allowed to apply, regardless of Ratio. |
| Gain-reduction bar | — | 0 to 40 dB GR | — | Horizontal amber strip, right-filled. Shows current attenuation depth. Tick at −15 dB marks the default Floor. |
| Transfer curve | — | — | — | Plots the static input-to-output curve and a live ball at the current input level. |

## Tips

- Start with Ratio at 2.0:1 (the default) and raise it only until background noise disappears between transmissions. Unnecessarily high ratios make speech sound chopped.
- The live ball on the transfer curve shows whether the gate is open (ball above the threshold knee) or closed (ball below). Use it together with the gain-reduction bar to judge whether Ratio is set appropriately before going on air.
- Changes to Ratio are saved immediately to `ClientGateTxRatio` and survive a restart. No separate save step is needed.
- If the gate closes too slowly after you stop speaking, a high Ratio will make the tail of words sound cut off. Adjust Release in conjunction with Ratio. See [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).

## Troubleshooting

- **Ratio knob has no effect on the transfer curve** — The Gate stage may be bypassed. Check the CHAIN widget and confirm the Gate stage is active. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).
- **Gate cuts into the beginnings or ends of words even at moderate Ratio** — Thresh may be set too high, causing the gate to close on speech transients. Lower Thresh so the knee sits below your voice level. See [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md). Also check Attack and Release. See [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).
- **Background noise is still audible at high Ratio** — Floor may be limiting how much attenuation is applied. Lower Floor below the noise floor level. See [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md).

## Related

- [Noise Gate / Expander overview](overview.md)
- [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
