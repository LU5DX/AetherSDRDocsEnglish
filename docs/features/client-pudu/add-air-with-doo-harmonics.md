# Aetherial TX Voice Processor / Aetherial RX Poodoo™ Overview

## Purpose

The PUDU exciter is the centrepiece of the Aetherial Audio chain. It applies Aphex-style Aural Exciter + Big Bottom processing (Even mode) or Behringer-style tanh shaping + bass compression (Odd mode) to shape and enhance audio. Two independent instances exist: one for transmit ("Aetherial TX Voice Processor") and one for receive ("Aetherial RX Poodoo™"), each with fully independent state.

## Opening the Applet

- Open the Aetherial TX Voice Processor or Aetherial RX Poodoo™ applet in the Applet Panel.
- Alternatively, double-click the PUDU stage in the CHAIN widget to open a floating editor titled "Aetherial Poodoo™ — TX" or "Aetherial Poodoo™ — RX".

## Control Overview

The applet is divided into two main processing sections:

### Body Group (Low-Frequency Processor)

Controls the low-end shaping and saturation. Three knobs below the "Body" bracket label:

| Control        | Default  | Valid Range   | Setting Key                    | Behavior                                                    |
|----------------|----------|---------------|-------------------------------|-------------------------------------------------------------|
| Poo / Drive    | 6.0 dB   | 0.0 to 24.0 dB| `ClientPuduTxPooDriveDb`      | Linear mapping. Drives the low-frequency saturator/compressor harder. |
| Poo / Tune     | 100 Hz   | 50 to 160 Hz  | `ClientPuduTxPooTuneHz`       | Linear mapping. Centres the low-frequency focus band.           |
| Poo / Mix      | 30 %     | 0.0 to 1.0    | `ClientPuduTxPooMix`          | Linear mapping. Blends the enhanced low band back with the dry signal. |

### Clarity Group (High-Frequency Processor)

Controls the high-frequency harmonic excitement and presence. Three knobs below the "Clarity" bracket label:

| Control        | Default  | Valid Range       | Setting Key                    | Behavior                                                    |
|----------------|----------|-------------------|-------------------------------|-------------------------------------------------------------|
| Doo / Tune     | 5000 Hz  | 1000 to 10000 Hz  | `ClientPuduTxDooTuneHz`       | Logarithmic mapping (1000 * 10^n). Centres the high-frequency excitement band. |
| Doo / Air      | 6.0 dB   | 0.0 to 24.0 dB    | `ClientPuduTxDooHarmonicsDb`  | Linear mapping. Amount of harmonics/'air' added at the high band. |
| Doo / Mix      | 30 %     | 0.0 to 1.0        | `ClientPuduTxDooMix`          | Linear mapping. Blends the excited highs back with the dry signal. |

### Mode Selection

| Control | Setting Key            | Behavior                                                    |
|---------|------------------------|-------------------------------------------------------------|
| Even    | `ClientPuduTxMode`     | Selects Aphex-lineage asymmetric shaping — predominantly even harmonics, warmer, with Big Bottom LF saturation. Amber PooDoo-colour when checked. Exclusive with Odd. |
| Odd     | `ClientPuduTxMode`     | Selects Behringer-lineage symmetric tanh shaping — pure odd harmonics, brighter, with a feed-forward bass compressor. Exclusive with Even. |

### Indicator

The **AetherVoice logo** is an animated branded logo that pulses with the wet-signal RMS. It displays the "AetherVoice™" wordmark and has a minimum height of 40 pixels.

## Theme Support (v26.6.1)

As of version 26.6.1, the PUDU applet and its floating editor fully support theme colours:

- Knob components (background ring, value arc, pointer handle, label text, value text) read colours from the theme system via `color.knob.*` and `color.text.*` namespaces.
- The `applet/pudu` container override allows per-applet colour overrides, such as the amber PooDoo-colour foreground used when the Even mode radio button is active.
- Bracket labels in both the applet and editor use `{{color.text.primary}}` from the theme for consistent appearance.

## Inline Value Editing

Starting with version 26.5.2, you can type an exact value directly on any knob instead of dragging:

1. Click the value text below any knob to reveal an inline editor.
2. Type a number and press Enter or click elsewhere to commit.
3. The value is automatically clamped to the valid range.
4. Press Escape to cancel the edit and revert to the previous value.

## Automatic Settings Persistence

All control values are saved automatically per side (TX/RX) and persist between sessions. Settings keys follow the pattern `ClientPudu{Type}{Side}{Parameter}` where type is Tx or Rx.

## Add Air with Doo Harmonics

Use the **Doo / Air** knob to add harmonic excitement and presence to the high-frequency band. This raises perceived "air" on TX to make your signal cut through, or on RX to improve intelligibility of incoming audio.

### Steps

1. Locate the **Clarity** group bracket — the three knobs on the right side of the applet, under the "Clarity" bracket label.
2. Turn the **Air** knob to set the amount of harmonic content added at the high-frequency band. The value is shown in dB below the knob.
3. Watch the AetherVoice logo pulse increase as the wet-signal level rises. Use this as a rough indicator of how much processing is being applied.
4. If the result is too aggressive, reduce **Air** or lower **Doo / Mix** to blend the effect back with the dry signal.

Settings are saved automatically. The value persists in `ClientPuduTxDooHarmonicsDb` (TX) or `ClientPuduRxDooHarmonicsDb` (RX).

### Tips

- Start with **Air** at 6.0 dB (default) and **Doo / Mix** at 30 % (default), then increase **Air** gradually while listening to the effect on program material.
- The **Doo / Tune** knob centres the band where harmonics are added. Set it to match your mic's presence peak on TX, or to the intelligibility range of incoming audio on RX. See [Centre Doo on the presence band for your mic (TX) or for RX intelligibility](centre-doo-on-the-presence-band-for-your-mic-tx-or-for-rx-intelligibility.md) for that procedure.
- Even mode (Aphex-lineage) produces warmer even harmonics; Odd mode (Behringer-lineage) produces brighter odd harmonics. The character of **Air** differs between the two. See [Pick Even vs Odd mode](pick-aphex-even-vs-behringer-odd-character.md).
- Use inline editing to quickly set precise values — click the displayed value, type the number with units if desired, and press Enter.

### Troubleshooting

- **Air knob has no audible effect** — The PUDU stage may be bypassed. When the stage is bypassed the entire applet tile dims to reduced opacity. Check that the stage is enabled in the CHAIN widget. See [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md).
- **Effect sounds harsh at moderate Air values** — Lower **Doo / Mix** to reduce the wet blend rather than cutting **Air** entirely. See [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md).

## Related

- [Aetherial TX Voice Processor / Aetherial RX Poodoo overview](overview.md)
- [Centre Doo on the presence band for your mic (TX) or for RX intelligibility](centre-doo-on-the-presence-band-for-your-mic-tx-or-for-rx-intelligibility.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Pick Even vs Odd mode](pick-aphex-even-vs-behringer-odd-character.md)
- [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md)