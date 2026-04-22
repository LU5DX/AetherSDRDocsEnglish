# Sweep Freq to locate peak sibilance

Use the Freq knob to scan across the sibilance band until the gain-reduction meter peaks, pinpointing the centre frequency where your microphone produces the harshest "S" and "T" sounds.

## Before you start

- The De-Ess stage must be enabled in the CHAIN widget. The De-Esser applet (DESS) is hidden until the stage is active.
- Open the DESS sub-container inside the PooDoo Audio (TXDSP) parent container. If it is not visible, double-click the DeEss stage in the CHAIN widget to open the floating editor, or right-click the DESS sub-container titlebar and select the appropriate option.
- Set Thresh to a level where sibilance already triggers some gain reduction before you start sweeping. See [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md).

## Steps

1. Speak or repeatedly say a sibilant phrase ("sixty-six", "Mississippi") into your microphone at your normal operating level.
2. Watch the Gain-reduction bar at the top of the DESS applet — soft-red fill moving rightward indicates the de-esser is actively attenuating.
3. Turn the Freq knob slowly from its default of 6.0 kHz upward or downward across the 1000–12000 Hz range.
4. Stop at the position where the Gain-reduction bar shows the deepest fill during your sibilant phrase — this is the centre frequency of peak sibilance for your voice and microphone combination.
5. Observe the centre-frequency ball on the Sidechain response curve; it moves along the curve peak to confirm the currently tuned frequency.
6. Continue speaking sibilant phrases and make small adjustments to Freq until the Gain-reduction bar responds most aggressively and consistently.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Freq | 6000 Hz | 1000 to 12000 Hz | `ClientDeEssTxFrequencyHz` | Sets the centre frequency of the sibilance band. Uses logarithmic mapping. Labels show "X.X kHz" at or above 1000 Hz. |
| Q | 2.00 | 0.5 to 5.0 | `ClientDeEssTxQ` | Sets the bandwidth of the sibilance band. Higher Q = narrower notch. |
| Thresh | -30.0 dB | -60.0 to 0.0 dB | `ClientDeEssTxThresholdDb` | Level above which the de-esser begins attenuating. |
| Amount | -6.0 dB | -24.0 to 0.0 dB | `ClientDeEssTxAmountDb` | Maximum attenuation applied at peak sibilance. |
| Sidechain response curve | — | — | — | Displays the bandpass filter response with a live ball at the current centre frequency. |
| Gain-reduction bar | — | 0 to 24 dB GR | — | Horizontal soft-red strip, right-filled. A tick marks the -6 dB point. Refreshed at approximately 30 Hz. |

## Tips

- Narrow Q before sweeping if your sibilance is sharp and tonal — a tighter band makes the Gain-reduction bar respond more selectively, making the peak easier to locate.
- If the Gain-reduction bar stays empty throughout the sweep, Thresh is set too high. Lower it until you see a response, then re-sweep.
- A Q of 2.00 (the default) is a reasonable starting width for an initial sweep. Refine with Q after you find the frequency.

## Troubleshooting

- **Gain-reduction bar shows no fill at any Freq position** — Thresh is set above your sibilance level. Lower Thresh until the bar responds, or increase your microphone gain and retry.
- **Gain-reduction bar is always fully filled regardless of Freq position** — Amount is set very high or Thresh is far below your average level, causing the de-esser to trigger on all audio, not just sibilance. Raise Thresh and reduce Amount before sweeping.
- **DESS applet is not visible** — The De-Ess stage is not enabled in the CHAIN widget. Enable it there first.

## Related

- [De-Esser overview](overview.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
