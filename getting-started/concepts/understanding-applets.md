# Understanding the AetherSDR Applet Panel

The applet panel is a dockable region of the AetherSDR window that groups the controls you use most during an operating session. This page explains what the applet panel is, how it is organized, and how to show, hide, or reposition it.

## Before you start

- AetherSDR must be installed and running.
- No radio connection is required to explore the panel layout, but most controls become active only when connected to a FLEX-8600.

## What the applet panel is

The applet panel sits on the right side of the main window. It contains a set of individual applets — compact control widgets for functions such as receive, transmit, TCI, and others. Each applet is represented by a tray button (for example, RX, TX, TCI) that toggles the applet's expanded view.

The panel can be docked inside the main window or floated as a separate window. Its applets can be reordered by dragging, and the order can be restored at any time.

## Steps

### Show or hide the applet panel

1. Click `View` in the menu bar.
2. Click `Applet Panel` to toggle the panel on or off. A check mark indicates the panel is visible.

### Float the applet panel into its own window

1. Click `View` in the menu bar.
2. Click `Pop Out Applet Panel`, or press `Ctrl+Shift+S`. The panel detaches from the main window.
3. To dock it again, repeat the same action.

### Reset the applet order to default

1. Click `View` in the menu bar.
2. Click `Reset Applet Order`. The applets return to their default sequence.

## What each control does

| Control | Location | What it does |
|---|---|---|
| `Applet Panel` | `View > Applet Panel` | Toggles visibility of the applet panel. |
| `Pop Out Applet Panel` | `View > Pop Out Applet Panel` | Floats the panel into a separate window or docks it back. Shortcut: `Ctrl+Shift+S`. |
| `Reset Applet Order` | `View > Reset Applet Order` | Restores the applets to their default order. |
| Tray buttons (RX, TX, TCI, etc.) | Applet panel | Each button expands or collapses its corresponding applet. |

## Tips

- If the applet panel disappears after resizing the window, check that `View > Applet Panel` has a check mark next to it.
- Floating the panel with `Pop Out Applet Panel` is useful on multi-monitor setups where you want to move controls to a second screen while keeping the panadapter on the primary display.
- If you have rearranged applets and want to return to a known state, `View > Reset Applet Order` restores the default layout without affecting any other settings.

## Related

- [Enable Applet Panel](../../reference/menu-actions/enable-applet-panel.md)
- [Enable Pop Out Applet Panel](../../reference/menu-actions/enable-pop-out-applet-panel.md)
- [Reset Applet Order](../../reference/menu-actions/reset-applet-order.md)
- [Enable Minimal Mode](../../reference/menu-actions/enable-minimal-mode.md)
