# Connect to a Radio overview

The Connect to a Radio panel is the starting point for getting AetherSDR talking to your Flex radio. It appears automatically before any radio is connected and whenever you disconnect. Use it to choose how AetherSDR reaches the radio: on the local network, through SmartLink, or by a direct IP address.

## Before you start

- AetherSDR is installed and running.
- Your Flex radio is powered on and reachable by at least one of the three connection paths described below.

## How it works

The panel presents three connection modes as selectable cards across the top. Clicking a card switches the area below it to show the controls for that mode. AetherSDR saves your last-used mode in `ConnectionMode` and restores it on the next launch.

**On This Network** is the default mode. AetherSDR uses mDNS/Flex discovery to find radios on the same LAN automatically. Discovered radios appear in the "Available radios" list. If nothing is found, the panel switches to an empty-state callout titled "No local radios found yet" and offers shortcuts to retry or switch modes.

**Remote with SmartLink** connects to a radio at a remote location over the internet using FlexRadio's SmartLink service. You sign in with your FlexRadio account, and available remote radios appear in the "Remote radios" list.

**Connect by IP** is for VPN tunnels, routed networks, or any situation where you already know the radio's IP address. You type the address directly and optionally choose which local network interface to use for the connection.

You can reopen this panel at any time by choosing `Settings > Connect to Radio...` from the menu bar.

## What each control does

### Mode selection

| Control | What it does | Persisted setting |
|---|---|---|
| On This Network | Switches to LAN discovery mode. Default mode. | `ConnectionMode` |
| Remote with SmartLink | Switches to SmartLink sign-in and remote radio list. | `ConnectionMode` |
| Connect by IP | Switches to manual IP entry. | `ConnectionMode` |

### On This Network mode

| Control | What it does |
|---|---|
| Available radios | Lists Flex radios discovered on the local network. |
| Connect Selected Radio | Connects to the highlighted radio in the list. Disabled until a radio is selected. |
| No local radios found yet | Callout shown when discovery has returned no results. |
| Retry Discovery | Re-runs LAN discovery. |
| Remote with SmartLink | Shortcut that switches directly to SmartLink mode. |
| Connect by IP | Shortcut that switches directly to manual IP mode. |
| Open Network Diagnostics | Opens the network diagnostics dialog. |

### Remote with SmartLink mode

| Control | What it does | Persisted setting |
|---|---|---|
| SmartLink account: Email | Your FlexRadio account email address. | `SmartLinkEmail` |
| SmartLink account: Password | Your FlexRadio account password. Not saved between sessions. | — |
| Sign In | Authenticates with SmartLink using the credentials entered above. | — |
| Sign Out | Logs out of the current SmartLink session. | — |
| Remote radios | Lists radios available to your SmartLink account after sign-in. | — |
| Connect Remote Radio | Starts a WAN connection to the selected remote radio. | — |

### Connect by IP mode

| Control | What it does | Persisted setting |
|---|---|---|
| Radio IP address | The IP address of the radio to connect to. | `ManualRadioIp` |
| Advanced: Source path | Selects which local network interface to use for the connection. | `ManualBindSource` |
| Use low bandwidth mode | Enables reduced-rate audio and data streams for slow or congested links. | `LowBandwidthMode` |
| Connect by IP (manual) | Starts the connection attempt to the address entered. | — |
| Network Diagnostics | Opens the network diagnostics dialog from the manual IP page. | — |

### Status indicators

| Indicator | Meaning |
|---|---|
| Status label | Shows the current connection state: searching, connecting, connected, or an error message. |
| Manual result label | Shows the outcome after AetherSDR probes a manually entered IP address. |
| Source warning label | Warns when the network interface selected in "Advanced: Source path" is stale or unreachable. |

### Disconnect

| Control | What it does |
|---|---|
| Disconnect | Ends the current radio connection and returns to this panel. |

## Tips

- If "No local radios found yet" appears, guest Wi-Fi network isolation, VPN software, or a firewall blocking mDNS packets are the most common causes. Click "Open Network Diagnostics" to investigate, or switch to "Connect by IP" if the radio is on a routed or VPN network.
- The SmartLink password is never saved to disk. You will need to enter it again after restarting AetherSDR.
- The "Source warning label" appears when the interface stored in `ManualBindSource` is no longer present or reachable — for example after a network reconfiguration. Select a current interface from "Advanced: Source path" before connecting.

## Related

- [Connect to a local LAN radio](../../getting-started/setup/connect-to-a-local-lan-radio.md)
- [Retry discovery when no radios appear](retry-discovery-when-no-radios-appear.md)
- [Log in to SmartLink to see remote radios](log-in-to-smartlink-to-see-remote-radios.md)
- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)
- [Pick the local network interface used for a manual connection](../../getting-started/setup/pick-the-local-network-interface-used-for-a-manual-connection.md)
- [Enable low-bandwidth mode for slow links](enable-low-bandwidth-mode-for-slow-links.md)
- [Disconnect from the current radio](../../getting-started/setup/disconnect-from-the-current-radio.md)
