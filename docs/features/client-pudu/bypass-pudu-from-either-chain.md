# Bypass PUDU from Either Chain

The CHAIN widget lets you bypass the PUDU stage on the TX chain, the RX chain, or both, without opening the PUDU editor. Use this when you want to A/B the effect or temporarily remove it from the signal path.

## Before you start

- AetherSDR must be running with the Aetherial Audio (TXDSP) parent container visible in the applet panel.
- The PUDU stage must already be present in the relevant chain (TX or RX).

## Steps

1. Locate the CHAIN widget in the applet panel for the side you want to bypass — TX or RX.
2. Single-click the PUDU stage block in the CHAIN widget to toggle the bypass on that side.
   - A bypassed stage is visually inactive; audio passes through unprocessed.
   - Click the same block again to re-engage PUDU.
3. Repeat on the other chain's CHAIN widget if you want to bypass both TX and RX independently.

The bypass state is persisted: `ClientPuduTxEnabled` for the TX chain and `ClientPuduRxEnabled` for the RX chain.

## Tips

- Single-click in the CHAIN widget bypasses the stage. Double-click opens the frameless PUDU editor ("Aetherial Voice Processor — TX" or "Aetherial RX Poodoo — RX") without changing the bypass state.
- When the stage is bypassed, the entire PUDU tile dims to reduced opacity (approximately 55 %), matching the dim effect used on the EQ curve display. This visual cue is consistent whether you bypass from the CHAIN widget or from within the editor.
- The PooDoo logo inside the editor pulses with the wet-signal RMS only when the stage is enabled. If the logo is static, the stage is bypassed.
- TX and RX bypass states are fully independent. You can bypass the TX PUDU while leaving RX PUDU active.

## Opening the PUDU editor

The PUDU editor can be opened separately for the TX and RX chains. Each opens a frameless floating window with its own independent state.

1. In the CHAIN widget for the TX or RX chain, double-click the PUDU stage block.
   - The TX editor opens with window title "Aetherial Poodoo — TX".
   - The RX editor opens with window title "Aetherial Poodoo — RX".
2. The editor shows six knobs in two groups, a mode selector (Even/Odd), and the AetherVoice logo.
3. Use the Close button at the top of the editor window to dismiss it.

## Knob groups

The PUDU editor organises its six knobs under two bracket labels.

| Bracket          | Knobs                                                                                        | Frequency range                           |
|------------------|----------------------------------------------------------------------------------------------|-------------------------------------------|
| **Body**         | Drive, Tune, Mix                                                                             | 50 – 160 Hz                               |
| **Clarity**      | Tune, Air, Mix                                                                               | 1000 – 10000 Hz                           |
| AetherVoice logo | Animated branded logo that pulses with the wet-signal RMS. Displays 'AetherVoice™' wordmark. | PooDooLogo widget — 40 px minimum height. |

## Knob controls

Each knob supports inline value editing. Click a knob's value text (the number below the knob arc) to activate a text entry field. Type a new value and press Enter or click anywhere else to commit. The value is clamped to the knob's valid range. Press Escape to cancel the edit and revert to the previous value.

| Control               | Default      | Range         | Setting key                | Behavior                                                        |
|-----------------------|--------------|---------------|----------------------------|-----------------------------------------------------------------|
| Even                  | —            | —             | `ClientPuduTxMode`         | Selects Aphex-lineage asymmetric shaping (even harmonics). Amber when checked. Exclusive with Odd. |
| Odd                   | —            | —             | `ClientPuduTxMode`         | Selects Behringer-lineage symmetric tanh shaping (odd harmonics). Exclusive with Even. |
| Body / Drive          | 6.0 dB       | 0.0 – 24.0 dB | `ClientPuduTxPooDriveDb`  | Drives the low-frequency saturator/compressor harder.           |
| Body / Tune           | 100 Hz       | 50 – 160 Hz   | `ClientPuduTxPooTuneHz`   | Centres the low-frequency focus band.                           |
| Body / Mix            | 30 %         | 0.0 – 1.0     | `ClientPuduTxPooMix`      | Blends the enhanced low band with the dry signal.               |
| Clarity / Tune        | 5000 Hz      | 1000 – 10000 Hz | `ClientPuduTxDooTuneHz`  | Centres the high-frequency excitement band. Logarithmic mapping. |
| Clarity / Air         | 6.0 dB       | 0.0 – 24.0 dB | `ClientPuduTxDooHarmonicsDb` | Amount of harmonics/'air' at the high band.                  |
| Clarity / Mix         | 30 %         | 0.0 – 1.0     | `ClientPuduTxDooMix`      | Blends the excited highs with the dry signal.                   |

## Mode selection

- **Even**: Amber PooDoo-colour when checked. Aphex-lineage asymmetric shaping — predominantly even harmonics, warmer, with Big Bottom LF saturation.
- **Odd**: Behringer-lineage symmetric tanh shaping — pure odd harmonics, brighter, with a feed-forward bass compressor.

The two radio buttons are mutually exclusive.

## Inline value editing

Each knob in the editor supports direct numerical entry:

1. Click the value text below any knob. A text entry field appears with the current value.
2. Type the desired value. You can include units (dB, Hz, %), but they are ignored. Locale-aware decimal separators (comma or dot) are accepted.
3. Press Enter or click anywhere else to commit the value. The knob updates immediately.
4. Press Escape to cancel the edit. The knob reverts to its previous value.

The editor field shows a subtle cyan border and dark background while active, and is transparent (matching the normal label appearance) when not in focus.

## Related

- [Aetherial TX Voice Processor / Aetherial RX Poodoo overview](overview.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Dial Body Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)