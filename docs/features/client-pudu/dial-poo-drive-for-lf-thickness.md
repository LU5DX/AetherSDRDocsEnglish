# Dial Body Drive for LF thickness

The **Body / Drive** knob controls how hard the low-frequency saturator or compressor is driven. Increasing it adds more LF thickness and harmonic density to the processed low band.

## Before you start

- The PUDU stage must be enabled in the CHAIN widget for the TX or RX side you want to adjust. See [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md).
- Open the applet: in the Aetherial Audio (TXDSP) parent container, locate the **Aetherial TX Voice Processor** or **Aetherial RX Poodoo™** sub-container. If it is hidden, double-click the PUDU stage in the CHAIN widget to open the matching editor ("Aetherial Poodoo™ — TX" or "Aetherial Poodoo™ — RX").
- When the PUDU stage is bypassed, the entire applet tile dims to approximately 55 % opacity. This confirms the stage is not processing. Re-enable the stage in the CHAIN widget to restore full opacity and active processing.

## Steps

1. Locate the **Body** group — the bracket label reading "Body" spans the three left-side knobs.
2. Find the first knob under that bracket, labelled **Drive**.
3. Turn **Drive** to the desired value. The knob displays the current value as `X.X dB`.
4. To type a precise value, click the knob's value text. A small inline editor appears. Type the desired number and press Enter, or click elsewhere to commit. The value is clamped to the valid range automatically. Press Escape to cancel the edit and revert to the previous value.
5. Release the knob. The setting is saved automatically.

## What each control does

| Control              | Default                                                                                      | Valid range                               |
|----------------------|----------------------------------------------------------------------------------------------|-------------------------------------------|
| **Poo / Drive** (TX) | 6.0 dB                                                                                       | 0.0 to 24.0 dB                            |
| **Poo / Drive** (RX) | 6.0 dB                                                                                       | 0.0 to 24.0 dB                            |
| **Body** group bracket | Group label — the three knobs below belong to the low-frequency processor (Drive, Tune, Mix). |                                           |
| AetherVoice logo     | Animated branded logo that pulses with the wet-signal RMS. Displays 'AetherVoice™' wordmark. | PooDooLogo widget — 40 px minimum height. |
| **Even**             | Selects Aphex-lineage asymmetric shaping — predominantly even harmonics, warmer, with Big Bottom LF saturation. | Radio button exclusive with 'Odd'. When checked, the button is coloured amber (PooDoo colour). |
| **Odd**              | Selects Behringer-lineage symmetric tanh shaping — pure odd harmonics, brighter, with a feed-forward bass compressor. | Radio button exclusive with 'Even'. |
| **Poo / Tune**       | 100 Hz                                                                                       | 50 to 160 Hz                              |
| **Poo / Mix**        | 30 %                                                                                         | 0.0 to 1.0 (displayed as percentage)      |
| **Clarity** group bracket | Group label — the three knobs below belong to the high-frequency processor (Tune, Air, Mix). |                                           |
| **Doo / Tune**       | 5000 Hz                                                                                      | 1000 to 10000 Hz (log mapping)            |
| **Doo / Air**        | 6.0 dB                                                                                       | 0.0 to 24.0 dB                            |
| **Doo / Mix**        | 30 %                                                                                         | 0.0 to 1.0 (displayed as percentage)      |

The mapping is linear. Higher values push the low-frequency saturator (**Even** mode) or bass compressor (**Odd** mode) harder, producing more LF effect at the same **Poo / Mix** blend level.

## Tips

- The PooDoo logo pulses with the wet-signal RMS. Watch it while turning **Drive** — visible pulsing on bass content confirms the stage is processing.
- When the PUDU stage is bypassed, the applet tile dims to 55 % opacity. This visual state matches the EQ curve dim used elsewhere in the chain and does not affect saved settings.
- In **Even** mode, high Drive values engage the Big Bottom LF saturation more aggressively. In **Odd** mode, high Drive values increase feed-forward bass compression. Pick your mode first, then set Drive. See [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md).
- Drive and **Poo / Mix** interact. A high Drive with a low Mix can deliver heavy low-end processing that is blended in subtly. See [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md).
- To focus the Drive on a specific frequency, set **Poo / Tune** first. See [Tune Poo to the fundamental of your voice (TX) or to bring out RX program lows](tune-poo-to-the-fundamental-of-your-voice-tx-or-to-bring-out-rx-program-lows.md).
- The inline value editor supports locale-aware number parsing (e.g., "12,5" in comma-decimal locales) and a fallback that strips non-numeric characters, so appending unit text like "dB" works.
- Knob component colours (background ring, foreground arc, handle) now read from the dedicated `color.knob.*` theme namespace. The PUDU applet container (`applet/pudu`) can supply per-applet colour overrides — knob foreground in PUDU may differ from standard knobs. This does not affect user interaction.
- Both mode buttons (**Even**, **Odd**) now use a unified style with no dedicated edit button appearance. The amber highlight is applied only when a mode button is selected.

## Related

- [Aetherial TX Voice Processor / Aetherial RX Poodoo overview](overview.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Tune Poo to the fundamental of your voice (TX) or to bring out RX program lows](tune-poo-to-the-fundamental-of-your-voice-tx-or-to-bring-out-rx-program-lows.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md)