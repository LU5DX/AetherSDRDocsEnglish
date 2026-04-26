# PUDU Exciter overview

The PUDU Exciter is the centrepiece of the PooDoo Audio TX chain. It adds harmonic enhancement and tonal shaping to your transmitted audio in two frequency regions: low-end body ("Poo") and high-frequency presence and air ("Doo").

## Before you start

- The PUDU stage must be enabled in the CHAIN widget before the PUDU applet becomes visible. The sub-container remains hidden until the stage is active.
- The PooDoo Audio (TXDSP) parent container must be open in the applet panel.

## How it works

PUDU processes audio in two independent bands, each controlled by a group of three knobs.

**Mode selection** — The Even and Odd radio buttons at the top of the applet select the character of the harmonic shaping applied across both bands. Even mode uses Aphex-lineage asymmetric saturation, producing predominantly even harmonics with a warmer character and Big Bottom low-frequency saturation. Odd mode uses Behringer-lineage symmetric tanh shaping, producing pure odd harmonics with a brighter character and a feed-forward bass compressor. The two buttons are mutually exclusive; the active selection is shown in amber.

**Poo group** — The three knobs under the "Poo" bracket act on the low-frequency band. Drive pushes the saturator or compressor harder. Tune centres the frequency band on your target fundamental. Mix blends the processed low band back with the dry signal.

**Doo group** — The three knobs under the "Doo" bracket act on the high-frequency band. Tune centres the excitement band in the presence or air region. Air controls the amount of harmonics added at that band. Mix blends the excited highs back with the dry signal.

The animated PooDoo logo pulses in brightness with the processed (wet) signal RMS, giving a continuous visual indication that the stage is active and passing audio.

To open the floating editor, double-click the PUDU (Enh) stage in the CHAIN widget. To float, pop out, or hide the sub-container, right-click the PUDU sub-container titlebar.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| Even | — | — | `ClientPuduTxMode` |
| Odd | — | — | `ClientPuduTxMode` |
| Poo / Drive | 6.0 dB | 0.0 – 24.0 dB | `ClientPuduTxPooDriveDb` |
| Poo / Tune | 100 Hz | 50 – 160 Hz | `ClientPuduTxPooTuneHz` |
| Poo / Mix | 30 % | 0 – 100 % | `ClientPuduTxPooMix` |
| Doo / Tune | 5000 Hz | 1000 – 10000 Hz | `ClientPuduTxDooTuneHz` |
| Doo / Air | 6.0 dB | 0.0 – 24.0 dB | `ClientPuduTxDooHarmonicsDb` |
| Doo / Mix | 30 % | 0 – 100 % | `ClientPuduTxDooMix` |

The `ClientPuduTxEnabled` setting persists whether the PUDU stage is active in the chain.

## Tips

- Poo / Tune responds to a linear frequency mapping, so small adjustments near 50 Hz and near 160 Hz move the band by the same absolute amount. Set Tune close to the fundamental of your voice before increasing Drive or Mix.
- Doo / Tune uses a logarithmic mapping, so the knob covers more octaves toward the top of its travel. A setting of 5.0 kHz is the label displayed at the default position; values below 1000 Hz display in Hz.
- Keep Poo / Mix and Doo / Mix conservative — both default to 30 %. Large mix values at high Drive settings can increase average power significantly.

## Related

- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Tune Poo to the fundamental of your voice](tune-poo-to-the-fundamental-of-your-voice.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [Centre Doo on the presence band for your mic](centre-doo-on-the-presence-band-for-your-mic.md)
- [Add air with Doo Harmonics](add-air-with-doo-harmonics.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Bypass PUDU from the chain](bypass-pudu-from-the-chain.md)
