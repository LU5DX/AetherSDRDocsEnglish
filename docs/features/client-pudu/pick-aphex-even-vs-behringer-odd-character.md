# Pick Aphex (Even) vs Behringer (Odd) character

Choose between two harmonic-enhancement algorithms in the PUDU exciter: Even mode (Aphex-lineage) for a warmer, asymmetric character, or Odd mode (Behringer-lineage) for a brighter, symmetric sound. The choice applies independently to the TX and RX chains.

## Before you start

- The PUDU stage must be visible in the Aetherial Audio chain. If the applet is hidden, enable the PUDU stage via the CHAIN widget on the TX or RX side, or double-click the PUDU stage in the CHAIN widget to open the floating editor.
- Decide whether you are adjusting the transmit path ("Aetherial TX Voice Processor — TX") or the receive path ("Aetherial RX Poodoo™ — RX"). The two sides are fully independent.
- On TX, the panel opens with the title "Aetherial Poodoo™ — TX". On RX, the panel opens with the title "Aetherial Poodoo™ — RX". Use the correct panel for the chain you want to adjust.

## Steps

1. Open the PUDU exciter panel: double-click the PUDU stage in the CHAIN widget on the TX or RX side. The floating editor appears with the correct title for that chain.
2. Find the two mode buttons directly below the AetherVoice logo: `Even` and `Odd`.
3. Click `Even` to select Aphex-lineage asymmetric shaping — predominantly even harmonics, warmer, with Big Bottom LF saturation. The button highlights in amber when active.
4. Click `Odd` to select Behringer-lineage symmetric tanh shaping — pure odd harmonics, brighter, with a feed-forward bass compressor.
5. Close the panel. To adjust the other chain, double-click its PUDU stage in the CHAIN widget to open its independent panel.

The selection is saved immediately to `ClientPuduTxMode` (TX) or `ClientPuduRxMode` (RX).

## What each control does

| Control          | Behavior                                                                                     | Default                                   |
|------------------|----------------------------------------------------------------------------------------------|-------------------------------------------|
| `Even`           | Selects Aphex-lineage asymmetric shaping. Exclusive with `Odd`.                              | —                                         |
| `Odd`            | Selects Behringer-lineage symmetric tanh shaping. Exclusive with `Even`.                     | —                                         |
| AetherVoice logo | Animated branded logo that pulses with the wet-signal RMS. Displays 'AetherVoice™' wordmark. | PooDooLogo widget — 40 px minimum height. |

Only one of `Even` or `Odd` can be active at a time. Selecting one deselects the other.

## Knob controls

The PUDU exciter provides six knobs arranged in two groups:

### Body group (low-frequency processor)

| Control       | Default    | Range           | Setting key             | Behavior                                                                 |
|---------------|------------|-----------------|-------------------------|--------------------------------------------------------------------------|
| Drive         | 6.0 dB     | 0.0 to 24.0 dB  | `ClientPuduTxPooDriveDb` | Linear mapping. Drives the low-frequency saturator / compressor harder. |
| Tune          | 100 Hz     | 50 to 160 Hz    | `ClientPuduTxPooTuneHz`  | Linear mapping. Centres the low-frequency focus band.                    |
| Mix           | 30 %       | 0.0 to 100.0 %  | `ClientPuduTxPooMix`     | Linear mapping. Blends the enhanced low band back with the dry signal.  |

### Clarity group (high-frequency processor)

| Control       | Default    | Range             | Setting key               | Behavior                                                                                 |
|---------------|------------|-------------------|---------------------------|------------------------------------------------------------------------------------------|
| Tune          | 5000 Hz    | 1000 to 10000 Hz  | `ClientPuduTxDooTuneHz`   | Logarithmic mapping. Centres the high-frequency excitement band.                         |
| Air           | 6.0 dB     | 0.0 to 24.0 dB    | `ClientPuduTxDooHarmonicsDb` | Linear mapping. Amount of harmonics / 'air' added at the high band.                      |
| Mix           | 30 %       | 0.0 to 100.0 %    | `ClientPuduTxDooMix`      | Linear mapping. Blends the excited highs back with the dry signal.                       |

## Inline value editing

Each knob supports direct numeric entry:

1. Click the value text displayed below the knob. A small text editor appears with a cyan border.
2. Type a new value. You can include units or extra characters — the editor strips non-numeric content automatically.
3. Press `Enter` or click elsewhere to apply the value. The value is clamped to the knob's valid range.
4. Press `Escape` to cancel the edit and revert to the previous value.

The inline editor is always available and uses the same display format as the knob label (e.g., "6.0 dB", "100 Hz", "30 %").

## Group labels

The "Body" bracket label groups the three low-frequency knobs (Drive, Tune, Mix). The "Clarity" bracket label groups the three high-frequency knobs (Tune, Air, Mix).

## Tips

- Even mode suits voice signals where warmth and low-end body are the goal. Odd mode suits situations where added presence and brightness are preferred.
- The AetherVoice logo pulses with the processed (wet) signal RMS, so you can see the exciter reacting as you switch modes without monitoring audio.
- When the PUDU stage is bypassed, the entire applet tile dims to approximately 55% opacity, matching the dim effect applied to the EQ curve. This is a visual indicator only and does not affect your settings.
- All six Body and Clarity knobs remain active regardless of which mode is selected; their effect on the signal changes character depending on the mode chosen.

## Related

- [Aetherial TX Voice Processor / Aetherial RX Poodoo overview](overview.md)
- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Add air with Doo Air](add-air-with-doo-harmonics.md)
- [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md)