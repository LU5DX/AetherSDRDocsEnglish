# Full AppSettings Key Reference

This page lists every persisted AppSettings key in AetherSDR, the UI control or menu item that writes it, and where to find that control. Use it when troubleshooting configuration files, scripting deployments, or understanding what a setting does behind the menu label.

## Before you start

- No connection to a radio is required to read or understand these settings.
- Settings are persisted locally on your machine. Changing a radio profile on the radio itself does not alter these keys.

## What each control does

The table below covers every key surfaced in the supplied catalog. Keys are sorted by the menu or dialog where they appear.

### Settings menu

| AppSettings key | Menu item / control | What it does | Notes |
|---|---|---|---|
| `AutoStartRigctld` | `Settings > Autostart rigctld with AetherSDR` | When checked, spawns the rigctld CAT server automatically each time AetherSDR launches. | — |
| `AutoStartCAT` | `Settings > Autostart CAT with AetherSDR` | When checked, creates virtual serial ports for CAT control on launch. | Linux and macOS only. |
| `AutoStartTCI` | `Settings > Autostart TCI with AetherSDR` | When checked, starts the TCI server automatically on launch. | Requires WebSockets build. |
| `AutoStartDAX` | `Settings > Autostart DAX with AetherSDR` | When checked, enables the DAX audio bridge on launch. | macOS and PipeWire only. |

### View menu

The View menu items listed below write their state as persisted preferences. Specific AppSettings key names for View items are not confirmed in the supplied catalog; do not assume key names for these controls. See the menu directly at `View` for their current state.

| Control | Menu item | What it does |
|---|---|---|
| Applet panel visibility | `View > Applet Panel` | Toggles the right-side applet panel on or off. |
| Applet panel float | `View > Pop Out Applet Panel` | Floats the applet panel into a separate window or docks it back. Shortcut: Ctrl+Shift+S. |
| Single-click tuning | `View > Single-Click to Tune` | When enabled, a single click on the panadapter retunes VFO. Default is double-click. |
| Panadapter tracking | `View > Pan Follows VFO` | When enabled, the panadapter scrolls to keep the VFO visible. On by default. |
| Minimal mode | `View > Minimal Mode` | Hides the title bar and controls to maximize panadapter area. Shortcut: Ctrl+M. |
| Frameless window | `View > Frameless Window` | Hides OS window decoration. Shortcut: Ctrl+Shift+F. |
| Propagation overlay | `View > Propagation Conditions` | Displays a real-time ionospheric propagation forecast overlay on panadapters. |
| Keyboard shortcuts active | `View > Keyboard Shortcuts` | Enables or disables keyboard shortcut processing globally. |
| Status indicator blink | `View > Blink Status Indicator` | Title bar indicator blinks to signal radio heartbeat. On by default. |
| UI scale | `View > UI Scale` | Sets the application UI scale. Options: 75%, 85%, 100%, 110%, 125%, 150%, 175%, 200%. |
| Band plan display | `View > Band Plan` | Controls band plan overlay size. Options: Off, Small (6 pt), Medium (10 pt), Large (12 pt), Huge (16 pt), plus region selector. |

## Tips

- The four `AutoStart*` keys are the most commonly scripted settings. They allow you to control which companion servers start with AetherSDR without opening any dialog.
- `AutoStartCAT` applies only on Linux and macOS. On Windows, use `AutoStartRigctld` for CAT integration via rigctld instead.
- `AutoStartTCI` is only present if AetherSDR was built with WebSocket support. If the menu item `Settings > Autostart TCI with AetherSDR` is absent, the key has no effect even if set manually.

## Troubleshooting

- **A companion server (rigctld, TCI, DAX) does not start at launch** — Check that the corresponding `AutoStart*` key is set by verifying the checkmark is present in the `Settings` menu. If the menu item is missing entirely, your build of AetherSDR does not include support for that feature.
- **`AutoStartCAT` has no effect on Windows** — Virtual serial port CAT is not supported on Windows. Use `Settings > Autostart rigctld with AetherSDR` (`AutoStartRigctld`) instead.
- **UI scale or panel layout resets after update** — These preferences are stored locally. If the settings file is removed or corrupted, all View preferences return to defaults. Reconfigure them from the `View` menu.
