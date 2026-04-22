# Narrow or widen the sidechain band with Q

The Q knob controls how wide or narrow the sidechain bandpass filter is around the sibilance centre frequency. A higher Q targets a tighter slice of the spectrum; a lower Q catches a broader range. Adjust Q after you have located the sibilance peak with Freq.

## Before you start

- The De-Ess stage must be enabled and the DESS applet must be visible inside the PooDoo Audio (TXDSP) container. See [De-Esser overview](overview.md).
- Identify the centre frequency of your sibilance first. See [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md).

## Steps

1. Open the DESS applet inside the PooDoo Audio (TXDSP) container.
2. Locate the Q knob in the four-knob row below the sidechain response curve.
3. Turn Q clockwise to increase the value and narrow the band, or counter-clockwise to decrease the value and widen the band.
4. Watch the sidechain response curve update in real time. The curve shape shows the resulting bandpass width around the centre-frequency ball.
5. Speak a sibilant phrase and watch the gain-reduction bar. Confirm the de-esser triggers only on the intended sibilance, not on surrounding audio.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Q | 2.00 | 0.5 to 5.0 | `ClientDeEssTxQ` | Linear mapping. Higher values narrow the sidechain bandpass; lower values widen it. |
| Sidechain response curve | — | — | — | Draws the bandpass filter shape with a live ball at the current centre frequency. Updates immediately as Q changes. |
| Gain-reduction bar | — | 0 to 24 dB GR | — | Shows current attenuation applied to the sidechain band, refreshed at approximately 30 Hz. |

## Tips

- Start at the default Q of 2.00 and adjust from there. Most sibilance is resolved in the range 1.5 to 3.5.
- A narrower Q (higher value) is more transparent because it leaves adjacent frequencies untouched, but it requires Freq to be precisely on the sibilance peak.
- A wider Q (lower value) is more forgiving of an imprecise Freq setting but can affect consonants and fricatives beyond the sibilant band.
- The response curve gives immediate visual feedback — use it alongside the gain-reduction bar rather than relying on either alone.

## Troubleshooting

- **Gain-reduction bar shows little or no activity** — Q may be too narrow and the filter is missing the sibilance peak. Lower Q slightly, or re-sweep Freq to confirm the centre frequency is correct.
- **De-esser triggers on normal speech, not just sibilants** — Q is likely too low (band is too wide). Increase Q to tighten the filter around the sibilance frequency.

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [De-Esser overview](overview.md)
