# Add air with Doo Harmonics

The **Doo / Air** knob controls how much high-frequency harmonic content the PUDU exciter adds at the Doo band. Increasing it adds presence and "air" to your transmitted audio without changing the underlying signal level.

## Before you start

- The PUDU stage must be enabled in the PooDoo Audio chain. See [Bypass PUDU from the chain](bypass-pudu-from-the-chain.md) if the PUDU sub-container is not visible.
- Open the PUDU applet: locate the **PUDU** sub-container inside the PooDoo Audio (TXDSP) parent container in the applet panel, or double-click the PUDU (Enh) stage in the CHAIN widget to open the floating editor.

## Steps

1. In the **Doo** group, locate the **Air** knob (the middle knob under the Doo bracket).
2. Turn **Air** clockwise to increase the amount of harmonic excitement added at the high band. The value displays in dB below the knob.
3. Watch the PooDoo logo — its brightness pulses with the processed signal level, giving you visual feedback as you adjust.
4. If the added harmonics are too prominent in the final mix, reduce **Doo / Mix** to blend the excited signal back toward the dry signal. See [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md).

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| **Air** | 6.0 dB | 0.0 to 24.0 dB | `ClientPuduTxDooHarmonicsDb` |
| **Doo / Tune** | 5000 Hz (5.0 kHz) | 1000 to 10000 Hz | `ClientPuduTxDooTuneHz` |
| **Doo / Mix** | 30 % | 0 to 100 % | `ClientPuduTxDooMix` |

**Air** — Sets the level of harmonics generated at the high band in dB. Higher values add more presence and air. Lower values reduce the effect toward bypass.

**Doo / Tune** — Sets the centre frequency of the high-frequency excitement band. The knob uses a logarithmic mapping; values at or above 1 kHz display as kHz (e.g. "5.0 kHz"). Tune this to the presence region of your microphone before raising Air. See [Centre Doo on the presence band for your mic](centre-doo-on-the-presence-band-for-your-mic.md).

**Doo / Mix** — Blends the processed high band back with the dry signal. At 0 % the Doo section is effectively silent regardless of the Air setting. At 100 % the full processed signal is used.

## Tips

- Set **Doo / Tune** first so the excitement is centred on the right frequency band before pushing **Air**. A higher **Air** value at the wrong frequency can add harshness rather than clarity.
- The Even mode (Aphex-lineage) and Odd mode (Behringer-lineage) change the harmonic character of what Air generates. Even produces warmer harmonics; Odd produces a brighter, more aggressive result. See [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md).
- Use **Doo / Mix** to keep the Air effect subtle — small amounts of harmonic excitement are usually more effective on air than large ones.

## Troubleshooting

- **Air knob has no audible effect** — Check that the PUDU stage is enabled in the CHAIN widget and that `ClientPuduTxEnabled` is active. Also confirm **Doo / Mix** is above 0 %; a Mix of 0 % silences the entire Doo section regardless of the Air setting.
- **Added harmonics sound harsh** — The Doo / Tune centre frequency may be too high or Air is set too far above the useful range for your microphone. Lower **Air**, then retune **Doo / Tune** to a lower frequency before raising **Air** again.

## Related

- [Centre Doo on the presence band for your mic](centre-doo-on-the-presence-band-for-your-mic.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [PUDU Exciter overview](overview.md)
