# Dial Poo Drive for LF thickness

The Poo / Drive knob controls how hard the low-frequency saturator or bass compressor is driven. Increasing it adds thickness and weight to the low end of your transmitted audio.

## Before you start

- The PUDU stage must be enabled in the PooDoo Audio chain. The PUDU applet is hidden until the stage is active.
- Open the PUDU applet by navigating to the "PUDU" sub-container inside the PooDoo Audio (TXDSP) parent container, or by double-clicking the PUDU (Enh) stage in the CHAIN widget to open the floating PUDU editor.

## Steps

1. Locate the "Poo" group in the PUDU applet. The three knobs beneath the "Poo" bracket label are Drive, Tune, and Mix.
2. Turn the first knob, labeled "Drive", clockwise to increase drive or counter-clockwise to reduce it.
3. Read the current value from the knob's center display, shown as `X.X dB`.
4. Release the knob. The setting is saved immediately to `ClientPuduTxPooDriveDb`.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Poo / Drive | 6.0 dB | 0.0 to 24.0 dB | `ClientPuduTxPooDriveDb` | Drives the low-frequency saturator (Even mode) or bass compressor (Odd mode) harder. Linear mapping. |
| Poo / Tune | 100 Hz | 50 to 160 Hz | `ClientPuduTxPooTuneHz` | Centers the low-frequency focus band. |
| Poo / Mix | 30 % | 0 to 100 % | `ClientPuduTxPooMix` | Blends the enhanced low band back with the dry signal. |

## Tips

- The character of the Drive knob depends on the selected mode. In "Even" mode it drives an Aphex-lineage asymmetric saturator with Big Bottom LF saturation. In "Odd" mode it drives a Behringer-lineage feed-forward bass compressor. Set the mode before dialing in Drive.
- The PooDoo logo pulses with the wet-signal RMS. Watch it as you increase Drive — a faster, brighter pulse indicates more low-end energy being added.
- Use Poo / Mix to control how much of the driven signal reaches the output. A high Drive with a low Mix can add subtle warmth without overwhelming the source.

## Related

- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Tune Poo to the fundamental of your voice](tune-poo-to-the-fundamental-of-your-voice.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [PUDU Exciter overview](overview.md)
