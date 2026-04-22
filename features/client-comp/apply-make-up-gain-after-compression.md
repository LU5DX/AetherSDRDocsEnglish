# Apply make-up gain after compression

Use the Makeup knob to restore loudness lost to compression, so your transmitted signal reaches a consistent level without manually re-adjusting drive.

## Before you start

- The Compressor stage must be enabled (bypass off). See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- The COMPRESSOR sub-container must be visible inside the PooDoo Audio (TXDSP) parent container.

## Steps

1. Locate the five-knob row at the bottom of the COMPRESSOR applet.
2. Find the rightmost knob, labeled **Makeup**.
3. Turn the **Makeup** knob clockwise to add gain, or counter-clockwise to reduce it.
4. Watch the gain-reduction bar while speaking. Aim to compensate for the typical amount of gain reduction shown — the amber strip's −6 dB tick is a useful reference point.
5. Release the knob. The value is saved immediately to `ClientCompTxMakeupDb`.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| Makeup | 0.0 dB | −12.0 to +24.0 dB | `ClientCompTxMakeupDb` |

The label on the knob shows an explicit `+` sign for positive values (for example, `+3.0 dB`) and no sign for negative values (for example, `-2.0 dB`). Makeup gain is applied after compression and after the limiter stage.

## Tips

- Start with **Makeup** at `0.0 dB` and increase it in small steps while watching the gain-reduction bar. If the compressor is reducing by roughly 6 dB on typical voice peaks, adding +6 dB of makeup brings average output back to the uncompressed level.
- If you find yourself adding more than 12–15 dB of makeup, the threshold or ratio may be set too aggressively. See [Adjust compressor threshold](adjust-compressor-threshold.md) and [Set compression ratio for voice](set-compression-ratio-for-voice.md).
- The transfer curve in the applet does not visually reflect makeup gain. Open the full editor to see how makeup interacts with the knee and limiter ceiling. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).

## Troubleshooting

- **Makeup knob has no effect** — Confirm the Compressor stage is active. If the stage is bypassed, the entire DSP chain for the compressor — including makeup — is skipped.
- **Output clips after adding makeup** — The limiter ceiling (`ClientCompTxLimCeilingDb`) may need adjustment. Open the full Compressor editor to enable or adjust the limiter. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).

## Related

- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
- [Adjust compressor threshold](adjust-compressor-threshold.md)
- [Set compression ratio for voice](set-compression-ratio-for-voice.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
