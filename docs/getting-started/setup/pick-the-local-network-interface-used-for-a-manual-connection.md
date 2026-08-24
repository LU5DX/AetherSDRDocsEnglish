# Pick the local network interface used for a manual connection

When connecting by IP across a VPN or routed network, AetherSDR lets you choose which local network interface (NIC) your computer uses to reach the radio. This matters when your machine has multiple network interfaces and the default route does not lead to the radio.

## Before you start

- You must know the radio's IP address or hostname. See [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md).
- The ConnectionPanel must be visible. It appears automatically before a radio is connected, or open it via `Settings > Connect to Radio...`.

## Steps

1. In the ConnectionPanel, click `Connect by IP` to switch to the Manual mode page.
2. Enter the radio's IP address or hostname in the `Radio IP address` field. This value is saved as `ManualRadioIp`. If you have connected to this radio before, you can open the `Radio IP address` drop-down and select it from the list of recent addresses instead of typing it again.
3. Locate the `Advanced: Source path` combo box below the IP address field.
4. Open the combo box and select the local network interface you want to use for this connection. The selected interface is saved as `ManualBindSource`.
5. If the interface you saved previously is no longer available, a `Source warning label` appears beneath the combo box indicating the saved source is stale or unreachable. Select a currently available interface before proceeding.
6. Click `Connect by IP` to start the connection.

## What each control does

| Control | What it does | Persisted key |
|---|---|---|
| `Radio IP address` | The IP address or hostname of the radio to connect to. Displayed as an editable combo box; the drop-down lists up to three recently used addresses. Hostnames (such as `ic-705.local`) are now remembered alongside numeric IP addresses. | `ManualRadioIp` |
| `Advanced: Source path` | Selects the local NIC that AetherSDR binds to when opening the connection. Leave on the default automatic entry unless you need to force a specific interface. | `ManualBindSource` |
| `Use low bandwidth mode` | Reduces stream data rates for slow or congested links. | `LowBandwidthMode` |
| `Enable adaptive frame-rate throttle` | Automatically reduces FFT/waterfall frame rate when network quality degrades. Useful for slow or intermittent links. Unchecked by default. | `AdaptiveThrottleEnabled` |
| `Connect to last radio on start up` | When checked, AetherSDR auto-connects to the last used radio on startup and on broadcast-discovery / routed-radio probe. When unchecked, the connection dialog opens and the user must pick a radio manually each session. Defaults to checked. | `AutoConnectToLastRadio` |
| `Connect by IP` (button) | Starts the manual connection using the IP and source path configured above. | — |
| `Network Diagnostics` (button) | Opens the Network Diagnostics dialog to help troubleshoot connectivity issues. | — |
| `Source warning label` (indicator) | Warns when the selected source NIC is stale or unreachable. | — |
| `Manual result label` (indicator) | Shows result text after probing a manual IP (success or error). | — |

## Tips

- If the previously saved interface is unavailable, the `Source warning label` shows the saved interface name (or ID) and the last known IPv4 address. Choose a different interface from `Advanced: Source path` before connecting.
- On a machine with only one network interface, the `Advanced: Source path` selection has no practical effect. It is most useful on machines with separate wired, wireless, and VPN interfaces.
- If you are on a slow link such as a cellular or satellite connection, enable `Use low bandwidth mode` on the same page before clicking `Connect by IP`.
- For links with variable latency, enable `Enable adaptive frame-rate throttle`. This reduces FFT and waterfall frame rates when network quality drops, keeping the connection usable.
- The `Radio IP address` field keeps the three most recently used addresses. Select a previous address from the drop-down to avoid retyping it. Hostnames are now remembered alongside numeric IP addresses, so a VPN radio reached by DNS name appears in the recent list just like a numeric address.
- If you uncheck `Connect to last radio on start up`, AetherSDR opens the connection dialog on every launch and waits for you to select a radio manually.
- The local and remote radio lists now have a maximum height of 240 pixels and scroll internally. If you have many discovered radios, scroll within the list to reach entries that are not immediately visible. This prevents the list from growing past the dialog on small displays (e.g., a 1024×600 panel).
- Right-click a discovered local radio to set a custom nickname without connecting first. This is available for non-Flex radios (such as HL2 or simulated radios). Flex radio names are set from Radio Setup while connected.
- The ConnectionPanel preserves its window geometry when toggling frameless mode.

## Troubleshooting

- **`Source warning label` appears after selecting an interface** — The interface saved in `ManualBindSource` is no longer present or has no active address. Open `Advanced: Source path` and select a currently available interface.
- **Connection fails immediately after clicking `Connect by IP`** — The `Manual result label` below the button shows the error. Verify the IP in `Radio IP address` is reachable from the interface selected in `Advanced: Source path`. Use `Network Diagnostics` on the same page to check reachability.
- **A hostname entered in `Radio IP address` is not remembered** — Only conservative hostnames (letters, digits, dot, hyphen, underscore, with alphanumeric ends, up to 253 characters) are saved to the recent list. If the hostname contains other characters, use its numeric IP address instead.

## Related

- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)