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

When you connect using the Manual page, AetherSDR now saves up to three recently used IP addresses. The **Radio IP address** field is an editable drop-down. Click the arrow to pick a previous address, or type a new one directly. Addresses are validated and normalised when saved; duplicates and malformed entries are discarded automatically.

If you previously used the legacy **LastRoutedRadioIp** setting, AetherSDR imports that address into the recent-addresses list the first time it starts after upgrading. The value is stored in `RecentConnectByIpAddresses`.

## Related

- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Retry discovery when no radios appear](../../features/connection/retry-discovery-when-no-radios-appear.md)
- [Connect to a Radio overview](../../features/connection/overview.md)