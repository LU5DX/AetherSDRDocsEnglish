# Click the spectrum to activate a panadapter (multi-slice mode)

When multiple panadapters are open, only one is active at a time. Clicking the spectrum of an inactive panadapter makes it the active one, directing tuning and slice controls to that panadapter.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- At least two panadapters must be open. In single-panadapter mode there is nothing to activate; the title bar buttons ⬈, □, and × are hidden.

## Steps

1. Locate the panadapter you want to activate. Its title bar shows the slice it is bound to (for example, "Slice A" or "Slice B").
2. Click anywhere on the spectrum or waterfall area of that panadapter.

The panadapter is now active. Tuning, scroll-to-zoom, and slice controls apply to the slice shown in its title bar.

## What each control does

| Control | Kind | Default | Range | Persisted key |
|---|---|---|---|---|
| Spectrum / waterfall | Click / drag | — | — | — |
| Slice title | Indicator | Slice A | Slice A – Slice H | — |
| ⬈ / ↩ (pop-out/dock) | Push button | — | — | — |
| □ (maximize) | Push button | — | — | — |
| × (close) | Push button | — | — | — |
| Sens | Slider | 30 | 0 – 100 | `CwDecoderSensitivity` |

The ⬈, □, and × buttons are hidden in single-panadapter mode and become visible once a second panadapter is open.

## Tips

- Drag on the spectrum to pan the frequency display; scroll to zoom. Both gestures work on the active panadapter only, so click to activate first if needed.
- The slice title in the title bar ("Slice A", "Slice B", etc.) confirms which slice will respond to your controls after you click.

## Related

- [Panadapter overview](overview.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
