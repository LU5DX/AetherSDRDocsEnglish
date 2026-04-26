# Dial Poo Drive for LF thickness

The **Poo / Drive** knob controls how hard the low-frequency saturator or compressor is driven. Increasing it adds more LF thickness and harmonic density to the processed low band.

## Before you start

- The PUDU stage must be enabled in the CHAIN widget for the TX or RX side you want to adjust. See [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md).
- Open the applet: in the Aetherial Audio (TXDSP) parent container, locate the **Aetherial TX Poodoo™** or **Aetherial RX Poodoo™** sub-container. If it is hidden, double-click the PUDU stage in the CHAIN widget to open the matching editor ("Aetherial Poodoo™ — TX" or "Aetherial Poodoo™ — RX").

## Steps

1. Locate the **Poo** group — the bracket label reading "Poo" spans the three left-side knobs.
2. Find the first knob under that bracket, labelled **Drive**.
3. Turn **Drive** to the desired value. The knob displays the current value as `X.X dB`.
4. Release the knob. The setting is saved automatically.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| **Poo / Drive** (TX) | 6.0 dB | 0.0 to 24.0 dB | `ClientPuduTxPooDriveDb` |
| **Poo / Drive** (RX) | 6.0 dB | 0.0 to 24.0 dB | `ClientPuduRxPooDriveDb` |

The mapping is linear. Higher values push the low-frequency saturator (Even mode) or bass compressor (Odd mode) harder, producing more LF effect at the same **Poo / Mix** blend level.

## Tips

- The PooDoo logo pulses with the wet-signal RMS. Watch it while turning **Drive** — visible pulsing on bass content confirms the stage is processing.
- In **Even** mode, high Drive values engage the Big Bottom LF saturation more aggressively. In **Odd** mode, high Drive values increase feed-forward bass compression. Pick your mode first, then set Drive. See [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md).
- Drive and **Poo / Mix** interact. A high Drive with a low Mix can deliver heavy low-end processing that is blended in subtly. See [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md).
- To focus the Drive on a specific frequency, set **Poo / Tune** first. See [Tune Poo to the fundamental of your voice (TX) or to bring out RX program lows](tune-poo-to-the-fundamental-of-your-voice-tx-or-to-bring-out-rx-program-lows.md).

## Related

- [Aetherial TX Poodoo / Aetherial RX Poodoo overview](overview.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Tune Poo to the fundamental of your voice (TX) or to bring out RX program lows](tune-poo-to-the-fundamental-of-your-voice-tx-or-to-bring-out-rx-program-lows.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md)
