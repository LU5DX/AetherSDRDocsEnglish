# Connect to a Radio overview

The Connect to a Radio panel is the starting point for every AetherSDR session. It lets you choose how to reach your FLEX-8600 — on your local network, through FlexRadio SmartLink, or by entering an IP address directly — and then initiate the connection.

## Before you start

- Your FLEX-8600 must be powered on and running firmware 4.2.
- For SmartLink connections, you need a FlexRadio account and internet access on both ends.
- For manual/VPN connections, you need the radio's IP address.

## How it works

The panel opens as a separate window whenever no radio is connected. It features a custom title bar with the text "Connect to Radio". You can drag the window by its title bar. The panel appears in the main window whenever no radio is connected. You can also open it at any time via `Settings > Connect to Radio...`.

The panel uses a frameless window style by default, controlled by the `FramelessWindow` setting (default: True). When frameless mode is on, the custom title bar provides window dragging capability. The panel restores its previous geometry when it becomes visible again after being hidden. Closing this window will close the connection panel.

Three mode buttons across the top determine which connection method is active. Selecting a mode switches the panel below to show the relevant controls. AetherSDR persists your last-used mode in `ConnectionMode`.

### On This Network (Local mode)

Use this mode when the radio and your computer are on the same LAN. AetherSDR runs mDNS/Flex discovery automatically and lists any radios it finds under **Available radios**. Select a radio from the list and click **Connect Selected Radio** to connect.

If discovery finds nothing, the panel switches to an empty-state view showing **No local radios found yet**. From there you can:

- Click **Retry Discovery** to run discovery again.
- Click **Connect by IP** to switch to the Manual page.
- Click **Remote with SmartLink** to switch to the SmartLink page.
- Click **Open Network Diagnostics** to investigate network problems.

Common reasons discovery returns nothing include guest Wi-Fi AP isolation, VPN software running on the host, and firewall rules blocking discovery packets.

The **Available radios** list has a bounded height (minimum 120px, maximum 240px) so it scrolls internally when more radios are discovered than fit the visible area. This prevents the list from growing past the dialog on small displays. The list includes custom-styled vertical scrollbar with rounded handles.

You can right-click any radio in the **Available radios** list to open a context menu. Choose **Set custom nickname** to assign a client-side nickname that persists across discovery sweeps. This is intended for non-Flex radios (such as HL2 or simulated radios) that do not store a name on the radio itself. For Flex radios, the nickname is managed through Radio Setup while connected, so the context menu is not offered for Flex radios to avoid conflicting sources of truth.

### Remote with SmartLink

Use this mode when the radio is at a different location. Enter your FlexRadio account email in **SmartLink account: Email** (persisted as `SmartLinkEmail`) and your password in **SmartLink account: Password** (not persisted), then click **Sign In**. After authentication, AetherSDR populates the **Remote radios** list with the WAN radios available to your account. The list has a fixed height; if you have many remote radios, scroll within the list to find the one you want. Select a radio and click **Connect Remote Radio**. To end the session, click **Sign Out**.

The email and password fields include accessibility metadata to help password managers (macOS Passwords, Windows Authenticator, KDE Wallet) associate the credential pair with the SmartLink login form.

### Connect by IP (Manual mode)

Use this mode for VPN or routed network connections where you already know the radio's IP address. Enter the address in **Radio IP address** (persisted as `ManualRadioIp`), then click **Connect by IP**.

The **Radio IP address** field is an editable drop-down. AetherSDR stores up to three recently used addresses (persisted as `RecentConnectByIpAddresses`) and populates the drop-down with them when the panel opens. Click the drop-down arrow to select a previous address, or type a new one directly. Addresses are normalized before saving; duplicates are not stored. If a legacy `LastRoutedRadioIp` value exists from an earlier version, it is imported automatically the first time the panel opens.

Three additional controls are available on this page:

- **Advanced: Source path** — selects which local network interface (NIC) is used for the connection. The chosen interface is persisted as `ManualBindSource`. A **Source warning label** appears if the saved interface is unavailable or stale.
- **Use low bandwidth mode** — reduces stream data rates for slow or congested links. Persisted as `LowBandwidthMode`.
- **Enable adaptive frame-rate throttle** — when enabled, automatically reduces FFT/waterfall frame rate when network quality degrades. Persisted as `AdaptiveThrottleEnabled`. Default: off.
- **Network Diagnostics** — opens the network diagnostics tool if the connection fails.

When probing a manual IP address, AetherSDR collects detailed status information from the radio. It captures radio model, nickname, callsign, multiFlex support, and client connection data during a 400-millisecond peek window after the initial handshake. This information is used to populate the radio identity fields and verify the connection.

### Startup behavior

The **Connect to last radio on start up** checkbox controls whether AetherSDR connects automatically when it starts. When checked (the default), AetherSDR attempts to reconnect to the last used radio on startup and whenever it probes broadcast-discovery or routed-radio addresses. When unchecked, the connection panel opens at startup and you must select a radio manually each session. This preference is persisted as `AutoConnectToLastRadio`.

### Status indicators

Regardless of mode, a **Status label** shows the current connection state (searching, connecting, connected, or an error message). After probing a manual IP, a **Manual result label** shows whether the probe succeeded or failed.

### Disconnecting

Once connected, click **Disconnect** to return to the connection panel. You can also reach the panel again via `Settings > Connect to Radio...`.

## What each control does

| Control | Mode | Behavior |
|---|---|---|
| **Local** | — | Switches to local LAN discovery mode. |
| **SmartLink** | — | Switches to SmartLink remote mode. |
| **Manual** | — | Switches to manual IP entry mode. |
| **Available radios** | Local | Lists radios found by LAN discovery. Bounded height (120–240px) with internal scrolling. Right-click to set a custom nickname for non-Flex radios. |
| **Connect Selected Radio** | Local | Connects to the highlighted radio. |
| **No local radios found yet** | Local | Indicator shown when discovery is empty. |
| **Retry Discovery** | Local | Re-runs LAN discovery. |
| **Remote with SmartLink** (shortcut) | Local | Switches to the SmartLink page. |
| **Connect by IP** (shortcut) | Local | Switches to the Manual page. |
| **Open Network Diagnostics** | Local | Opens the network diagnostics tool. |
| **SmartLink account: Email** | SmartLink | FlexRadio account email address. Persisted as `SmartLinkEmail`. Includes accessibility metadata for password manager integration. |
| **SmartLink account: Password** | SmartLink | Account password (not saved between sessions). Includes accessibility metadata for password manager integration. |
| **Sign In** | SmartLink | Authenticates with SmartLink. |
| **Sign Out** | SmartLink | Logs out of SmartLink. |
| **Remote radios** | SmartLink | Lists WAN radios available to the account. Scrollable; fixed display height. |
| **Connect Remote Radio** | SmartLink | Starts a WAN connection to the selected radio. |
| **Radio IP address** | Manual | Editable drop-down showing up to three recent addresses (persisted as `RecentConnectByIpAddresses`). Type a new address or select a previous one. Persisted as `ManualRadioIp`. |
| **Advanced: Source path** | Manual | Selects the local NIC for the connection. Persisted as `ManualBindSource`. |
| **Use low bandwidth mode** | Manual | Enables reduced-rate streams for slow links. Persisted as `LowBandwidthMode`. |
| **Enable adaptive frame-rate throttle** | Manual | Automatically reduces FFT/waterfall frame rate when network quality degrades. Persisted as `AdaptiveThrottleEnabled`. Default: off. |
| **Network Diagnostics** | Manual | Opens the network diagnostics tool. |
| **Connect by IP** (manual) | Manual | Initiates the manual/VPN connection. |
| **Connect to last radio on start up** | All | When checked, AetherSDR auto-connects to the last used radio on startup and on broadcast-discovery / routed-radio probe. When unchecked, the connection panel opens and the user must pick a radio manually each session. Defaults to checked. Persisted as `AutoConnectToLastRadio`. |
| **Disconnect** | All | Disconnects from the current radio. |

## Related

- [Connect to a local LAN radio](../../getting-started/setup/connect-to-a-local-lan-radio.md)
- [Retry discovery when no radios appear](retry-discovery-when-no-radios-appear.md)
- [Log in to SmartLink to see remote radios](log-in-to-smartlink-to-see-remote-radios.md)
- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)
- [Pick the local network interface used for a manual connection](../../getting-started/setup/pick-the-local-network-interface-used-for-a-manual-connection.md)
- [Enable low-bandwidth mode for slow links](enable-low-bandwidth-mode-for-slow-links.md)
- [Disconnect from the current radio](../../getting-started/setup/disconnect-from-the-current-radio.md)
- [Set a custom nickname for a discovered radio](set-a-custom-nickname-for-a-discovered-radio.md)