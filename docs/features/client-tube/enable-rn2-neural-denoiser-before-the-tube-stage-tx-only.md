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

| Control  | Kind          | Default   | Valid Range       | Setting Key              |
|----------|---------------|-----------|-------------------|--------------------------|
| RN2      | Toggle button | Unchecked | —                 | (persisted via AudioEngine) |
| Dry/Wet  | Knob          | 100 %     | 0.0 to 1.0       | `ClientTubeTxDryWet`     |
| Drive    | Knob          | 0.00 dB   | 0.0 to 24.0 dB   | `ClientTubeTxDriveDb`    |
| Tone     | Knob          | 0.00      | -1.0 to 1.0      | `ClientTubeTxTone`       |
| Bias     | Knob          | 0 %       | 0.0 to 1.0       | `ClientTubeTxBias`       |
| Output   | Knob          | 0.00 dB   | -24.0 to 12.0 dB | `ClientTubeTxOutputDb`   |
| Envelope | Knob          | 0 %       | -1.0 to 1.0      | `ClientTubeTxEnvelope`   |
| Attack   | Knob          | 5.00 ms   | 0.1 to 30.0 ms   | `ClientTubeTxAttackMs`   |
| Release  | Knob          | 35.00 ms  | 10.0 to 500.0 ms | `ClientTubeTxReleaseMs`  |
| A        | Toggle button | Checked   | —                | `ClientTubeTxModel`      |
| B        | Toggle button | Unchecked | —                | `ClientTubeTxModel`      |
| C        | Toggle button | Unchecked | —                | `ClientTubeTxModel`      |

## Tube Character Models (A, B, C)

The three tube character models provide different harmonic flavours:

- **Model A** (default): Standard warm tube character.
- **Model B**: Brighter harmonic profile with increased upper harmonics.
- **Model C**: Darker, smoother character with reduced high-frequency harmonics.

Select a model by clicking the corresponding toggle button. Only one model can be active at a time. The selected model affects the shape of the transfer curve displayed in the Tube curve widget.

## Envelope Follower Controls

When Envelope is set to a non-zero value, the Attack and Release knobs control the dynamics of the envelope follower:

- **Attack**: Controls how quickly the envelope follower responds to rising signal levels. Shorter attack times (0.1 ms) provide faster response to transients.
- **Release**: Controls how quickly the envelope follower recovers after signal levels drop. Longer release times (up to 500 ms) sustain the effect longer.

These controls only have an effect when Envelope is not at 0%.

## Tips

- Enable RN2 first, then adjust Drive and Bias on the Tube. The denoiser removes noise before saturation, so you can use more Tube drive without amplifying background hiss.
- If you switch to a digital mode (RADE, DAX, RTTY, FT8, FDV, CW), the RN2 stage is automatically bypassed. The button remains in its current state and will reactivate when you return to a voice mode.
- The RN2 toggle appears only in the TX editor. The RX Tube editor ("Aetherial Dynamic Tube") does not have an RN2 control.
- Use the Dry/Wet control to blend the processed signal with the original. At 100% (default), the signal is fully processed. Lower values mix in unprocessed signal for a more subtle effect.
- The Envelope control allows dynamic tube character changes. Positive values emphasize transients for a punchier sound; negative values compress harmonics for a smoother, more consistent tone.

## Troubleshooting

- **RN2 button is missing** — Open the TX Tube editor (double-click TUBE in the CHAIN widget on the TX side). The button appears below the output level meter, TX side only.
- **Denoiser seems to have no effect** — Verify you are in a voice mode (SSB, AM, FM). RN2 is bypassed in digital modes. Also check that the Tube stage itself is not bypassed (the applet tile should be at full opacity, not dimmed).
- **Background noise still audible after enabling RN2** — The denoiser suppresses steady background noise but may not remove sudden impulse noises. For best results, position your microphone close to your mouth and reduce gain at the source where possible.
- **Tube character buttons not working** — Ensure only one model (A, B, or C) is selected at a time. The buttons are mutually exclusive.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Select a tube character (Model A, B, or C) to change harmonic flavour](select-a-tube-character-model-a-b-or-c-to-change-harmonic-flavour.md)
- [Shift Bias to tweak the harmonic balance](shift-bias-to-tweak-the-harmonic-balance.md)