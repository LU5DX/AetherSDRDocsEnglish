# Set threshold just below the loudest 'S' peaks

The **Thresh** knob controls the level above which the de-esser begins attenuating the sibilance band. Setting it just below your loudest 'S' peaks ensures the de-esser triggers on harsh sibilance without affecting normal speech.

## Before you start

- The De-Ess stage must be enabled in the CHAIN widget and the DESS applet must be visible. See [De-Esser overview](overview.md).
- Identify the sibilance centre frequency first. See [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md).

## Steps

1. Open the DESS sub-container inside the PooDoo Audio (TXDSP) parent container. If it is hidden, double-click the DeEss stage in the CHAIN widget to open the floating De-Ess editor.
2. Key your transmit audio and speak a sustained 'S' sound or a sibilant phrase.
3. Watch the gain-reduction bar. If it shows no soft-red fill, the threshold is set too high and the de-esser is not triggering.
4. Turn the **Thresh** knob counter-clockwise to lower the threshold until the gain-reduction bar begins to show a small fill on your loudest 'S' peaks.
5. Continue speaking sibilant phrases. Adjust **Thresh** upward again until the gain-reduction bar barely activates on normal speech but lights up clearly on harsh 'S' sounds.
6. Confirm the value shown below the **Thresh** knob is set just below the level of your peak sibilance. A typical starting point is around `-30.0 dB`.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Thresh** | -30.0 dB | -60.0 to 0.0 dB | `ClientDeEssTxThresholdDb` | Level above which the de-esser starts attenuating the sibilance band. |
| Gain-reduction bar | — | 0 to 24 dB GR | — | Horizontal soft-red strip, right-filled. Shows current attenuation being applied. A tick marks the -6 dB point. Refreshed at approximately 30 Hz. |

## Tips

- The gain-reduction bar is your primary feedback tool. A threshold set correctly will show brief, moderate activity on 'S' and 'T' sounds and remain empty during vowels and normal consonants.
- The gain-reduction bar scale maxes at 24 dB. If the bar is consistently pegged near full, **Thresh** is too low or **Amount** is too aggressive. Raise **Thresh** first, then revisit **Amount**.
- If the bar never lights during heavy sibilance, raise **Freq** or widen the band with **Q** before concluding the threshold needs changing. See [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md).

## Troubleshooting

- **Gain-reduction bar shows no activity despite loud 'S' sounds** — **Thresh** is set above the sibilance level. Lower it gradually until the bar activates on peak 'S' sounds.
- **Gain-reduction bar is active continuously during normal speech** — **Thresh** is set too low. Raise it until the bar is mostly quiet and only triggers on true sibilance peaks.
- **De-esser triggers but speech sounds over-processed** — The threshold may be correct but **Amount** is too large. See [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md).

## Related

- [De-Esser overview](overview.md)
- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)
