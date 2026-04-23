# Retry Discovery When No Radios Appear

When AetherSDR opens in local mode and no radios appear in the list, use the "No local radios found yet" callout to re-run discovery or switch to an alternative connection path.

## Before you start

- The Flex radio is powered on and connected to the same LAN as your computer.
- AetherSDR is running and showing the "Connect to a Radio" panel. If it is not visible, click `Settings > Connect to Radio...`.

## Steps

1. Open the "Connect to a Radio" panel. If a radio is already connected, it will appear after you disconnect.
2. Click `Local` (labeled **On This Network**) if it is not already selected. This is the default mode (`ConnectionMode` = `LocalMode`).
3. Wait a few seconds. AetherSDR listens for discovery packets automatically. If no radios are found, the **No local radios found yet** callout appears in place of the radio list.
4. Click **Retry Discovery** to re-run LAN discovery immediately.
5. If a radio now appears in the **Available radios** list, select it and click **Connect Selected Radio**.
6. If no radio appears after retrying, use one of the alternative buttons in the callout:
   - Click **Connect by IP** to switch to the Manual page and enter the radio's IP address directly.
   - Click **Remote with SmartLink** to switch to the SmartLink page and connect over the internet.
   - Click **Open Network Diagnostics** to inspect network state and identify what is blocking discovery.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **On This Network** | Mode button | Selects local LAN discovery mode. | `ConnectionMode` |
| **No local radios found yet** | Indicator | Shown when discovery returns no results. | — |
| **Retry Discovery** | Button | Re-runs LAN discovery without restarting the application. | — |
| **Available radios** | List | Displays radios found via mDNS/Flex discovery. | — |
| **Connect Selected Radio** | Button | Connects to the highlighted radio in the list. | — |
| **Connect by IP** | Button | Switches to the Manual page for direct IP entry. | `ManualRadioIp` |
| **Remote with SmartLink** | Button | Switches to the SmartLink page. | `SmartLinkEmail` |
| **Open Network Diagnostics** | Button | Opens the network diagnostics dialog. | — |

## Tips

- Discovery relies on mDNS and Flex discovery packets. Guest Wi-Fi networks, VPN software, and firewall rules commonly block these packets, causing the **No local radios found yet** callout to appear even when the radio is reachable. If retrying does not help, check whether your computer and radio are on the same subnet and that no VPN is routing traffic away from the local interface.
- If the radio is on a different subnet or behind a VPN, **Retry Discovery** will not succeed. Use **Connect by IP** instead.

## Troubleshooting

- **Retry Discovery has no effect and the list stays empty** — The radio and computer are likely on different network segments, or a firewall is blocking discovery traffic. Switch to **Connect by IP** and enter the radio's IP address, or connect through SmartLink if the radio is at a remote location.
- **The radio appeared once but vanished from the list** — A network interruption dropped the discovery packet. Click **Retry Discovery**. If this recurs, check for IP address changes on the radio or unstable Wi-Fi.

## Related

- [Connect to a local LAN radio](../../getting-started/setup/connect-to-a-local-lan-radio.md)
- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)
- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Log in to SmartLink to see remote radios](log-in-to-smartlink-to-see-remote-radios.md)
- [Pick the local network interface used for a manual connection](../../getting-started/setup/pick-the-local-network-interface-used-for-a-manual-connection.md)
