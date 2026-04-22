# Pop a panadapter out into its own window

Popping a panadapter into a floating window lets you move it to a second monitor or resize it independently from the main AetherSDR layout.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio. The pop-out button is not available without a radio connection.
- You must have more than one panadapter open. The ⬈ / ↩ button is hidden in single-pan mode.

## Steps

1. Locate the title bar at the top of the panadapter you want to pop out. It shows the slice name (for example, "Slice A") and a row of small buttons on the right.
2. Click the **⬈** button in that title bar. The panadapter detaches and opens in a separate floating window.
3. Resize or move the floating window using standard OS window controls.
4. To dock the panadapter back into the main window, click the **↩** button in the floating window's title bar.

## What each control does

| Control | Behavior | Default | Notes |
|---|---|---|---|
| **⬈ / ↩** (pop-out/dock) | Pops the panadapter into a floating window (⬈), or docks it back into the main layout (↩). | — | Hidden when only one panadapter is open. |
| **□** (maximize) | Maximizes this panadapter to fill the main area in a multi-pan layout. | — | Hidden when only one panadapter is open. |
| **×** (close) | Closes this panadapter. | — | Hidden when only one panadapter is open. |
| Slice title | Indicates which slice is bound to this panadapter (Slice A through Slice H). | Slice A | Read-only indicator. |

## Tips

- The ⬈ and ↩ buttons share the same position in the title bar; the icon changes depending on whether the panadapter is currently docked or floating.
- If you want to give one panadapter the full main-window area without floating it, use **□** (maximize) instead.

## Related

- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Panadapter overview](overview.md)
