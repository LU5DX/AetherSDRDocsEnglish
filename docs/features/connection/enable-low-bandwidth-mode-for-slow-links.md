# Enable low-bandwidth mode for slow links

Low-bandwidth mode reduces the rate of audio and data streams sent from the radio. Use it when connecting over a slow or congested link — such as a cellular hotspot, a long-distance VPN, or a satellite connection — to reduce dropouts and improve stability.

## Before you start

- AetherSDR must be open and not yet connected to a radio, or you must disconnect first before changing this setting.
- Know which connection mode you are using: Local, SmartLink, or Manual. The `LowBandwidthMode` checkbox is present on the connection panel regardless of mode.

## Steps

1. Open the connection panel. It appears automatically before a radio is connected. If a radio is already connected, click `Settings > Connect to Radio...` and disconnect first.
2. Locate the **Use low bandwidth mode** checkbox near the bottom of the connection panel.
3. Check **Use low bandwidth mode** to enable reduced-rate streams.
4. Proceed to connect using your preferred mode — **On This Network**, **Remote with SmartLink**, or **Connect by IP** — as normal.

## What each control does

| Control | Kind | Default | Persisted key | Behavior |
|---|---|---|---|---|
| Use low bandwidth mode | Checkbox | (not set) | `LowBandwidthMode` | When checked, AetherSDR requests reduced-rate audio and data streams from the radio to suit slow or congested links. |

## Tips

- Enable this setting before initiating the connection. The mode is negotiated at connect time.
- If audio still breaks up after enabling low-bandwidth mode, check your VPN or routing path using `Settings > Network...`.

## Related

- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)
- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Pick the local network interface used for a manual connection](../../getting-started/setup/pick-the-local-network-interface-used-for-a-manual-connection.md)
- [Operating remotely over SmartLink](../../operating/remote/remote-operation-smartlink.md)
