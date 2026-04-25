# Connect to a Radio overview

The Connect to a Radio panel is the starting point for every AetherSDR session. It lets you choose how to reach your FLEX-8600 — on your local network, through FlexRadio SmartLink, or by entering an IP address directly — and then initiate the connection.

## Before you start

- Your FLEX-8600 must be powered on and running firmware 4.1.5.
- For SmartLink connections, you need a FlexRadio account and internet access on both ends.
- For manual/VPN connections, you need the radio's IP address.

## How it works

The panel appears in the main window whenever no radio is connected. You can also open it at any time via `Settings > Connect to Radio...`.

Three mode buttons across the top determine which connection method is active. Selecting a mode switches the panel below to show the relevant controls. AetherSDR persists your last-used mode in `ConnectionMode`.

### On This Network (Local mode)

Use this mode when the radio and your computer are on the same LAN. AetherSDR runs mDNS/Flex discovery automatically and lists any radios it finds under **Available radios**. Select a radio from the list and click **Connect Selected Radio** to connect.

If discovery finds nothing, the panel switches to an empty-state view showing **No local radios found yet**. From there you can:

- Click **Retry Discovery** to run discovery again.
- Click **Connect by IP** to switch to the Manual page.
- Click **Remote with SmartLink** to switch to the SmartLink page.
- Click **Open Network Diagnostics** to investigate network problems.

Common reasons discovery returns nothing include guest Wi-Fi AP isolation, VPN software running on the host, and firewall rules blocking discovery packets.

### Remote with SmartLink

Use this mode when the radio is at a different location. Enter your FlexRadio account email in **SmartLink account: Email** (persisted as `SmartLinkEmail`) and your password in **SmartLink account: Password** (not persisted), then click **Sign In**. After authentication, AetherSDR populates the **Remote radios** list with the WAN radios available to your account. Select a radio and click **Connect Remote Radio**. To end the session, click **Sign Out**.

### Connect by IP (Manual mode)

Use this mode for VPN or routed network connections where you already know the radio's IP address. Enter the address in **Radio IP address** (persisted as `ManualRadioIp`), then click **Connect by IP**.

Two additional controls are available on this page:

- **Advanced: Source path** — selects which local network interface (NIC) is used for the connection. The chosen interface is persisted as `ManualBindSource`. A **Source warning label** appears if the saved interface is unavailable or stale.
- **Use low bandwidth mode** — reduces stream data rates for slow or congested links. Persisted as `LowBandwidthMode`.

Click **Network Diagnostics** on this page to open the network diagnostics tool if the connection fails.

### Status indicators

Regardless of mode, a **Status label** shows the current connection state (searching, connecting, connected, or an error message). After probing a manual IP, a **Manual result label** shows whether the probe succeeded or failed.

### Disconnecting

Once connected, click **Disconnect** to return to the connection panel. You can also reach the panel again via `Settings > Connect to Radio...`.

## What each control does

| Control | Mode | Behavior | Persisted key | Default |
|---|---|---|---|---|
| **On This Network** | — | Switches to local LAN discovery mode. | `ConnectionMode` | Local |
| **Remote with SmartLink** | — | Switches to SmartLink remote mode. | `ConnectionMode` | — |
| **Connect by IP** | — | Switches to manual IP entry mode. | `ConnectionMode` | — |
| **Available radios** | Local | Lists radios found by LAN discovery. | — | — |
| **Connect Selected Radio** | Local | Connects to the highlighted radio. | — | — |
| **No local radios found yet** | Local | Indicator shown when discovery is empty. | — | — |
| **Retry Discovery** | Local | Re-runs LAN discovery. | — | — |
| **Remote with SmartLink** (shortcut) | Local | Switches to the SmartLink page. | — | — |
| **Connect by IP** (shortcut) | Local | Switches to the Manual page. | — | — |
| **Open Network Diagnostics** | Local | Opens the network diagnostics tool. | — | — |
| **SmartLink account: Email** | SmartLink | FlexRadio account email address. | `SmartLinkEmail` | — |
| **SmartLink account: Password** | SmartLink | Account password (not saved between sessions). | — | — |
| **Sign In** | SmartLink | Authenticates with SmartLink. | — | — |
| **Sign Out** | SmartLink | Logs out of SmartLink. | — | — |
| **Remote radios** | SmartLink | Lists WAN radios available to the account. | — | — |
| **Connect Remote Radio** | SmartLink | Starts a WAN connection to the selected radio. | — | — |
| **Radio IP address** | Manual | IP address of the radio to connect to. | `ManualRadioIp` | — |
| **Advanced: Source path** | Manual | Selects the local NIC for the connection. | `ManualBindSource` | — |
| **Use low bandwidth mode** | Manual | Enables reduced-rate streams for slow links. | `LowBandwidthMode` | — |
| **Network Diagnostics** | Manual | Opens the network diagnostics tool. | — | — |
| **Connect by IP** (manual) | Manual | Initiates the manual/VPN connection. | — | — |
| **Disconnect** | All | Disconnects from the current radio. | — | — |

## Related

- [Connect to a local LAN radio](../../getting-started/setup/connect-to-a-local-lan-radio.md)
- [Retry discovery when no radios appear](retry-discovery-when-no-radios-appear.md)
- [Log in to SmartLink to see remote radios](log-in-to-smartlink-to-see-remote-radios.md)
- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)
- [Pick the local network interface used for a manual connection](../../getting-started/setup/pick-the-local-network-interface-used-for-a-manual-connection.md)
- [Enable low-bandwidth mode for slow links](enable-low-bandwidth-mode-for-slow-links.md)
- [Disconnect from the current radio](../../getting-started/setup/disconnect-from-the-current-radio.md)
