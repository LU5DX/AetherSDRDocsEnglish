# Bypass the tube from the chain

When you want to hear your TX signal without tube saturation — for comparison or troubleshooting — you can bypass the Tube stage without changing any of its settings. Bypassing leaves all knob positions intact so you can re-enable the stage exactly as you left it.

## Before you start

- The TXDSP (PooDoo Audio) processing chain must be visible in the applet panel.
- The Tube stage must already be present in the CHAIN widget. If it is not in the chain, there is nothing to bypass.

## Steps

1. Locate the CHAIN widget inside the PooDoo Audio (TXDSP) container in the applet panel.
2. Single-click the Tube stage in the CHAIN widget to toggle its bypass state.

   - When bypassed, the stage is removed from the active signal path. The TUBE sub-container, if visible, continues to show the transfer curve and knob positions but the tube model is not applied to the TX signal.
   - Single-click again to re-enable the stage.

The bypass state is persisted in `ClientTubeTxEnabled`.

## Tips

- To open the floating Tube editor without toggling bypass, double-click the Tube stage in the CHAIN widget instead of single-clicking.
- The transfer curve and live input ball in the TUBE sub-container continue to update visually regardless of bypass state. Watch the curve to confirm your Drive, Bias, and Tone settings before re-engaging.
- If you want a partial blend rather than a hard bypass, reduce the Mix knob toward 0 % instead. That keeps the stage active but fades to dry signal. See [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md).

## Related

- [Tube Saturator overview](overview.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Dial Drive until the curve starts to bend](dial-drive-until-the-curve-starts-to-bend.md)
