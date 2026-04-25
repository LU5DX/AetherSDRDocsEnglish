# Connect to a local LAN radio

Use this page to connect AetherSDR to a FLEX-8600 that is on the same LAN as your computer. AetherSDR discovers the radio automatically using mDNS — no IP address required.

## Before you start

- The FLEX-8600 must be powered on and reachable on the same local network as your computer.
- AetherSDR must be running. The connection screen appears automatically before any radio is connected, or after a disconnect.
- Confirm that no VPN, guest Wi-Fi isolation, or host firewall is blocking mDNS/discovery traffic on your network.

## Steps

1. Open the connection screen. It appears automatically at startup. You can also open it at any time via `Settings > Connect to Radio...`.
2. Click **On This Network**. This is the default mode, so it may already be selected.
3. Wait a few seconds for the **Available radios** list to populate. AetherSDR listens for discovery packets from the radio; this normally completes within a few seconds.
4. Click your radio in the **Available radios** list to highlight it.
5. Click **Connect Selected Radio**.

The status label at the bottom of the panel updates through connecting and then connected states as the link is established.

## What each control does

| Control | What it does | Persisted setting |
|---|---|---|
| **On This Network** | Selects local LAN discovery mode. Default mode on first launch. | `ConnectionMode` |
| **Available radios** | Lists FLEX-8600 radios discovered on the LAN via mDNS. Populated automatically; no input required. | — |
| **Connect Selected Radio** | Connects to the highlighted radio. Enabled only when a radio is selected in the list. | — |
| **No local radios found yet** | Callout shown when discovery returns no results. Replaces the list until a radio is found or discovery is retried. | — |
| **Retry Discovery** | Re-runs LAN discovery immediately. Appears inside the empty-state callout. | — |
| **Connect by IP** | Shortcut to the **Connect by IP** mode. Appears inside the empty-state callout. | `ConnectionMode` |
| **Remote with SmartLink** | Shortcut to the **Remote with SmartLink** mode. Appears inside the empty-state callout. | `ConnectionMode` |
| **Open Network Diagnostics** | Opens the network diagnostics window. Appears inside the empty-state callout. | — |

## Tips

- If the list is slow to populate, wait at least 10–15 seconds before using **Retry Discovery**. The radio sends periodic discovery packets and AetherSDR may not have received the first one yet.
- If your computer has multiple network interfaces, AetherSDR may be listening on the wrong one. If discovery consistently fails, consider switching to **Connect by IP** mode and specifying the interface with **Advanced: Source path**.

## Troubleshooting

- **"No local radios found yet" appears and does not go away** — The radio's discovery packets are not reaching AetherSDR. Common causes: the radio and computer are on different VLANs or subnets, guest Wi-Fi AP isolation is enabled, or a software VPN is intercepting multicast traffic. Click **Open Network Diagnostics** for details, or switch to **Connect by IP** mode if you know the radio's IP address.
- **Connect Selected Radio is greyed out** — No radio is selected in the **Available radios** list. Click a radio in the list first.
- **The status label shows an error after clicking Connect Selected Radio** — The radio was discovered but the TCP connection failed. Check that no firewall is blocking the SmartSDR protocol port, and that no other SmartSDR-compatible client holds the exclusive connection.

## Related

- [Retry discovery when no radios appear](../../features/connection/retry-discovery-when-no-radios-appear.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)
- [Pick the local network interface used for a manual connection](pick-the-local-network-interface-used-for-a-manual-connection.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- [Disconnect from the current radio](disconnect-from-the-current-radio.md)
- [Make your first QSO with AetherSDR](../tutorials/first-qso.md)
