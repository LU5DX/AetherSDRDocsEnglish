# Connect by IP across a VPN or routed network

Use the Manual mode to connect to a Flex radio when mDNS discovery cannot reach it — for example, when the radio is on a VPN tunnel or a different routed subnet and you already know its IP address.

## Before you start

- Confirm you can ping the radio's IP address from the computer running AetherSDR.
- Know the radio's IPv4 address (check your VPN gateway, router DHCP table, or the radio's front panel).
- If you have multiple network interfaces (e.g. a VPN adapter and a physical NIC), decide which one should carry the connection.

## Steps

1. Open the connection screen. If no radio is connected, it appears automatically in the main window. If a radio is already connected, go to `Settings > Connect to Radio...`.
2. Click **Connect by IP** in the mode row at the top of the panel. The panel switches to the Manual mode page.
3. In the **Radio IP address** field, type the IPv4 address of the radio.
4. (Optional) If your machine has more than one network interface, open the **Advanced: Source path** drop-down and select the interface that can reach the radio. Leave it on the default automatic entry if you are unsure.
5. (Optional) If your link is slow or has limited bandwidth, check **Use low bandwidth mode**.
6. Click **Connect by IP**.
7. Watch the **Manual result label** below the button. It shows whether the connection attempt succeeded or failed.

## What each control does

| Control | What it does | Persisted setting |
|---|---|---|
| **Connect by IP** mode button | Switches the panel to Manual mode. | `ConnectionMode` |
| **Radio IP address** | The IPv4 address AetherSDR dials directly. | `ManualRadioIp` |
| **Advanced: Source path** | Selects the local network interface (NIC) used for the connection. Leave on automatic unless you have multiple interfaces. | `ManualBindSource` |
| **Use low bandwidth mode** | Reduces stream data rates for slow or high-latency links. | `LowBandwidthMode` |
| **Network Diagnostics** | Opens the network diagnostics dialog to inspect reachability. | — |
| **Connect by IP** (action button) | Starts the connection to the address in **Radio IP address**. | — |

## Tips

- If the **Source warning label** appears, the previously saved interface in **Advanced: Source path** is no longer available. Open the drop-down and choose an active interface, or leave it on automatic.
- If discovery is running and shows **No local radios found yet**, the empty-state screen offers a **Connect by IP** shortcut button that takes you directly to Manual mode.

## Troubleshooting

- **Manual result label shows an error immediately** — The radio is not reachable at the address you entered. Verify the IP address, confirm the VPN tunnel is up, and check that no firewall is blocking port 4992 (SmartSDR TCP) between the two hosts.
- **Source warning label appears on the Manual page** — The NIC saved in `ManualBindSource` is gone or has no IP. Open **Advanced: Source path** and choose a current interface.
- **Connection attempt hangs without a result** — A firewall is silently dropping packets. Use **Network Diagnostics** to examine the path, or check firewall rules on the radio's host network.

## Related

- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)
- [Pick the local network interface used for a manual connection](pick-the-local-network-interface-used-for-a-manual-connection.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- [Connect to a Radio overview](../../features/connection/overview.md)
