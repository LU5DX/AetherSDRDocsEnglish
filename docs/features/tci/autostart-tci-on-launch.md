# Autostart TCI on launch

Configure AetherSDR to start the TCI server automatically each time the application launches, so third-party software such as Log4OM or SunSDR tools connects without manual intervention.

## Before you start

- AetherSDR must be built with WebSocket support (`HAVE_WEBSOCKETS`). If the `Settings > Autostart TCI with AetherSDR` menu item is absent, your build does not include TCI.
- Confirm the TCI server works manually before enabling autostart. See [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md).
- A radio connection is required for the TCI server to operate after launch.

## Steps

1. Open the `Settings` menu.
2. Click `Autostart TCI with AetherSDR`. A check mark appears next to the item when it is active.
3. Restart AetherSDR. The TCI server starts automatically on the port stored in `TciPort` (default `50001`).

To disable autostart, repeat steps 1–2. The check mark is removed and the server will no longer start on launch.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| `Autostart TCI with AetherSDR` menu item | Off (unchecked) | On / Off | `AutoStartTCI` |
| Port field | `50001` | 1024–65535 | `TciPort` |
| RX1 gain | 0.5 | 0.0–1.0 | `TciRxGain1` |
| RX2 gain | 0.5 | 0.0–1.0 | `TciRxGain2` |
| RX3 gain | 0.5 | 0.0–1.0 | `TciRxGain3` |
| RX4 gain | 0.5 | 0.0–1.0 | `TciRxGain4` |
| TX gain | 0.5 | 0.0–1.0 | `TciTxGain` |

## Tips

- Autostart uses whatever port is saved in `TciPort` at the time of launch. Set the correct port before enabling autostart to avoid having to change it later. See [Change the TCI port](change-the-tci-port.md).
- If the saved port is already in use when AetherSDR starts, the server will not bind. The TCI applet status indicator will show `(port in use)` in red and the `Enable` button will be off. Change the port and click `Enable` manually.
- Gain values (`TciRxGain1`–`TciRxGain4`, `TciTxGain`) are saved independently of autostart. They persist across restarts regardless of whether autostart is enabled.

## Troubleshooting

- **`Autostart TCI with AetherSDR` is not in the Settings menu** — This build of AetherSDR does not include WebSocket support. TCI is not available.
- **Server does not start after launch despite autostart being enabled** — The radio connection had not been established before the autostart attempt, or the configured port was in use. Open the TCI applet via the `TCI` tray button and check the status indicator. Correct the port if needed, then click `Enable`.
- **Status shows `(port in use)` on launch** — Another application is bound to `TciPort`. Change the port in the TCI applet Port field to a free port in the range 1024–65535 and click `Enable`. Update `TciPort` before the next restart.

## Related

- [TCI Server overview](overview.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
