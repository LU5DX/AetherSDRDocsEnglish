# Bypass the gate from the chain

The CHAIN widget controls whether the Gate stage is active or bypassed for the TX and RX audio paths. Bypassing removes the gate from signal processing without changing any of its tuned parameters.

## Before you start

- AetherSDR must be running. A radio connection is not required to bypass the gate, but the Gate stage must already be enabled in the CHAIN widget before bypass is meaningful.
- Locate the CHAIN widget for the side you want to bypass (TX or RX) inside the Aetherial Audio (TXDSP) parent container in the applet panel.

## Steps

1. Find the CHAIN widget for the path you want to affect — TX or RX.
2. Single-click the **GATE** stage in the CHAIN widget.
   - A single click toggles the bypass state of that stage. When bypassed, the gate is removed from the chain; `ClientGateTxEnabled` (TX) or `ClientGateRxEnabled` (RX) is set to disabled accordingly.
3. To re-enable the gate, single-click the **GATE** stage again.

## Tips

- Bypassing via the CHAIN widget leaves all five knob values — Thresh, Ratio, Attack, Release, and Floor — unchanged. Your tuning is preserved and takes effect immediately when you re-enable the stage.
- Double-clicking the **GATE** stage in the CHAIN widget opens the floating gate editor ("Aetherial Gate — TX" or "Aetherial Gate — RX") rather than toggling bypass. Use single-click only to bypass.
- The "Aetherial TX Gate" and "Aetherial AGC-T" sub-containers are hidden when the Gate stage is not enabled. If the sub-container disappears after bypass, this is expected behavior.

## Related

- [Aetherial TX Gate / Aetherial AGC-T (RX) overview](overview.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
