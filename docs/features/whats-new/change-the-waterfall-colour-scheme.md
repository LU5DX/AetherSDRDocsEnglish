# Change the waterfall colour scheme

The Spectrum / Waterfall widget renders a scrolling waterfall for each panadapter and lets you choose from five colour palettes to map signal intensity to colour. Your choice is saved separately for each panadapter.

## Steps

1. In the panadapter, locate the **Waterfall colour scheme** drop-down.
2. Select one of the available options: **Default**, **Grayscale**, **Blue-Green**, **Fire**, or **Plasma**. The waterfall updates immediately.

## What each control does

| Control | Behavior |
|---|---|
| Waterfall colour scheme | Changes the gradient palette used to map signal intensity to waterfall colour. Persisted per-panadapter. Defaults to **Default** (index 0). Valid options: `0` = Default, `1` = Grayscale, `2` = Blue-Green, `3` = Fire, `4` = Plasma. |

## Tips

- If you open a saved panadapter and the colour scheme looks wrong, the stored index is automatically clamped to the valid range, so it will fall back to the nearest valid option rather than error.
- Each panadapter stores its own colour scheme independently — changing one does not affect others.

## Related

- [spectrum-waterfall-overview.md](spectrum-waterfall-overview.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
