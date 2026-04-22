# Centre Doo on the presence band for your mic

The **Doo / Tune** knob sets the centre frequency of the high-frequency excitement band. Moving it to match your microphone's presence peak lets the Doo processor add harmonics and air at exactly the right part of the spectrum.

## Before you start

- The PUDU stage must be enabled in the CHAIN widget. The PUDU applet is hidden until the stage is active.
- Open the PUDU applet inside the PooDoo Audio (TXDSP) parent container, or double-click the PUDU (Enh) stage in the CHAIN widget to open the floating editor.

## Steps

1. Locate the **Doo** group — the right-hand set of three knobs under the "Doo" bracket label.
2. Find the **Tune** knob (the first knob under the Doo bracket).
3. Turn **Doo / Tune** until the value shown under the knob matches the presence or air frequency of your microphone. The knob displays values as `X.X kHz` at 1000 Hz and above, and `X Hz` below 1000 Hz.
4. Transmit into a dummy load or use monitor audio to check the result. Adjust until the desired presence range is engaged.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| Doo / Tune | 5000 Hz (5.0 kHz) | 1000 to 10000 Hz | `ClientPuduTxDooTuneHz` |

The knob uses a logarithmic mapping: equal physical travel covers proportionally equal frequency ratios across the range.

## Tips

- Most dynamic microphones have a presence peak between 3 kHz and 6 kHz; most condenser microphones between 5 kHz and 10 kHz. Start near the known peak of your microphone and sweep slowly while monitoring.
- The PooDoo logo pulses brighter as the processed (wet) signal level rises. This gives a rough visual indication that the Doo processor is working, but use your ears for the final setting.
- After setting Doo / Tune, adjust **Doo / Air** to control how much harmonic content is added at that frequency, then use **Doo / Mix** to blend the effect back with the dry signal.

## Related

- [Add air with Doo Harmonics](add-air-with-doo-harmonics.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Tune Poo to the fundamental of your voice](tune-poo-to-the-fundamental-of-your-voice.md)
- [PUDU Exciter overview](overview.md)
