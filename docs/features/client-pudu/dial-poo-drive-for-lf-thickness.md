# Dial Poo Drive for LF thickness

The **Poo / Drive** knob controls how hard the low-frequency saturator or bass compressor is driven. Increasing it adds thickness and weight to the low end of your transmitted audio.

## Before you start

- The PUDU stage must be enabled in the PooDoo Audio (TXDSP) chain. The PUDU applet is hidden until that stage is active.
- Open the PUDU applet by navigating to the **PUDU** sub-container inside the PooDoo Audio (TXDSP) parent container, or by double-clicking the PUDU (Enh) stage in the CHAIN widget to open the floating PUDU editor.

## Steps

1. Locate the **Poo** group in the PUDU applet. The three knobs under the **Poo** bracket label are **Drive**, **Tune**, and **Mix**.
2. Turn the **Drive** knob to the desired value. The knob displays its current value as `X.X dB`.
3. Release the knob. The setting is saved automatically to `ClientPuduTxPooDriveDb`.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Drive** | 6.0 dB | 0.0 to 24.0 dB | `ClientPuduTxPooDriveDb` | Drives the low-frequency saturator (Even mode) or bass compressor (Odd mode) harder. Higher values add more low-end thickness. |

## Tips

- In **Even** mode, Drive feeds the Aphex-lineage Big Bottom LF saturator. In **Odd** mode, it feeds the Behringer-lineage feed-forward bass compressor. The character of the effect at high Drive settings differs between the two modes.
- Use the **Poo / Mix** knob to control how much of the driven low-end signal is blended back with the dry signal. A high Drive with a low Mix can add subtle warmth without overwhelming the original tone.
- The PooDoo logo pulses with the processed signal RMS, giving a visual indication that the Poo stage is working.

## Related

- [PUDU Exciter overview](overview.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Tune Poo to the fundamental of your voice](tune-poo-to-the-fundamental-of-your-voice.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [Bypass PUDU from the chain](bypass-pudu-from-the-chain.md)
