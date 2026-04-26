# Click the spectrum to activate a panadapter (multi-slice mode)

When multiple panadapters are open, only one is active at a time. Clicking the spectrum area of a panadapter makes it the active one, directing tune and scroll input to that panadapter.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The panadapter display requires an active radio connection.
- At least two panadapters must be open. In single-panadapter mode, the activation click has no visible effect and the title bar buttons described below are hidden.

## Steps

1. Open AetherSDR with multiple panadapters visible in the main window.
2. Locate the panadapter you want to make active.
3. Click anywhere on the Spectrum / waterfall area of that panadapter.

The panadapter is now active. Subsequent drag gestures tune the VFO and scroll gestures zoom the spectrum on that panadapter.

## What each control does

| Control | Kind | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|---|
| Slice title | Indicator | Slice A | Slice A–Slice H | — | Shows which slice is bound to this panadapter. |
| Spectrum / waterfall | Drag handle | — | — | — | Click activates the panadapter; drag to tune, scroll to zoom. |
| ⬈ / ↩ (pop-out/dock) | Push button | — | — | — | Pops the panadapter into a floating window or docks it back. Hidden in single-pan mode. |
| □ (maximize) | Push button | — | — | — | Maximizes this panadapter in a multi-pan layout. Hidden in single-pan mode. |
| × (close) | Push button | — | — | — | Closes this panadapter. Hidden in single-pan mode. |

## Tips

- In multi-pan layouts the ⬈ / ↩, □, and × buttons in the title bar only appear once more than one panadapter is open. If you do not see them, you are in single-pan mode.
- To tune by single-clicking the spectrum rather than double-clicking, enable `View > Single-Click to Tune`.

## Related

- [Panadapter overview](overview.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
