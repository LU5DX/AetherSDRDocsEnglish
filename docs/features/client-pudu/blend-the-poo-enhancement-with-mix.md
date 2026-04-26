# Blend the Poo enhancement with Mix

The **Poo / Mix** knob controls how much of the processed low-frequency signal is blended back with your dry audio. Use it to dial in just enough Poo enhancement without overwhelming your transmit signal.

## Before you start

- The PUDU stage must be enabled in the PooDoo Audio chain. If the PUDU applet is not visible, enable the PUDU (Enh) stage via the CHAIN widget or double-click it to open the floating editor.
- Audio engine must be running with a transmit audio source active so you can hear the effect of the blend.

## Steps

1. Open the PUDU sub-container inside the PooDoo Audio (TXDSP) parent container in the applet panel.
2. Locate the **Poo** group — the three knobs under the bracket labelled **Poo**.
3. Turn the third knob in the Poo group, labelled **Mix**, to set the wet/dry blend for the low-frequency processor.
   - Turning left toward 0 % passes only the dry signal.
   - Turning right toward 100 % passes only the processed low-band signal.
4. Release the knob. The value is saved automatically to `ClientPuduTxPooMix`.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| Poo / Mix | 30 % | 0 % to 100 % (internal 0.0 to 1.0) | `ClientPuduTxPooMix` |

The knob uses a linear mapping. The displayed label shows the blend as a whole-number percentage (for example, **30 %**).

## Tips

- Start at the default of 30 % and increase slowly. At high values the low-band saturation can add significant weight; small increases have an audible effect.
- The PooDoo logo pulses brighter as the wet (processed) RMS increases — use it as a visual guide when you cannot monitor audio directly.
- Set Poo / Drive and Poo / Tune to appropriate values before committing to a Mix level. The character of what you are blending in depends on those two knobs.

## Troubleshooting

- **Turning Poo / Mix has no audible effect** — confirm the PUDU stage is enabled in the CHAIN widget and not bypassed. If the stage is bypassed, all three Poo knobs have no effect on the output.
- **Mix snaps back after adjustment** — the audio engine may not be connected. Check that AetherSDR is connected to the FLEX-8600 and the TX audio path is active.

## Related

- [PUDU Exciter overview](overview.md)
- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Tune Poo to the fundamental of your voice](tune-poo-to-the-fundamental-of-your-voice.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Bypass PUDU from the chain](bypass-pudu-from-the-chain.md)
