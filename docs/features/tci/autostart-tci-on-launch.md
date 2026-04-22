# Autostart TCI on launch

Configure AetherSDR to start the TCI server automatically each time the application launches, so third-party software such as Log4OM or SunSDR tools connects without manual intervention.

## Before you start

- AetherSDR must be built with WebSocket support (`HAVE_WEBSOCKETS`). If the `Settings > Autostart TCI with AetherSDR` menu item is absent, your build does not include TCI.
- Confirm the TCI server works manually before enabling autostart. See [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md).
- Decide which port you want the server to use. The default is `50001`. See [Change the TCI port](change-the-tci-port.md).

## Steps

1. Click `Settings` in the menu bar.
2. Click `Autostart TCI with AetherSDR`.

A checkmark appears next to the item. AetherSDR persists this choice as `AutoStartTCI`.

On the next launch, AetherSDR starts the TCI server on the port stored in `TciPort` before the applet panel is shown. The TCI tray button and the server status indicator in the TCI Server applet reflect the running state automatically.

To disable autostart, repeat steps 1–2. The checkmark clears and the server will no longer start on launch.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| `Autostart TCI with AetherSDR` | Checkable menu item. When checked, the TCI server starts on every launch. | Off | On / Off | `AutoStartTCI` |
| Port | TCP port the server binds to. Set in the TCI Server applet before enabling autostart. | `50001` | 1024–65535 | `TciPort` |
| RX1–RX4 gain | Per-channel TCI receive gain, applied when the server starts. | `0.5` | 0.0–1.0 | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| TX gain | TCI transmit gain, applied when the server starts. | `0.5` | 0.0–1.0 | `TciTxGain` |

## Tips

- Set `TciPort` and gain levels before enabling autostart. Autostart uses whatever values are already persisted.
- The TCI Server applet is hidden by default. Toggle it with the `TCI` tray button on the right sidebar to verify the server status after launch.

## Troubleshooting

- **Menu item `Autostart TCI with AetherSDR` is not visible** — The build does not include WebSocket support. TCI is unavailable in this installation.
- **Server status shows `(port in use)` after autostart** — Another application is already bound to `TciPort`. Open the TCI Server applet, change the Port value to a free port, save it, then relaunch. Out-of-range values snap back to `50001`.
- **Enable button appears off after autostart** — The server failed to bind. The toggle snaps back to off and status shows `(port in use)`. Change the port as above.

## Related

- [TCI Server overview](overview.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
