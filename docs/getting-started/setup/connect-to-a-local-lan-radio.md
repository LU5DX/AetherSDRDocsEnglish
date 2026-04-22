# Connect to a local LAN radio

Open AetherSDR's connection screen and connect to a FLEX-8600 that is on the same LAN as your computer. This is the recommended path for first-time users at a home or club station.

## Before you start

- The FLEX-8600 is powered on and connected to the same local network as your computer.
- No VPN or guest Wi-Fi isolation is active between the radio and the computer. Either can block mDNS discovery.
- AetherSDR is installed and launched.

## Steps

1. Open the connection screen. It appears automatically in the main window before a radio is connected. You can also reach it at any time via `Settings > Connect to Radio...`.
2. Click **On This Network**. This selects local LAN discovery mode and sets `ConnectionMode` to `LocalMode`.
3. Wait a few seconds for the **Available radios** list to populate. AetherSDR discovers radios automatically via mDNS.
4. Click your radio in the **Available radios** list to highlight it.
5. Click **Connect Selected Radio**.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **On This Network** | Mode button | Switches to the local LAN discovery page. Default mode. | `ConnectionMode` |
| **Remote with SmartLink** | Mode button | Switches to the SmartLink page. | `ConnectionMode` |
| **Connect by IP** | Mode button | Switches to the manual/IP page. | `ConnectionMode` |
| **Available radios** | List | Shows FLEX-8600 radios found on the LAN via mDNS. Updates automatically. | — |
| **Connect Selected Radio** | Button | Connects to the highlighted radio. Disabled until a radio is selected. | — |
| **No local radios found yet** | Indicator | Shown instead of the list when discovery has not found any radios. | — |
| **Retry Discovery** | Button | Re-runs LAN discovery immediately. Visible only in the empty state. | — |
| **Open Network Diagnostics** | Button | Opens the network diagnostics dialog. Visible only in the empty state. | — |

## Tips

- If the list stays empty for more than 10–15 seconds, click **Retry Discovery** before changing any network settings.
- VPN client software running on the same machine is a common cause of discovery failure even when the radio is on the local network. Try disabling the VPN, then click **Retry Discovery**.
- If your radio is on a different subnet or reachable only through a VPN, use **Connect by IP** instead of **On This Network**.

## Troubleshooting

- **"No local radios found yet" appears and does not clear** — mDNS discovery is being blocked. Check for guest Wi-Fi isolation on your access point, a host firewall blocking UDP, or VPN software redirecting traffic. Click **Open Network Diagnostics** to inspect the network path, or switch to **Connect by IP** if you know the radio's IP address.
- **Connect Selected Radio is greyed out** — No radio is highlighted in the **Available radios** list. Click a radio in the list first.

## Related

- [Retry discovery when no radios appear](../../features/connection/retry-discovery-when-no-radios-appear.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)
- [Disconnect from the current radio](disconnect-from-the-current-radio.md)
- [Make your first QSO with AetherSDR](../tutorials/first-qso.md)
