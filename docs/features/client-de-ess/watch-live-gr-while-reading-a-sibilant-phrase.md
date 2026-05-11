# Watch live GR while reading a sibilant phrase

The gain-reduction (GR) bar in the Aetherial De-Esser updates in real time while you transmit or speak. Use this procedure to watch the meter respond as you read a sibilant phrase, so you can confirm the de-esser is catching your "S" and "T" sounds before going on air.

## Before you start

- The Aetherial De-Esser must be enabled via the CHAIN widget. The applet is hidden until the De-Ess stage is active.
- Your microphone must be routed through the TX audio chain and producing signal — either by keying the radio or by using a monitor/test mode so audio flows through the DSP.
- Open the "Aetherial De-Esser" sub-container inside the Aetherial Audio (TXDSP) parent container. Bypass and editing are both handled through the Aetherial Audio Channel Strip — there is no separate floating editor for the de-esser in v0.9.7.
- The de-esser panel supports both TX and RX sides. The RX instance is titled "Aetherial De-Esser — RX" and is reachable through the Aetherial Audio Channel Strip.

## Steps

1. Ensure the De-Ess stage is enabled in the CHAIN widget. The applet will be visible once the stage is active. When the stage is bypassed, the entire tile dims to approximately 55% opacity.
2. Locate the **Gain-reduction bar** — the horizontal strip directly below the sidechain response curve.
3. Key your radio or activate your audio path so microphone audio flows through the TX DSP.
4. Speak a phrase containing heavy sibilance — for example, "She sells seashells by the seashore" — at your normal microphone level and distance.
5. Watch the **Gain-reduction bar** fill from right to left in soft red on each "S" or "T" sound. No fill means the de-esser is not triggering; a fill that reaches the full width means up to 24 dB of reduction is being applied.
6. Note where the bar typically peaks. The tick mark on the bar indicates the −6 dB point, which is the default **Amount** value and a common target for transparent de-essing.
7. If the bar never moves, lower **Thresh** toward −60.0 dB until it begins to respond. If the bar is pegged to the right on every syllable, raise **Thresh** toward 0.0 dB.
8. Repeat the phrase until the bar responds only on genuine sibilant peaks, not on ordinary speech.

## What each control does

| Control                  | Default  | Valid range      | Description                                                                                                                                 |
|--------------------------|----------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Sidechain response curve | —        | —                | Compact-mode ClientDeEssCurveWidget. Draws the bandpass filter response with a live ball at the current centre frequency.                   |
| Gain-reduction bar       | —        | 0 to 24 dB GR    | Horizontal soft-red strip, right-filled. Scale maxes at 24 dB; a tick marks the −6 dB typical amount. Refreshed ~30 Hz.                      |
| Freq                     | 6000 Hz  | 1000 to 12000 Hz | Logarithmic mapping. Sets the centre frequency of the sibilance band. Label shows "6.0 kHz" above 1 kHz, "N Hz" below.                      |
| Q                        | 2.00     | 0.5 to 5.0       | Linear mapping. Sets the bandwidth of the sibilance band — higher Q = narrower. Label shows "X.XX".                                         |
| Thresh                   | −30.0 dB | −60.0 to 0.0 dB  | Linear mapping. Level above which the de-esser starts attenuating the band.                                                                 |
| Amount                   | −6.0 dB  | −24.0 to 0.0 dB  | Linear mapping. Maximum attenuation applied at peak sibilance. Values are negative (or zero) because they represent reduction.              |
| Attack                   | 1.0 ms   | 0.1 to 30.0 ms   | Exponential mapping. Sets how quickly the de-esser responds once sibilance crosses the threshold. Present only in the Channel Strip panel. |
| Release                  | 100 ms   | 10.0 to 500.0 ms | Exponential mapping. Sets how quickly gain returns after sibilance drops below the threshold. Present only in the Channel Strip panel.      |

**Note:** Attack and Release controls are available in the Channel Strip's StripDeEssPanel (both RX and TX instances). The docked ClientDeEssApplet omits these two knobs.

## Indicators

| Indicator              | States                         | Meaning                                                               |
|------------------------|--------------------------------|-----------------------------------------------------------------------|
| Centre-frequency ball  | Resting on curve peak          | Marks the currently-tuned sibilance centre frequency on the response curve. |
| Gain-reduction strip   | Empty or soft-red fill         | Current attenuation applied to the sibilance band.                    |

## Tips

- The meter runs at approximately 30 Hz, so short, sharp transients may appear as brief flashes. This is normal.
- Keep the **Amount** knob at its default of −6.0 dB while watching the meter for the first time. Dial it down only after you have confirmed the meter is triggering on the right sounds.
- If the ball on the sidechain response curve sits far from where your sibilance peaks, use **Freq** to move it. The meter will only show GR when energy in the current **Freq** band crosses **Thresh**.
- When the De-Ess stage is bypassed in the CHAIN widget, the entire applet tile dims visibly. If the tile appears faded, confirm the stage is not bypassed before interpreting the meter.
- To access the RX de-esser instance (titled "Aetherial De-Esser — RX"), open it from the Aetherial Audio Channel Strip rather than the docked applet panel.
- The frequency axis labels in the sidechain response curve use "100", "500", "1k", etc. for clarity and are rendered at 8-pixel font size. The curve widget caches these labels for improved rendering performance.

## Troubleshooting

- **Gain-reduction bar never moves** — The de-esser is not triggering. Check that the De-Ess stage is enabled in the CHAIN widget, that audio is flowing through the TX DSP, and that **Thresh** is not set too high (too close to 0.0 dB) for your microphone level.
- **Gain-reduction bar is pegged to the right on every syllable, including non-sibilant speech** — **Thresh** is set too low. Raise it toward 0.0 dB until ordinary vowels no longer trigger the meter.
- **Bar moves but you hear no effect on air** — **Amount** may be set too close to 0.0 dB. Lower it toward −24.0 dB for more audible reduction, or confirm the stage is not bypassed in the CHAIN widget.
- **Applet tile appears dimmed** — The De-Ess stage is bypassed. Single-click the DESS stage in the CHAIN widget to re-enable it. The tile will return to full opacity when the stage is active.

## Related

- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)