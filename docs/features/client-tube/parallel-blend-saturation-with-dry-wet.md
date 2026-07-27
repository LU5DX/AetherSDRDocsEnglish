# Parallel-blend saturation with Dry/Wet

Use the Dry/Wet control to blend the saturated tube signal with the original unprocessed signal. Setting Dry/Wet below 100 % lets you dial in subtle harmonic color without fully replacing the clean signal.

## Before you start

- The Tube stage must be enabled for the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- Open the floating editor for the relevant side: double-click the TUBE stage in the CHAIN widget to open "Aetherial Tube — TX" or "Aetherial Tube — RX".

## Steps

1. Open the floating editor by double-clicking the TUBE stage in the CHAIN widget on the TX or RX side.
2. Locate the **Dry/Wet** knob in the left column of the editor (top knob in that column).
3. Turn **Dry/Wet** toward 0 % to blend in more of the unprocessed signal, or toward 100 % for a fully saturated output.
4. Watch the transfer curve and the **OUT** level meter on the right of the editor as you adjust. Reducing Dry/Wet lowers the contribution of the saturated signal; use **Output** to compensate if overall level changes.

Alternatively, adjust **Mix** directly from the docked applet tile without opening the editor. The **Mix** knob on the tile is the same Dry/Wet control.

### Inline value editing

To enter a precise numeric value for Dry/Wet, click the value display below the knob. A transparent text editor appears, showing the current value. Type the desired value (for example, `67.5`) and press Enter, or click elsewhere to confirm. The value is clamped to the valid range. Press Escape to cancel and revert to the previous value.

The inline editor is also available on all other knobs in the floating editor (Drive, Tone, Bias, Output, Envelope, Attack, Release) and on the docked tile knobs.

## What each control does

| Control                                      | Default                                                                                                                                                                             | Valid range                                                                                                                                                                                               |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dry/Wet** (editor) / **Mix** (docked tile) | 100 %                                                                                                                                                                               | 0 % to 100 % (stored as 0.0 to 1.0)                                                                                                                                                                       |
| **Drive**                                    | 0.00 dB                                                                                                                                                                             | 0.0 to 24.0 dB                                                                                                                                                                                            |
| **Tone**                                     | 0.00                                                                                                                                                                                | -1.0 to 1.0                                                                                                                                                                                               |
| **Bias**                                     | 0 %                                                                                                                                                                                 | 0 % to 100 % (stored as 0.0 to 1.0)                                                                                                                                                                       |
| **Output**                                   | 0.00 dB                                                                                                                                                                             | -24.0 to 12.0 dB                                                                                                                                                                                          |
| **Envelope**                                 | 0 %                                                                                                                                                                                 | -100 % to 100 % (stored as -1.0 to 1.0)                                                                                                                                                                   |
| **Attack**                                   | 5.00 ms                                                                                                                                                                             | 0.1 to 30.0 ms                                                                                                                                                                                            |
| **Release**                                  | 35.00 ms                                                                                                                                                                            | 10.0 to 500.0 ms                                                                                                                                                                                          |
| **RN2**                                      | TX-only toggle (hidden in RX mode). Enables RNNoise neural denoiser on the mic input before the DSP chain. Suppresses background noise before it reaches gate/compressor/saturator. | Located in the floating StripTubePanel below the output level meter, TX side only. Voice modes only — digital modes (RADE, DAX, RTTY, FT8, FDV, CW) bypass this stage. Setting persisted via AudioEngine. |

### Tube character models

Use the **A**, **B**, and **C** toggle buttons in the centre row of the editor to select the tube character model. Only one model can be active at a time.

| Control | Default   | Behavior                                                                 |
|---------|-----------|--------------------------------------------------------------------------|
| **A**   | checked   | Selects tube character Model A. Amber when checked. Exclusive with B and C. |
| **B**   | unchecked | Selects tube character Model B. Amber when checked. Exclusive with A and C. |
| **C**   | unchecked | Selects tube character Model C. Amber when checked. Exclusive with A and B. |

### Knob visual colors

The AetherSDR tube applet controls use theme-aware colors for all knob components. The knob background ring, foreground arc, handle, label text, and value text each read from dedicated theme color keys. The tube applet container (`applet/tube`) may supply per-applet overrides — for example, the tube applet's knob foreground can differ from other applets' knob colors. The transfer curve widget similarly reads its background, frame, grid, axis, curve, ball glow, and ball core colors from the active theme, ensuring consistent visual appearance across all themes.

## Tips

- A Dry/Wet value between 20 % and 50 % is effective for adding warmth on SSB TX without audible distortion artifacts. The dry signal anchors the fundamental while the wet signal contributes harmonics.
- Changes made in the floating editor and on the docked tile stay in sync. A 30 Hz polling timer keeps both views updated automatically.
- If you raise **Drive** for more harmonic density, lowering **Dry/Wet** lets you recover a natural-sounding blend without reducing Drive itself.
- Use inline value editing to restore a previously saved value exactly, or to set a precise blend percentage.

## Troubleshooting

- **Adjusting Dry/Wet has no audible effect** — confirm the Tube stage is enabled. If the stage is bypassed in the CHAIN widget, the signal passes through unprocessed regardless of the Dry/Wet setting. When the stage is bypassed, the entire docked applet tile dims to approximately 55 % opacity as a visual reminder that the stage is inactive.
- **Level changes when moving Dry/Wet** — this is expected. Use the **Output** knob (range −24.0 to 12.0 dB, default 0.00 dB) to trim the post-saturation level. See [Compensate level changes with Output](compensate-level-changes-with-output.md).
- **Inline value edit is rejected or reverts** — verify your input is a number in the valid range (0 to 100). Locale-aware parsing supports comma as decimal separator. Non-numeric characters are stripped automatically.

## Related

- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Monitor output clipping with the level meter in the editor](monitor-output-clipping-with-the-level-meter-in-the-editor.md)