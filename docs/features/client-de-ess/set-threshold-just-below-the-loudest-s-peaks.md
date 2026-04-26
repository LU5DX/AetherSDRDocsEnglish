# Set threshold just below the loudest 'S' peaks

This page explains how to set the Thresh knob so the de-esser acts only on genuine sibilance and leaves quieter speech untouched. A well-placed threshold is the difference between transparent de-essing and audible pumping.

## Before you start

- The Aetherial De-Esser must be enabled via the CHAIN widget. See [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md).
- The Aetherial De-Esser applet must be visible in the applet panel (sub-container "Aetherial De-Esser" inside the Aetherial Audio (TXDSP) parent container).
- You need a way to transmit or monitor your own TX audio so that genuine speech reaches the de-esser's sidechain.

## Steps

1. Open the de-esser controls: double-click the DESS stage in the CHAIN widget to open the floating "Aetherial De-Esser — TX" editor, or work directly on the Thresh knob in the docked applet.
2. Start speaking into your microphone, repeating a sibilant phrase — something with repeated 'S' and 'T' sounds works well.
3. Watch the Gain-reduction bar. If it shows a soft-red fill during normal vowels and consonants (not just on 'S' peaks), the threshold is too low. If it never moves during loud 'S' sounds, the threshold is too high.
4. Turn the Thresh knob clockwise to raise the threshold (toward 0.0 dB) until the Gain-reduction bar stays empty during normal speech.
5. Then turn Thresh slowly counter-clockwise (toward −60.0 dB) until the Gain-reduction bar just starts to fill on your loudest 'S' peaks and no more.
6. Verify: speak normally through a full sentence. The Gain-reduction bar should be empty most of the time and fill briefly only on hard sibilants.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| Thresh | −30.0 dB | −60.0 to 0.0 dB | `ClientDeEssTxThresholdDb` |
| Gain-reduction bar | — | 0 to 24 dB GR | — |

**Thresh** — the level above which the de-esser begins attenuating the sibilance band. Raising this value (toward 0.0 dB) makes the de-esser act only on the very loudest sibilance. Lowering it (toward −60.0 dB) causes the de-esser to trigger on progressively quieter signals.

**Gain-reduction bar** — a horizontal soft-red strip that fills from the right to show current attenuation. The scale runs from 0 to 24 dB. A tick marks the −6 dB position, which is the default Amount value. The bar refreshes approximately 30 times per second.

## Tips

- The threshold interacts with Amount (`ClientDeEssTxAmountDb`). Set the threshold first, then dial Amount to taste. See [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md).
- If you are unsure where your sibilance peaks are in frequency, locate them first before finalising the threshold. See [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md).
- Watching the Gain-reduction bar in real time while speaking is the most reliable way to judge threshold placement. See [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md).

## Troubleshooting

- **Gain-reduction bar fills continuously, even on vowels** — Thresh is set too low. Raise it (clockwise) until the bar is empty during non-sibilant speech.
- **Gain-reduction bar never moves, even on hard 'S' sounds** — Thresh is set too high, or the sibilance band (Freq, Q) is not centred on the problem frequencies. Raise the band level by lowering Thresh, or revisit Freq. See [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md).
- **De-esser appears to do nothing at all** — confirm the DESS stage is enabled in the CHAIN widget. See [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md).

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)
