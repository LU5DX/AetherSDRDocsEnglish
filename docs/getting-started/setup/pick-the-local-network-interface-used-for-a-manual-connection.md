# Pick the local network interface used for a manual connection

When connecting by IP across a VPN or routed network, AetherSDR needs to know which local network interface (NIC) to use as the source of outgoing traffic. This page explains how to select that interface using the **Advanced: Source path** control on the Manual connection page.

## Before you start

- You must be using the **Connect by IP** connection mode. The **Advanced: Source path** control is not available in Local or Remote with SmartLink modes.
- You need to know which network interface on your computer reaches the radio. If you are unsure, check your operating system's network settings or use `Settings > Network...` to open network diagnostics.
- Have the radio's IP address ready to enter in **Radio IP address**.

## Steps

1. Open the **Connect to a Radio** panel. If a radio is already connected, go to `Settings > Connect to Radio...`.
2. Click **Connect by IP** in the mode row at the top of the panel.
3. Locate the **Advanced: Source path** combo box near the bottom of the Manual page.
4. Open the **Advanced: Source path** drop-down. The list shows all network interfaces currently detected on your computer.
5. Select the interface that has a path to the radio. For a VPN connection, choose the VPN adapter. For a second physical NIC, choose that NIC's entry.
6. Check the **Source warning label** below the combo box. If it shows a warning such as `<interface> (unavailable, last <address>)`, the previously saved interface is no longer reachable. Select a current interface from the list instead.
7. Enter the radio's IP address in **Radio IP address**.
8. Click **Connect by IP** to start the connection.

## What each control does

| Control | What it does | Persisted setting |
|---|---|---|
| **Advanced: Source path** | Selects the local NIC used as the source address for the manual connection. When set to an explicit interface, AetherSDR binds outgoing traffic to that interface. | `ManualBindSource` |
| **Radio IP address** | The IP address or hostname of the Flex radio to connect to. | `ManualRadioIp` |
| **Use low bandwidth mode** | Enables reduced-rate audio and data streams, useful for slow or high-latency VPN links. | `LowBandwidthMode` |
| **Network Diagnostics** | Opens the network diagnostics panel so you can verify interface reachability without leaving the connection screen. | — |

## Tips

- If you previously connected successfully and the interface has since changed (for example, a VPN was assigned a different adapter), the **Source warning label** will display the last known IPv4 address alongside the unavailable interface name. Pick the correct current interface before attempting to reconnect.
- If none of the interfaces in **Advanced: Source path** lead to the radio, verify that your VPN or routing is active before opening AetherSDR, as interface discovery runs when the panel loads.

## Troubleshooting

- **Source warning label shows the saved interface as unavailable** — The NIC selected during a previous session is no longer present or has no IP address. Open **Advanced: Source path** and choose the interface that is currently active on your system.
- **Connection attempt fails immediately after selecting an interface** — The selected interface may not have a route to the radio's subnet. Confirm the routing table on your computer, then retry with the correct interface selected.
- **Advanced: Source path is empty or shows no useful entries** — AetherSDR found no usable network interfaces at startup. Check that your VPN or network adapter is connected and has an assigned IP address, then reopen `Settings > Connect to Radio...` to reload the interface list.

## Related

- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- [Retry discovery when no radios appear](../../features/connection/retry-discovery-when-no-radios-appear.md)
