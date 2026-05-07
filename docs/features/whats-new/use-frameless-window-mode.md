# Use frameless window mode

The AetherSDR title bar provides built-in window controls (minimize, maximize/restore, and close) when the application runs in frameless-window mode, replacing the native OS window frame.

## Before you start

- Frameless-window mode must be enabled in your AetherSDR installation. The window controls only appear when the OS window frame has been removed.

## Steps

1. Confirm the application is running in frameless-window mode — the **— (minimize)**, **□ (maximize/restore)**, and **✕ (close)** buttons are visible at the right end of the title bar.
2. Use the window controls as needed:
   - Click **—** to minimize the main window.
   - Click **□** to maximize the window; click **❐** to restore it to normal size.
   - Click **✕** to close the application.
3. To move the window, click and drag any empty area of the title bar (the drag-handle areas show an open-hand cursor when you hover over them).

## What each control does

| Control | Behavior |
|---|---|
| **AetherSDR vX.Y.Z** | Displays the running application version. Clicking does nothing. |
| **Radio heartbeat** | Flashes green when a discovery packet arrives; turns solid amber while connecting; blinks red/grey when radio discovery is lost. Right-click to toggle blink on/off. |
| **multiFLEX** | Visible only when other SmartSDR clients share the radio. Click to open the multiFLEX detail dialog. |
| **PC Audio** | Toggles PC microphone audio input on or off. Default: on. Persists across sessions. |
| **🔊 (line out mute)** | Click to mute or unmute line-out speaker audio. Icon changes to 🔇 when muted. |
| **Master volume** | Sets the line-out audio level (0–100). Current value shown in a numeric label to the right. Default: 100. |
| **🎧 (headphone mute)** | Click to mute or unmute headphone audio. Icon changes to 🔇 when muted. |
| **Headphone volume** | Sets the headphone audio level (0–100). Current value shown in a numeric label to the right. Default: 50. |
| **— (minimize)** | Minimizes the main window. Only visible in frameless-window mode. |
| **□ (maximize/restore)** | Toggles between maximized and normal window size. Icon changes to ❐ when maximized. Only visible in frameless-window mode. |
| **✕ (close)** | Closes the application. Only visible in frameless-window mode. |

## Tips

- Drag handles span several areas of the title bar — including the version label, heartbeat indicator, and empty gutters — any area that shows an open-hand cursor can be used to drag the window.
- Right-click the **Radio heartbeat** indicator to disable its blink animation if you find it distracting. The preference is saved as `HeartbeatBlinkEnabled`.

## Related

- [title-bar.md](title-bar.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
