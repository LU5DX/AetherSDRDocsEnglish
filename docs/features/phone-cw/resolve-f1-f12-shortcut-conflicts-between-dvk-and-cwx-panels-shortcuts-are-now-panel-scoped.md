# Resolve F1-F12 shortcut conflicts between DVK and CWX panels (shortcuts are now panel-scoped)

This page explains how F1-F12 keyboard shortcuts are now scoped to the visible panel, so that DVK (Digital Voice Keyer) and CWX (CW Macros) panels no longer fire simultaneously when both are open.

## Before you start

- Both the DVK panel and the CWX panel must be open in the right sidebar applet panel
- The "P/CW" tray button must be visible on the right sidebar

## Steps

1. Click the **P/CW** tray button on the right sidebar to open the Phone/CW applet.
2. The Phone/CW applet automatically switches between its Phone panel (for voice modes) and CW panel (for CW modes) depending on the active slice mode.
3. Press any F1-F12 key — the shortcut only fires for the panel that is currently visible (Phone panel → DVK macros; CW panel → CWX macros).

No configuration is required. The behavior is automatic.

## What each control does

| Control | Behavior |
|---------|----------|
| **P/CW tray button** | Toggles the Phone/CW applet visibility in the right sidebar |
| **Phone/CW applet stacked panel** | Automatically shows Phone controls (voice modes) or CW controls (CW mode); only the visible panel's F1-F12 shortcuts are active |

## Tips

- This behavior was introduced to fix issue #2464/#2469. Previously, having both DVK and CWX panels open caused both sets of F1-F12 macros to fire simultaneously.
- CWX macros automatically release TX when the queue drains (issue #2450/#2507), so you don't need to manually stop transmission after a macro finishes.

## Related

- [Overview](overview.md)
