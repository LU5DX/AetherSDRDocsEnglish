# Connect by IP across a VPN or routed network

Use this method when your FLEX-8600 is on a different subnet from your computer — for example, across a VPN tunnel or a routed station network — and mDNS discovery cannot reach it. You will enter the radio's IP address directly and AetherSDR will open the SmartSDR protocol connection without relying on discovery.

## Before you start

- You must know the radio's IPv4 address or hostname on the remote or VPN network.
- The radio must be reachable from your computer (ping it first to confirm routing is working).
- If you are connecting over a slow or metered link, decide in advance whether you want to enable low-bandwidth mode.

## Steps

1. Open the connection screen. It appears automatically before a radio is connected. If a radio is already connected, go to `Settings > Connect to Radio...` or disconnect first.
2. Click **Manual** in the mode button row at the top of the panel. The panel switches to the manual connection page. (Persisted as `ConnectionMode` = `ManualMode`.)
3. Choose the radio family from **Advanced: Radio family**. Select **FlexRadio** or **Icom** depending on the radio you are connecting to. The selection is remembered per IP address. (Persisted as `ConnectByIpRadioFamily`.)
4. In the **Radio IP address** field, type the IPv4 address or hostname of your radio, or select a recently used address from the drop-down list. AetherSDR stores up to three recent addresses. This value is saved as `ManualRadioIp`. Hostnames such as `ic-705.local` are now remembered in the recent list.
5. If your computer has more than one network interface and you need to control which one is used for the connection, select the correct interface from **Advanced: Source path**. This is saved as `ManualBindSource`. If you are unsure, leave it on the default automatic selection.
6. If the link is slow or metered, check **Use low bandwidth mode** to enable reduced-rate streams. This is saved as `LowBandwidthMode`.
7. To further reduce bandwidth on very slow links, check **Enable adaptive frame-rate throttle**. When enabled, AetherSDR automatically reduces FFT and waterfall frame rates when network quality degrades. This is saved as `AdaptiveThrottleEnabled`. By default, this option is unchecked.
8. If you do not want AetherSDR to connect automatically to the last used radio each time it starts, uncheck **Connect to last radio on start up**. This is saved as `AutoConnectToLastRadio`. The checkbox is enabled by default.
9. Click **Connect by IP (manual)** (the button at the bottom of the manual page). AetherSDR probes the address and shows the result in the manual result label below the button.
10. Watch the status label. When it shows a connected state the radio is ready to use.

## What each control does

| Control | What it does | Persisted key |
|---|---|---|
| **Local / SmartLink / Manual** (mode buttons) | Switches the panel among the three connection modes. | `ConnectionMode` |
| **Advanced: Radio family** | Selects the protocol family for the manual connection: FlexRadio or Icom. The selection is stored per IP address and defaults to FlexRadio for older profiles. | `ConnectByIpRadioFamily` |
| **Radio IP address** | The IPv4 address or hostname AetherSDR dials directly. Type a new address or select one of the last three used addresses from the drop-down. | `ManualRadioIp` |
| **Advanced: Source path** | Selects the local network interface (NIC) used for the outgoing connection. | `ManualBindSource` |
| **Use low bandwidth mode** | Reduces stream data rates for slow or metered links. | `LowBandwidthMode` |
| **Enable adaptive frame-rate throttle** | Automatically reduces FFT and waterfall frame rates when network quality degrades, for very slow links. | `AdaptiveThrottleEnabled` |
| **Connect to last radio on start up** | When checked, AetherSDR auto-connects to the last used radio on startup and on broadcast-discovery / routed-radio probe. When unchecked, the connection dialog opens and the user must pick a radio manually each session. Defaults to checked. | `AutoConnectToLastRadio` |
| **Connect by IP (manual)** (action button) | Starts the connection attempt to the entered IP address. | — |
| **Network Diagnostics** | Opens the network diagnostics dialog from the manual page. | — |
| Manual result label | Shows the outcome of the last connection probe (success or error text). | — |
| Source warning label | Warns when the interface selected in **Advanced: Source path** is no longer available or its last known address has changed. | — |

## Tips

- The **Radio IP address** field keeps a drop-down history of the last three addresses you connected to successfully. Click the arrow to reselect a previous address without retyping it. Hostnames such as `ic-705.local` are now remembered alongside numeric addresses.
- The **Advanced: Radio family** selection is remembered for each IP address independently. Older profiles without an explicit family default to FlexRadio, which matches the previous behavior.
- If the source warning label shows that your saved interface is unavailable, open **Advanced: Source path** and reselect the correct NIC for your VPN adapter. The warning appears when the previously saved interface is stale or unreachable.
- If you land on the **Local** page and see "No local radios found yet", click **Connect by IP** in the callout to jump directly to the manual page.
- If you previously connected using an older version of AetherSDR, your last used IP address is migrated automatically into the recent addresses history on first launch.

## Troubleshooting

- **Manual result label shows an error immediately after clicking Connect by IP (manual)** — The radio is not answering on that address. Confirm the IP or hostname is correct, that the VPN tunnel is up, and that no firewall on the radio's network is blocking the protocol port (4992 for FlexRadio, 50001 for Icom).
- **Source warning label says the saved source is unavailable** — Your VPN adapter has changed or is down. Re-establish the VPN connection, then reselect the adapter in **Advanced: Source path**.
- **Connection probe succeeds but the radio never reaches a connected state** — The UDP data streams may be blocked. Check that your VPN or router permits bidirectional UDP traffic between your computer and the radio.
- **The connection window opens in frameless mode and the geometry is not restored correctly when the window is shown again** — This issue has been resolved. The window geometry is now properly restored only when the window was previously visible.

## Related

- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)
- [Pick the local network interface used for a manual connection](pick-the-local-network-interface-used-for-a-manual-connection.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- Enable adaptive frame-rate throttle for very slow links
- [Connect to a Radio overview](../../features/connection/overview.md)