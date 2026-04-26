# Apply make-up gain after compression

After the compressor reduces peaks, the overall signal level drops. The Makeup knob adds back the lost gain so your transmitted audio reaches the intended loudness.

## Before you start

- The Compressor stage must be enabled (bypass off). If it is bypassed, make-up gain has no effect. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- The COMPRESSOR sub-container must be visible inside the PooDoo Audio (TXDSP) parent container.

## Steps

1. Locate the COMPRESSOR sub-container in the applet panel.
2. Find the **Makeup** knob — the rightmost knob in the five-knob row.
3. Turn or click-drag the **Makeup** knob to set the desired gain.
   - Positive values are displayed with an explicit `+` sign, for example `+6.0 dB`.
   - Watch the transfer curve and the gain-reduction bar while speaking to judge how much gain to restore.
4. Release the knob. The value is saved automatically to `ClientCompTxMakeupDb`.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| Makeup | `0.0 dB` | `-12.0 to 24.0 dB` | `ClientCompTxMakeupDb` |

The **Makeup** knob uses a linear mapping. It adds a fixed gain stage after the compressor. Raising it compensates for the average level reduction caused by gain reduction; lowering it below `0.0 dB` can attenuate the post-compressor signal.

## Tips

- Start with the **Makeup** value approximately equal to the typical reading on the gain-reduction bar. If the compressor is pulling back 6 dB on average, try `+6.0 dB` as a starting point, then adjust by ear.
- The gain-reduction bar's tick mark sits at the 6 dB point and gives a quick visual reference for a typical working amount of compression.
- For a more precise match, open the full editor where the knee and limiter ceiling (`ClientCompTxLimCeilingDb`) are also accessible. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).

## Troubleshooting

- **Makeup knob has no effect** — The Compressor stage may be bypassed. Enable it via the CHAIN widget or the floating editor, then adjust Makeup again.
- **Output is too loud after adding make-up gain** — Reduce `ClientCompTxMakeupDb` or enable the limiter and lower `ClientCompTxLimCeilingDb` to prevent clipping. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).

## Related

- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
- [Adjust compressor threshold](adjust-compressor-threshold.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Set compression ratio for voice](set-compression-ratio-for-voice.md)
