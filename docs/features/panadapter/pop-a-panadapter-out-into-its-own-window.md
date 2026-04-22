# Pop a panadapter out into its own window

Pop out a panadapter to give it a dedicated floating window — useful when you want to move the spectrum display to a second monitor or keep it visible while working in another application.

## Before you start

- AetherSDR must be connected to the radio. The pop-out controls are not available without an active radio connection.
- You must be in multi-slice mode. The ⬈, □, and × title bar buttons are hidden when only one panadapter is present.

## Steps

1. Locate the thin title bar at the top of the panadapter you want to pop out. It shows the slice name (for example, "Slice A") and the drag grip on the left.
2. Click the **⬈** button on the right side of that title bar. The panadapter detaches into a floating window.
3. Drag or resize the floating window as needed using the OS window controls.
4. To dock it back, click the **↩** button that now appears in the same position on the floating window's title bar.

## What each control does

| Control | Behavior | Default | Notes |
|---|---|---|---|
| **⬈** (pop-out) | Detaches the panadapter into a floating window. | — | Visible only in multi-slice mode. |
| **↩** (dock) | Returns the floating panadapter to the main window. | — | Replaces ⬈ while the panadapter is floating. |
| **□** (maximize) | Maximizes this panadapter to fill the main area. | — | Visible only in multi-slice mode. |
| **×** (close) | Closes this panadapter. | — | Visible only in multi-slice mode. |
| Slice title | Indicates which slice is bound to this panadapter (Slice A through Slice H). | Slice A | Read-only indicator. |

## Tips

- The drag grip (⋮⋮) at the left of the title bar does not trigger pop-out; use the **⬈** button specifically.
- You can maximize a different panadapter with **□** while another is already floating.

## Related

- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
