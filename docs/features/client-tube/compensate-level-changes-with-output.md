# Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX)

The AetherSDR client-side dynamic tube saturator adds harmonic richness by shaping the signal through a bias-swept tube model. The system instantiates two independent copies: one for the transmit chain ("Aetherial Mic-PreAmp") and one for the receive chain ("Aetherial Dynamic Tube").

## Opening the tube controls

- **Docked applet tile**: Click "Aetherial Mic-PreAmp" (TX) or "Aetherial Dynamic Tube" (RX) in the applet dock. The compact tile shows a transfer curve with a live input ball and five tuning knobs.
- **Floating editor**: Double-click the TUBE stage in the CHAIN widget, or right-click and select "Open editor". The frameless editor is titled "Aetherial Tube — TX" or "Aetherial Tube — RX" and shows the full nine-knob layout with a tube-character selector and a live output level meter.

## Tube character models

The tube stage offers three exclusive tube character models:

| Button | Default | Behavior |
|---|---|---|
| A | Checked | Selects tube character Model A. Amber when checked. |
| B | Unchecked | Selects tube character Model B. Amber when checked. Exclusive with A and C. |
| C | Unchecked | Selects tube character Model C. Amber when checked. Exclusive with A and B. |

The buttons are part of an exclusive QButtonGroup. The selected model is persisted in `ClientTubeTxModel` / `ClientTubeRxModel` as an integer (0, 1, or 2).

## Inline value editing

You can now click a knob's value display to enter text mode:

1. **Click the value text** below any knob to open an inline editor. The editor appears as a dark rectangle with a cyan border.
2. **Type a new value** and press Enter to apply it. The value is clamped to the knob's valid range.
3. **Click elsewhere** or press Tab to commit the value.
4. **Press Escape** to cancel the edit and revert to the previous value.

The inline editor supports locale-aware decimal parsing, so values like "12,5" work in comma-decimal locales. You can also include unit text — the parser strips non-numeric characters automatically.

## Knob controls

The docked applet tile shows five knobs in a row: Drive, Tone, Bias, Output, Dry/Wet. The floating editor adds four more knobs in a right column: Envelope, Attack, Release, and the Model selector buttons.

Knob colors (ring background, arc, pointer, label, and value text) follow the current theme. The tube saturator's knob foreground uses the `color.accent.dim` theme color, while label and value text use `color.text.secondary` and `color.text.primary` respectively. The tube applet container is registered under `applet/tube` for theme customization.

### Drive

- **Label format**: `X.XX dB`
- **Default**: 0.00 dB
- **Valid range**: 0.0 to 24.0 dB
- **Setting key (TX)**: `ClientTubeTxDriveDb`
- **Setting key (RX)**: `ClientTubeRxDriveDb`

Linear mapping. Pushes more signal into the tube stage. Left column of the editor.

### Tone

- **Label format**: `X.XX`
- **Default**: 0.00
- **Valid range**: -1.0 to 1.0
- **Setting key (TX)**: `ClientTubeTxTone`
- **Setting key (RX)**: `ClientTubeRxTone`

Linear mapping. Negative values darken the saturated signal; positive values brighten it. Centre row of the editor, left of the Model selector.

### Bias

- **Label format**: Percentage (e.g., `50 %`)
- **Default**: 0 %
- **Valid range**: 0.0 to 1.0
- **Setting key (TX)**: `ClientTubeTxBias`
- **Setting key (RX)**: `ClientTubeRxBias`

Linear mapping. Shifts the operating point on the transfer curve, changing the harmonic mix. Centre row of the editor, right of the Model selector.

### Output

- **Label format**: `X.XX dB`
- **Default**: 0.00 dB
- **Valid range**: -24.0 to 12.0 dB
- **Setting key (TX)**: `ClientTubeTxOutputDb`
- **Setting key (RX)**: `ClientTubeRxOutputDb`

Post-tube make-up/trim gain. Left column of the editor.

### Dry/Wet

- **Label format**: Percentage (e.g., `100 %`)
- **Default**: 100 %
- **Valid range**: 0.0 to 1.0
- **Setting key (TX)**: `ClientTubeTxDryWet`
- **Setting key (RX)**: `ClientTubeRxDryWet`

Linear mapping. Dry/wet blend (100 % = fully saturated signal). Left column of the editor (top knob).

### Envelope

- **Label format**: Signed percentage (e.g., `+25 %`, `-50 %`)
- **Default**: 0 %
- **Valid range**: -1.0 to 1.0
- **Setting key (TX)**: `ClientTubeTxEnvelope`
- **Setting key (RX)**: `ClientTubeRxEnvelope`

Linear mapping (-1.0 to +1.0). Positive values increase drive on transients (the tube gets hotter on loud peaks); negative values reduce it, compressing harmonics dynamically. Right column of the editor.

### Attack

- **Label format**: `X.XX ms` (below 10 ms), `X.X ms` (above 10 ms)
- **Default**: 5.00 ms
- **Valid range**: 0.1 to 30.0 ms
- **Setting key (TX)**: `ClientTubeTxAttackMs`
- **Setting key (RX)**: `ClientTubeRxAttackMs`

Exponential mapping (0.1 * 300^n). Sets how quickly the envelope follower responds to rising levels when Envelope ≠ 0. Right column of the editor.

### Release

- **Label format**: `X.XX ms` (below 100 ms), `X.X ms` (above 100 ms)
- **Default**: 35.00 ms
- **Valid range**: 10.0 to 500.0 ms
- **Setting key (TX)**: `ClientTubeTxReleaseMs`
- **Setting key (RX)**: `ClientTubeRxReleaseMs`

Exponential mapping (10 * 50^n). Sets how quickly the envelope follower recovers after levels drop when Envelope ≠ 0. Right column of the editor.

## Transfer curve display

The compact-mode ClientTubeCurveWidget draws the currently-configured tube transfer curve with a live ball at the input level. The curve widget uses theme-aware colors:

| Element | Theme key |
|---|---|
| Background | `color.background.0` |
| Frame | `color.background.1` |
| Grid lines | `color.background.1` |
| Axes | `color.background.1` |
| Curve | `color.accent.dim` (cyan) |
| Ball glow | `color.accent.warning` |
| Ball core | `color.text.primary` |

The ball moves along the curve as the input level changes, visualising the saturation regime.

## Output level meter

The floating editor includes an **OUT** peak level meter (the `ClientLevelMeter` widget) positioned at the far right of the editor panel. It shows the post-saturation peak level with fast-attack and slow-release ballistics and uses the following colour bands:

| Colour | Level range |
|---|---|
| Green | −60 to −12 dB |
| Lime | −12 to −6 dB |
| Amber | −6 to −3 dB |
| Red | Above −3 dB |

The meter is only visible in the floating editor, not in the docked applet tile. It updates continuously alongside the knob controls whenever the floating editor is open.

## RN2 (TX-only noise reduction)

The TX-only floating editor includes an **RN2** toggle button located below the output level meter. This control enables the RNNoise neural denoiser on the mic input before the DSP chain, suppressing background noise before it reaches the gate, compressor, or saturator.

- The RN2 toggle is hidden in RX mode.
- Available only in voice modes. Digital modes (RADE, DAX, RTTY, FT8, FDV, CW) bypass this stage.
- The setting is persisted via the AudioEngine.

## Bypass dim

When the tube stage is bypassed, the entire docked applet tile renders at reduced opacity (approximately 55 % of normal). This matches the dim effect used on the EQ curve tile and gives a clear at-a-glance indication that the stage is not processing audio. The tile returns to full opacity as soon as the stage is re-enabled.

## Tips

- If raising Drive increases loudness more than desired, reduce Output by a matching amount to keep the net level consistent.
- Use the **OUT** meter in the floating editor to verify that the post-tube signal stays below −3 dB (red) under normal operating conditions.
- Changes made in the floating editor and the docked applet stay in sync. A 30 Hz polling timer keeps both views updated, so adjusting any control in one location is reflected immediately in the other.
- Click any knob's value display in the floating editor to type an exact value instead of dragging the knob.
- When the applet tile appears dimmed, the tube stage is bypassed. Re-enable it before making adjustments, otherwise the controls have no effect on the live signal.
- Enable RN2 on the TX tab to reduce background noise before it reaches the tube saturation stage.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)