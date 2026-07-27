# Adjust Compressor Threshold (TX or RX Side)

This page explains how to set the threshold level at which the Aetherial Compressor (TX) or Aetherial AGC-C (RX) begins to act. Lowering the threshold causes the compressor to engage earlier and affect more of your signal.

## Before you start

- The compressor must be enabled (bypass off) on the side you want to adjust. When the stage is bypassed, the applet tile remains visible but is dimmed to approximately 55% opacity. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md) if the tile appears dimmed or if you need to re-enable the stage.
- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel. If the applet panel is hidden, click `View > Applet Panel` to show it.

## Steps

1. Locate the **Aetherial Compressor** sub-container (TX side) or **Aetherial AGC-C** sub-container (RX side) in the applet panel.
2. Find the **Thresh** knob in the five-knob row at the bottom of the tile.
3. Click and drag the **Thresh** knob up to raise the threshold or down to lower it. The label below the knob updates in real time and shows the current value in dB (for example, `-18.0 dB`).
4. To enter a value directly, click on the value label beneath any knob. A QLineEdit overlay appears with a subtle dark inset and cyan border. Type the desired value and press Enter. The editor also commits when focus is lost (for example, clicking elsewhere on the applet). The value is clamped to the valid range automatically.
5. Watch the transfer curve and the envelope ball above the knob row. As you adjust the threshold, the knee point on the curve shifts and the ball's position relative to the curve changes to reflect where the current signal level falls.
6. Watch the gain-reduction bar. Amber fill appearing from the right indicates active compression. A tick mark at −6 dB indicates a typical working amount of gain reduction.
7. Release the knob when the displayed value is where you want it. The new threshold is saved automatically to `ClientCompTxThresholdDb` (TX) or `ClientCompRxThresholdDb` (RX).

## What each control does

| Control            | Default                                                                                                               | Valid range                                                                                                                                                                                                                                |
|--------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Thresh             | −18.0 dB                                                                                                              | −60.0 to 0.0 dB                                                                                                                                                                                                                            |
| Ratio              | 3.0                                                                                                                   | 1.0 to 20.0                                                                                                                                                                                                                                |
| Attack             | 20.0 ms                                                                                                               | 0.1 to 300.0 ms                                                                                                                                                                                                                            |
| Release            | 200 ms                                                                                                                | 5 to 2000 ms                                                                                                                                                                                                                               |
| Makeup             | 0.0 dB                                                                                                                | −12.0 to 24.0 dB                                                                                                                                                                                                                           |
| Transfer curve     | —                                                                                                                     | —                                                                                                                                                                                                                                          |
| Gain-reduction bar | Horizontal amber strip, right-filled. Scale maxes at 20 dB reduction; a tick at -6 dB marks a typical working amount. | Polled at ~30 Hz from ClientComp::gainReductionDb(); MeterSmoother ballistics (125 Hz animation, 30 ms attack / 180 ms release) make the fill read identically across all metering surfaces. The curve widget updates on every animation tick. |
| Drive              | 0.0 dB                                                                                                                | 0.0 to 18.0 dB                                                                                                                                                                                                                            |
| Phase              | 0 stages                                                                                                              | 0 to 6 stages                                                                                                                                                                                                                             |
## Tips

- Start with the default of −18.0 dB and lower the threshold gradually while speaking (TX) or listening to a typical signal (RX) until the gain-reduction bar shows a few dB of amber fill.
- If you want threshold changes to take effect alongside knee and limiter adjustments, open the full editor by double-clicking the COMP stage in the CHAIN widget. Knee and limiter ceiling controls are only available there.
- The envelope ball on the transfer curve gives immediate visual feedback: if the ball never leaves the lower-left straight segment, the threshold is set above your typical signal level and the compressor is not acting.
- To enter precise values, click the value label beneath any knob to open the inline editor. Type the number (locale-aware; comma as decimal separator is supported) and press Enter.
- When the stage is bypassed, the entire applet tile dims to roughly half brightness. This is a visual indicator only and does not affect any saved knob values.
- The transfer curve and envelope ball now respect the current theme colors. The background, grid lines, curve, and ball glow all reflect the active theme palette for consistent visual appearance across the application.

## Troubleshooting

- **The Thresh knob is present but the gain-reduction bar stays empty regardless of threshold position** — The compressor stage may still be bypassed, or the audio engine is not running. Confirm the stage is enabled via the CHAIN widget and that audio is flowing.
- **The applet tile appears dimmed** — The compressor stage is bypassed. Enable it from the CHAIN widget to restore full brightness and restore active processing. The tile remains visible while bypassed, unlike previous releases where it was hidden.
- **The applet tile is not visible at all** — The parent Aetherial Audio (TXDSP) container is collapsed. Expand it in the applet panel to reveal the tile.

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
- [Set compression ratio for voice (TX) or for received audio (RX AGC-C)](set-compression-ratio-for-voice-tx-or-for-received-audio-rx-agc-c.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)