# Change NR2 noise power estimator (OSMS/MMSE/NSTAT)

The NR2 noise power estimator (NPE) controls how AetherSDR's NR2 engine measures the background noise floor before applying gain reduction. Switching between OSMS, MMSE, and NSTAT changes how the estimator tracks noise, which affects suppression quality on stationary versus rapidly changing noise sources.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- NR2 must be active on a receiver for changes to take audible effect immediately.

## Steps

1. Open `Settings > AetherDSP Settings...`.
2. Click the **NR2** tab.
3. In the **NPE Method** group, select one of the three radio buttons: **OSMS**, **MMSE**, or **NSTAT**.

The setting takes effect immediately and is saved automatically to `NR2NpeMethod`.

## What each control does

| Control                        | Kind                                                                                                        | Default                                                                                                        |
|--------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Gain Method**                | Radio button (Linear, Log, Gamma, Trained)                                                                  | Gamma                                                                                                          |
| **NPE Method** — **OSMS**      | Radio button                                                                                                | Default (0)                                                                                                    |
| **NPE Method** — **MMSE**      | Radio button                                                                                                | —                                                                                                              |
| **NPE Method** — **NSTAT**     | Radio button                                                                                                | —                                                                                                              |
| **AE Filter (artifact elimination)** | Checkbox                                                                                              | True                                                                                                           |
| Reduction:                     | Slider, 0.50–2.00                                                                                           | 1.50                                                                                                           |
| Smoothing:                     | Slider, 0.50–0.98                                                                                           | 0.85                                                                                                           |
| Threshold:                     | Slider, 0.05–0.50                                                                                           | 0.20                                                                                                           |
| Reset Defaults (↺ icon)        | Restores NR2 defaults (Gamma/OSMS/AE on, 1.50/0.85/0.20).                                                   | Rendered as a flat icon button showing anticlockwise arrow (U+21BA).                                           |
| Title bar — AetherDSP Settings | Frameless 18 px gradient title bar with grip glyph (⋮⋮) on the left and the dialog title.                   | Matching the chrome family of NetworkDiagnosticsDialog and AetherialAudioStrip. Added in v0.9.8 (#2425 refit). |
| — (Minimize)                   | Minimizes the dialog.                                                                                       |                                                                                                                |
| □ (Maximize)                   | Maximizes or restores the dialog.                                                                           |                                                                                                                |
| × (Close)                      | Closes the dialog.                                                                                          |                                                                                                                |
| NR4 (tab)                      | Selects the NR4 (libspecbleach) page.                                                                       |                                                                                                                |
| Noise Estimation:              | Radio button (MMSE, Brandt, Martin)                                                                         | MMSE                                                                                                           |
| Adaptive Noise Estimation      | Checkbox                                                                                                    | True                                                                                                           |
| Reduction (dB):                | Slider, 0.0–40.0                                                                                            | 10.0                                                                                                           |
| Smoothing (%):                 | Slider, 0–100                                                                                               | 0                                                                                                              |
| Whitening (%):                 | Slider, 0–100                                                                                               | 0                                                                                                              |
| Masking Depth:                 | Slider, 0.00–1.00                                                                                           | 0.50                                                                                                           |
| Suppression:                   | Slider, 0.00–1.00                                                                                           | 0.50                                                                                                           |
| Reset Defaults (↺ icon)        | Restores NR4 defaults (MMSE/adaptive on, 10 dB, 0, 0, 0.50, 0.50).                                          | Rendered as a flat icon button showing anticlockwise arrow (U+21BA).                                           |
| MNR (tab)                      | Selects the MNR (macOS MMSE-Wiener) page. MNR toggle is dimmed on Windows/Linux builds — the engine has no backend on those platforms. |                                     |
| Enable MNR (macOS only)        | Checkbox                                                                                                    | Read live from AudioEngine                                                                                     |
| Strength                       | Slider, 0–100                                                                                               | 100                                                                                                            |
| RN2 (tab)                      | Selects the RN2 (RNNoise) page — purely informational, no adjustable parameters.                            |                                                                                                                |
| BNR (tab)                      | Selects the BNR (NVIDIA) page — intensity controlled from overlay menu. BNR toggle is dimmed on builds without the NVIDIA Broadcast SDK. |                                                                                                |
| DFNR (tab)                     | Selects the DeepFilterNet3 page.                                                                            |                                                                                                                |
| Attenuation Limit              | Slider, 0–100 dB                                                                                            | 100                                                                                                            |
| Post-Filter Beta               | Slider, 0.00–0.30                                                                                           | 0.00                                                                                                           |
| Drag-to-move                   | Click and drag the title bar to move the dialog.                                                            | Double-click the title bar to toggle maximize/restore.                                                         |
| 8-axis resize                  | Click and drag any edge or corner of the dialog to resize. Cursor changes to indicate the resize direction. | 6 px resize hit zone around the inner content widget.                                                          |

`NR2NpeMethod` is stored as an integer: OSMS = 0, MMSE = 1, NSTAT = 2.

## Notes

- The six DSP toggles (NR2, NR4, MNR, DFNR, RN2, BNR) act as exclusive selectors and engine enable/disable controls. When NR2 is activated, AudioEngine cascades exclusion, disabling DFNR and other mutually exclusive modules.
- The dialog now uses `PersistentDialog`, which automatically saves and restores its geometry across sessions. The dialog position and size are persisted using the `AetherDspDialogGeometry` setting key.

## Tips

- OSMS is the default and works well for steady background noise such as atmospheric hiss or white noise from the receiver itself.
- NSTAT is the better starting point when the noise floor changes rapidly, for example during a contest with varying band conditions or intermittent interference.
- If changing the NPE method introduces more musical noise artifacts, enable **AE Filter (artifact elimination)** on the same tab.
- Click **Reset Defaults** on the NR2 tab to return to OSMS along with all other NR2 parameters at once.

## Troubleshooting

- **Changing the NPE method produces no audible difference** — Confirm NR2 is enabled on the receiver. The AetherDSP Settings dialog adjusts parameters but does not itself activate NR2; NR2 must be switched on from the receiver controls.
- **NSTAT introduces more residual noise than OSMS** — NSTAT trades floor accuracy for faster adaptation. Reduce **Reduction:** or increase **Smoothing:** on the NR2 tab to compensate.

## Related

- [Tune NR2 reduction depth and voice threshold](tune-nr2-reduction-depth-and-voice-threshold.md)
- [Switch NR2 gain method between Linear, Log, Gamma and Trained](switch-nr2-gain-method-between-linear-log-gamma-and-trained.md)
- [Reset NR2 or NR4 parameters to defaults](reset-nr2-or-nr4-parameters-to-defaults.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)