# Blend the Poo enhancement with Mix

The **Poo / Mix** knob controls how much of the processed low-frequency signal blends back into your dry audio. Use it to dial in just enough low-end enhancement without overwhelming the signal.

## Before you start

- The PUDU stage must be enabled in the PooDoo Audio chain. See [Bypass PUDU from the chain](bypass-pudu-from-the-chain.md) if the PUDU sub-container is not visible.
- The PUDU sub-container must be visible in the applet panel. If it is hidden, double-click the PUDU (Enh) stage in the CHAIN widget, or right-click the PUDU sub-container titlebar and select the show option.

## Steps

1. Locate the **Poo** group in the PUDU sub-container. It is the left group of three knobs, identified by the **Poo** bracket label above them.
2. Find the third knob in that group, labelled **Mix**.
3. Turn the **Mix** knob to the right to increase the proportion of processed low-frequency signal in the output, or to the left to reduce it.
4. Watch the PooDoo logo pulse brightness to confirm the wet signal level. A higher **Mix** value produces a more pronounced pulse.

## What each control does

| Control | Default | Range | Persisted key |
|---|---|---|---|
| **Poo / Mix** | 30 % | 0 % to 100 % | `ClientPuduTxPooMix` |

The knob uses a linear mapping. At 0 % the Poo processor has no effect on the output. At 100 % the full processed low-band signal replaces the dry contribution from the Poo stage. Values between 20 % and 40 % suit most voice applications.

## Tips

- Set **Poo / Drive** and **Poo / Tune** before committing to a **Mix** value. Drive and Tune determine what the Poo processor produces; Mix only controls how much of that result reaches the output.
- If the low end sounds heavy or boomy, reduce **Mix** before reducing **Drive**. Mix changes are immediate and make it easy to hear the threshold where the enhancement becomes audible.
- In **Even** mode the Poo stage uses asymmetric LF saturation. In **Odd** mode it uses a feed-forward bass compressor. The appropriate **Mix** level may differ between the two modes.

## Related

- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Tune Poo to the fundamental of your voice](tune-poo-to-the-fundamental-of-your-voice.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Bypass PUDU from the chain](bypass-pudu-from-the-chain.md)
