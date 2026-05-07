# Aetherial TX Voice Processor / Aetherial RX Poodoo™ overview

The Aetherial Poodoo applet is the harmonic-enhancement stage at the centre of the Aetherial Audio chain. It runs as two fully independent instances — one on the TX path ("Aetherial TX Voice Processor") and one on the RX path ("Aetherial RX Poodoo™") — letting you shape low-end weight and high-frequency air separately for transmit and receive audio.

## Before you start

- The PUDU stage must be enabled in the CHAIN widget on the matching TX or RX side before the applet is visible.
- The Aetherial Audio (TXDSP) parent container must be open in the applet panel.

## How it works

Each Poodoo instance processes audio in two parallel bands, referred to as **Poo** (low-frequency) and **Doo** (high-frequency). The character of the processing is set by the mode you choose:

- **Even** mode uses Aphex-lineage asymmetric shaping — predominantly even harmonics, warmer in character, with Big Bottom low-frequency saturation.
- **Odd** mode uses Behringer-lineage symmetric tanh shaping — pure odd harmonics, brighter in character, with a feed-forward bass compressor.

Both bands produce a wet signal that is blended back with the dry signal using their respective Mix knobs. The animated PooDoo logo pulses with the brightness of the processed (wet) signal RMS, giving a visual indication of how much enhancement is active.

The TX and RX instances are opened by double-clicking the PUDU stage in the CHAIN widget on the corresponding side. The floating editor is titled "Aetherial Voice Processor — TX" or "Aetherial Voice Processor — RX". You can also right-click the "Aetherial TX Poodoo" or "Aetherial RX Poodoo" sub-container titlebar to float, pop out, or hide it. Bypass is handled from the CHAIN widget directly; there is no separate Enable button inside the applet. When the stage is bypassed, the entire applet tile dims to reduced opacity to indicate that DSP is inactive.

All settings are persisted independently for the TX and RX sides.

## What each control does

### Mode

| Control | Behavior | Persisted setting |
|---|---|---|
| Even | Selects Aphex-lineage asymmetric shaping. Lit amber PooDoo-colour when active. Exclusive with Odd. | `ClientPuduTxMode` / `ClientPuduRxMode` |
| Odd | Selects Behringer-lineage symmetric tanh shaping. Exclusive with Even. | `ClientPuduTxMode` / `ClientPuduRxMode` |

### Poo group (low-frequency processor)

| Control | Default | Range | Behavior | TX setting key | RX setting key |
|---|---|---|---|---|---|
| Poo / Drive | 6.0 dB | 0.0 – 24.0 dB | Drives the low-frequency saturator or compressor harder. Linear mapping. Displays as "X.X dB". | `ClientPuduTxPooDriveDb` | `ClientPuduRxPooDriveDb` |
| Poo / Tune | 100 Hz | 50 – 160 Hz | Centres the low-frequency focus band. Linear mapping. Displays as "X Hz". | `ClientPuduTxPooTuneHz` | `ClientPuduRxPooTuneHz` |
| Poo / Mix | 30 % | 0 – 100 % | Blends the enhanced low band back with the dry signal. Linear mapping. Displayed as percentage. | `ClientPuduTxPooMix` | `ClientPuduRxPooMix` |

### Doo group (high-frequency processor)

| Control | Default | Range | Behavior | TX setting key | RX setting key |
|---|---|---|---|---|---|
| Doo / Tune | 5000 Hz | 1000 – 10000 Hz | Centres the high-frequency excitement band. Logarithmic mapping (1000 * 10^n). Displays as "5.0 kHz" above 1 kHz, "X Hz" below. | `ClientPuduTxDooTuneHz` | `ClientPuduRxDooTuneHz` |
| Doo / Air | 6.0 dB | 0.0 – 24.0 dB | Amount of harmonics and air added at the high band. Linear mapping. Displays as "X.X dB". | `ClientPuduTxDooHarmonicsDb` | `ClientPuduRxDooHarmonicsDb` |
| Doo / Mix | 30 % | 0 – 100 % | Blends the excited highs back with the dry signal. Linear mapping. Displayed as percentage. | `ClientPuduTxDooMix` | `ClientPuduRxDooMix` |

### Indicators

| Indicator | Behavior |
|---|---|
| PooDoo logo pulse | Animated branded logo. Brightness pulses with the processed (wet) signal RMS. Minimum 40 px height. |
| Poo group bracket | Group label — the three knobs below belong to the low-frequency processor. |
| Doo group bracket | Group label — the three knobs below belong to the high-frequency processor. |

## Tips

- Keep Mix values moderate — both Poo / Mix and Doo / Mix default to 30 %, which blends the effect in without overwhelming the dry signal.
- Poo / Tune uses a linear mapping across 50 – 160 Hz. For a typical male voice TX, tune toward the lower end of that range; for RX program material, tune to taste by ear.
- Doo / Tune uses a logarithmic mapping, so the knob gives finer resolution at lower frequencies within the 1 – 10 kHz range.
- The TX and RX instances are fully independent. You can run Even on TX and Odd on RX, or different Drive and Air amounts on each side.
- When the PUDU stage is bypassed from the CHAIN widget, the applet tile dims visually. This matches the dim behaviour on the EQ curve and confirms at a glance that no DSP is being applied.

## Related

- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Tune Poo to the fundamental of your voice (TX) or to bring out RX program lows](tune-poo-to-the-fundamental-of-your-voice-tx-or-to-bring-out-rx-program-lows.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [Centre Doo on the presence band for your mic (TX) or for RX intelligibility](centre-doo-on-the-presence-band-for-your-mic-tx-or-for-rx-intelligibility.md)
- [Add air with Doo Harmonics](add-air-with-doo-harmonics.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md)