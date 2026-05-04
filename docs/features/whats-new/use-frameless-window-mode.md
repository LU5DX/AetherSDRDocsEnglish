# Use frameless window mode

AetherSDR's frameless window mode removes the operating system title bar and replaces it with built-in window controls in the application's own Title Bar. This gives you minimize, maximize/restore, and close buttons alongside the rest of the Title Bar controls.

## Steps

1. Open AetherSDR. The Title Bar is always visible at the top of the main window.
2. When frameless window mode is active, three window controls appear on the right side of the Title Bar: **— (minimize)**, **□ (maximize/restore)**, and **✕ (close)**. Use these in place of the OS window buttons.
   - Click **—** to minimize the main window.
   - Click **□** to maximize the window; the icon changes to **❐** when maximized. Click again to restore the previous size.
   - Click **✕** to close the application.

## What each control does

| Control | Behavior |
|---|---|
| AetherSDR vX.Y.Z | Displays the running application version. Clicking does nothing. |
| Radio heartbeat | Flashes green when a discovery packet arrives; turns solid amber while connecting; blinks red/grey when radio discovery is lost. Right-click to toggle blink on/off. |
| multiFLEX | Visible only when other SmartSDR clients share the radio. Click to open the multiFLEX detail dialog. |
| PC Audio | Enables or disables PC microphone audio input. Default: on. Persists across sessions. |
| 🔊 (line out mute) | Click to mute or unmute line-out speaker audio. Icon changes to 🔇 when muted. |
| Master volume | Sets the line-out audio level (0–100). Current value shown in a numeric label to the right. Default: 100. |
| 🎧 (headphone mute) | Click to mute or unmute headphone audio. Icon changes to 🔇 when muted. |
| Headphone volume | Sets the headphone audio level (0–100). Current value shown in a numeric label to the right. Default: 50. |
| — (minimize) | Minimizes the main window. Visible only in frameless-window mode. |
| □ (maximize/restore) | Toggles between maximized and normal window size. Icon changes to ❐ when maximized. Visible only in frameless-window mode. |
| ✕ (close) | Closes the application. Visible only in frameless-window mode. |

## Tips

- The version label (**AetherSDR vX.Y.Z**) in the Title Bar always reflects the exact running build. If you do not see a version number, you may be running a build earlier than V0.9.5 where a frameless-window regression hid this label.
- The **Radio heartbeat** blink behavior is persisted via `HeartbeatBlinkEnabled`. If the flashing is distracting, right-click the indicator to turn it off.

## Related

- [title-bar.md](title-bar.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
