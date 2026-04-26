# Sweep Freq to locate peak sibilance

Use the Freq knob to scan across the sibilance range while transmitting or monitoring audio, watching the gain-reduction bar for the frequency that triggers the most reduction. This identifies the centre of the problem sibilance band before you finalize your Q, Thresh, and Amount settings.

## Before you start

- The Aetherial De-Esser must be enabled via the CHAIN widget in the Aetherial Audio (TXDSP) container. The applet is hidden until the DESS stage is active.
- You need a live audio source — either transmitting or routing audio through the TX DSP chain — so the gain-reduction bar responds in real time.
- Open the de-esser applet or the floating editor. To open the floating editor, double-click the DESS stage in the CHAIN widget. The editor is titled "Aetherial De-Esser — TX".

## Steps

1. Set Thresh to a value just below your typical sibilance peaks — a starting point of -30.0 dB (the default) works for most voices.
2. Set Amount to a clearly audible value such as -12.0 dB or lower so gain reduction is easy to see on the bar.
3. Speak or play audio containing sustained "S" and "T" sounds continuously into the microphone.
4. Slowly turn the Freq knob from its default of 6.0 kHz upward or downward across the 1000 to 12000 Hz range.
5. Watch the gain-reduction bar. The bar fills furthest to the right — indicating maximum attenuation — when Freq is centred on the dominant sibilance band.
6. Stop at the Freq value that produces the highest gain-reduction reading. That value is your sibilance centre frequency.
7. Return Amount to your intended operating value (default -6.0 dB) once the sweep is complete.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Freq | 6000 Hz | 1000 to 12000 Hz | `ClientDeEssTxFrequencyHz` | Sets the centre frequency of the sibilance band. Uses logarithmic mapping. The sidechain response curve and its live centre-frequency ball update as you turn the knob. |
| Q | 2.00 | 0.5 to 5.0 | `ClientDeEssTxQ` | Sets the bandwidth of the sibilance band. Higher Q = narrower band. Keep Q moderate during the sweep so you do not miss the peak. |
| Thresh | -30.0 dB | -60.0 to 0.0 dB | `ClientDeEssTxThresholdDb` | Level above which attenuation starts. Set low enough during the sweep that the bar responds clearly to sibilance. |
| Amount | -6.0 dB | -24.0 to 0.0 dB | `ClientDeEssTxAmountDb` | Maximum attenuation applied at peak sibilance. Increase temporarily during the sweep to make the gain-reduction bar easier to read. |
| Sidechain response curve | — | — | — | Draws the bandpass filter response. The live ball marks the current centre frequency. |
| Gain-reduction bar | — | 0 to 24 dB GR | — | Horizontal soft-red strip, right-filled. A tick marks the -6 dB point. Refreshed at approximately 30 Hz. |

## Tips

- Keep Q at its default of 2.00 during the initial sweep. A very narrow Q can cause you to sweep past the true peak without triggering the bar. Narrow the band with Q only after you have located the peak.
- If the gain-reduction bar never moves, Thresh is set too high. Lower it until the bar responds to "S" sounds.
- The centre-frequency ball on the sidechain response curve moves as you turn Freq, giving a visual reference even before audio is present.

## Troubleshooting

- **Gain-reduction bar does not move during the sweep** — Thresh is above the level of your sibilance peaks. Lower Thresh until the bar begins to respond, then re-sweep.
- **Bar stays near maximum across a wide Freq range** — Amount is set to a very large negative value and Thresh is very low. Raise Thresh slightly so the bar discriminates between frequencies rather than clamping at maximum everywhere.
- **Applet is not visible** — The DESS stage has not been enabled in the CHAIN widget. Enable it there first; the applet remains hidden until the stage is active.

## Related

- [Aetherial De-Esser overview](overview.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
