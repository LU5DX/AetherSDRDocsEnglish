# Adjust Compressor Threshold (TX or RX Side)

This page explains how to set the threshold level at which the Aetherial Compressor (TX) or Aetherial AGC-C (RX) begins to act. Lowering the threshold causes the compressor to engage earlier and affect more of your signal.

## Before you start

- The compressor must be enabled (bypass off) on the side you want to adjust. A bypassed stage hides the applet tile. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md) if the tile is not visible.
- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel. If the applet panel is hidden, click `View > Applet Panel` to show it.

## Steps

1. Locate the **Aetherial Compressor** sub-container (TX side) or **Aetherial AGC-C** sub-container (RX side) in the applet panel.
2. Find the **Thresh** knob in the five-knob row at the bottom of the tile.
3. Click and drag the **Thresh** knob up to raise the threshold or down to lower it. The label below the knob updates in real time and shows the current value in dB (for example, `-18.0 dB`).
4. Watch the transfer curve and the envelope ball above the knob row. As you adjust the threshold, the knee point on the curve shifts and the ball's position relative to the curve changes to reflect where the current signal level falls.
5. Watch the gain-reduction bar. Amber fill appearing from the right indicates active compression. A tick mark at −6 dB indicates a typical working amount of gain reduction.
6. Release the knob when the displayed value is where you want it. The new threshold is saved automatically to `ClientCompTxThresholdDb` (TX) or `ClientCompRxThresholdDb` (RX).

## What each control does

| Control | Default | Valid range | Persisted key (TX / RX) | Behavior |
|---|---|---|---|---|
| Thresh | −18.0 dB | −60.0 to 0.0 dB | `ClientCompTxThresholdDb` / `ClientCompRxThresholdDb` | Sets the input level above which compression begins. Lower values engage the compressor earlier. Mapping is linear. |
| Transfer curve | — | — | — | View-only display of the input/output gain relationship. The live envelope ball shows where the current signal sits on the curve. |
| Gain-reduction bar | — | 0 to 20 dB GR | — | Horizontal amber strip, right-filled. Shows how much attenuation the compressor is applying at this moment. The tick marks −6 dB. |

## Tips

- Start with the default of −18.0 dB and lower the threshold gradually while speaking (TX) or listening to a typical signal (RX) until the gain-reduction bar shows a few dB of amber fill.
- If you want threshold changes to take effect alongside knee and limiter adjustments, open the full editor by double-clicking the COMP stage in the CHAIN widget. Knee and limiter ceiling controls are only available there.
- The envelope ball on the transfer curve gives immediate visual feedback: if the ball never leaves the lower-left straight segment, the threshold is set above your typical signal level and the compressor is not acting.

## Troubleshooting

- **The Thresh knob is present but the gain-reduction bar stays empty regardless of threshold position** — The compressor stage may still be bypassed, or the audio engine is not running. Confirm the stage is enabled via the CHAIN widget and that audio is flowing.
- **The applet tile is not visible** — The stage is bypassed or the parent Aetherial Audio (TXDSP) container is collapsed. Enable the compressor from the CHAIN widget; the tile appears automatically.

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
- [Set compression ratio for voice (TX) or for received audio (RX AGC-C)](set-compression-ratio-for-voice-tx-or-for-received-audio-rx-agc-c.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
