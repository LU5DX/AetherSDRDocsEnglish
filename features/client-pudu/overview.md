# PUDU Exciter overview

The PUDU Exciter is the centrepiece of the PooDoo Audio transmit DSP chain. It adds low-frequency body ("Poo") and high-frequency presence or air ("Doo") to your transmitted audio using two independent parallel processors, each with its own character, tuning, and wet/dry blend.

## Before you start

- The PUDU stage must be enabled in the CHAIN widget before the applet becomes visible. The sub-container remains hidden until the stage is active.
- No radio connection is required to adjust PUDU settings.

## How it works

PUDU processes transmit audio in two parallel bands.

**Mode** selects the overall character of both processors. Click **Even** for Aphex-lineage asymmetric shaping — predominantly even harmonics, warmer, with Big Bottom low-frequency saturation. Click **Odd** for Behringer-lineage symmetric tanh shaping — pure odd harmonics, brighter, with a feed-forward bass compressor. The two buttons are mutually exclusive; the selected mode is saved to `ClientPuduTxMode`.

**Poo group** — the three knobs under the "Poo" bracket label shape the low-frequency band:

- **Drive** sets how hard the low-frequency saturator or compressor is driven. Higher values add more low-end thickness and density.
- **Tune** centres the low-frequency focus band on a specific frequency.
- **Mix** blends the processed low band back with the dry signal. At 0 % the Poo processor is fully bypassed; at 100 % it is fully wet.

**Doo group** — the three knobs under the "Doo" bracket label add presence and air in the high-frequency band:

- **Tune** centres the high-frequency excitement band on a specific frequency. The mapping is logarithmic, so the knob travels more slowly at higher frequencies.
- **Air** sets the amount of harmonics added at the Doo band.
- **Mix** blends the excited highs back with the dry signal.

The **PooDoo logo** at the top of the applet pulses in brightness with the processed (wet) signal RMS, giving a visual indication that the exciter is active and receiving audio.

Bypass and enable are handled by the CHAIN widget, not by controls inside the applet. To open the floating PUDU editor, double-click the PUDU (Enh) stage in the CHAIN widget.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| Even / Odd | — | Either/or | `ClientPuduTxMode` |
| Poo / Drive | 6.0 dB | 0.0 – 24.0 dB | `ClientPuduTxPooDriveDb` |
| Poo / Tune | 100 Hz | 50 – 160 Hz | `ClientPuduTxPooTuneHz` |
| Poo / Mix | 30 % | 0 – 100 % | `ClientPuduTxPooMix` |
| Doo / Tune | 5000 Hz | 1000 – 10000 Hz | `ClientPuduTxDooTuneHz` |
| Doo / Air | 6.0 dB | 0.0 – 24.0 dB | `ClientPuduTxDooHarmonicsDb` |
| Doo / Mix | 30 % | 0 – 100 % | `ClientPuduTxDooMix` |

Enable/disable state is persisted separately as `ClientPuduTxEnabled` and controlled from the CHAIN widget.

## Tips

- The PooDoo logo pulse is a quick check that audio is flowing through the wet path. If the logo is not pulsing during transmit, verify the PUDU stage is enabled in the CHAIN widget.
- Poo / Tune responds linearly, so dial it close to the fundamental frequency of your voice for the most focused low-end enhancement.
- Doo / Tune uses a logarithmic scale. A small physical movement near the top of the range covers a wide frequency span; use slow, deliberate turns when targeting a specific presence peak.
- Keep Poo / Mix and Doo / Mix at moderate values (20–40 %) as a starting point. Parallel processing at high mix levels can cause the signal to sound over-processed on the receiving end.

## Related

- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Tune Poo to the fundamental of your voice](tune-poo-to-the-fundamental-of-your-voice.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [Centre Doo on the presence band for your mic](centre-doo-on-the-presence-band-for-your-mic.md)
- [Add air with Doo Harmonics](add-air-with-doo-harmonics.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Bypass PUDU from the chain](bypass-pudu-from-the-chain.md)
