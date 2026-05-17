# Autostart TCI on launch

Configure AetherSDR to start the TCI WebSocket server automatically every time the application launches, so third-party software such as Log4OM or SunSDR tools connects without manual intervention.

## Before you start

- AetherSDR must be built with WebSocket support (`HAVE_WEBSOCKETS`). If the TCI tray button is absent, this build does not include TCI.
- The radio must be connected before the TCI server can serve clients, though the autostart setting can be configured while disconnected.
- Decide which port the server should use. The default is `50001`. See [Change the TCI port](change-the-tci-port.md) if you need a different port before enabling autostart.

## Steps

1. Click `Settings > Autostart TCI with AetherSDR`.
2. Confirm the item is checked. AetherSDR will now start the TCI server on every subsequent launch.
3. To verify the setting took effect immediately, click the TCI tray button on the right sidebar to open the TCI Server applet. The server status should read `:<port> (0 clients)` rather than `(stopped)`.

To disable autostart, click `Settings > Autostart TCI with AetherSDR` again to uncheck it.

## What each control does

| Control                                                         | Default                                              | Valid range                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Settings > Autostart TCI with AetherSDR` (checkable menu item) | Off                                                  | On / Off                                                                                                                                                                                                                                                            |
| Port                                                            | `50001`                                              | 1024–65535                                                                                                                                                                                                                                                          |
| Enable (toggle button in TCI Server applet)                     | Off                                                  | On / Off                                                                                                                                                                                                                                                            |
| RX1–RX4 gain+meter                                              | 0.5                                                  | 0.0–1.0                                                                                                                                                                                                                                                             |
| TX gain+meter                                                   | Drags set the TCI TX gain and emit tciTxGainChanged. | TciServer::setTxGain persists TciTxGain internally; UI mirrors the stored value. TCI TX audio is always allowed regardless of platform or hosted-DAX availability (evaluateDaxTxPolicy now unconditionally allows DaxTxRequestReason::TciTxAudio, v0.9.5.1, #2276). |
| RX/TX slice-assignment labels                                   | — (em dash)                                          | — or Slice letter                                                                                                                                                                                                                                                   |

### RX/TX slice-assignment labels

The RX1–RX4 and TX status labels show which slice currently drives each channel. The slice letter is now rendered as rich text (HTML) so that styled slice identifiers from `SliceLabel::richText` display correctly. The labels update automatically when slice assignments change.

## Tips

- Enabling autostart also sets `AutoStartTCI` to `True`. Toggling Enable in the TCI Server applet writes the same key, so both controls stay in sync.
- If the port is already in use at launch, the server will not start: the Enable toggle snaps back to off and the status shows `(port in use)`. Change the port and restart AetherSDR, or clear the conflicting process.
- Out-of-range port values snap back to `50001` automatically.

## Troubleshooting

- **`Settings > Autostart TCI with AetherSDR` is absent from the menu** — This build of AetherSDR does not include WebSocket support. TCI is unavailable.
- **Server status shows `(port in use)` after launch** — Another process is already bound to the configured port. Change the port in the TCI Server applet's Port field, save, and restart AetherSDR. See [Change the TCI port](change-the-tci-port.md).
- **Status stays `(stopped)` despite autostart being enabled** — The radio is not yet connected. The TCI server requires a radio connection. Connect to the radio; the server will start once the connection is established.
- **Slice labels appear as raw HTML** — This indicates an older build without the rich-text fix. Update to v26.5.2.1 or later to ensure HTML-rendered slice letters display correctly (#2606).

## Related

- [TCI Server overview](overview.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)