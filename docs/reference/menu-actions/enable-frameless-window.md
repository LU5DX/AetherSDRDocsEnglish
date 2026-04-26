# Enable Frameless Window

`View > Frameless Window` toggles the custom frameless window style for the AetherSDR main window. When enabled, AetherSDR manages its own title bar, giving you a consistent look across desktop environments and precise control over window chrome.

## Before you start

- AetherSDR must be running.
- Frameless Window is on by default in v0.9.0. If you have upgraded from an earlier version, it is forced on once automatically.

## Steps

1. Click `View` in the menu bar.
2. Click `Frameless Window`. A checkmark next to the item indicates it is on.

Alternatively, press `Ctrl+Shift+F` to toggle the setting without opening the menu.

## What each control does

| Control | Description | Default | Persisted key |
|---|---|---|---|
| `View > Frameless Window` | Toggles `Qt::FramelessWindowHint` on the main window. When on, the native OS window decorations are removed and replaced with AetherSDR's own 20px title bar. | On | `FramelessWindow` |

**When Frameless Window is on:**

- A 20px custom title bar appears at the top of the window. Drag it to move the window.
- Double-click the title bar to maximize or restore the window.
- Minimize, maximize, and close buttons appear in the title bar.
- A resize grip appears in the bottom-right corner of the window.

**When Frameless Window is off:**

- The native OS window decorations are restored.
- The custom title bar and bottom-right resize grip are hidden.

## Tips

- If your desktop environment or window manager conflicts with AetherSDR's custom title bar (for example, double title bars or missing window controls), turn Frameless Window off to fall back to native decorations.
- The setting persists across restarts via `FramelessWindow`.

## Troubleshooting

- **Two title bars visible** — Your window manager is drawing its own title bar on top of AetherSDR's. Go to `View > Frameless Window` and confirm the checkmark is present. If the issue persists, check your window manager's settings for overriding client-side decorations.
- **Window cannot be moved or resized after turning Frameless Window off** — The native title bar may not have appeared yet. Try minimizing and restoring the window so the window manager redraws its decorations.

## Related

- [Configure UI Scale](configure-ui-scale.md)
- [Enable Minimal Mode](enable-minimal-mode.md)
