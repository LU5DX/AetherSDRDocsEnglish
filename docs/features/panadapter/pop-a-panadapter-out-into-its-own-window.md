# Pop a panadapter out into its own window

When you have more than one panadapter open, you can detach any of them into a separate floating window. This is useful for placing the panadapter on a second monitor or resizing it independently from the main AetherSDR layout.

## Before you start

- Connect to a FLEX-8600 radio. The pop-out button is only available when a radio connection is active.
- Open at least one additional panadapter. In single-panadapter mode, the pop-out button is hidden.

## Steps

1. Locate the title bar at the top of the panadapter you want to detach. It shows the slice label (for example, **Slice A**) and a row of small buttons on the right.
2. Click the **⬈** button in that title bar.

   The panadapter detaches into a floating, frameless window.

3. To move the floating window, click and drag the title strip at the top of the floating window.
4. To resize the floating window, drag the size grip in its bottom-right corner.
5. To dock the window back into the main layout, click the **↩** button in the floating window's title bar.

## What each control does

| Control | Description | Default | Notes |
|---|---|---|---|
| **⬈** (pop-out) | Detaches the panadapter into a floating window. | — | Hidden in single-panadapter mode. |
| **↩** (dock) | Returns the floating panadapter to the main layout. | — | Appears in place of ⬈ while the window is floating. |
| **□** (maximize) | Expands this panadapter to fill the main area. | — | Hidden in single-panadapter mode. |
| **×** (close) | Closes this panadapter. | — | Hidden in single-panadapter mode. |
| Slice title | Indicator showing which slice is bound to this panadapter (Slice A through Slice H). | Slice A | Read-only. |

## Tips

- The floating window is frameless. Use the in-app title strip to drag it and the bottom-right size grip to resize it. There is no operating-system window border.
- The ⬈ and ↩ button labels change to reflect the current state: ⬈ when docked, ↩ when floating.

## Troubleshooting

- **The ⬈ button is not visible** — You have only one panadapter open. The pop-out, maximize, and close buttons are all hidden in single-panadapter mode. Open an additional panadapter to make them appear.
- **The floating window cannot be moved** — Click and drag the title strip inside the floating window, not the spectrum area. The spectrum area is used for tuning.

## Related

- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Panadapter overview](overview.md)
