# Change the TCI port

The TCI server listens on a configurable port so third-party software can connect to it. Change the port if the default conflicts with another application or if your logging or digital-mode software requires a specific port number.

## Before you start

- The TCI applet must be visible. If it is not, click the TCI tray button on the right sidebar to show it.
- A radio connection must be active.

## Steps

1. Open the TCI applet by clicking the TCI tray button on the right sidebar.
2. Click the Port field (default: `50001`) and type the new port number. Valid values are 1024–65535. Values outside this range snap back to `50001`.
3. Press Enter or Tab to confirm. AetherSDR saves the value to `TciPort` immediately.
4. If the server is already running (Enable is checked), AetherSDR restarts the server on the new port automatically. No further action is needed.
5. If the server is not yet running, click Enable to start it on the new port.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Port | `50001` | 1024–65535 | `TciPort` | Sets the WebSocket port the TCI server binds to. Out-of-range values snap to `50001`. Changing the port while the server is running restarts the server. |
| Enable | Off | On / Off | — | Starts or stops the TCI server. If the port is already in use, the toggle snaps back to off and the status indicator shows `(port in use)` in red. |

## Tips

- The status indicator next to Enable shows `:<port> (N clients)` when the server is running, so you can confirm the new port took effect without opening a terminal.

## Troubleshooting

- **Status shows `(port in use)` and Enable snaps off** — Another application is bound to that port. Choose a different port number, then click Enable again.
- **Port field reverts to `50001` after you type a number** — The value you entered was outside the 1024–65535 range. Enter a value within that range.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
- [TCI Server overview](overview.md)
