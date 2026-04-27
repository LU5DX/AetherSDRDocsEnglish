# Bypass the Gate from the Chain

The CHAIN widget controls whether the Gate stage is active in the audio processing chain. Bypassing it lets you disable the TX or RX gate entirely without changing any of its tuning knobs, so you can compare gated and ungated audio or temporarily silence the stage.

## Before you start

- Open the Aetherial Audio (TXDSP) parent container in the Applet Panel. The "Aetherial TX Gate" (TX) and "Aetherial AGC-T" (RX) sub-containers are hidden until the Gate stage is enabled via the CHAIN widget.
- Know which side you want to bypass — TX (affects your transmitted audio) or RX (affects received audio).

## Steps

1. Locate the CHAIN widget for the side you want to change — TX or RX — inside the Aetherial Audio (TXDSP) parent container in the Applet Panel.
2. Single-click the GATE stage in the CHAIN widget to toggle the gate bypass on that side.
   - When the stage is enabled, the "Aetherial TX Gate" or "Aetherial AGC-T" sub-container becomes visible and the gate is active in the chain.
   - When the stage is bypassed, the sub-container is hidden and no gain reduction is applied.
3. To re-enable the stage, single-click the GATE stage in the CHAIN widget again.

The bypass state is persisted as `ClientGateTxEnabled` (TX side) or `ClientGateRxEnabled` (RX side) and restored on the next application launch.

## Tips

- Bypassing from the CHAIN widget does not reset any of the five tuning knobs — Thresh, Ratio, Attack, Release, and Floor values are preserved.
- To open the floating gate editor for detailed tuning without bypassing, double-click the GATE stage in the CHAIN widget instead of single-clicking.

## Related

- [Aetherial TX Gate / Aetherial AGC-T (RX) overview](overview.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
