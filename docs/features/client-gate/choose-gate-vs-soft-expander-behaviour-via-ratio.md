# Choose Gate vs Soft-Expander Behaviour via Ratio

The Ratio knob controls how aggressively the gate attenuates audio below the threshold. Low values produce gentle downward expansion; high values produce a hard gate that cuts almost completely. Adjusting this one knob lets you choose anywhere on that spectrum without touching any other setting.

## Before you start

- The Gate stage must be enabled. If the GATE sub-container is not visible in the PooDoo Audio (TXDSP) panel, enable the Gate stage via the CHAIN widget or double-click the Gate stage in the CHAIN widget to open the floating Gate editor.
- You should be able to produce audio near your noise floor (fan noise, room ambience) so the effect is audible while you tune.

## Steps

1. Locate the GATE sub-container inside the PooDoo Audio (TXDSP) panel.
2. Find the knob labelled **Ratio** — it displays its value as `X.X:1`.
3. Turn **Ratio** toward **1.0** (minimum) for soft downward expansion: audio below the threshold is attenuated gently, with natural-sounding fades between words.
4. Turn **Ratio** toward **10.0** (maximum) for hard gate behaviour: audio below the threshold is cut sharply, approaching a full mute.
5. Watch the gain-reduction bar while speaking and then going silent. A moderate amber fill confirms attenuation is occurring. A full-width fill at high ratio settings indicates a hard cut is in effect.
6. Check the transfer curve — the slope of the curve below the threshold steepens as you raise the ratio, showing the harder cut visually.

## What each control does

| Control | Default | Valid range | Persisted key | Behaviour |
|---|---|---|---|---|
| Ratio | 2.0 | 1.0 to 10.0 | `ClientGateTxRatio` | Controls the steepness of attenuation below the threshold. Lower values act as a soft downward expander; higher values act as a hard gate. Displayed as `X.X:1`. |
| Thresh | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` | Level below which the gate begins to attenuate. The ratio is applied relative to this point. |
| Floor | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` | Maximum attenuation the gate is allowed to apply, regardless of ratio. The gain-reduction bar includes a tick mark at −15 dB marking this default. |
| Gain-reduction bar | — | 0 to 40 dB GR | — | Horizontal amber strip, right-filled. Shows the current depth of attenuation while the gate is active. |
| Transfer curve | — | — | — | Plots the static input-to-output curve. The slope below the threshold reflects the current ratio setting. The live input ball shows whether the gate is currently open or closed. |

## Tips

- A ratio of 2.0:1 (the default) is a reasonable starting point for voice: it reduces background noise noticeably without the unnatural snap of a hard gate.
- If speech sounds clipped or chopped at high ratios, raise the Floor value toward 0 dB to limit maximum cut, or reduce the ratio.
- The Floor knob caps attenuation regardless of how high you set the ratio. If a hard gate is not cutting deep enough, check that Floor is set low enough (for example, −40 dB or lower) to allow the full cut.
- Changes made in the floating Gate editor are reflected in the GATE applet knobs within one refresh cycle, and vice versa.

## Troubleshooting

- **Ratio is at 10.0:1 but background noise is still audible between words** — the Floor value may be limiting attenuation before the gate reaches full depth. Lower `ClientGateTxFloorDb` (for example, to −40.0 dB or below) to allow deeper cuts.
- **Speech sounds unnaturally chopped even at moderate ratios** — the threshold may be set too high, causing the gate to trigger on quiet speech as well as noise. Lower `ClientGateTxThresholdDb` until only genuine background noise falls below it.
- **Transfer curve does not update when the Ratio knob is turned** — the GATE stage may not be enabled. Enable it via the CHAIN widget.

## Related

- [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Noise Gate / Expander overview](overview.md)
