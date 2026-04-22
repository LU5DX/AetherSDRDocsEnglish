# Bypass the Gate from the Chain

This page explains how to bypass the TX noise gate without deleting its settings. Use bypass when you want to temporarily disable the gate — for example, to compare processed and unprocessed audio — while keeping all your tuned parameters intact.

## Before you start

- The Gate stage must be enabled in the CHAIN widget before you can bypass it. If the GATE sub-container is not visible in the PooDoo Audio (TXDSP) parent container, the gate has not yet been added to the chain.
- A radio connection is not required to bypass the gate; the setting is local to AetherSDR.

## Steps

1. Locate the **CHAIN** widget inside the PooDoo Audio (TXDSP) parent container in the applet panel.
2. Single-click the **Gate** stage in the CHAIN widget to toggle bypass on or off.
   - When bypassed, the gate applies no attenuation and the transfer curve and gain-reduction bar in the GATE sub-container reflect the inactive state.
   - Single-clicking again re-enables the gate; your previously set Thresh, Ratio, Attack, Release, and Floor values are restored immediately.

The bypass state is persisted in `ClientGateTxEnabled`. All other gate parameters (`ClientGateTxThresholdDb`, `ClientGateTxRatio`, `ClientGateTxAttackMs`, `ClientGateTxReleaseMs`, `ClientGateTxFloorDb`) are unaffected by bypass.

## Tips

- To open the floating Gate editor instead of toggling bypass, double-click the Gate stage in the CHAIN widget.
- The gain-reduction bar in the GATE tile goes dark (no amber fill) while the gate is bypassed, which makes it easy to confirm bypass is active at a glance.

## Related

- [Noise Gate / Expander overview](overview.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md)
