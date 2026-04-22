# Adjust TCI TX gain

This page explains how to set the TCI TX gain in the TCI Server applet. Adjusting this value controls the audio level sent to connected TCI clients for the transmit channel.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The TCI applet requires an active radio connection.
- The TCI Server applet must be visible. If you do not see it, click the TCI tray button on the right sidebar to show it.

## Steps

1. Click the TCI tray button on the right sidebar to open the TCI Server applet.
2. Locate the row labelled **TX:** near the bottom of the applet, above the Port row.
3. Drag the TX gain+meter slider left to decrease gain or right to increase gain. The valid range is 0.0 to 1.0. The default is 0.5.
4. Release the slider. AetherSDR saves the new value to `TciTxGain` immediately.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| TX gain+meter | 0.5 | 0.0–1.0 | `TciTxGain` | Drag to set TCI TX gain. The meter reflects live transmit audio level. The slider position reflects the stored gain value. |
| TX slice indicator | — | — or `Slice <letter>` | — | Shows which slice is currently the TX slice. Updates automatically when the TX slice changes. |

## Tips

- The TX gain+meter doubles as a live level meter. The meter display uses exponential smoothing with a fast attack and slower decay, so brief peaks appear quickly but fall back gradually.
- The slice indicator next to the TX meter shows which slice drives the TX channel. If it reads `—`, no slice is currently assigned as the TX slice.
- `TciTxGain` is persisted by the TCI server. The slider reads this stored value at startup so the display matches the server state.

## Troubleshooting

- **TX meter shows no movement during transmission** — Confirm the TCI server is running (status line reads `:<port> (N clients)` rather than `(stopped)`). Also confirm the TX slice indicator shows a slice letter rather than `—`.
- **Slider resets to 0.5 after restarting AetherSDR** — This indicates `TciTxGain` was not saved. Ensure AetherSDR had sufficient write permissions to its settings storage when you made the change.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Change the TCI port](change-the-tci-port.md)
