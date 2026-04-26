# Pop a panadapter out into its own window

This page explains how to detach a panadapter from the main window so it floats in its own window. This is useful when you have multiple monitors and want to place the spectrum display independently.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The pop-out button is only available when a radio connection is active.
- You must be in multi-slice mode. The ⬈ button is hidden in single-pan mode.

## Steps

1. In the main window, locate the thin title bar at the top of the panadapter you want to pop out. It shows the slice name (for example, "Slice A") and a row of small buttons on the right.
2. Click the **⬈** button on that panadapter's title bar. The tooltip reads "Pop out panadapter".
3. The panadapter detaches and opens in a separate floating window. The **⬈** button changes to **↩**.
4. Drag the floating window by its title bar to position it on any monitor.
5. To dock the panadapter back into the main window, click the **↩** button in the floating window's title bar.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| ⬈ / ↩ (pop-out/dock) | Button | Pops the panadapter into a floating window when docked; docks it back when floating. Hidden in single-pan mode. |
| □ (maximize) | Button | Maximizes this panadapter within a multi-pan layout. Hidden in single-pan mode. |
| × (close) | Button | Closes this panadapter. Hidden in single-pan mode. |
| Slice title | Indicator | Shows which slice is bound to this panadapter (Slice A through Slice H). |

## Tips

- The floating window retains its full title bar with ⬈ / ↩, □, and × buttons, so you can dock, maximize, or close it from the floating position.
- Dragging the title bar of the floating window moves the window; this does not affect the radio's slice assignment.

## Related

- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Panadapter overview](overview.md)
