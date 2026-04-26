# Watch live gain reduction while speaking or listening

The ClientCompApplet shows a live gain-reduction meter and an animated transfer curve while audio is passing through the compressor. Use these indicators to see how hard the compressor is working in real time — while transmitting (TX side) or while receiving audio (RX side) — without opening the floating editor.

## Before you start

- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel.
- The compressor stage you want to monitor (TX or RX) must be enabled — the tile stays hidden while the stage is bypassed. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md) if the tile is not visible.

## Steps

1. Locate the "Aetherial Compressor" sub-container (TX side) or "Aetherial AGC-C" sub-container (RX side) inside the Aetherial Audio (TXDSP) parent container in the applet panel.
2. Speak into your microphone (TX) or let received audio play (RX).
3. Watch the **Gain-reduction bar** — the horizontal amber strip below the transfer curve. The strip fills from the right as gain reduction increases, up to a maximum of 20 dB.
4. Watch the **Transfer curve** — the live envelope ball moves along the static curve to show the current input level relative to the threshold and ratio settings.
5. Use the -6 dB tick mark on the **Gain-reduction bar** as a reference. A fill that consistently reaches or slightly exceeds that tick is a typical working amount of compression.

## What each control does

| Control | Kind | What you see | Notes |
|---|---|---|---|
| Transfer curve | Indicator | Static input/output curve with a live ball at the current envelope level. | View-only in the applet; editable in the floating editor. |
| Gain-reduction bar | Meter | Horizontal amber strip, right-filled. Scale runs 0 to 20 dB of gain reduction. A tick marks the -6 dB point. | Refreshed at approximately 30 Hz with smoothed ballistics. |
| Thresh | Knob | Current threshold. Default -18.0 dB; range -60.0 to 0.0 dB. | TX: `ClientCompTxThresholdDb`. RX: `ClientCompRxThresholdDb`. |
| Ratio | Knob | Current ratio. Default 3.0; range 1.0 to 20.0. Displayed as X.XX:1. | TX: `ClientCompTxRatio`. RX: `ClientCompRxRatio`. |
| Attack | Knob | Current attack time. Default 20.0 ms; range 0.1 to 300.0 ms. | TX: `ClientCompTxAttackMs`. RX: `ClientCompRxAttackMs`. |
| Release | Knob | Current release time. Default 200 ms; range 5 to 2000 ms. | TX: `ClientCompTxReleaseMs`. RX: `ClientCompRxReleaseMs`. |
| Makeup | Knob | Current makeup gain. Default 0.0 dB; range -12.0 to 24.0 dB. | TX: `ClientCompTxMakeupDb`. RX: `ClientCompRxMakeupDb`. |

## Tips

- If the **Gain-reduction bar** never moves, the input level is not crossing the threshold. Lower the Thresh knob or raise your microphone gain.
- If the **Gain-reduction bar** is pegged at or near 20 dB continuously, the ratio or threshold is set very aggressively. Raise the Thresh value or lower the Ratio knob to ease the compression.
- The envelope ball on the **Transfer curve** rests at the threshold line when no audio is present. During audio, it travels along the curve; a ball sitting in the bent portion of the curve confirms active compression.
- Both the TX and RX tiles update independently. You can monitor both simultaneously if both sub-containers are expanded.

## Troubleshooting

- **The tile is not visible** — The compressor stage is bypassed. Enable the stage from the CHAIN widget (single-click the COMP stage) or see [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- **The Gain-reduction bar shows no movement during audio** — The input level is not reaching the threshold. Reduce the Thresh knob value or check that the correct audio device is active and producing signal.
- **The envelope ball does not move** — The applet is not connected to an active audio engine. Verify the radio is connected and audio is flowing through the relevant TX or RX processing chain.

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Set compression ratio for voice (TX) or for received audio (RX AGC-C)](set-compression-ratio-for-voice-tx-or-for-received-audio-rx-agc-c.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
