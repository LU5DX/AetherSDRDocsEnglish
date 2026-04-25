# Connect by IP across a VPN or routed network

Use this method when your FLEX-8600 is on a different subnet from your computer — for example, across a VPN tunnel or a routed station network — and mDNS discovery cannot reach it. You will enter the radio's IP address directly and AetherSDR will open the SmartSDR protocol connection without relying on discovery.

## Before you start

- You must know the radio's IPv4 address on the remote or VPN network.
- The radio must be reachable from your computer (ping it first to confirm routing is working).
- If you are connecting over a slow or metered link, decide in advance whether you want to enable low-bandwidth mode.

## Steps

1. Open the connection screen. It appears automatically before a radio is connected. If a radio is already connected, go to `Settings > Connect to Radio...` or disconnect first.
2. Click **Connect by IP** in the mode button row at the top of the panel. The panel switches to the manual connection page. (Persisted as `ConnectionMode` = `ManualMode`.)
3. In the **Radio IP address** field, type the IPv4 address of your FLEX-8600. This value is saved as `ManualRadioIp`.
4. If your computer has more than one network interface and you need to control which one is used for the connection, select the correct interface from **Advanced: Source path**. This is saved as `ManualBindSource`. If you are unsure, leave it on the default automatic selection.
5. If the link is slow or metered, check **Use low bandwidth mode** to enable reduced-rate streams. This is saved as `LowBandwidthMode`.
6. Click **Connect by IP** (the button at the bottom of the manual page). AetherSDR probes the address and shows the result in the manual result label below the button.
7. Watch the status label. When it shows a connected state the radio is ready to use.

## What each control does

| Control | What it does | Persisted key |
|---|---|---|
| **Connect by IP** (mode button) | Switches the panel to the manual connection page. | `ConnectionMode` |
| **Radio IP address** | The IPv4 address AetherSDR dials directly. | `ManualRadioIp` |
| **Advanced: Source path** | Selects the local network interface (NIC) used for the outgoing connection. | `ManualBindSource` |
| **Use low bandwidth mode** | Reduces stream data rates for slow or metered links. | `LowBandwidthMode` |
| **Connect by IP** (action button) | Starts the connection attempt to the entered IP address. | — |
| **Network Diagnostics** | Opens the network diagnostics dialog from the manual page. | — |
| Manual result label | Shows the outcome of the last connection probe (success or error text). | — |
| Source warning label | Warns when the interface selected in **Advanced: Source path** is no longer available or its last known address has changed. | — |

## Tips

- If the source warning label shows that your saved interface is unavailable, open **Advanced: Source path** and reselect the correct NIC for your VPN adapter. The warning appears when the previously saved interface is stale or unreachable.
- If you land on the **On This Network** page and see "No local radios found yet", click **Connect by IP** in the callout to jump directly to the manual page.

## Troubleshooting

- **Manual result label shows an error immediately after clicking Connect by IP** — The radio is not answering on that address. Confirm the IP is correct, that the VPN tunnel is up, and that no firewall on the radio's network is blocking TCP port 4992 (the SmartSDR command port).
- **Source warning label says the saved source is unavailable** — Your VPN adapter has changed or is down. Re-establish the VPN connection, then reselect the adapter in **Advanced: Source path**.
- **Connection probe succeeds but the radio never reaches a connected state** — The UDP data streams may be blocked. Check that your VPN or router permits bidirectional UDP traffic between your computer and the radio.

## Related

- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)
- [Pick the local network interface used for a manual connection](pick-the-local-network-interface-used-for-a-manual-connection.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- [Connect to a Radio overview](../../features/connection/overview.md)
