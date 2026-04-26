# Watch live GR while reading a sibilant phrase

The gain-reduction (GR) bar in the Aetherial De-Esser updates in real time while you transmit or speak. Use this procedure to watch the meter respond as you read a sibilant phrase, so you can confirm the de-esser is catching your "S" and "T" sounds before going on air.

## Before you start

- The Aetherial De-Esser must be enabled via the CHAIN widget. The applet is hidden until the De-Ess stage is active.
- Your microphone must be routed through the TX audio chain and producing signal — either by keying the radio or by using a monitor/test mode so audio flows through the DSP.
- Open the "Aetherial De-Esser" sub-container inside the Aetherial Audio (TXDSP) parent container, or double-click the DESS stage in the CHAIN widget to open the floating "Aetherial De-Esser — TX" editor.

## Steps

1. Ensure the De-Ess stage is enabled in the CHAIN widget. The applet will be visible once the stage is active.
2. Locate the **Gain-reduction bar** — the horizontal strip directly below the sidechain response curve.
3. Key your radio or activate your audio path so microphone audio flows through the TX DSP.
4. Speak a phrase containing heavy sibilance — for example, "She sells seashells by the seashore" — at your normal microphone level and distance.
5. Watch the **Gain-reduction bar** fill from right to left in soft red on each "S" or "T" sound. No fill means the de-esser is not triggering; a fill that reaches the full width means up to 24 dB of reduction is being applied.
6. Note where the bar typically peaks. The tick mark on the bar indicates the −6 dB point, which is the default **Amount** value and a common target for transparent de-essing.
7. If the bar never moves, lower **Thresh** toward −60.0 dB until it begins to respond. If the bar is pegged to the right on every syllable, raise **Thresh** toward 0.0 dB.
8. Repeat the phrase until the bar responds only on genuine sibilant peaks, not on ordinary speech.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Sidechain response curve | — | — | — | Draws the bandpass filter response. A live ball marks the current centre frequency. |
| Gain-reduction bar | — | 0 to 24 dB GR | — | Horizontal soft-red strip, right-filled. Refreshed at approximately 30 Hz. A tick marks the −6 dB point. |
| Freq | 6000 Hz | 1000 to 12000 Hz | `ClientDeEssTxFrequencyHz` | Centre frequency of the sibilance band. Uses logarithmic mapping. |
| Q | 2.00 | 0.5 to 5.0 | `ClientDeEssTxQ` | Bandwidth of the sibilance band. Higher Q = narrower. |
| Thresh | −30.0 dB | −60.0 to 0.0 dB | `ClientDeEssTxThresholdDb` | Level above which the de-esser begins attenuating the band. |
| Amount | −6.0 dB | −24.0 to 0.0 dB | `ClientDeEssTxAmountDb` | Maximum attenuation applied at peak sibilance. |

## Tips

- The meter runs at approximately 30 Hz, so short, sharp transients may appear as brief flashes. This is normal.
- Keep the **Amount** knob at its default of −6.0 dB while watching the meter for the first time. Dial it down only after you have confirmed the meter is triggering on the right sounds.
- If the ball on the sidechain response curve sits far from where your sibilance peaks, use **Freq** to move it. The meter will only show GR when energy in the current **Freq** band crosses **Thresh**.

## Troubleshooting

- **Gain-reduction bar never moves** — The de-esser is not triggering. Check that the De-Ess stage is enabled in the CHAIN widget, that audio is flowing through the TX DSP, and that **Thresh** is not set too high (too close to 0.0 dB) for your microphone level.
- **Gain-reduction bar is pegged to the right on every syllable, including non-sibilant speech** — **Thresh** is set too low. Raise it toward 0.0 dB until ordinary vowels no longer trigger the meter.
- **Bar moves but you hear no effect on air** — **Amount** may be set too close to 0.0 dB. Lower it toward −24.0 dB for more audible reduction, or confirm the stage is not bypassed in the CHAIN widget.

## Related

- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)
