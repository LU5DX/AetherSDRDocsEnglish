# Retry Discovery When No Radios Appear

When AetherSDR's local discovery finds no radios, the "No local radios found yet" callout appears in place of the radio list. This page explains how to trigger a fresh discovery scan and what to try if the list stays empty.

## Before you start

- AetherSDR is open and showing the "Connect to a Radio" panel. If it is not visible, go to `Settings > Connect to Radio...`.
- Your FLEX-8600 is powered on and connected to the same LAN as your computer.

## Steps

1. In the "Connect to a Radio" panel, confirm that **Local** is the selected mode. If it is not, click **Local**.
2. If the "No local radios found yet" callout is visible, click **Retry Discovery**.
3. Wait a few seconds for AetherSDR to listen for discovery packets. If your radio is found, it appears in the **Available radios** list.
4. Select your radio in the **Available radios** list, then click **Connect Selected Radio**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Local** | Mode button | Switches to local LAN discovery mode. |
| **SmartLink** | Mode button | Switches to SmartLink remote connection mode. |
| **Manual** | Mode button | Switches to manual IP connection mode. |
| **No local radios found yet** | Indicator | Shown when discovery returns no results. Replaces the radio list. |
| **Retry Discovery** | Button | Re-runs the LAN discovery scan immediately. |
| **Connect Selected Radio** | Button | Connects to the radio highlighted in the **Available radios** list. |
| **Connect by IP** | Button | Shortcut to the Manual connection mode. |
| **Remote with SmartLink** | Button | Shortcut to the SmartLink connection mode. |
| **Open Network Diagnostics** | Button | Opens the network diagnostics display to inspect connectivity. |
| **Radio IP address** | Text field | Enter the IP address or host name (for example, `ic-705.local`) to use for a manual connection. Saved as `ManualRadioIp`. |
| **Advanced: Source path** | Combo box | Picks the local network interface used for the manual connection. Saved as `ManualBindSource`. |
| **Use low bandwidth mode** | Checkbox | Enables reduced-rate streams for slow links. Saved as `LowBandwidthMode`. |
| **Enable adaptive frame-rate throttle** | Checkbox | When checked, automatically reduces FFT/waterfall frame rate when network quality degrades. Saved as `AdaptiveThrottleEnabled`. Defaults to unchecked. |
| **Connect to last radio on start up** | Checkbox | When checked, AetherSDR auto-connects to the last used radio on startup and on broadcast-discovery / routed-radio probe. When unchecked, the connection dialog opens and the user must pick a radio manually each session. Saved as `AutoConnectToLastRadio`. Defaults to checked. |
| **Disconnect** | Button | Disconnects from the current radio. |

## Indicators

| Indicator | Meaning |
|---|---|
| **Status label** | Shows the current connection state: searching, connecting, connected, or errored. |
| **Manual result label** | Shows the result text after probing a manual IP (success or error). |
| **Source warning label** | Warns when the selected source network interface is stale or unreachable. |

## SmartLink connection

| Control | Kind | Behavior |
|---|---|---|
| **SmartLink account: Email** | Text field | Your SmartLink account email address. Saved as `SmartLinkEmail`. |
| **SmartLink account: Password** | Text field | Your SmartLink account password (not persisted). |
| **Sign In** | Button | Authenticates with SmartLink. |
| **Sign Out** | Button | Logs out of SmartLink. |
| **Remote radios** | List | Lists SmartLink WAN radios available to your account. |
| **Connect Remote Radio** | Button | Starts a WAN connection to the selected remote radio. |

## Radio list context menu

Right-click a radio in the **Available radios** list to display a context menu. The available action depends on the radio type:

| Action | Behavior |
|---|---|
| **Set Nickname...** | Opens a dialog to assign a custom nickname to the radio. The nickname is stored client-side and displayed in the radio list on subsequent discovery scans. This option is available only for radios without an onboard name store (such as HL2 or simulated radios). For FlexRadio radios, set the radio name from Radio Setup while connected. |

## Tips

- The "No local radios found yet" callout also shows while discovery is still in progress immediately after launch. Wait a few seconds before concluding the radio is unreachable.
- If the radio and computer are on different subnets or you are using a VPN, mDNS discovery packets will not cross the network boundary. Click **Connect by IP** instead and enter the radio's IP address or host name directly.
- Guest Wi-Fi networks commonly block device-to-device traffic. If you are on Wi-Fi, check whether your access point enforces client isolation.
- If you share the computer with other operators or prefer to choose a radio explicitly each session, uncheck **Connect to last radio on start up**. AetherSDR will open the connection dialog on every launch instead of connecting automatically.
- The **Advanced: Source path** control lets you choose which local network interface to use for manual/VPN connections. Select the NIC that has the best route to your radio.
- Enable **Use low bandwidth mode** when connecting over a slow or unreliable link to reduce audio and data stream rates.
- Enable **Enable adaptive frame-rate throttle** to let AetherSDR automatically reduce FFT/waterfall frame rate when network quality degrades. This helps maintain a stable connection over intermittent links. The throttle resumes full frame rate when network quality improves.
- Right-click a non-Flex radio in the **Available radios** list and select **Set Nickname...** to give it a custom name that persists across restarts.

## Troubleshooting

- **Retry Discovery does nothing and the list stays empty** — The radio may be on a different subnet, behind a VPN, or blocked by a host firewall. Click **Connect by IP** and enter the radio's IP address or host name manually, or click **Open Network Diagnostics** for more detail.
- **Radio appears briefly then disappears** — Network instability or a firewall dropping mDNS traffic intermittently. Check your firewall rules and retry. If the problem persists, use **Connect by IP** for a stable connection.
- **Open Network Diagnostics shows no useful information** — Go to `Settings > Network...` to open the full network diagnostics display.
- **AetherSDR connects to the wrong radio on startup** — Uncheck **Connect to last radio on start up** so the connection dialog opens on launch, then select the intended radio manually.
- **Manual connection fails** — Check that the **Advanced: Source path** is set to a valid network interface. If the **Source warning label** is visible, select a different NIC or reconnect your network.
- **SmartLink sign-in fails** — Verify your email and password are correct. If you have changed your SmartLink password recently, sign out and sign in again with the new credentials.

## Related

- [Connect to a local LAN radio](../../getting-started/setup/connect-to-a-local-lan-radio.md)
- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)
- [Log in to SmartLink to see remote radios](log-in-to-smartlink-to-see-remote-radios.md)
- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)