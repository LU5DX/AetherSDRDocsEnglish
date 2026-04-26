# Click the spectrum to activate a panadapter (multi-slice mode)

In a multi-panadapter layout, only one panadapter is active at a time. Clicking the spectrum area of an inactive panadapter brings it into focus so that your controls, slices, and tuning apply to it.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- At least two panadapters must be open. In single-panadapter mode, the title bar buttons (⬈, □, ×) are hidden and there is nothing to switch between.

## Steps

1. Locate the panadapter you want to activate. Its title bar shows the slice it is bound to (for example, "Slice B").
2. Click anywhere on the Spectrum / waterfall area of that panadapter.
3. The panadapter is now active. Tuning, scroll-to-zoom, and all slice controls apply to it.

## What each control does

| Control | Kind | Default | Range | Persisted key |
|---|---|---|---|---|
| Slice title | Indicator | Slice A | Slice A – Slice H | — |
| Spectrum / waterfall | Click / drag area | — | — | — |
| ⬈ / ↩ (pop-out/dock) | Push button | — | — | — |
| □ (maximize) | Push button | — | — | — |
| × (close) | Push button | — | — | — |
| Sens | Slider | 30 | 0 – 100 | `CwDecoderSensitivity` |

The ⬈ / ↩, □, and × buttons are hidden in single-panadapter mode. They appear only when more than one panadapter is open.

## Tips

- Drag on the Spectrum / waterfall area to tune the slice frequency. Scroll to zoom the span.
- To give one panadapter more screen space without closing others, click □ (maximize) in its title bar. See [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md).
- To move a panadapter to a separate window, click ⬈ (pop-out). See [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md).

## Related

- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
