# Watch live gain reduction while speaking or listening

The ClientCompApplet shows a live gain-reduction meter and an animated transfer curve while audio is passing through the compressor. Use these indicators to see how hard the compressor is working in real time — while transmitting (TX side) or while receiving audio (RX side) — without opening the floating editor.

Each compressor knob supports inline value editing: click the value text to enter a precise numeric value directly, then press Enter or click elsewhere to commit it.

## Before you start

- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel.
- The compressor stage you want to monitor (TX or RX) must be enabled — the tile renders at reduced opacity when the stage is bypassed. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md) if the tile appears dimmed.

## Steps

1. Locate the "Aetherial Compressor" sub-container (TX side) or "Aetherial AGC-C" sub-container (RX side) inside the Aetherial Audio (TXDSP) parent container in the applet panel.
2. Speak into your microphone (TX) or let received audio play (RX).
3. Watch the **Gain-reduction bar** — the horizontal amber strip below the transfer curve. The strip fills from the right as gain reduction increases, up to a maximum of 20 dB.
4. Watch the **Transfer curve** — the live envelope ball moves along the static curve to show the current input level relative to the threshold and ratio settings.
5. Use the -6 dB tick mark on the **Gain-reduction bar** as a reference. A fill that consistently reaches or slightly exceeds that tick is a typical working amount of compression.

## Entering precise values directly

Click any knob's displayed value text to open an inline editor. Type a number and press Enter, or click elsewhere to apply the value. The editor closes automatically and the knob updates.

- The editor accepts locale-aware decimal formats (e.g., "12,5" in comma-decimal locales).
- Enter plain numbers with units stripped (e.g., type "5" or "5.0" for 5.0 ms Attack).
- Press Escape to cancel editing and restore the previous value.
- The editor appears as a transparent overlay that matches the normal label appearance. When focused, a subtle dark background and cyan border indicate editing mode.

## What each control does

| Control            | Kind                                                                                                                                                                                                                                                                    | What you see                                                                                                                                                                                                                                           |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transfer curve     | Indicator                                                                                                                                                                                                                                                               | Static input/output curve with a live ball at the current envelope level. Curve, grid, ball, and axis label colors follow the active theme via `ThemeManager`.                                                                                         |
| Gain-reduction bar | Meter                                                                                                                                                                                                                                                                   | Horizontal amber strip, right-filled. Scale runs 0 to 20 dB of gain reduction. A tick marks the -6 dB point. Slider fill styled via `applet/comp` theme container.                                                                                     |
| Thresh             | Knob                                                                                                                                                                                                                                                                    | Current threshold. Default -18.0 dB; range -60.0 to 0.0 dB. Click the value to type a precise threshold. Setting stored as `ClientCompTxThresholdDb` or `ClientCompRxThresholdDb`.                                                                     |
| Ratio              | Knob                                                                                                                                                                                                                                                                    | Current ratio. Default 3.0; range 1.0 to 20.0. Displayed as X.XX:1. Click the value to type a precise ratio. Setting stored as `ClientCompTxRatio` or `ClientCompRxRatio`.                                                                             |
| Attack             | Knob                                                                                                                                                                                                                                                                    | Current attack time. Default 20.0 ms; range 0.1 to 300.0 ms. Click the value to type a precise attack time. Setting stored as `ClientCompTxAttackMs` or `ClientCompRxAttackMs`.                                                                        |
| Release            | Knob                                                                                                                                                                                                                                                                    | Current release time. Default 200 ms; range 5 to 2000 ms. Click the value to type a precise release time. Setting stored as `ClientCompTxReleaseMs` or `ClientCompRxReleaseMs`.                                                                        |
| Makeup             | Knob                                                                                                                                                                                                                                                                    | Current makeup gain. Default 0.0 dB; range -12.0 to 24.0 dB. Click the value to type a precise makeup gain. Shows explicit '+' sign for positive values. Setting stored as `ClientCompTxMakeupDb` or `ClientCompRxMakeupDb`.                           |
| Drive              | Pre-comp gain boost with linked auto-makeup. Pushes more signal across the threshold so the compressor engages harder, and simultaneously adds equal gain at the output so average RMS lifts alongside peaks rather than dropping. Pair with Phase to keep peaks clean. | Displayed in the floating StripCompPanel only (right column). Label shows as '+X.X dB'. Range 0.0 to 18.0 dB. Tooltip explains #2887 PAPR reduction pairing. Setting stored as `ClientCompTxDriveDb`.                                                  |
| Phase              | Number of cascaded all-pass sections (0 = off). Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz). Symmetrizes asymmetric voice peaks before compression to reduce PAPR.                          | Displayed in the floating StripCompPanel only (right column). Label 'Off' when 0, 'N stg' when active. Range 0 to 6 stages. Setting stored as `ClientCompTxPhaseRotatorStages`. Tooltip: 'Pre-comp phase rotator (#2887). 0=off, 4=broadcast default.' |
## Tips

- If the **Gain-reduction bar** never moves, the input level is not crossing the threshold. Lower the Thresh knob or raise your microphone gain.
- If the **Gain-reduction bar** is pegged at or near 20 dB continuously, the ratio or threshold is set very aggressively. Raise the Thresh value or lower the Ratio knob to ease the compression.
- The envelope ball on the **Transfer curve** rests at the threshold line when no audio is present. During audio, it travels along the curve; a ball sitting in the bent portion of the curve confirms active compression.
- Both the TX and RX tiles update independently. You can monitor both simultaneously if both sub-containers are expanded.
- The transfer curve axis labels use cached static text for improved rendering performance. The cache rebuilds automatically when switching between compact and full display modes.
- To enter a precise value, click the displayed value text. The inline editor accepts numeric input with locale-aware decimal separators. Use negative signs where appropriate (e.g., "-24.0" for threshold).
- The transfer curve and gain-reduction bar colors adapt to the active theme. The curve uses the `color.accent.dim` theme color, the ball glow uses `color.accent.warning`, and the grid uses `color.background.1`.
- The Drive knob's auto-makeup follows the broadcast-Optimod model — it pushes more material into the curve AND adds equal gain back, so the user's fixed Makeup knob stays a clean post-everything trim knob.
- Phase rotator default of 4 stages (broadcast standard) uses staggered center frequencies of 300/700/1500/2500 Hz with optional 1000/2000 Hz to cover the speech formant range without bunching.
- The gain-reduction meter and envelope ball animations run at a smooth, efficient refresh rate. The animation timer automatically stops when the signal settles and restarts when audio activity resumes. The display repaints only when necessary — either when the smoother reaches a settled state or when the current value warrants a visual update.

## Troubleshooting

- **The tile appears dimmed** — The compressor stage is bypassed. The tile now renders at approximately 55 % opacity when the stage is disabled, matching the dim effect used on the EQ curve. Enable the stage from the CHAIN widget (single-click the COMP stage) or see [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- **The Gain-reduction bar shows no movement during audio** — The input level is not reaching the threshold. Reduce the Thresh knob value or check that the correct audio device is active and producing signal.
- **The envelope ball does not move** — The applet is not connected to an active audio engine. Verify the radio is connected and audio is flowing through the relevant TX or RX processing chain.
- **Inline editor does not appear** — Click directly on the numeric value text below each knob. The editor only appears when clicking the value, not the knob body itself.

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Set compression ratio for voice (TX) or for received audio (RX AGC-C)](set-compression-ratio-for-voice-tx-or-for-received-audio-rx-agc-c.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)