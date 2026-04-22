# Adjust Compressor Threshold

Use the Thresh knob to set the input level above which the compressor begins reducing gain. Lowering the threshold means more of your voice signal is compressed; raising it lets quieter passages pass through unaffected.

## Before you start

- The Compressor stage must be enabled (bypass off). If the COMPRESSOR tile is hidden, enable the stage via the CHAIN widget or the floating Compressor editor. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- The COMPRESSOR sub-container must be visible inside the PooDoo Audio (TXDSP) parent container in the applet panel.

## Steps

1. Locate the COMPRESSOR sub-container in the applet panel.
2. Find the knob labelled **Thresh** in the five-knob row at the bottom of the tile.
3. Click and drag the **Thresh** knob up to raise the threshold or down to lower it. The label beneath the knob updates in real time and shows the current value in dB (for example, `-18.0 dB`).
4. Watch the transfer curve above the knob row. The knee point on the curve moves as you adjust the threshold, showing where compression will begin.
5. Speak into the microphone and observe the envelope ball on the transfer curve. When the ball rides above the knee, the compressor is active. The gain-reduction bar lights amber to confirm gain is being reduced.
6. Release the knob when the threshold is set where you want it. The value is saved automatically to `ClientCompTxThresholdDb`.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| **Thresh** | -18.0 dB | -60.0 to 0.0 dB | `ClientCompTxThresholdDb` |
| **Ratio** | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` |
| **Attack** | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` |
| **Release** | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` |
| **Makeup** | +0.0 dB | -12.0 to 24.0 dB | `ClientCompTxMakeupDb` |

The **Transfer curve** is a view-only indicator in the applet. It draws the static input/output curve and shows a live ball at the current envelope level. To edit the knee and limiter settings not exposed in the applet, open the floating editor.

The **Gain-reduction bar** is a horizontal amber strip that fills from the right. The scale runs from 0 to 20 dB of reduction. A tick mark at −6 dB indicates a typical working amount of gain reduction.

## Tips

- Start with the default threshold of -18.0 dB and lower it in small steps while speaking. Stop when the gain-reduction bar shows roughly 6 dB of reduction during normal speech peaks.
- If you lower the threshold significantly, add makeup gain with the **Makeup** knob to compensate for the average level reduction.
- The knee and limiter ceiling are not adjustable from the applet. Open the full editor to access those controls.

## Troubleshooting

- **The Thresh knob is visible but the gain-reduction bar never lights up** — The Compressor stage may be bypassed. Check the CHAIN widget and confirm the Compressor stage is enabled. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- **The COMPRESSOR tile is not visible in the applet panel** — The tile is hidden until the Compressor stage is enabled. Enable the stage from the CHAIN widget or the floating Compressor editor.

## Related

- [Compressor overview](overview.md)
- [Set compression ratio for voice](set-compression-ratio-for-voice.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
