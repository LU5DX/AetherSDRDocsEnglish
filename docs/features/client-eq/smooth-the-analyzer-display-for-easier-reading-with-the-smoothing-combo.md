# Smooth the analyzer display for easier reading with the Smoothing combo

The Smoothing combo applies fractional-octave power-averaging to the live FFT analyzer trace in the Aetherial Parametric EQ editor. Use it to reduce trace jitter and make broad response trends easier to read while tuning. The setting affects display only — EQ math is unchanged.

## Before you start

- The floating editor must be open. Double-click the EQ stage in the CHAIN widget (TX or RX side) to open it. The editor is titled "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX".
- The Smoothing combo is in the editor header strip. It is not available in the docked applet tile.

## Steps

1. Open the floating editor for either the TX or RX EQ stage by double-clicking the matching EQ stage in the CHAIN widget.
2. Locate the "Smoothing:" label in the editor header strip.
3. Click the combo box to the right of the "Smoothing:" label.
4. Select a smoothing level from the list:
   - `Off (1/96)` — effectively no smoothing (default)
   - `1/24` — light smoothing
   - `1/12` — moderate smoothing
   - `1/6` — heavier smoothing
   - `1/3` — most smoothed
5. The analyzer trace updates immediately.

## What each control does

| Control | Default | Valid values | Persisted setting |
|---|---|---|---|
| Smoothing | `Off (1/96)` | `Off (1/96)` / `1/24` / `1/12` / `1/6` / `1/3` | `ClientEqSmoothingFraction` |

**Smoothing** — Applies fractional-octave power-averaging to the analyzer trace. Lower fraction values produce a smoother trace: `1/3` is the most smoothed; `Off (1/96)` is effectively unsmoothed. The setting is shared between the TX and RX editors — changing it in one editor also affects the other. EQ math and the peak-hold trace are not affected.

## Tips

- The peak-hold trace tracks raw bins regardless of the smoothing setting. If you want to see both the smoothed trend and the raw peaks simultaneously, enable Peak Hold while smoothing is active.
- `1/6` or `1/3` smoothing is useful for comparing your EQ curve against the broad shape of the analyzer fill without fine bin-level noise obscuring the comparison.

## Troubleshooting

- **Smoothing combo is not visible** — The combo is only present in the floating editor, not in the docked "Aetherial TX EQ" or "Aetherial RX EQ" applet tile. Open the editor by double-clicking the EQ stage in the CHAIN widget.
- **Changing smoothing in the TX editor also changes the RX editor** — This is expected. `ClientEqSmoothingFraction` is a single global preference shared between both editors.

## Related

- [Freeze the analyzer peak-hold trace to spot resonances while tuning](freeze-the-analyzer-peak-hold-trace-to-spot-resonances-while-tuning.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
