# Adjust TCI TX gain

This page explains how to set the TCI TX gain in the TCI Server applet. Adjusting this value controls the audio level sent to connected TCI clients for the transmit channel.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The TCI Server applet must be visible. If it is not, click the TCI tray button on the right sidebar to show it.

## Steps

1. Click the TCI tray button on the right sidebar to open the TCI Server applet.
2. Locate the row labelled **TX:** in the applet. The slice indicator to its right shows which slice currently drives the TX channel (for example, `Slice A`), or `—` if none is assigned.
3. Drag the **TX gain+meter** slider left or right to decrease or increase the TX gain. The slider also acts as a live level meter, showing transmit audio activity as you operate.
4. Release the slider. The new value is saved automatically to `TciTxGain` and takes effect immediately for all connected TCI clients.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| TX gain+meter | Combined meter and slider. Drag to set the TCI TX gain level. The meter portion reflects live transmit audio. | 0.5 | 0.0–1.0 | `TciTxGain` |
| RX/TX slice-assignment label | Indicator showing which slice drives the TX row. Read-only. | `—` | `—` or `Slice <letter>` | — |

## Tips

- The TX gain+meter displays live audio activity while transmitting. If the meter does not move during transmission, confirm that the correct slice is assigned as the TX slice; the label next to **TX:** will show `—` if no TX slice is assigned.
- The TX gain value persists across restarts. You do not need to re-enter it each session.

## Troubleshooting

- **The TX gain+meter label shows `—` instead of a slice name** — No slice is currently set as the TX slice on the radio. Assign a TX slice in the radio's slice controls, then return to the TCI applet; the label updates automatically.
- **Dragging the slider has no audible effect on the TCI client** — Confirm the TCI server is running (the status line should show `:<port> (N clients)`, not `(stopped)`). Click Enable if the server is not running.

## Related

- [TCI Server overview](overview.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
