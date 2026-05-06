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

- Single-click in the CHAIN widget bypasses the stage. Double-click opens the frameless PUDU editor ("Aetherial Poodoo™ — TX" or "— RX") without changing the bypass state.
- When the stage is bypassed, the entire PUDU tile dims to reduced opacity (approximately 55 %), matching the dim effect used on the EQ curve display. This visual cue is consistent whether you bypass from the CHAIN widget or from within the editor.
- The AetherVoice™ logo inside the editor pulses with the wet-signal RMS only when the stage is enabled. If the logo is static, the stage is bypassed.
- TX and RX bypass states are fully independent. You can bypass the TX PUDU while leaving RX PUDU active.

## Knob groups

The PUDU editor organises its six knobs under two bracket labels.

| Bracket | Knobs | Frequency range | Purpose |
|---------|-------|-----------------|---------|
| **Body** | Drive, Tune, Mix | 50 – 160 Hz | Low-frequency saturator / compressor |
| **Clarity** | Tune, Air, Mix | 1000 – 10 000 Hz | High-frequency excitement and harmonics |

In earlier versions these groups were labelled **Poo** and **Doo** respectively. Any references to those names in other parts of the manual refer to the same controls now labelled **Body** and **Clarity**.

## Related

- [Aetherial TX Poodoo / Aetherial RX Poodoo overview](overview.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Dial Body Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)