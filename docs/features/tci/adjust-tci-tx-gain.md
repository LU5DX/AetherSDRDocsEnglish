# Adjust TCI TX gain

Use this page to set the gain applied to the transmit audio stream that AetherSDR's TCI server sends to connected clients. Adjusting TX gain lets you match the signal level expected by your digital-mode or logging software without touching the radio's main TX settings.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The TCI server must be running (Enable toggled on). The TX gain slider is present regardless, but has no effect on audio until the server is active and a client is connected.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Locate the **TX:** row. The slice assignment indicator to the right of the label shows which slice is currently driving TX (for example, `Slice A`), or `—` if no TX slice is assigned.
3. Drag the **TX gain+meter** slider left to decrease gain or right to increase gain. The valid range is `0.0` to `1.0`; the default is `0.5`.
4. Release the slider. AetherSDR saves the new value immediately to `TciTxGain`.

## What each control does

| Control | Description | Default | Range | Persisted key |
|---|---|---|---|---|
| TX gain+meter | Combined level meter and gain slider for the TCI TX channel. Drag to set gain; the meter shows live TX audio level. | `0.5` | `0.0`–`1.0` | `TciTxGain` |
| TX slice indicator | Read-only label showing which slice drives TX (`Slice A`, `Slice B`, etc.) or `—` if none. | `—` | `—` or `Slice <letter>` | — |

## Tips

- The meter shows a smoothed live level of the TX audio reaching the TCI server. Use it to confirm audio is flowing before adjusting gain.
- The slider position is restored from `TciTxGain` each time AetherSDR starts, so your setting persists across sessions.

## Troubleshooting

- **TX slice indicator shows `—`** — No slice has TX assigned on the radio. Assign a TX slice in your radio's slice controls; the label updates automatically.
- **Dragging the slider has no audible effect on the client** — Confirm the TCI server is running (server status shows `:<port> (N clients)`, not `(stopped)`). If status shows `(port in use)`, see [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md).

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Change the TCI port](change-the-tci-port.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
