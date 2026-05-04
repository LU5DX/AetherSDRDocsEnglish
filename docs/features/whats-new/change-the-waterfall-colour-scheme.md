# Change the waterfall colour scheme

The Spectrum / Waterfall widget renders a scrolling waterfall for each panadapter and lets you choose from five colour palettes to map signal intensity to colour. The selected scheme is saved separately for each panadapter.

## Steps

1. Open the panadapter whose waterfall you want to change — the Spectrum / Waterfall widget is always visible inside each Panadapter applet.
2. Locate the **Waterfall colour scheme** combo box in the widget controls and select one of the available options: **Default**, **Grayscale**, **Blue-Green**, **Fire**, or **Plasma**.

The waterfall updates immediately and the choice is saved automatically for that panadapter.

## What each control does

| Control | Behavior |
|---|---|
| **Waterfall colour scheme** | Changes the gradient palette used to map signal intensity to waterfall colour. Accepts five options: Default (0), Grayscale (1), Blue-Green (2), Fire (3), Plasma (4). The setting is persisted per-panadapter and clamped to the valid range on load. |

## Tips

- If you run multiple panadapters, set the colour scheme independently on each one — the setting is not shared.
- **Fire** and **Plasma** palettes can make weak signals easier to distinguish from the noise floor on high-contrast displays.

## Related

- [Spectrum / Waterfall overview](spectrum-waterfall.md)
- [Adjust the waterfall level and zoom](waterfall-level-zoom.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
