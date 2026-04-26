# Add air with Doo Harmonics

Use the **Doo / Air** knob to control how much harmonic excitement the Doo processor adds at the high-frequency band. Increasing this adds presence and "air" to your transmitted audio.

## Before you start

- The PUDU stage must be enabled and visible. It is hidden until enabled via the CHAIN widget or the floating editor. See [Bypass PUDU from the chain](bypass-pudu-from-the-chain.md).
- AetherSDR must be connected to your FLEX-8600 radio with audio routing active.

## Steps

1. Open the PUDU Exciter applet. It appears as the **PUDU** sub-container inside the PooDoo Audio (TXDSP) parent container.
2. Locate the **Doo** group — the right-hand set of three knobs, marked with the "Doo" bracket label.
3. Turn the **Air** knob (the center knob of the Doo group) clockwise to increase the amount of harmonics added at the Doo frequency band, or counter-clockwise to reduce it.
4. Monitor the PooDoo logo — its brightness pulses with the processed signal RMS, giving a rough indication of how much wet signal is being produced.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Air | 6.0 dB | 0.0 to 24.0 dB | `ClientPuduTxDooHarmonicsDb` | Sets the amount of harmonic content added at the Doo high-frequency band. Linear mapping. |
| Doo / Tune | 5000 Hz | 1000 to 10000 Hz | `ClientPuduTxDooTuneHz` | Centers the frequency band where Air is applied. Logarithmic mapping. |
| Doo / Mix | 30 % | 0 to 100 % | `ClientPuduTxDooMix` | Blends the excited high band back with the dry signal. |

## Tips

- The **Air** knob and the **Doo / Tune** knob work together. Set **Doo / Tune** to the presence or air frequency of your microphone before increasing **Air**, so the harmonics are added where your mic already has output.
- Use **Doo / Mix** to rein in the overall effect without having to reduce **Air**. This keeps harmonic character while controlling the wet/dry balance.
- In **Even** mode, harmonic generation follows Aphex-lineage asymmetric shaping — the added harmonics are warmer. In **Odd** mode, Behringer-lineage symmetric tanh shaping produces brighter harmonics. The **Air** knob behaves the same in both modes, but the character of what it adds differs.

## Related

- [Centre Doo on the presence band for your mic](centre-doo-on-the-presence-band-for-your-mic.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [PUDU Exciter overview](overview.md)
