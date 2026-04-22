# Dial Amount for the most transparent de-essing

The Amount knob sets the maximum attenuation the de-esser applies when sibilance peaks hit hardest. Dialing it to the smallest value that tames harshness keeps the treatment inaudible on normal speech.

## Before you start

- The De-Ess stage must be enabled. See [De-Esser overview](overview.md) for how to enable the stage from the CHAIN widget.
- The DESS applet must be visible inside the PooDoo Audio (TXDSP) container. If it is hidden, double-click the DeEss stage in the CHAIN widget to open the floating editor, or right-click the DESS sub-container titlebar and show it.
- Set Freq and Thresh before adjusting Amount, so the de-esser is already triggering on your sibilance. See [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md) and [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md).

## Steps

1. Open the DESS applet inside the PooDoo Audio (TXDSP) container.
2. Speak continuously into the microphone, repeating sibilant words ("sister", "sixty-six", "success") to keep the de-esser triggering.
3. Watch the Gain-reduction bar. The soft-red fill shows how much attenuation is being applied right now; the tick marks the −6 dB point.
4. Turn the Amount knob fully counter-clockwise to its minimum (−24.0 dB) so you can hear the effect clearly.
5. Slowly turn Amount clockwise (toward 0.0 dB) until the harshness returns, then back off slightly — this is the most transparent setting.
6. Confirm the Gain-reduction bar peaks briefly on hard 'S' sounds but sits near zero on normal vowels. If it is pegged at maximum on ordinary speech, the threshold is set too low; see [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md).
7. Release the knob. The value is saved automatically to `ClientDeEssTxAmountDb`.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Amount | −6.0 dB | −24.0 to 0.0 dB | `ClientDeEssTxAmountDb` | Maximum attenuation applied to the sibilance band when the sidechain signal is at its peak. Values are negative because they represent reduction. 0.0 dB means no attenuation. |
| Gain-reduction bar | — | 0 to 24 dB shown | — | Horizontal soft-red strip, right-filled. Shows current attenuation in real time. A tick marks the −6 dB point. Refreshed approximately 30 times per second. |

## Tips

- The −6.0 dB default is a safe starting point. Most voices need between −3.0 dB and −9.0 dB for transparent treatment.
- Larger negative values (toward −24.0 dB) produce more aggressive ducking that is easier to hear as an artifact. Use only for severe sibilance.
- If you cannot find a setting where sibilants are tamed without affecting normal speech, the sidechain band may be too wide. Narrow it first with the Q knob; see [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md).
- Use [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md) to evaluate the final setting under realistic conditions before transmitting.

## Troubleshooting

- **Gain-reduction bar is always pegged at the Amount limit** — Thresh is set too low and the de-esser is triggering on all speech, not just sibilants. Raise Thresh until the bar only deflects on hard 'S' and 'T' sounds.
- **No gain reduction shows even with Amount at −24.0 dB** — The de-esser is not triggering. Either the stage is bypassed or Thresh is above your sibilance level. Check that the stage is enabled in the CHAIN widget, then lower Thresh.
- **Amount change has no effect after reconnecting** — Settings are restored from `ClientDeEssTxAmountDb` on load. If the knob shows the correct value but the audio is unaffected, confirm the De-Ess stage is enabled, not bypassed; see [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md).

## Related

- [De-Esser overview](overview.md)
- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)
