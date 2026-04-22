# Set compression ratio for voice

The Ratio knob controls how hard the compressor clamps peaks once the signal crosses the threshold. Raising the ratio produces a more aggressive, consistent level; lowering it gives a gentler, more natural squeeze. Adjust this control to suit your voice and operating style.

## Before you start

- The compressor must be enabled (bypass off). If the COMPRESSOR tile is hidden, enable the Comp stage via the CHAIN widget first. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- The COMPRESSOR sub-container must be visible inside the PooDoo Audio (TXDSP) parent container in the applet panel.

## Steps

1. Locate the COMPRESSOR tile in the applet panel.
2. Find the **Ratio** knob — the second knob in the five-knob row, labeled "Ratio".
3. Click and drag the knob to set the desired ratio. The label beneath the knob updates in the format `X.XX:1` as you turn it.
4. Release the knob. The new value is saved automatically to `ClientCompTxRatio`.
5. Watch the transfer curve above the knob row and the gain-reduction bar update to reflect the new ratio. The envelope ball moves along the steeper or shallower curve segment in real time as you speak.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| **Ratio** | 3.0 | 1.0 to 20.0 (displayed as `X.XX:1`) | `ClientCompTxRatio` |

The knob uses a logarithmic mapping, so small turns at the low end give fine control over gentle ratios (e.g. 1.5:1 to 4:1 for natural voice), while turns at the high end move quickly toward limiting territory (10:1 and above).

## Tips

- A ratio between 2:1 and 4:1 is typical for SSB voice. Higher ratios (8:1 and above) approach limiting behavior and can cause a pumping effect if attack and release are not matched carefully.
- Watch the gain-reduction bar while speaking. The amber fill should reach around the -6 dB tick for moderate compression. If the bar is always empty, the threshold may be set too high for the current ratio to engage. See [Adjust compressor threshold](adjust-compressor-threshold.md).
- After raising the ratio, you will likely need to add make-up gain to restore average output level. See [Apply make-up gain after compression](apply-make-up-gain-after-compression.md).
- For knee and advanced limiter settings (`ClientCompTxKneeDb`, `ClientCompTxLimEnabled`, `ClientCompTxLimCeilingDb`) that are not available on the applet, open the full editor. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).

## Troubleshooting

- **The Ratio knob has no effect on the audio** — The compressor stage may be bypassed. Check that the Comp stage is active in the CHAIN widget. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- **The gain-reduction bar stays empty at high ratios** — The input signal is not crossing the threshold. Lower the Thresh knob (`ClientCompTxThresholdDb`) or increase microphone gain until the envelope ball moves above the threshold line on the transfer curve.
- **The transfer curve does not update after turning the knob** — The COMPRESSOR tile may not be bound to the audio engine yet. Verify the radio is connected and the TX DSP chain is active.

## Related

- [Adjust compressor threshold](adjust-compressor-threshold.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
