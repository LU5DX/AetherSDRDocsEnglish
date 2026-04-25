# Pick the local network interface used for a manual connection

When connecting by IP across a VPN or routed network, AetherSDR lets you choose which local network interface (NIC) your computer uses to reach the radio. This matters when your machine has multiple network interfaces and the default route does not lead to the radio.

## Before you start

- You must know the radio's IP address. See [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md).
- The ConnectionPanel must be visible. It appears automatically before a radio is connected, or open it via `Settings > Connect to Radio...`.

## Steps

1. In the ConnectionPanel, click `Connect by IP` to switch to the Manual mode page.
2. Enter the radio's IP address in the `Radio IP address` field. This value is saved as `ManualRadioIp`.
3. Locate the `Advanced: Source path` combo box below the IP address field.
4. Open the combo box and select the local network interface you want to use for this connection. The selected interface is saved as `ManualBindSource`.
5. If the interface you saved previously is no longer available, a `Source warning label` appears beneath the combo box indicating the saved source is stale or unreachable. Select a currently available interface before proceeding.
6. Click `Connect by IP` to start the connection.

## What each control does

| Control | What it does | Persisted key |
|---|---|---|
| `Radio IP address` | The IP address or hostname of the radio to connect to. | `ManualRadioIp` |
| `Advanced: Source path` | Selects the local NIC that AetherSDR binds to when opening the connection. Leave on the default automatic entry unless you need to force a specific interface. | `ManualBindSource` |
| `Use low bandwidth mode` | Reduces stream data rates for slow or congested links. | `LowBandwidthMode` |
| `Connect by IP` (button) | Starts the manual connection using the IP and source path configured above. | — |

## Tips

- If the previously saved interface is unavailable, the `Source warning label` shows the saved interface name (or ID) and the last known IPv4 address. Choose a different interface from `Advanced: Source path` before connecting.
- On a machine with only one network interface, the `Advanced: Source path` selection has no practical effect. It is most useful on machines with separate wired, wireless, and VPN interfaces.
- If you are on a slow link such as a cellular or satellite connection, enable `Use low bandwidth mode` on the same page before clicking `Connect by IP`.

## Troubleshooting

- **`Source warning label` appears after selecting an interface** — The interface saved in `ManualBindSource` is no longer present or has no active address. Open `Advanced: Source path` and select a currently available interface.
- **Connection fails immediately after clicking `Connect by IP`** — The `Manual result label` below the button shows the error. Verify the IP in `Radio IP address` is reachable from the interface selected in `Advanced: Source path`. Use `Network Diagnostics` on the same page to check reachability.

## Related

- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)
