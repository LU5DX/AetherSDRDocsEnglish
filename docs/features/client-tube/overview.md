# Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview

AetherSDR includes a client-side tube saturation stage that runs on your computer, independent of the radio. Two fully separate instances exist: **Aetherial Mic-PreAmp** shapes your transmitted audio before it reaches the radio, and **Aetherial Dynamic Tube** shapes received audio on the way to your speakers or headphones. Both use the same bias-swept tube model and the same controls; their settings are stored independently.

## Before you start

- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel. The Tube sub-containers are hidden until the Tube stage is enabled via the CHAIN widget on the matching side.
- No radio connection is required to configure the tube controls.

## How it works

Each instance runs its signal through a tube transfer curve model. The curve bends according to Drive, Bias, and the selected tube character model (A, B, or C). A live input ball rides the curve in real time, showing which part of the saturation regime is active at the current signal level.

You can open the full editor for either side by double-clicking the TUBE stage in the CHAIN widget. The floating editor is titled **Aetherial Tube — TX** or **Aetherial Tube — RX**. The docked sub-container tile shows a compact set of knobs and the transfer curve without opening the editor. Changes made in the floating editor and in the docked tile stay in sync automatically.

The floating editor also includes an **OUT** level meter on its far right, showing post-saturation peak level. The meter is not visible in the docked tile.

When a tube stage is bypassed via the CHAIN widget, the entire docked tile renders at reduced opacity (approximately 55 % of normal). This matches the dim effect used by the EQ curve when bypassed and gives a clear at-a-glance indication that the stage is inactive.

To open the docked tile's context menu, right-click the **Aetherial Mic-PreAmp** or **Aetherial Dynamic Tube** sub-container titlebar. From there you can float, pop out, or hide the tile.

## Inline value editing

In v26.5.2.1, every knob throughout the tube applet (and all other AetherSDR applets that use knobs) supports **inline value editing**. This makes it easy to type an exact number instead of turning a knob by eye.

To use inline editing:

1. **Click** any knob's value display (the position where the numeric label normally appears). The label switches to a small text input with a cyan border.
2. **Type** the desired value, using any number format your locale understands — for example, `12.5` or `12,5` (comma as decimal separator). You can also type just the number without the unit (e.g., `15` instead of `15.00 ms`). A trailing unit string such as `dB` or `ms` is ignored.
3. **Press Enter** to commit the value. The knob updates to the nearest valid setting within its range.
4. **Click anywhere else** or **press Tab** to commit the value and close the editor. If you click outside the editor, the value is also applied (commit-on-blur).

To cancel without changing the value, press **Escape**. The editor reverts to the previously stored value.

While the inline editor is active, mouse wheel events still work, so you can fine-tune by scrolling after typing an approximate value.

## What each control does

The table below applies to both the TX and RX instances. Where setting keys differ by side, both are shown. Controls marked **Editor only** are available in the floating editor but not in the docked tile.

| Control        | Behavior description | Default | Valid range | Setting key |
|----------------|----------------------|---------|-------------|-------------|
| Transfer curve | Compact-mode ClientTubeCurveWidget. Draws the currently-configured tube transfer curve with a live ball at the input. | — | — | — |
| Drive          | Linear mapping. Pushes more signal into the tube stage. | 0.00 dB | 0.0 to 24.0 dB | `ClientTubeTxDriveDb` / `ClientTubeRxDriveDb` |
| Tone           | Linear mapping. Negative values darken, positive brighten the saturated signal. | 0.00 | -1.0 to 1.0 | `ClientTubeTxTone` / `ClientTubeRxTone` |
| A              | Selects tube character Model A. Exclusive with B and C. Amber when checked. | checked | — | `ClientTubeTxModel` / `ClientTubeRxModel` |
| B              | Selects tube character Model B. Exclusive with A and C. Amber when checked. | unchecked | — | `ClientTubeTxModel` / `ClientTubeRxModel` |
| C              | Selects tube character Model C. Exclusive with A and B. Amber when checked. | unchecked | — | `ClientTubeTxModel` / `ClientTubeRxModel` |
| Bias           | Linear mapping. Shifts the operating point on the transfer curve, changing the harmonic mix. Label displayed as percentage. | 0 % | 0.0 to 1.0 (displayed as 0 – 100 %) | `ClientTubeTxBias` / `ClientTubeRxBias` |
| Output         | Linear mapping. Post-tube make-up / trim gain. Label 'X.XX dB'. | 0.00 dB | -24.0 to 12.0 dB | `ClientTubeTxOutputDb` / `ClientTubeRxOutputDb` |
| Dry/Wet        | Linear mapping. Dry / wet blend (100 % = fully saturated signal). Label displayed as percentage. | 100 % | 0.0 to 1.0 (displayed as 0 – 100 %) | `ClientTubeTxDryWet` / `ClientTubeRxDryWet` |
| Envelope       | Linear mapping (-1.0 to +1.0). Positive values increase drive on transients; negative values reduce it, compressing harmonics dynamically. Label displayed as signed percentage. | 0 % | -1.0 to 1.0 (displayed as signed percentage) | `ClientTubeTxEnvelope` / `ClientTubeRxEnvelope` |
| Attack         | Exponential mapping (0.1 * 300^n). Sets how quickly the envelope follower responds to rising levels when Envelope ≠ 0. Label 'X.XX ms' below 10 ms, 'X.X ms' above. | 5.00 ms | 0.1 to 30.0 ms | `ClientTubeTxAttackMs` / `ClientTubeRxAttackMs` |
| Release        | Exponential mapping (10 * 50^n). Sets how quickly the envelope follower recovers after levels drop when Envelope ≠ 0. Label 'X.XX ms' below 100 ms, 'X.X ms' above. | 35.00 ms | 10.0 to 500.0 ms | `ClientTubeTxReleaseMs` / `ClientTubeRxReleaseMs` |
| RN2            | TX-only toggle (hidden in RX mode). Enables RNNoise neural denoiser on the mic input before the DSP chain. Suppresses background noise before it reaches gate/compressor/saturator. Located in the floating StripTubePanel below the output level meter, TX side only. Voice modes only — digital modes (RADE, DAX, RTTY, FT8, FDV, CW) bypass this stage. Setting persisted via AudioEngine. | unchecked | — | — |

## Output level meter (editor only)

The floating editor contains an **OUT** level meter on its far right column. It shows the post-saturation peak level using fast-attack / slow-release ballistics. The color bands are:

| Color | Range |
|---|---|
| Green | −60 to −12 dB |
| Lime | −12 to −6 dB |
| Amber | −6 to −3 dB |
| Red | Above −3 dB |

The meter is not present in the docked applet tile.

Bypass for each instance is controlled from the CHAIN widget, not from within the tube tile itself. See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).

## Knob appearance and theme support

In v26.6.1, all knobs in the tube applet (and across AetherSDR) follow the color theme. Their appearance is drawn from five dedicated theme color keys:

| Knob component | Theme key | Example effect |
|----------------|-----------|----------------|
| Background ring | `color.knob.background` | The unlit arc behind the knob arc |
| Foreground arc | `color.knob.foreground` | The arc showing the current value |
| Handle / pointer | `color.knob.handle` | The line pointing to the current value |
| Value text | `color.text.primary` | The numeric value drawn below the knob |
| Label text | `color.text.secondary` | The control name drawn above the knob |

The transfer curve widget also follows the theme:

| Curve element | Theme key | Example effect |
|---------------|-----------|----------------|
| Background | `color.background.0` | The plot area fill |
| Frame / grid | `color.background.1` | The border and grid lines |
| Axis lines | `color.background.1` | Horizontal and vertical axis lines |
| Curve line | `color.accent.dim` | The tubed transfer curve |
| Ball glow | `color.accent.warning` | The glow around the live input ball |
| Ball core | `color.text.primary` | The center dot of the live input ball |

The widget container itself is tagged with the theme container `applet/tube`, which allows per-applet color overrides for the tube's knobs and curve.

## Tips

- Start with Drive at 0.00 dB and raise it slowly until the transfer curve begins to bend visibly. The live input ball shows whether peaks are reaching the saturated region.
- Use Output to bring the processed level back in line with the dry level after adding Drive, so comparisons are level-matched. Watch the OUT meter in the editor to check post-saturation peak levels.
- Set Dry/Wet below 100 % to blend in parallel with the dry signal, which can add body without the full character of full saturation.
- Bias at 0 % produces a symmetrical curve. Raising it introduces asymmetry, shifting the harmonic content toward even-order harmonics.
- Use Model A, B, or C to change the fundamental character of the tube curve before adjusting Drive and Bias.
- Set Envelope to a positive value to make the saturation track transients — loud peaks drive the tube harder automatically. Use Attack and Release to control how quickly the follower reacts and recovers.
- When a tube stage is bypassed, the docked tile dims visibly. If you notice the tile appears faded, check that the stage is enabled in the CHAIN widget before adjusting controls.
- Use inline value editing (click the knob label) to enter exact numbers quickly instead of turning a knob. Press Escape to cancel the edit.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Dry/Wet](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)