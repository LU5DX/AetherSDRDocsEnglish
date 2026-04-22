# Enable low-bandwidth mode for slow links

Low-bandwidth mode reduces the data rate of audio and panadapter streams from the radio. Use it when connecting over a slow or congested link — such as a cellular connection, a low-speed VPN, or satellite internet — where full-rate streams would cause audio dropouts or connection instability.

## Before you start

- The "Connect to a Radio" panel must be visible. If AetherSDR is already connected to a radio, disconnect first.
- Low-bandwidth mode applies at connection time. You must enable it before clicking a connect button.

## Steps

1. Open the connection panel. If it is not already visible, click `Settings > Connect to Radio...`.
2. Select the connection mode you intend to use: click `On This Network`, `Remote with SmartLink`, or `Connect by IP`. The `Use low bandwidth mode` checkbox is available across all three modes.
3. Check `Use low bandwidth mode`.
4. Proceed to connect normally — click `Connect Selected Radio`, `Connect Remote Radio`, or `Connect by IP` depending on your chosen mode.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| `Use low bandwidth mode` | Checkbox | Enables reduced-rate audio and panadapter streams for the connection. | `LowBandwidthMode` |

## Tips

- The setting is persisted. Once checked, `Use low bandwidth mode` remains enabled for future sessions until you uncheck it.
- If you are on a fast local LAN, leave this option unchecked. Reduced-rate streams lower audio quality and panadapter update speed unnecessarily.

## Troubleshooting

- **Audio dropouts persist even with low-bandwidth mode on** — The link may be too slow or too lossy even for reduced-rate streams. Check your VPN or network path with `Settings > Network...`.

## Related

- [Connect to a local LAN radio](../../getting-started/setup/connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)
- [Pick the local network interface used for a manual connection](../../getting-started/setup/pick-the-local-network-interface-used-for-a-manual-connection.md)
