# Enable low-bandwidth mode for slow links

Low-bandwidth mode reduces the rate of audio and data streams sent from the radio. Use it when connecting over a slow or congested link — such as a cellular hotspot, a long-distance VPN, or a satellite connection — to reduce dropouts and improve stability.

## Before you start

- AetherSDR must be open and not yet connected to a radio, or you must disconnect first before changing this setting.
- Know which connection mode you are using: Local, SmartLink, or Manual. The `LowBandwidthMode` checkbox is present on the connection panel regardless of mode.

## Steps

1. Open the connection panel. It appears automatically before a radio is connected. If a radio is already connected, click `Settings > Connect to Radio...` and disconnect first.
2. Locate the **Use low bandwidth mode** checkbox near the bottom of the connection panel.
3. Check **Use low bandwidth mode** to enable reduced-rate streams.
4. Proceed to connect using your preferred mode — **Local**, **SmartLink**, or **Manual** — as normal.

## What each control does

| Control | Kind | Default |
|---|---|---|
| Local / SmartLink / Manual (mode buttons) | Radio button | Local |
| Available radios | List | (not set) |
| Connect Selected Radio | Push button | — |
| No local radios found yet | Indicator | — |
| Retry Discovery | Push button | — |
| Remote with SmartLink | Push button | — |
| Connect by IP | Push button | — |
| Open Network Diagnostics | Push button | — |
| SmartLink account: Email | Text field | (not set) |
| SmartLink account: Password | Text field | (not set) |
| Sign In | Push button | — |
| Sign Out | Push button | — |
| Remote radios | List | (not set) |
| Connect Remote Radio | Push button | — |
| Radio IP address | Text field. Stores up to three recently used IP addresses. Select a previous address from the drop-down or type a new one. The field replaces the plain text entry used in earlier versions. Stored as `ManualRadioIp`; recent entries stored as `RecentConnectByIpAddresses`. | (not set) |
| Network Diagnostics | Push button | — |
| Connect by IP (manual) | Push button | — |
| Advanced: Source path | Combo box | (not set) |
| Use low bandwidth mode | Checkbox | (not set) |
| Enable adaptive frame-rate throttle | Checkbox | False. When checked, AetherSDR automatically reduces FFT/waterfall frame rate when network quality degrades. This helps maintain stability on slow or congested links without requiring manual changes. Stored as `AdaptiveThrottleEnabled`. |
| Connect to last radio on start up | Checkbox. When checked, AetherSDR auto-connects to the last used radio on startup and on broadcast-discovery / routed-radio probe. When unchecked, the connection dialog opens and the user must pick a radio manually each session. Stored as `AutoConnectToLastRadio`. | True (checked). New in v0.9.7. Existing users keep previous behavior automatically. |
| Disconnect | Push button | — |

## Indicators

| Indicator | Meaning |
|---|---|
| Status label | Current connection state (searching / connecting / connected / errored). |
| Manual result label | Result text after probing a manual IP (success or error). |
| Source warning label | Warns when the selected source NIC is stale or unreachable. |

## Tips

- Enable **Use low bandwidth mode** or **Enable adaptive frame-rate throttle** before initiating the connection. These settings are negotiated at connect time.
- The adaptive throttle works alongside low-bandwidth mode. If you enable only the adaptive throttle, AetherSDR will reduce frame rates when needed but keep the full stream rate otherwise.
- If audio still breaks up after enabling these options, check your VPN or routing path using `Settings > Network...`.
- The **Radio IP address** field now remembers up to three recent addresses. If you previously saved an IP under the legacy `LastRoutedRadioIp` setting, AetherSDR migrates it automatically the first time you open the connection panel.
- To prevent AetherSDR from connecting automatically at startup — for example, when you want to choose a different radio — uncheck **Connect to last radio on start up**.
- The connection panel now uses a frameless window with a custom title bar when **FramelessWindow** is enabled in settings (default: True). The **Connect to Radio** title appears in the window title bar. To resize the dialog, drag from any edge or corner. When the frameless window is hidden and then shown again, its previous geometry is preserved.
- When probing a manual IP, AetherSDR collects radio status information such as model, nickname, callsign, and MultiFlex status during the connection negotiation. This information appears in the radio list after a successful probe.
- The SmartLink login form now includes accessibility hints for password managers on macOS, Windows, and Linux. Password managers can recognize and auto-fill credentials for the SmartLink account fields.

## Related

- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)
- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Pick the local network interface used for a manual connection](../../getting-started/setup/pick-the-local-network-interface-used-for-a-manual-connection.md)
- [Operating remotely over SmartLink](../../operating/remote/remote-operation-smartlink.md)