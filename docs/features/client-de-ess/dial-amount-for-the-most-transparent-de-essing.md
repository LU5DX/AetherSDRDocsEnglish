# Dial Amount for the most transparent de-essing

The Amount knob sets the maximum attenuation the de-esser applies when sibilance peaks above the threshold. Dialing the right value lets you tame harshness without making your audio sound processed or pumped.

## Before you start

- The Aetherial De-Esser (DESS) stage must be enabled in the CHAIN widget. The applet is hidden until the stage is active.
- Open the Aetherial De-Esser applet or the floating editor. To open the editor, double-click the DESS stage in the CHAIN widget (titled "Aetherial De-Esser — TX").
- Set Freq and Thresh first so the de-esser is already triggering on the right band. See [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md) and [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md).

## Steps

1. Have someone transmit into the microphone — or read a sibilant phrase aloud — so the de-esser is actively triggering.
2. Watch the Gain-reduction bar. It fills right-to-left in soft red to show how much attenuation is being applied. A tick marks the −6 dB point.
3. Turn the Amount knob counterclockwise to increase attenuation (more negative values) until the harshness is gone.
4. Back off clockwise until the Gain-reduction bar only reaches the −6 dB tick on the loudest "S" peaks. Stopping here keeps processing transparent.
5. If the Gain-reduction bar is pegged near 24 dB or the audio sounds hollow, raise Amount toward 0 dB in small steps until naturalness returns.
6. Changes are saved automatically. The setting persists as `ClientDeEssTxAmountDb`.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Amount | −6.0 dB | −24.0 to 0.0 dB | `ClientDeEssTxAmountDb` | Maximum attenuation applied to the sibilance band when signal exceeds the threshold. More negative = more reduction. 0 dB disables attenuation entirely. |
| Gain-reduction bar | — | 0 to 24 dB GR | — | Horizontal soft-red strip showing current gain reduction in real time. Scale maxes at 24 dB; a tick marks −6 dB. Refreshed approximately 30 times per second. |

## Tips

- −6 dB (the default) is a reasonable starting point for most voices. The tick on the Gain-reduction bar marks this level, making it easy to use as a reference during adjustment.
- Aim for the Gain-reduction bar to move noticeably on "S" and "T" sounds but never pin against the 24 dB end. Heavy gain reduction at that extreme is audible as a lisp or dropout.
- Narrowing the sidechain band with Q before finalizing Amount reduces collateral attenuation on nearby speech energy, which helps transparency. See [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md).
- Amount values are always negative or zero — they represent reduction, not boost.

## Troubleshooting

- **Audio sounds hollow or lisping on every "S"** — Amount is set too low (too much attenuation). Raise it toward 0 dB in 2 dB steps while speaking until naturalness returns.
- **Gain-reduction bar never moves** — The de-esser is not triggering. Check that Thresh is set below your actual sibilance level and that the DESS stage is enabled. See [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md).
- **Gain-reduction bar pins at 24 dB constantly** — Thresh is set too low, causing the de-esser to trigger on all speech, not just sibilance. Raise Thresh first, then re-evaluate Amount.

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)
- [Aetherial De-Esser overview](overview.md)
