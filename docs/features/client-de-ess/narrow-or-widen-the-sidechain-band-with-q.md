# Narrow or widen the sidechain band with Q

The Q knob controls how wide or narrow the sidechain bandpass filter is around the sibilance centre frequency. A higher Q focuses attenuation on a tighter slice of the spectrum; a lower Q affects a broader band. Adjust Q after locating the sibilance peak with Freq so the de-esser targets exactly the right content without dulling nearby consonants.

## Before you start

- The Aetherial De-Esser (DESS) stage must be enabled and visible. It appears as a sub-container inside the Aetherial Audio (TXDSP) parent container.
- If the applet is not visible, double-click the DESS stage in the CHAIN widget to open the frameless editor titled "Aetherial De-Esser — TX", which exposes the same Q knob.
- Set the centre frequency with Freq before fine-tuning Q. See [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md).

## Steps

1. Open the Aetherial De-Esser applet or the "Aetherial De-Esser — TX" editor.
2. Locate the **Q** knob in the four-knob tuning row.
3. Rotate **Q** clockwise to increase the value and narrow the sidechain band, or counter-clockwise to decrease the value and widen it.
4. Watch the sidechain response curve — the bandpass peak broadens or sharpens as Q changes.
5. While transmitting or speaking a sibilant phrase, observe the gain-reduction bar to confirm the de-esser is still triggering at the adjusted bandwidth. See [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md).

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Q** | 2.00 | 0.5 to 5.0 | `ClientDeEssTxQ` | Linear mapping. Higher values narrow the sidechain bandpass; lower values widen it. |
| Sidechain response curve | — | — | — | Displays the bandpass filter shape. Updates live as Q changes. The ball marks the current centre frequency. |
| Gain-reduction bar | — | 0 to 24 dB GR | — | Shows current attenuation applied to the sibilance band, refreshed approximately 30 times per second. |

## Tips

- Start at the default of 2.00 and increase Q only if attenuation is spilling onto vowels or other consonants adjacent to the sibilance band.
- Very high Q values (above 4.0) can make the de-esser miss slightly off-centre sibilants. If GR stops triggering reliably, lower Q slightly or re-sweep Freq.
- The response curve gives immediate visual feedback — use it to judge whether the bell is too broad or too sharp before committing to a setting.

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)
