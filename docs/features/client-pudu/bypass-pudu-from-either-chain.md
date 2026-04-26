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
- The PooDoo logo inside the editor pulses with the wet-signal RMS only when the stage is enabled. If the logo is static, the stage is bypassed.
- TX and RX bypass states are fully independent. You can bypass the TX PUDU while leaving RX PUDU active.

## Related

- [Aetherial TX Poodoo / Aetherial RX Poodoo overview](overview.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
