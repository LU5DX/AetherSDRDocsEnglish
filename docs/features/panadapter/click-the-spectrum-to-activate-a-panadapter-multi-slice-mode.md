# Click the spectrum to activate a panadapter (multi-slice mode)

When multiple panadapters are open, only one is active at a time. Clicking the spectrum area of any panadapter makes it the active one and directs tuning, scrolling, and keyboard input to it.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The panadapter display requires an active radio connection.
- At least one additional panadapter must be present. In single-pan mode the title bar buttons are hidden and only one panadapter exists.

## Steps

1. Locate the panadapter you want to activate. Each panadapter shows a "Slice title" indicator (for example, "Slice A" or "Slice B") in its title bar.
2. Click anywhere on the spectrum or waterfall area of that panadapter.

The click activates the panadapter. Tuning, scroll-to-zoom, and keyboard input now apply to the slice bound to that panadapter.

## What each control does

| Control | Kind | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|---|
| Slice title | Indicator | Slice A | Slice A – Slice H | — | Shows which slice is bound to this panadapter. |
| Spectrum / waterfall | Drag handle | — | — | — | Click activates the panadapter. Drag to tune. Scroll to zoom. |
| ⬈ / ↩ (pop-out/dock) | Push button | — | — | — | Pops the panadapter out into a floating window or docks it back. Hidden in single-pan mode. |
| □ (maximize) | Push button | — | — | — | Maximizes this panadapter in a multi-pan layout. Hidden in single-pan mode. |
| × (close) | Push button | — | — | — | Closes this panadapter. Hidden in single-pan mode. |

## Tips

- In single-pan mode the ⬈, □, and × title bar buttons are hidden. They appear only when more than one panadapter is present.
- If you want a single click to also retune the VFO at that point, enable `View > Single-Click to Tune` before clicking.

## Related

- [Panadapter overview](overview.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
