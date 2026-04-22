# Watch live GR while reading a sibilant phrase

Use the gain-reduction bar in the De-Esser applet to see how much attenuation the de-esser is applying in real time. Reading a phrase heavy with "S" and "T" sounds while watching the bar helps you confirm your Thresh and Amount settings are working correctly before going on air.

## Before you start

- The De-Ess stage must be enabled via the CHAIN widget. The DESS applet is hidden until the stage is active.
- The DESS sub-container must be visible inside the PooDoo Audio (TXDSP) parent container. If it is not visible, right-click the DESS sub-container titlebar and select the option to show it, or double-click the DeEss stage in the CHAIN widget to open the floating De-Ess editor.
- Your microphone and TX audio path must be active so that live audio is passing through the de-esser.

## Steps

1. Open the DESS sub-container in the PooDoo Audio (TXDSP) parent container.
2. Locate the gain-reduction bar — the horizontal strip directly below the sidechain response curve.
3. Key your transmitter and read a sibilant phrase aloud (for example, "sixty-six sizzling sausages").
4. Watch the gain-reduction bar fill from the right with a soft-red color on each "S" or "T" sound. The bar scale runs 0 to 24 dB; a tick mark at the one-quarter position from the right indicates the −6 dB point.
5. If the bar never fills, the de-esser is not triggering — lower Thresh toward a more negative value.
6. If the bar pegs at maximum on every syllable, not just sibilants, raise Thresh toward 0 dB or reduce Amount.
7. Aim for the bar reaching roughly the −6 dB tick on sharp sibilants and returning to empty between words.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Sidechain response curve | — | — | — | Draws the bandpass filter shape; a live ball marks the current centre frequency. |
| Gain-reduction bar | — | 0 to 24 dB GR | — | Horizontal soft-red strip, right-filled. Shows attenuation currently applied to the sibilance band. A tick marks the −6 dB point. Refreshed at approximately 30 Hz. |
| Freq | 6000 Hz | 1000 to 12000 Hz | `ClientDeEssTxFrequencyHz` | Sets the centre frequency of the sibilance band. Uses logarithmic mapping. |
| Q | 2.00 | 0.5 to 5.0 | `ClientDeEssTxQ` | Sets the bandwidth of the sibilance band. Higher Q is narrower. |
| Thresh | −30.0 dB | −60.0 to 0.0 dB | `ClientDeEssTxThresholdDb` | Level above which the de-esser begins attenuating. |
| Amount | −6.0 dB | −24.0 to 0.0 dB | `ClientDeEssTxAmountDb` | Maximum attenuation applied at peak sibilance. |

## Tips

- The gain-reduction bar updates at approximately 30 Hz, so fast transient "S" sounds may appear as brief flickers. This is normal.
- The centre-frequency ball on the sidechain response curve moves with Freq. Watching both the ball and the bar together helps confirm the de-esser is centered on the correct part of your voice.
- Keep the bar from pegging at 24 dB: that indicates more reduction than Amount allows, which means Thresh is set too low.

## Troubleshooting

- **Gain-reduction bar stays empty during speech** — The de-esser is not triggering. Lower Thresh (more negative) until the bar reacts on sharp sibilants. Also confirm the De-Ess stage is enabled in the CHAIN widget and that audio is actually passing through the TX chain.
- **Gain-reduction bar fills continuously, not just on sibilants** — Thresh is too low or Freq is centered on a frequency that dominates your voice. Raise Thresh or sweep Freq to a higher frequency where sibilance is more isolated.
- **DESS applet is not visible** — The De-Ess stage is not enabled. Enable it via the CHAIN widget or by double-clicking the DeEss stage in the CHAIN widget to open the floating editor, then enable from there.

## Related

- [De-Esser overview](overview.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)
