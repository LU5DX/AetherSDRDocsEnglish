# Retry Discovery When No Radios Appear

When AetherSDR's local discovery finds no radios, the "No local radios found yet" callout appears in place of the radio list. This page explains how to trigger a fresh discovery scan and what to try if the list stays empty.

## Before you start

- AetherSDR is open and showing the "Connect to a Radio" panel. If it is not visible, go to `Settings > Connect to Radio...`.
- Your FLEX-8600 is powered on and connected to the same LAN as your computer.

## Steps

1. In the "Connect to a Radio" panel, confirm that **On This Network** is the selected mode. If it is not, click **On This Network**.
2. If the "No local radios found yet" callout is visible, click **Retry Discovery**.
3. Wait a few seconds for AetherSDR to listen for discovery packets. If your radio is found, it appears in the **Available radios** list.
4. Select your radio in the **Available radios** list, then click **Connect Selected Radio**.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **On This Network** | Mode button | Switches to local LAN discovery mode. | `ConnectionMode` |
| **No local radios found yet** | Indicator | Shown when discovery returns no results. Replaces the radio list. | — |
| **Retry Discovery** | Button | Re-runs the LAN discovery scan immediately. | — |
| **Connect Selected Radio** | Button | Connects to the radio highlighted in the **Available radios** list. | — |
| **Connect by IP** | Button | Shortcut to the manual IP connection mode. | `ConnectionMode` |
| **Remote with SmartLink** | Button | Shortcut to the SmartLink connection mode. | `ConnectionMode` |
| **Open Network Diagnostics** | Button | Opens the network diagnostics display to inspect connectivity. | — |

## Tips

- The "No local radios found yet" callout also shows while discovery is still in progress immediately after launch. Wait a few seconds before concluding the radio is unreachable.
- If the radio and computer are on different subnets or you are using a VPN, mDNS discovery packets will not cross the network boundary. Click **Connect by IP** instead and enter the radio's IP address directly.
- Guest Wi-Fi networks commonly block device-to-device traffic. If you are on Wi-Fi, check whether your access point enforces client isolation.

## Troubleshooting

- **Retry Discovery does nothing and the list stays empty** — The radio may be on a different subnet, behind a VPN, or blocked by a host firewall. Click **Connect by IP** and enter the radio's IP address manually, or click **Open Network Diagnostics** for more detail.
- **Radio appears briefly then disappears** — Network instability or a firewall dropping mDNS traffic intermittently. Check your firewall rules and retry. If the problem persists, use **Connect by IP** for a stable connection.
- **Open Network Diagnostics shows no useful information** — Go to `Settings > Network...` to open the full network diagnostics display.

## Related

- [Connect to a local LAN radio](../../getting-started/setup/connect-to-a-local-lan-radio.md)
- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)
- [Log in to SmartLink to see remote radios](log-in-to-smartlink-to-see-remote-radios.md)
- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
