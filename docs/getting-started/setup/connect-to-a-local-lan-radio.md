# Connect to a Radio

Use the connection panel to connect AetherSDR to a FLEX-8600. You can connect to a radio on your local LAN, a remote radio through SmartLink, or a radio at a manual IP address (for VPN or routed network connections).

The connection panel opens automatically when AetherSDR starts and no radio is connected. You can also open it at any time via `Settings > Connect to Radio...`.

## Before you start

- The FLEX-8600 must be powered on and reachable on your network.
- For LAN connections: Confirm that no VPN, guest Wi-Fi isolation, or host firewall is blocking mDNS/discovery traffic on your local network.
- For SmartLink: Ensure you have a valid FlexRadio SmartLink account.

## Connection modes

The connection panel has three modes, selected by the radio buttons at the top:

- **Local** — Discovers and connects to radios on your local LAN.
- **SmartLink** — Connects to remote radios through FlexRadio's SmartLink service.
- **Manual** — Connects to a radio at a specific IP address, useful for VPN or routed network connections.

The panel remembers your last mode and restores it on next launch.

## Local mode steps

1. Click **Local**.
2. Wait a few seconds for the **Available radios** list to populate. AetherSDR listens for discovery packets from the radio; this normally completes within a few seconds.
3. Click your radio in the **Available radios** list to highlight it.
4. Click **Connect Selected Radio**.

The status label at the bottom of the panel updates through searching, connecting, and then connected states as the link is established.

## SmartLink mode steps

1. Click **SmartLink**.
2. Enter your SmartLink account email in the **SmartLink account: Email** field.
3. Enter your account password in the **SmartLink account: Password** field.
4. Click **Sign In**.
5. Wait for the **Remote radios** list to populate with radios available to your account.
6. Click a radio in the list to highlight it.
7. Click **Connect Remote Radio**.

To sign out of SmartLink, click **Sign Out**.

## Manual mode steps

1. Click **Manual**.
2. Enter the IP address of the radio in the **Radio IP address** field.
   - You can also click the drop-down arrow to select a previously used address.
3. (Optional) Click **Advanced: Source path** to select a specific network interface.
4. (Optional) Check **Use low bandwidth mode** if you are on a slow or metered link.
5. Click **Connect by IP (manual)**.

The status label shows the connection result, and the **Manual result label** provides additional detail.

## What each control does

| Control | What it does | Persisted setting |
|---|---|---|
| **Local / SmartLink / Manual** | Switches the panel among the three connection modes. Default mode on first launch is **Local**. | `ConnectionMode` |
| **Available radios** | Lists FLEX-8600 radios discovered on the LAN via mDNS. Populated automatically; no input required. | — |
| **Connect Selected Radio** | Connects to the highlighted LAN radio. Enabled only when a radio is selected in the list. | — |
| **No local radios found yet** | Callout shown when discovery returns no results. Replaces the list until a radio is found or discovery is retried. | — |
| **Retry Discovery** | Re-runs LAN discovery immediately. Appears inside the empty-state callout. | — |
| **Remote with SmartLink** | Shortcut to the **SmartLink** mode. Appears inside the empty-state callout. | `ConnectionMode` |
| **Connect by IP** | Shortcut to the **Manual** mode. Appears inside the empty-state callout. | `ConnectionMode` |
| **Open Network Diagnostics** | Opens the network diagnostics window. Appears inside the empty-state callout. | — |
| **SmartLink account: Email** | Email address used to sign in to SmartLink. Saved between sessions. | `SmartLinkEmail` |
| **SmartLink account: Password** | Password used to sign in to SmartLink. Not saved between sessions. | — |
| **Sign In** | Authenticates with SmartLink using the supplied email and password. | — |
| **Sign Out** | Logs out of the current SmartLink session. | — |
| **Remote radios** | Lists SmartLink WAN radios available to the signed-in account. | — |
| **Connect Remote Radio** | Starts a WAN connection to the selected radio in the **Remote radios** list. | — |
| **Radio IP address** | The IP address used for a manual or VPN connection. The field accepts typed input and also shows up to three recently used addresses in a drop-down for quick reuse. Addresses are normalised and deduplicated before being saved. | `ManualRadioIp` / `RecentConnectByIpAddresses` |
| **Network Diagnostics** | Opens the network diagnostics window from the Manual page. | — |
| **Connect by IP (manual)** | Starts the manual or VPN connection to the address entered in **Radio IP address**. | — |
| **Advanced: Source path** | Selects the local network interface used for the manual connection. Use this when the computer has multiple NICs and AetherSDR is binding to the wrong one. | `ManualBindSource` |
| **Use low bandwidth mode** | Enables reduced-rate audio and data streams. Use this on slow or metered links. | `LowBandwidthMode` |
| **Connect to last radio on start up** | When checked, AetherSDR automatically connects to the last used radio on startup and whenever a broadcast-discovery or routed-radio probe succeeds. When unchecked, the connection screen opens at startup and you must pick a radio manually each session. Defaults to checked so existing users keep their current behaviour. | `AutoConnectToLastRadio` |
| **Disconnect** | Disconnects from the currently connected radio. | — |

## Recent IP addresses (Manual mode)

The **Radio IP address** field is a drop-down combo box that remembers the last three addresses you connected to successfully. Click the arrow to see the list and select a previous address, or type a new one directly in the field.

Addresses are normalised (trimmed and parsed through `QHostAddress`) before being stored so that equivalent forms of the same address are not saved as duplicates. The list is written to the `RecentConnectByIpAddresses` setting as a compact JSON array.

If you are upgrading from a version prior to v0.9.7, the single address previously stored under `LastRoutedRadioIp` is automatically carried forward as the first entry in the new list. No manual migration is required.

## Window appearance

The connection panel is a frameless dialog with a custom title bar. The title bar shows "Connect to Radio" and includes standard window control buttons. This appearance can be controlled by the `FramelessWindow` setting.

When the panel is hidden during a frameless mode toggle, its geometry is preserved only if the panel was visible at the time of the toggle.

## Tips

- If the list is slow to populate, wait at least 10–15 seconds before using **Retry Discovery**. The radio sends periodic discovery packets and AetherSDR may not have received the first one yet.
- If your computer has multiple network interfaces, AetherSDR may be listening on the wrong one. If discovery consistently fails, consider switching to **Manual** mode and specifying the interface with **Advanced: Source path**.
- If you share a computer and do not want AetherSDR to connect to a radio before you have a chance to choose one, uncheck **Connect to last radio on start up**.

## Troubleshooting

- **"No local radios found yet" appears and does not go away** — The radio's discovery packets are not reaching AetherSDR. Common causes: the radio and computer are on different VLANs or subnets, guest Wi-Fi AP isolation is enabled, or a software VPN is intercepting multicast traffic. Click **Open Network Diagnostics** for details, or switch to **Manual** mode if you know the radio's IP address.
- **Connect Selected Radio is greyed out** — No radio is selected in the **Available radios** list. Click a radio in the list first.
- **The status label shows an error after clicking Connect Selected Radio** — The radio was discovered but the TCP connection failed. Check that no firewall is blocking the SmartSDR protocol port, and that no other SmartSDR-compatible client holds the exclusive connection.
- **The Radio IP address drop-down shows an old or unreachable address** — Type a new address directly in the field. The old entry will age out of the list once three newer successful connections have been made.
- **AetherSDR connects to the wrong radio at startup** — Uncheck **Connect to last radio on start up**. AetherSDR will then open the connection screen on every launch so you can choose the radio manually.

## Related

- [Retry discovery when no radios appear](../../features/connection/retry-discovery-when-no-radios-appear.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)
- [Pick the local network interface used for a manual connection](pick-the-local-network-interface-used-for-a-manual-connection.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- [Disconnect from the current radio](disconnect-from-the-current-radio.md)
- [Make your first QSO with AetherSDR](../tutorials/first-qso.md)