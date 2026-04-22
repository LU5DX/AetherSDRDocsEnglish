# Blend the Doo excitement with Mix

Use the Doo / Mix knob to control how much of the high-frequency excited signal is blended back into your dry audio. A lower value adds subtle presence; a higher value pushes the Doo effect further forward.

## Before you start

- The PUDU stage must be enabled in the PooDoo Audio chain. If the PUDU applet is not visible, see [Bypass PUDU from the chain](bypass-pudu-from-the-chain.md).
- Open the PUDU Exciter applet. It appears in the PUDU sub-container inside the PooDoo Audio (TXDSP) parent container. You can also double-click the PUDU (Enh) stage in the CHAIN widget to open the floating PUDU editor.

## Steps

1. Locate the **Doo** group — the three knobs on the right side of the PUDU applet, under the bracket label **Doo**.
2. Find the third knob in the Doo group, labelled **Mix**.
3. Turn **Mix** to set the wet/dry blend. The knob displays the current value as a percentage (for example, `30 %`).
4. Release the knob. The setting is saved automatically.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| **Doo / Mix** | 30 % | 0 % to 100 % (stored as 0.0 to 1.0) | `ClientPuduTxDooMix` |

## Tips

- Start at the default of `30 %` and increase gradually while transmitting. The PooDoo logo pulses brighter as the processed (wet) signal level rises, giving a visual indication of how much effect is present.
- Doo / Mix works alongside **Doo / Air** and **Doo / Tune**. Dial in the right frequency and harmonic amount first, then use Mix to set the final blend. See [Add air with Doo Harmonics](add-air-with-doo-harmonics.md) and [Centre Doo on the presence band for your mic](centre-doo-on-the-presence-band-for-your-mic.md).
- Setting Mix to `0 %` effectively bypasses the Doo section without changing any other parameters.

## Related

- [Add air with Doo Harmonics](add-air-with-doo-harmonics.md)
- [Centre Doo on the presence band for your mic](centre-doo-on-the-presence-band-for-your-mic.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [PUDU Exciter overview](overview.md)
