# Autostart TCI on launch

Enable the autostart option so that AetherSDR starts the TCI WebSocket server automatically each time the application launches, without requiring you to open the TCI applet and click Enable manually.

## Before you start

- AetherSDR must be built with WebSocket support (`HAVE_WEBSOCKETS`). If the `Settings > Autostart TCI with AetherSDR` menu item is absent, your build does not include TCI.
- Confirm the TCI server works manually at least once before enabling autostart. See [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md).
- Decide which port you want the server to use. The default is `50001`. See [Change the TCI port](change-the-tci-port.md).

## Steps

1. Open `Settings > Autostart TCI with AetherSDR`.
2. Click the menu item to place a checkmark next to it. The setting is saved immediately.
3. Restart AetherSDR. The TCI server starts automatically on launch and the server status indicator in the TCI applet changes from `(stopped)` to `:<port> (N clients)`.

To disable autostart, repeat step 1 to remove the checkmark.

## What each control does

| Control | Description | Default | Valid values | Setting key |
|---|---|---|---|---|
| `Settings > Autostart TCI with AetherSDR` | Checkable menu item. When checked, the TCI server starts on every launch without manual intervention. | Off (unchecked) | Checked / unchecked | `AutoStartTCI` |
| Port | The port the TCI server binds to on autostart. Set this in the TCI applet before relying on autostart. | `50001` | 1024–65535 | `TciPort` |
| RX1–RX4 gain | TCI receive gain for each channel, applied when the server starts. | `0.5` | 0.0–1.0 | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| TX gain | TCI transmit gain, applied when the server starts. | `0.5` | 0.0–1.0 | `TciTxGain` |

## Tips

- The TCI applet is hidden by default. Toggle it open with the `TCI` tray button on the right sidebar to verify the server status after AetherSDR launches.
- Gain values (`TciRxGain1`–`TciRxGain4`, `TciTxGain`) and port (`TciPort`) are persisted separately. Configure them before setting up autostart so they are correct from the first automatic start.

## Troubleshooting

- **Menu item `Autostart TCI with AetherSDR` is missing** — This build of AetherSDR was compiled without WebSocket support. TCI is not available.
- **Server status shows `(port in use)` after autostart** — Another application claimed port `TciPort` before AetherSDR finished launching. Change the port in the TCI applet to a free port in the range 1024–65535, then restart AetherSDR. See [Change the TCI port](change-the-tci-port.md).
- **Enable button in the TCI applet appears off after autostart** — A bind failure caused the toggle to snap back to off. Check the server status indicator for `(port in use)` and resolve the port conflict as above.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [TCI Server overview](overview.md)
