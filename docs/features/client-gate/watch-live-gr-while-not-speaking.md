# Watch live GR while not speaking

The gain-reduction meter and transfer curve update in real time even when you are not transmitting. Watching them while the room is quiet tells you how deep the gate is cutting at any given moment, so you can judge whether your threshold and floor settings are appropriate before you key up.

## Before you start

- The Gate stage must be enabled on the side you want to observe. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if the applet is not visible.
- The "Aetherial TX Gate" or "Aetherial AGC-G (RX)" sub-container must be open inside the Aetherial Audio (TXDSP) parent container.

## Steps

1. Open the applet panel if it is not already visible: `View > Applet Panel`.
2. Locate the "Aetherial TX Gate" sub-container (TX side) or "Aetherial AGC-G (RX)" sub-container (RX side).
3. Stay silent — do not speak or key the radio.
4. Watch the amber Gain-reduction bar. While input stays below the Thresh level, the bar fills from the right, showing the depth of attenuation being applied.
5. Watch the input ball on the Transfer curve. The ball sits in the lower-left region of the curve when the gate is closed (input below threshold) and moves up and to the right when the gate opens.
6. Note how far the bar fills. If it reaches or exceeds the -15 dB tick mark, the gate is applying at least 15 dB of attenuation — the default Floor value.

## Bypass dimming

When the gate stage is bypassed, the entire applet tile renders at reduced opacity (approximately 55% of full brightness). This matches the dim effect used on the EQ curve and gives an at-a-glance indication that the stage is not processing audio. The applet returns to full brightness as soon as the stage is re-enabled.

## What each control does

| Control                | Kind        | Default    | Behavior / Notes                                                                                                                                                                                                                                 |
|------------------------|-------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transfer curve         | Indicator   | —          | Compact-mode ClientGateCurveWidget. Plots the expander's static transfer curve and a live ball at the current input level.                                                                                                                       |
| Gain-reduction bar     | Meter       | —          | Horizontal amber strip, right-filled. Scale maxes at 40 dB (gates can cut very deep); a tick at -15 dB marks the soft-expander default floor.                                                                                                    |
| Thresh                 | Knob        | -40.0 dB   | Linear mapping. Level below which the gate starts attenuating. Range: -80.0 to 0.0 dB. Setting key: `ClientGateTxThresholdDb`.                                                                                                                        |
| Ratio                  | Knob        | 2.0        | Linear mapping. Higher ratios give a harder, more gate-like cut; lower ratios act as a soft downward expander. Label format 'X.X:1'. Range: 1.0 to 10.0. Setting key: `ClientGateTxRatio`.                                                            |
| Return                 | Knob        | 2.0 dB     | Linear mapping (n * 20). Sets the hysteresis deadband: the gate opens above Thresh and doesn't close again until the input drops below Thresh − Return, preventing rapid chatter near the threshold. Label format 'X.XX dB'. Range: 0.0 to 20.0 dB. Setting key: `ClientGateTxReturnDb`. |
| Release                | Knob        | 100 ms     | Exponential mapping (5 * 400^n). Sets how quickly the gate closes after input falls below Thresh − Return. Label format 'X.X ms' below 100, 'X ms' above. Range: 5 to 2000 ms. Setting key: `ClientGateTxReleaseMs`.                                |
| Floor                  | Knob        | -15.0 dB   | Linear mapping. Maximum attenuation the gate is allowed to apply. Range: -80.0 to 0.0 dB. Setting key: `ClientGateTxFloorDb`.                                                                                                                        |

**Gain-reduction bar:** Horizontal amber strip, right-filled. Scale maxes at 40 dB. A tick at -15 dB marks the default Floor value. Empty means no attenuation; full right-fill means the gate is cutting at the maximum depth set by Floor.

**Transfer curve / Input ball:** The static curve shows the expander's input-to-output relationship. The live ball tracks the current input level, moving below or above the threshold knee in real time. The ball is white when below threshold and green when above threshold.

**Hysteresis band:** A soft-cyan vertical band drawn on the transfer curve between (Thresh − Return) and Thresh. It makes the gate's sticky zone visible: the gate opens when the input rises above Thresh and does not close again until the input falls below Thresh − Return. The band is absent when Return is set to 0.

**Return knob:** Sets the hysteresis deadband width in dB. Increasing Return prevents the gate from chattering when the input hovers near the threshold. The label displays in the format X.XX dB.

## Animation update behavior

The gain-reduction meter and transfer curve use a smooth animation timer that updates the display approximately every 33 ms. When audio levels are settled (no change in input level), the animation timer stops to save CPU resources. The transfer curve and gain-reduction bar repaint on every animation tick while values are changing, ensuring no visual frames are skipped. The gain-reduction bar and curve widget always render the latest state on each redraw, so the display remains responsive and never shows stale data.

## Inline value editing

Each knob supports inline direct entry of a numeric value. Click the displayed value text below the knob to activate an in-place editor. The editor appears with a dark inset background and cyan border to indicate edit mode. Type a new value and press Enter or click elsewhere to commit. The value is clamped to the knob's valid range when committed.

- The editor accepts locale-aware decimal formatting (comma or period as decimal separator).
- If the entered text cannot be parsed as a number, the editor silently reverts to the previous value.
- Press Escape while editing to discard changes and revert to the prior value.
- While the editor is active, mouse wheel events still adjust the knob value normally.
- The editor is available on both the TX Gate and RX AGC-G copies independently.

## Theme colors

The knob components and transfer curve widget use theme colors from the `color.knob.*` and `color.background.*` namespaces. Knob elements have a dedicated container override `applet/gate` that allows per-applet styling (for example, the amber knob foreground used in the gate applet). The label and value text below knobs remain on standard `color.text.secondary` and `color.text.primary` respectively, while the curve widget's background, grid, axis labels, and curve line use `color.background.0`, `color.background.1`, `color.text.label`, and `color.accent.warning` (amber). This ensures a consistent appearance with the current theme without hardcoded color values.

## Tips

- The meter updates approximately every 33 ms, so the bar tracks gain reduction closely enough to catch brief noise events.
- Knob changes made in the floating Gate editor are reflected in the applet within the same 33 ms poll cycle, so you can leave the applet visible as a live meter while tuning in the editor.
- A bar that never fully empties while you are silent means the gate is always attenuating — the input never rises above Thresh even when you stop speaking. This is normal and expected behavior for a noise gate at rest.
- If the gate chatters — opens and closes rapidly while you are speaking near the threshold — increase Return to widen the hysteresis deadband. The cyan band on the transfer curve grows wider as you do so, giving you a visual indication of how much deadband is in effect.
- If the applet tile appears dimmed, the gate stage is bypassed and no processing is active. Re-enable the stage to restore full brightness and resume attenuation.
- Clicking a knob's value label provides a faster way to set an exact value compared to dragging the knob, especially for fine adjustments or values near the range bounds.

## Related

- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Tune return / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)