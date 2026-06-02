# Bypass reverb from the chain

Disabling the reverb stage removes the Aetherial FreeVerb processing from the TX audio chain without changing any of the knob values. Use this when you want a dry transmission but intend to re-enable reverb later with the same settings intact.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible in the applet panel.
- The VERB stage must already appear in the CHAIN widget. If the reverb stage has never been enabled, it will not yet be present in the chain.

## Steps

1. Locate the CHAIN widget inside the Aetherial Audio (TXDSP) container in the applet panel.
2. Single-click the VERB stage in the CHAIN widget to toggle it off.

The VERB stage indicator changes to show it is inactive. The "Aetherial FreeVerb — TX" editor hides, and the TX audio path passes through without reverb processing. All five knob values (`ClientReverbTxSize`, `ClientReverbTxDecayS`, `ClientReverbTxDamping`, `ClientReverbTxPreDelayMs`, `ClientReverbTxMix`) are preserved.

To re-enable reverb, single-click the VERB stage again. The editor reappears and processing resumes with the previously saved settings.

## Live reverb visualisation

The Aetherial FreeVerb applet includes a compact live visualisation panel (90 px tall) that updates in real time as you adjust the knobs. It is displayed directly inside the "Aetherial FreeVerb — TX" editor above the knob row and requires no configuration.

The visualisation shows three overlaid elements against a thin dashed-grid background with crosshairs at centre for spatial reference:

| Element | Colour | What it represents |
|---------|--------|--------------------|
| Dry sine packet | Cyan, gradient-faded to transparent rightward | The unprocessed signal. |
| First-order reflections | Yellow, decaying sine bursts | Early reflections. Spacing and amplitude respond to Size and Damp. |
| Reverberant tail | Magenta, exponentially decaying | The full reverb tail. Length follows Decay; high-frequency roll-off follows Damp; onset position follows Pre. |

All five knobs feed the visualisation directly. Changes to Size, Decay, Damp, Pre, or Mix are reflected immediately — you do not need to transmit to see the effect.

## Inline value editing

Each knob supports inline value editing. Instead of dragging the knob, you can click the value label below any knob and type a numeric value directly.

### Steps

1. Locate the "Aetherial FreeVerb — TX" editor by double-clicking the VERB stage in the CHAIN widget.
2. Click the value text below any knob (Size, Decay, Damp, Pre, or Mix).
3. Type the desired numeric value.
4. Press Enter or click elsewhere to commit.

The knob updates to the entered value, clamped to the valid range. If you type an invalid value, the knob reverts to its previous setting.

**Notes:**
- The value editor supports locale-aware decimal separators (e.g., "12,5" in comma-decimal locales).
- While editing, a dark inset background with a cyan border appears to indicate edit mode.
- Press Escape or click outside the editor to cancel without applying changes.
- Mouse wheel events still work while the editor is focused.

## Knob controls

The Aetherial FreeVerb contains five knobs arranged in a single row. Each knob controls a reverb parameter. Knob colours (ring background, ring arc, pointer, label, value) are determined by the current theme's `color.knob.*` and `color.text.*` settings. When the applet is placed inside a container with its own colour override (e.g. an applet/comp with an amber knob foreground), those overrides are applied automatically.

| Control | Label | Default | Valid range | Setting key | Behavior | Notes |
|---------|-------|---------|-------------|-------------|----------|-------|
| Knob | Size | 50 % | 0.0 to 1.0 | `ClientReverbTxSize` | Linear mapping. Sets the modelled room size. | Label displayed as percentage. |
| Knob | Decay | 1.20 s | 0.3 to 5.0 s | `ClientReverbTxDecayS` | Exponential mapping (0.3 * (5.0/0.3)^n, ~16.7x). Sets the reverb tail length. | Label 'X.XX s'. |
| Knob | Damp | 50 % | 0.0 to 1.0 | `ClientReverbTxDamping` | Linear mapping. Higher values damp high frequencies faster in the tail. | Label displayed as percentage. |
| Knob | Pre | 20 ms | 0 to 100 ms | `ClientReverbTxPreDelayMs` | Linear mapping. Pre-delay between the dry signal and the first reflections. | Label 'X ms'. |
| Knob | Mix | 15 % | 0.0 to 1.0 | `ClientReverbTxMix` | Linear mapping. Dry / wet balance. | Label displayed as percentage. |

## Tips

- Bypassing via the CHAIN widget is non-destructive. Your Size, Decay, Damp, Pre, and Mix values are not reset when the stage is disabled.
- To inspect or adjust knob values while reverb is bypassed, double-click the VERB stage to open the floating "Aetherial FreeVerb — TX" editor. Changes made there take effect the next time the stage is enabled.
- Use the live visualisation to set Decay and Mix before going on air. A short Decay (0.3–1.2 s) with a low Mix (10–15 %) keeps voice intelligible.
- Use inline value editing for precise numeric entry instead of dragging the knob.

## Related

- [Aetherial FreeVerb overview](overview.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)