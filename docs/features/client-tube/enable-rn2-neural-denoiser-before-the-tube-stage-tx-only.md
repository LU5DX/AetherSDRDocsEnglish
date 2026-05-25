# Enable RN2 neural denoiser before the Tube stage (TX only)

Enable the built-in RNNoise denoiser to suppress background noise on your microphone input before it reaches the Tube saturator, gate, and compressor. This cleans up room noise, fan hum, or breath pops early in the TX DSP chain. RN2 is available on the TX side only and works in voice modes (not digital modes).

## Before you start

- The Tube stage must be enabled in the CHAIN widget on the TX side (single-click the TUBE tile).
- You must be in a voice mode (SSB, AM, FM, etc.). Digital modes (RADE, DAX, RTTY, FT8, FDV, CW) bypass the denoiser automatically.

## Steps

1. Ensure the TX Tube stage is visible in the TXDSP container. If not, click the TX side of the CHAIN widget to toggle the stage on.
2. Double-click the TUBE tile in the CHAIN widget (TX side). The frameless editor opens, titled "Aetherial Tube — TX".
3. In the bottom area of the editor, below the output level meter, locate the RN2 toggle button.
4. Click RN2 to enable it. The button illuminates (amber when checked) to show the denoiser is active.

   > RN2 is a simple on/off toggle. There are no additional controls — the neural model runs at a fixed suppression strength.

5. Speak normally into the microphone. Background noise should be noticeably reduced before the signal enters the Tube saturator and other TX DSP stages.
6. To disable, click RN2 again so the button returns to the unchecked (off) state.

## What each control does

| Control | Kind | Default | Notes |
|---------|------|---------|-------|
| RN2 | Toggle button | Unchecked | Enables the RNNoise neural denoiser on the mic input, before the TX DSP chain (gate, compressor, Tube). Persisted via AudioEngine. |

## Tips

- Enable RN2 first, then adjust Drive and Bias on the Tube. The denoiser removes noise before saturation, so you can use more Tube drive without amplifying background hiss.
- If you switch to a digital mode (RADE, DAX, RTTY, FT8, FDV, CW), the RN2 stage is automatically bypassed. The button remains in its current state and will reactivate when you return to a voice mode.
- The RN2 toggle appears only in the TX editor. The RX Tube editor ("Aetherial Dynamic Tube") does not have an RN2 control.

## Troubleshooting

- **RN2 button is missing** — Open the TX Tube editor (double-click TUBE in the CHAIN widget on the TX side). The button appears below the output level meter, TX side only.
- **Denoiser seems to have no effect** — Verify you are in a voice mode (SSB, AM, FM). RN2 is bypassed in digital modes. Also check that the Tube stage itself is not bypassed (the applet tile should be at full opacity, not dimmed).
- **Background noise still audible after enabling RN2** — The denoiser suppresses steady background noise but may not remove sudden impulse noises. For best results, position your microphone close to your mouth and reduce gain at the source where possible.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Select a tube character (Model A, B, or C) to change harmonic flavour](select-a-tube-character-model-a-b-or-c-to-change-harmonic-flavour.md)
- [Shift Bias to tweak the harmonic balance](shift-bias-to-tweak-the-harmonic-balance.md)
