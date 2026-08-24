# Connection panel

The Connection panel is the main entry point for connecting AetherSDR to a FlexRadio radio. It provides three connection modes: Local (LAN discovery), SmartLink (remote WAN radios), and Manual (direct IP connection, useful for VPN or routed networks).

## Connect to a Local LAN Radio

1. Open **Settings > Connect to Radio...**.
2. Ensure **Local** is selected at the top of the dialog.
3. Wait for the "Available radios" list to populate with discovered radios on your LAN.
4. Select the radio you want to connect to from the list.
5. Click **Connect Selected Radio**.

If no radios appear, click **Retry Discovery** to re-run LAN discovery.

### Set a Custom Nickname for a Non-Flex Radio

For radios that do not have an on-radio name store (e.g., HL2, simulator), you can set a custom nickname without connecting first.

1. Open **Settings > Connect to Radio...**.
2. Ensure **Local** is selected at the top of the dialog.
3. Wait for the "Available radios" list to populate with discovered radios on your LAN.
4. Right-click the radio you want to nickname.
5. Select **Set Nickname...** from the context menu.
6. Enter the desired nickname in the dialog.
7. Click **OK**.

The nickname is saved and will appear in the radio list on subsequent discovery sweeps. This option is not shown for FlexRadio radios, whose names are set from Radio Setup while connected.

## Connect to a Remote Radio through SmartLink

1. Open **Settings > Connect to Radio...**.
2. Click **Remote with SmartLink** or select the **SmartLink** mode button.
3. Enter your FlexRadio account email in the **Email** field.
4. Enter your FlexRadio account password in the **Password** field.
5. Click **Sign In**.
6. After successful authentication, select a radio from the **Remote radios** list.
7. Click **Connect Remote Radio**.

To sign out, click **Sign Out**.

## Connect by IP across a VPN or Routed Network

1. Open **Settings > Connect to Radio...**.
2. Click **Connect by IP** or select the **Manual** mode button.
3. Enter the radio's IP address or hostname (e.g., `ic-705.local`) in the **Radio IP address** field.
4. (Optional) Select a local network interface from the **Advanced: Source path** dropdown if you need to route through a specific NIC.
5. Click **Connect by IP (manual)**.

The Manual page remembers the last three addresses you entered. The address can be either a numeric IP address or a hostname; both are saved in the recent-address list. Previously, only numeric IP addresses were remembered, so VPN radios reached by DNS name would not appear in the recent list.

## Connection Options for Slower Links

1. Open **Settings > Connect to Radio...**.
2. Scroll to the bottom of the panel.
3. Locate the **Connection options for slower links** section.
4. Check **Use low bandwidth mode** to enable reduced-rate streams.
5. Check **Enable adaptive frame-rate throttle** to automatically reduce FFT/waterfall frame rate when network quality degrades.

## Disconnect from the Current Radio

- Click **Disconnect** at any time to terminate the connection to the current radio.

## Network Diagnostics

- Click **Open Network Diagnostics** from any mode to open the Network Diagnostics dialog for troubleshooting connectivity issues.

## Disable Auto-Connect for Manual Radio Selection on Startup

By default, AetherSDR reconnects to the last used radio every time it starts. Disabling this makes AetherSDR open the connection dialog on startup instead, so you can choose a radio manually each session.

### Before you start

- AetherSDR must be running.
- No radio connection is required to change this setting.

### Steps

1. Click **Settings > Connect to Radio...**.
2. In the Connect to Radio dialog, scroll to the bottom of the page.
3. Locate the checkbox labelled **Connect to last radio on start up**.
4. Uncheck **Connect to last radio on start up**.

The setting is saved immediately to `AutoConnectToLastRadio`. The next time AetherSDR starts, it will open the connection dialog automatically instead of reconnecting to the last radio.

### What each control does

| Control | Default | Persisted setting | Behavior |
|---|---|---|---|
| "Connect to last radio on start up" checkbox | Checked (True) | `AutoConnectToLastRadio` | When checked, AetherSDR auto-connects to the last used radio on startup and on broadcast-discovery / routed-radio probe. When unchecked, the connection dialog opens and you must select a radio manually each session. |

### Tips

- This setting also suppresses the automatic connection attempt that occurs during broadcast discovery and routed-radio probing, not only the initial startup reconnect.
- If you share the computer across multiple stations or switch between radios frequently, leaving this unchecked avoids connecting to the wrong radio by accident.

### Troubleshooting

- **AetherSDR still auto-connects after unchecking the box** — Confirm you unchecked the box inside **Settings > Connect to Radio...** and not a different dialog. The checkbox label is exactly "Connect to last radio on start up". Quit and relaunch AetherSDR to verify the change takes effect.

## All Controls Summary

| Control | Default | Persisted setting | Behavior |
|---|---|---|---|
| Local / SmartLink / Manual mode buttons | Local | `ConnectionMode` | Switches between the three connection modes. |
| Available radios list | — | — | Displays LAN radios discovered via mDNS/Flex discovery. Right-click a non-Flex radio to set a custom nickname. |
| Connect Selected Radio | — | — | Connects to the highlighted LAN radio. |
| No local radios found yet | — | — | Callout shown when discovery is empty. |
| Retry Discovery | — | — | Re-runs LAN discovery. |
| Remote with SmartLink | — | — | Shortcut to the SmartLink page. |
| Connect by IP | — | — | Shortcut to the Manual page. |
| Open Network Diagnostics | — | — | Opens NetworkDiagnosticsDialog. |
| SmartLink account: Email | — | `SmartLinkEmail` | SmartLink account email. |
| SmartLink account: Password | — | — | SmartLink password (not persisted). |
| Sign In | — | — | Authenticates with SmartLink. |
| Sign Out | — | — | Logs out of SmartLink. |
| Remote radios list | — | — | Lists SmartLink WAN radios available to the account. |
| Connect Remote Radio | — | — | Starts a WAN connection to the selected radio. |
| Radio IP address | — | `ManualRadioIp` | Manual IP address or hostname to connect to. Hostnames such as `ic-705.local` are now remembered in the recent-address list. |
| Advanced: Source path | — | `ManualBindSource` | Picks local NIC used for the manual connection. |
| Connect by IP (manual) | — | — | Starts the manual/VPN connection. |
| Use low bandwidth mode | — | `LowBandwidthMode` | Enables reduced-rate streams for slow links. |
| Enable adaptive frame-rate throttle | Unchecked (False) | `AdaptiveThrottleEnabled` | Automatically reduces FFT/waterfall frame rate when network quality degrades. |
| Connect to last radio on start up | Checked (True) | `AutoConnectToLastRadio` | When checked, AetherSDR auto-connects to the last used radio on startup and on broadcast-discovery / routed-radio probe. When unchecked, the connection dialog opens and you must select a radio manually each session. |
| Disconnect | — | — | Disconnects from the current radio. |

## Indicators

| Label | Meaning |
|---|---|
| Status label | Current connection state (searching / connecting / connected / errored). |
| Manual result label | Result text after probing a manual IP (success or error). |
| Source warning label | Warns when the selected source NIC is stale or unreachable. |

## Related

- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Disconnect from the current radio](disconnect-from-the-current-radio.md)