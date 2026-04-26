# Bypass the Gate from the Chain

Bypassing the gate removes it from the TX audio processing chain without changing any of its settings. Use this when you want to disable noise gating temporarily — for example, during a net check-in — and restore it later with the same configuration.

## Before you start

- The GATE stage must already be present in the CHAIN widget inside the PooDoo Audio (TXDSP) container.
- The GATE sub-container applet is only visible when the Gate stage is enabled in the CHAIN widget; bypassing is done from the CHAIN widget itself.

## Steps

1. Locate the CHAIN widget inside the PooDoo Audio (TXDSP) container in the applet panel.
2. Single-click the Gate stage block in the CHAIN widget to toggle its bypass state.

The Gate stage is bypassed when the block appears inactive in the CHAIN widget. The GATE sub-container remains visible but the gate applies no attenuation — the gain-reduction bar will read 0 dB and the transfer curve ball will track the input level without triggering any gain reduction.

3. To re-enable the gate, single-click the Gate stage block again.

The bypass state is persisted in `ClientGateTxEnabled`. All knob values (`ClientGateTxThresholdDb`, `ClientGateTxRatio`, `ClientGateTxAttackMs`, `ClientGateTxReleaseMs`, `ClientGateTxFloorDb`) are unchanged by bypassing.

## Tips

- Bypassing from the CHAIN widget is non-destructive. All five tuning knobs (Thresh, Ratio, Attack, Release, Floor) retain their values and take effect immediately when you re-enable the stage.
- To open the floating Gate editor for detailed adjustments without bypassing, double-click the Gate stage in the CHAIN widget.

## Related

- [Noise Gate / Expander overview](overview.md)
- [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
