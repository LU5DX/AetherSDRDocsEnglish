# Blend the Doo excitement with Mix

Use the Doo / Mix knob to control how much of the Doo high-frequency excitement is blended back into your transmit signal. A lower value keeps the effect subtle; a higher value makes the presence and air enhancement more prominent.

## Before you start

- The PUDU Exciter applet must be visible. It is hidden until the PUDU stage is enabled via the CHAIN widget or the floating PUDU editor.
- Audio engine must be running and connected to the transmit chain for changes to take effect in real time.

## Steps

1. Locate the PUDU Exciter applet in the PooDoo Audio (TXDSP) parent container.
2. Find the **Doo** group — the three knobs under the right-hand bracket label.
3. Turn the third knob in that group, labeled **Mix**, to set the wet/dry blend for the Doo stage.
4. Watch the value display under the knob. It reads as a percentage (for example, `30 %`).
5. Release the knob. The setting is saved automatically.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Doo / Mix | 30 % | 0 % to 100 % (stored as 0.0 to 1.0) | `ClientPuduTxDooMix` | Linearly blends the excited high-frequency signal with the dry signal. 0 % passes no Doo effect; 100 % passes only the processed signal. |

## Tips

- Start with the default 30 % and increase gradually while transmitting into a dummy load or monitoring your TX audio. The PooDoo logo pulses with the wet-signal RMS, giving a visual indication of how much processed signal is present.
- Doo / Mix works alongside Doo / Air (`ClientPuduTxDooHarmonicsDb`). If Air is set low, raising Mix will have little audible effect. Dial in Air first, then use Mix to taste.
- Very high Mix values can make the effect harsh on SSB. Values between 20 % and 50 % are typical for voice use.

## Related

- [Add air with Doo Harmonics](add-air-with-doo-harmonics.md)
- [Centre Doo on the presence band for your mic](centre-doo-on-the-presence-band-for-your-mic.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [PUDU Exciter overview](overview.md)
