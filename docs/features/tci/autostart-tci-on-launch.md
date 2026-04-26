# Autostart TCI on launch

This page explains how to make AetherSDR start the TCI server automatically every time the application launches, so you do not need to enable it manually after each restart.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The TCI applet requires an active radio connection.
- Decide which port the TCI server should use. The default is `50001`. If you need a different port, set it before enabling autostart. See [Change the TCI port](change-the-tci-port.md).

## Steps

1. Open the TCI applet by clicking the **TCI** tray button on the right sidebar. If the applet panel is not visible, enable it via `View > Applet Panel`.
2. Click `Settings > Autostart TCI with AetherSDR`.
   A checkmark appears next to the menu item. AetherSDR saves `AutoStartTCI` = `True` and will start the TCI server on every subsequent launch.
3. To confirm the setting is active, quit and relaunch AetherSDR. The TCI server status indicator in the applet should show `:<port> (0 clients)` rather than `(stopped)`.

To turn autostart off, click `Settings > Autostart TCI with AetherSDR` again to remove the checkmark.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| `Settings > Autostart TCI with AetherSDR` | Off (unchecked) | On / Off | `AutoStartTCI` | When checked, starts the TCI server on launch at the saved port. |
| Port field | `50001` | 1024–65535 | `TciPort` | Sets the port the server binds to. Values outside the valid range snap to `50001`. Changing the port while the server is running restarts it automatically. |
| Enable | Off | On / Off | — | Starts or stops the TCI server immediately. Toggling this also updates `AutoStartTCI`. If the port is already in use, the button snaps back to off and the status shows `(port in use)`. |

## Tips

- Enabling autostart via the menu and clicking Enable in the applet both write `AutoStartTCI`. If you enable the server by clicking Enable in the applet, autostart is also set, meaning the next launch will start the server automatically.
- If the server fails to bind on launch (port in use), the status indicator turns red and shows `(port in use)`. Change the port and re-enable.

## Troubleshooting

- **Status shows `(stopped)` after relaunch despite autostart being checked** — Another application may have taken the port before AetherSDR started. Change the port in the Port field to a free port (1024–65535), then re-enable autostart.
- **`Settings > Autostart TCI with AetherSDR` is not present in the menu** — This build of AetherSDR was compiled without WebSocket support. TCI features are not available.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [TCI Server overview](overview.md)
