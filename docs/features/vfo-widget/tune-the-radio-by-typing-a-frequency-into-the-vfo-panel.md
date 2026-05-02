# Tune the radio by typing a frequency into the VFO panel

Direct frequency entry lets you jump to an exact frequency without clicking around the panadapter. Type a value in MHz into the VFO panel's frequency display and press Enter.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio.
- The VFO panel for the target slice must be open. If it is not visible, click the VFO marker flag for that slice on the spectrum display.

## Steps

1. Click the **Frequency display** once. The display enters direct entry mode.
2. Type the desired frequency in MHz.
3. Press **Enter** or **Tab** to apply. The slice retunes immediately.

## What each control does

| Control | Behavior | Default | Persisted key |
|---|---|---|---|
| **Frequency display** | Shows the current slice frequency. Click once to begin direct entry; type MHz and press Enter or Tab to apply. Scroll the mouse wheel over the display to step-tune up or down by the current step size. | — | — |
| **Collapse toggle** | Collapses the VFO panel to a compact frequency-only strip. In collapsed mode, scrolling anywhere on the strip tunes by the current step size. | Expanded | `SliceFlagCollapsed_{N}` |

## Tips

- If the panel is collapsed to the frequency-only strip, click anywhere on it to expand it so the **Frequency display** is accessible for direct entry.
- The scroll wheel also tunes the slice when the pointer is over the **Frequency display**, stepping by the slice's current step size. On macOS, inertial scroll events are ignored to prevent unintended tuning after a gesture ends.

## Troubleshooting

- **Typing has no effect** — Check that the slice is not locked. A locked slice ignores tune commands. Unlock it before entering a frequency.
- **The VFO panel is not visible** — Click the VFO marker flag for the desired slice on the spectrum display to open the panel.

## Related

- [VFO Panel overview](overview.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- [Change mode from the VFO panel](change-mode-from-the-vfo-panel.md)
- [Enable RIT or XIT offset from the VFO panel](enable-rit-or-xit-offset-from-the-vfo-panel.md)
