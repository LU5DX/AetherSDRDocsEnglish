# Collapse the VFO panel to frequency-only view

When screen space is limited, you can collapse the VFO panel to a compact strip that shows only the slice frequency. The collapsed state is saved per slice so it persists across sessions.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires a live radio connection.
- The VFO panel for the slice must be open. If it is not visible, click the VFO marker flag on the spectrum display for that slice.

## Steps

1. Locate the slice badge in the header area of the VFO panel. The badge shows the slice identifier (for example, **A** or **B**).
2. Click the slice badge. The panel collapses to a compact frequency-only strip.
3. To restore the full panel, click anywhere on the collapsed strip.

## What each control does

| Control | Default | Persisted setting |
|---|---|---|
| Collapse toggle | Expanded | `SliceFlagCollapsed_{N}` |

The `SliceFlagCollapsed_{N}` setting is stored per slice, where `{N}` is the slice number. Collapsing one slice does not affect other slices.

## Tips

- In collapsed view, scrolling the mouse wheel over the strip tunes the slice frequency by the current step size — the same as scrolling over the frequency display in the full panel.
- In collapsed view, clicking the TX badge painted on the strip toggles the TX assignment for that slice. Clicking anywhere else on the strip expands the panel.
- The panel flips to the right side of the VFO marker automatically if expanding it would be clipped by the window edge. This behavior applies in both expanded and collapsed states.

## Related

- [VFO Panel overview](overview.md)
- [Tune the radio by typing a frequency into the VFO panel](tune-the-radio-by-typing-a-frequency-into-the-vfo-panel.md)
- [Change the VFO marker line thickness](change-the-vfo-marker-line-thickness.md)
- [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md)
