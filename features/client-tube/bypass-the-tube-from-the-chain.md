# Bypass the tube from the chain

Use this page to remove the Tube Saturator from the TX signal path without changing any of its settings. Bypassing lets you compare your signal with and without saturation, or simply disable the stage when it is not needed.

## Before you start

- The Tube Saturator stage must already be present in the CHAIN widget inside the PooDoo Audio (TXDSP) container.
- The TUBE sub-container must be visible, or you must have access to the CHAIN widget.

## Steps

1. Locate the Tube stage in the CHAIN widget inside the PooDoo Audio (TXDSP) container.
2. Single-click the Tube stage in the CHAIN widget to toggle bypass on or off.

When the stage is bypassed, the tube transfer curve and knobs in the TUBE sub-container remain at their last values. The setting `ClientTubeTxEnabled` is updated and persisted automatically.

## Tips

- To re-engage the tube, single-click the Tube stage in the CHAIN widget again.
- Bypassing via the CHAIN widget does not reset Drive, Tone, Bias, Output, or Mix — all values are preserved for when you re-enable the stage.
- To open the full floating editor instead of bypassing, double-click the Tube stage in the CHAIN widget.

## Related

- [Tube Saturator overview](overview.md)
- [Dial Drive until the curve starts to bend](dial-drive-until-the-curve-starts-to-bend.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
