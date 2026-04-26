# Centre Doo on the presence band for your mic

The **Doo / Tune** knob sets the centre frequency of the PUDU exciter's high-frequency processor. Positioning it at your microphone's natural presence peak lets the Doo stage add harmonics and air where they have the most effect on intelligibility and perceived brightness.

## Before you start

- The PUDU stage must be enabled in the PooDoo Audio chain. If it is hidden, enable it via the CHAIN widget or double-click the PUDU (Enh) stage to open the floating editor.
- The PUDU sub-container must be visible inside the PooDoo Audio (TXDSP) parent container.

## Steps

1. Locate the **Doo** group in the PUDU applet. The bracket label reads "Doo" and sits above the three rightmost knobs.
2. Find the first knob under the Doo bracket, labelled **Tune**.
3. Turn **Doo / Tune** to the frequency where your microphone's presence peak sits. The default is 5.0 kHz; the valid range is 1000 to 10000 Hz.
4. Speak into the microphone at your normal operating level and adjust **Doo / Tune** while watching the animated PooDoo logo — its brightness follows the processed signal. Listen for the point where clarity and presence increase without harshness.
5. The setting is saved automatically when you release the knob.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Doo / Tune** | 5.0 kHz | 1000 to 10000 Hz | `ClientPuduTxDooTuneHz` | Sets the centre frequency of the high-frequency excitement band. Uses logarithmic mapping. Displays as "X.X kHz" at or above 1 kHz. |
| **Doo / Air** | 6.0 dB | 0.0 to 24.0 dB | `ClientPuduTxDooHarmonicsDb` | Controls the amount of harmonics added at the tuned frequency. |
| **Doo / Mix** | 30 % | 0.0 to 1.0 | `ClientPuduTxDooMix` | Blends the excited high band back with the dry signal. Displayed as a percentage. |

## Tips

- The **Doo / Tune** knob uses a logarithmic scale, so small movements near the low end of the range (1 kHz) produce larger frequency changes than the same movement near 10 kHz. Take smaller steps when working below 2 kHz.
- Tune **Doo / Tune** before increasing **Doo / Air**. Setting the centre frequency first lets you hear the character of the band before adding harmonics.
- If you are using Even mode, the Doo stage interacts with the Big Bottom LF saturation from the Poo group. Set Doo / Tune high enough (typically 3 kHz or above for voice) to keep the two bands from overlapping.

## Troubleshooting

- **Doo / Tune has no audible effect** — Check that **Doo / Mix** is above 0 % and that **Doo / Air** is above 0.0 dB. With either at minimum, the Doo processor produces no output regardless of the Tune setting.
- **PUDU applet is not visible** — The sub-container is hidden until the PUDU stage is enabled. Enable it from the CHAIN widget or by double-clicking the PUDU (Enh) stage.

## Related

- [PUDU Exciter overview](overview.md)
- [Add air with Doo Harmonics](add-air-with-doo-harmonics.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Tune Poo to the fundamental of your voice](tune-poo-to-the-fundamental-of-your-voice.md)
