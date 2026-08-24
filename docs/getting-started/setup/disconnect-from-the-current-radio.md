# Disconnect from the Current Radio

This page explains how to disconnect AetherSDR from a connected FLEX-8600. You would do this to switch radios, change connection modes, or shut down your session cleanly.

## Before you start

- AetherSDR must currently be connected to a radio. If no radio is connected, the ConnectionPanel is already shown and no action is needed.

## Steps

1. Open `Settings > Connect to Radio...`.
2. Click `Disconnect`.

AetherSDR drops the connection and returns to the ConnectionPanel, where you can connect to a different radio or choose a different connection mode.

## Tips

- After disconnecting, the `ConnectionMode` setting retains whichever mode was last selected (Local, Remote with SmartLink, or Connect by IP), so the panel reopens on the same page you used previously.
- If you intend to reconnect to the same radio immediately, the `Available radios` list on the Local page will still show it as soon as discovery finds it again. Click the entry and then click `Connect Selected Radio`.

## Auto-connect on startup

The **Connect to last radio on start up** checkbox controls whether AetherSDR reconnects automatically when the application starts.

| Setting | Key | Default |
|---|---|---|
| Connect to last radio on start up | `AutoConnectToLastRadio` | Enabled |

- When checked, AetherSDR automatically connects to the last used radio on startup and when broadcast-discovery or a routed-radio probe finds it. No manual action is required.
- When unchecked, the ConnectionPanel opens on every startup and you must select a radio manually each session.

To change this setting, open the ConnectionPanel and check or uncheck **Connect to last radio on start up**. The preference is saved immediately.

## Recent IP addresses (Manual / VPN mode)

When you connect using the Manual page, AetherSDR now saves up to three recently used addresses. The **Radio IP address** field is an editable drop-down that accepts both numeric IP addresses and host names such as `ic-705.local`. Click the arrow to pick a previous address, or type a new one directly. Numeric addresses are canonicalised (so `192.168.001.5` and `192.168.1.5` count as one entry); host names are validated against a conservative character set (letters, digits, dot, hyphen, underscore, alphanumeric at both ends, up to 253 characters). Duplicates and malformed entries are discarded automatically.

If you previously used the legacy **LastRoutedRadioIp** setting, AetherSDR imports that address into the recent-addresses list the first time it starts after upgrading. The value is stored in `RecentConnectByIpAddresses`.

## Manual connection: Source path and low bandwidth options

In the Manual connection page, under **Advanced**: collapse panel titled **Advanced**, you can configure:

- **Source path** (`ManualBindSource`): Selects the local network interface used for the manual connection. The drop-down lists all available NICs. If the selected NIC becomes stale or unreachable, a warning appears below the field.
- **Use low bandwidth mode** (`LowBandwidthMode`): When checked, AetherSDR uses reduced-rate streams for slow or high-latency links. Useful for VPN or satellite connections.
- **Enable adaptive frame-rate throttle** (`AdaptiveThrottleEnabled`, default `False`): When checked, AetherSDR automatically reduces FFT and waterfall frame rates when network quality degrades. This helps maintain a responsive UI on slow or congested links.

## Radio family selection in Manual mode

The Manual page now remembers which radio family (Flex or Icom) was used for each manual connection. The **Advanced: Source path** drop-down is accompanied by a radio-family selector that persists per saved address:

- Older profiles that predate the selector are treated as Flex, preserving the behavior of existing installs.
- When you reconnect to a previously used manual address, the correct radio family is selected automatically.

## Accessible login form

The SmartLink login form is now accessible to operating-system password managers. macOS Passwords, Windows Authenticator, and KDE Wallet read the accessibility tree to associate credential fields.

- The **Email** field has accessible name "SmartLink account email" and accessible description "FlexRadio account email address used to sign in to SmartLink".
- The **Password** field has accessible name "SmartLink account password" and accessible description "FlexRadio account password used to sign in to SmartLink".
- The form container is named "smartlinkLoginForm" so password managers can scope the credential pair.

Connection mode buttons (Local, Remote with SmartLink, Connect by IP) also have accessible names.

## Frameless mode

The Connection Panel now supports frameless mode. When enabled (controlled by the `FramelessWindow` setting, default `True`), the dialog has no native window title bar. Instead, a custom title bar is displayed at the top of the dialog. The title bar includes the dialog title and can be used to drag or close the window, depending on the operating system.

- If `FramelessWindow` is set to `True`, the custom title bar is shown.
- If set to `False`, the standard OS window decorations are used.
- The change takes effect the next time the Connection Panel is opened.

The dialog geometry is only restored when the panel was previously visible, preventing odd placement when switching frameless mode while hidden.

## Theme-aware styling

The Connection Panel now uses theme variables for colors instead of hardcoded values. This ensures the panel integrates with the selected application theme. The following elements respect theme colors:

- Panel background uses `{{color.background.0}}`
- Group box borders use `{{color.background.2}}`
- Text labels use `{{color.text.primary}}`

Theme changes take effect when the panel is opened or refreshed.

## Local radio list improvements

The local radio list now has bounded dimensions so it scrolls internally when more radios are discovered than fit. This prevents the list from growing past the dialog on small displays (e.g., a 1024x600 tablet panel). The list has:

- Minimum height: 120 pixels
- Maximum height: 240 pixels
- Vertical scrollbar policy: shown as needed
- Vertical scroll mode: per-pixel scrolling

## Radio nickname context menu

You can right-click a discovered radio in the local radio list to set a custom nickname without connecting first. This is useful for non-Flex radios (e.g., HL2, simulator backends) that do not have an on-radio name store. The nickname is persisted keyed by serial number and is picked up on the next discovery sweep.

To set a nickname:

1. Right-click a radio in the **Available radios** list.
2. Select the option to set a nickname from the context menu.
3. Enter the desired nickname in the dialog that appears.
4. Click **OK** to save.

The nickname is displayed in the radio list on subsequent discovery sweeps. FlexRadio radios do not support client-side nicknames — their names are set from Radio Setup while connected.

## Related

- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Retry discovery when no radios appear](../../features/connection/retry-discovery-when-no-radios-appear.md)
- [Connect to a Radio overview](../../features/connection/overview.md)