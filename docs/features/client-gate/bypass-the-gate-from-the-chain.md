# Aetherial TX Gate / Aetherial AGC-G (RX)

The AetherSDR client implements a downward expander / noise gate that runs entirely on the client side, with no round-trip to the radio. Two independent copies are created by the AppletPanel:

- **Aetherial TX Gate** — processes the transmit audio chain.
- **Aetherial AGC-G (RX)** — processes the receive audio chain (AGC stands for Automatic Gain Control – Gate variant).

The gate silences background noise between words (TX) or below a desired RX-audio floor by attenuating audio below a threshold. The user interface shows the static transfer curve with a live input ball, a cyan hysteresis-band overlay between (Thresh − Return) and Thresh, a 40 dB gain-reduction meter, and five tuning knobs: Thresh, Ratio, Return, Release, Floor.

## Controls

| Label | Kind | Default | Valid Range | Setting Key | Behavior | Notes |
|---|---|---|---|---|---|---|
| Transfer curve | indicator | — | — | — | Compact-mode ClientGateCurveWidget. Plots the expander's static transfer curve and a live ball at the current input level. | |
| Gain-reduction bar | meter | — | 0 to 40 dB GR | — | Horizontal amber strip, right-filled. Scale maxes at 40 dB (gates can cut very deep); a tick at -15 dB marks the soft-expander default floor. | |
| Thresh | knob | -40.0 dB | -80.0 to 0.0 dB | `ClientGateTxThresholdDb` (TX side)<br>`ClientGateRxThresholdDb` (RX side) | Linear mapping. Level below which the gate starts attenuating. | |
| Ratio | knob | 2.0 | 1.0 to 10.0 | `ClientGateTxRatio` (TX side)<br>`ClientGateRxRatio` (RX side) | Linear mapping. Higher ratios give a harder, more gate-like cut; lower ratios act as a soft downward expander. | Label 'X.X:1'. |
| Return | knob | 2.0 dB | 0.0 to 20.0 dB | `ClientGateTxReturnDb` (TX side)<br>`ClientGateRxReturnDb` (RX side) | Linear mapping (n * 20). Sets the hysteresis deadband: the gate opens above Thresh and doesn't close again until the input drops below Thresh − Return, preventing rapid chatter near the threshold. | Label 'X.XX dB'. The curve widget draws a soft-cyan vertical band between (Thresh − Return) and Thresh to make the sticky zone visible. |
| Release | knob | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` (TX side)<br>`ClientGateRxReleaseMs` (RX side) | Exponential mapping (5 * 400^n). Sets how quickly the gate closes after input falls below Thresh − Return. | Label 'X.X ms' below 100, 'X ms' above. |
| Floor | knob | -15.0 dB | -80.0 to 0.0 dB | `ClientGateTxFloorDb` (TX side)<br>`ClientGateRxFloorDb` (RX side) | Linear mapping. Maximum attenuation the gate is allowed to apply. | |

## Indicators

| Label | States | Meaning |
|---|---|---|
| Input ball | below threshold, above threshold | Shows whether the gate is currently open or closed. |
| Hysteresis band | absent (Return = 0), soft-cyan vertical band | Visualises the Return deadband on the transfer-curve input axis — the gate's sticky zone between (Thresh − Return) and Thresh. |
| Gain-reduction strip | empty, amber fill, -15 dB tick | Depth of attenuation while the gate is closed. |

## Transfer Curve Widget

The ClientGateCurveWidget displays the static transfer curve. In compact mode (used within the Applet Panel) it uses a smaller 7-pixel font for axis labels. In full-size mode (floating editor) it uses a 9-pixel font and draws -dB grid labels at the major tick positions. Labels are pre-rendered as `QStaticText` objects for improved painting performance.

# Bypass the Gate from the Chain

The CHAIN widget controls whether the Gate stage is active in the audio processing chain. Bypassing it lets you disable the TX or RX gate entirely without changing any of its tuning knobs, so you can compare gated and ungated audio or temporarily silence the stage.

## Before you start

- Open the Aetherial Audio (TXDSP) parent container in the Applet Panel. The "Aetherial TX Gate" (TX) and "Aetherial AGC-G (RX)" sub-containers are hidden until the Gate stage is enabled via the CHAIN widget.
- Know which side you want to bypass — TX (affects your transmitted audio) or RX (affects received audio).

## Steps

1. Locate the CHAIN widget for the side you want to change — TX or RX — inside the Aetherial Audio (TXDSP) parent container in the Applet Panel.
2. Single-click the GATE stage in the CHAIN widget to toggle the gate bypass on that side.
   - When the stage is enabled, the "Aetherial TX Gate" or "Aetherial AGC-G (RX)" sub-container becomes visible at full opacity and the gate is active in the chain.
   - When the stage is bypassed, the sub-container dims to reduced opacity (approximately 55 % of full brightness) and no gain reduction is applied.
3. To re-enable the stage, single-click the GATE stage in the CHAIN widget again. The sub-container returns to full opacity.

The bypass state is persisted as `ClientGateTxEnabled` (TX side) or `ClientGateRxEnabled` (RX side) and restored on the next application launch.

## Tips

- The dim effect when bypassed matches the visual treatment applied to the EQ curve when its stage is bypassed, giving a consistent visual cue across DSP stages.
- Bypassing from the CHAIN widget does not reset any of the five tuning knobs — Thresh, Ratio, Return, Release, and Floor values are preserved.
- To open the floating gate editor for detailed tuning without bypassing, double-click the GATE stage in the CHAIN widget instead of single-clicking.

## Related

- [Aetherial Audio (TXDSP) overview](overview.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)