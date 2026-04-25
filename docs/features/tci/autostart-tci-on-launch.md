# Autostart TCI on launch

Configure AetherSDR to start the TCI WebSocket server automatically every time the application launches, so third-party software such as Log4OM or SunSDR tools connects without manual intervention.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The TCI server requires an active radio connection.
- Open the TCI Server applet by clicking the TCI tray button on the right sidebar if you want to verify the server state after enabling autostart.

## Steps

1. Click `Settings > Autostart TCI with AetherSDR`.
2. Confirm the menu item shows a check mark. Autostart is now enabled and persisted as `AutoStartTCI`.
3. Restart AetherSDR. The TCI server starts automatically on the port stored in `TciPort` (default: `50001`).
4. In the TCI Server applet, confirm the server status reads `:<port> (0 clients)` or higher once a client connects. The Enable button will appear active.

To disable autostart, click `Settings > Autostart TCI with AetherSDR` again to remove the check mark.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| `Settings > Autostart TCI with AetherSDR` | Checkable menu item. When checked, starts the TCI server on launch. | Off | On / Off | `AutoStartTCI` |
| Port | Port the TCI server listens on. Changing it while the server is running restarts the server. Out-of-range values snap to `50001`. | `50001` | 1024–65535 | `TciPort` |
| Enable | Starts or stops the TCI server manually. Snaps back to off and shows `(port in use)` if the port cannot be bound. | Off | On / Off | — |
| RX1–RX4 gain+meter | Gain slider and level meter for each TCI RX channel. | 0.5 | 0.0–1.0 | `TciRxGain1` – `TciRxGain4` |
| TX gain+meter | Gain slider and level meter for the TCI TX channel. | 0.5 | 0.0–1.0 | `TciTxGain` |

## Tips

- Enabling autostart also sets `AutoStartTCI` to `True` the next time you toggle Enable in the applet directly — the menu item and the Enable button stay in sync.
- If the port is already in use at launch, the server will not start. Change `TciPort` to an available port before restarting.

## Troubleshooting

- **Server status shows `(port in use)` after launch** — Another application is bound to the configured port. Open the TCI Server applet, change Port to an unused value in the range 1024–65535, and restart AetherSDR.
- **Enable snaps back to off after launch** — The bind failed. See the `(port in use)` entry above. `AutoStartTCI` is automatically reset to `False` when a bind failure is detected.
- **`Settings > Autostart TCI with AetherSDR` does not appear** — This feature requires WebSocket support in the AetherSDR build. Contact your distribution source if the menu item is absent.

## Related

- [TCI Server overview](overview.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
