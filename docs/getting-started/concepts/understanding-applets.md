# Understanding the AetherSDR Applet Panel

The applet panel is a dockable area on the right side of the AetherSDR window that groups related controls into discrete applets. This page explains what the applet panel is, how it is organized, and how to show, hide, and reposition it.

## Before you start

- AetherSDR must be installed and running.
- You do not need to be connected to a radio to explore the applet panel layout.

## What the applet panel is

The applet panel is a vertical strip of controls docked to the right edge of the main window. Each applet within the panel covers a specific function — for example, slice controls, noise cancellation, or propagation conditions. The panel can be hidden when you want to maximize the panadapter area, or floated into a separate window if you are working with multiple monitors.

The panel contains tray buttons along its top edge. These are compact toggle buttons labeled with their function (for example, RX, TX, TCI). Clicking a tray button shows or hides the corresponding applet within the panel.

## Steps

### Show or hide the applet panel

1. Click `View` in the menu bar.
2. Click `Applet Panel`. A check mark indicates the panel is visible. Clicking again hides it.

### Float the applet panel into its own window

1. Click `View` in the menu bar.
2. Click `Pop Out Applet Panel`, or press `Ctrl+Shift+S`. The panel detaches from the main window and becomes a free-floating window.
3. To dock it again, click `View > Pop Out Applet Panel` again, or press `Ctrl+Shift+S`.

### Reset the applet order

If you have rearranged applets and want to return to the default layout:

1. Click `View` in the menu bar.
2. Click `Reset Applet Order`. The applets return to their default positions within the panel.

## What each control does

| Control | Where | What it does |
|---|---|---|
| `Applet Panel` | `View` menu | Toggles visibility of the applet panel. Checkable. |
| `Pop Out Applet Panel` | `View` menu | Floats the applet panel into a separate window or docks it back. Shortcut: `Ctrl+Shift+S`. Checkable. |
| `Reset Applet Order` | `View` menu | Restores the applet panel to its default applet order. |
| Tray buttons | Top of applet panel | Each button shows or hides one applet inside the panel (for example, RX, TX, TCI). |

## Tips

- If you are running AetherSDR on a small display, use `View > Minimal Mode` (`Ctrl+M`) together with hiding the applet panel to maximize panadapter space.
- When the applet panel is popped out, you can move it to a second monitor independently of the main window.
- If tray buttons or applets appear in an unexpected order after an update, use `View > Reset Applet Order` to restore the defaults.

## Related

- [Enable Applet Panel](../../reference/menu-actions/enable-applet-panel.md)
- [Enable Pop Out Applet Panel](../../reference/menu-actions/enable-pop-out-applet-panel.md)
- [Reset Applet Order](../../reference/menu-actions/reset-applet-order.md)
- [Enable Minimal Mode](../../reference/menu-actions/enable-minimal-mode.md)
- [Understanding slices and VFOs](understanding-slices.md)
