# Connect to a Radio

The Connection Panel is the main screen for discovering and connecting to a FLEX-8600 radio. It provides three connection modes: Local (LAN discovery), SmartLink (remote via internet), and Manual (direct IP or VPN). The panel appears automatically when AetherSDR starts and no radio is connected, or you can open it at any time from `Settings > Connect to Radio...`.

## Before you start

- AetherSDR must not already be connected to a radio.
- The panel now opens as a frameless dialog. You can drag it by the title bar at the top.

## Steps

### Connect to a local LAN radio

1. Open the connection panel. By default, the Local tab is active.
2. Wait for AetherSDR to discover radios on the local network. The `Available radios` list populates automatically.
3. Select a radio from the list.
4. Click `Connect Selected Radio`.

### Connect to a remote radio through SmartLink

1. Open the connection panel.
2. Click `Remote with SmartLink`. The panel switches to the SmartLink page.
3. Under **SmartLink account**, enter your FlexRadio account email in the `SmartLink account: Email` field.
4. Enter your password in the `SmartLink account: Password` field. The password is not saved between sessions.
5. Click `Sign In`. AetherSDR authenticates with SmartLink and, if successful, populates the `Remote radios` list with the radios available to your account.
6. Select a radio from the `Remote radios` list.
7. Click `Connect Remote Radio`.

### Connect by IP address (manual or VPN)

1. Open the connection panel.
2. Click `Connect by IP` (from the Local page) or select the Manual page directly.
3. In the `Radio IP address` field, enter the IP address or hostname of the radio.
4. (Optional) Select a network interface from the `Advanced: Source path` drop-down to bind the connection to a specific NIC.
5. (Optional) Check `Use low bandwidth mode` for reduced-rate streams on slow links.
6. Click `Connect by IP (manual)`.

### Additional controls

- `Open Network Diagnostics` — Opens a diagnostics dialog for troubleshooting network connectivity.
- `Retry Discovery` — Re-runs LAN discovery on the Local page.
- `Disconnect` — Disconnects from the current radio and returns to the connection panel.
- `Connect to last radio on start up` — When checked (default), AetherSDR automatically reconnects to the last used radio on startup. When unchecked, the connection panel opens each session.
- `Enable adaptive frame-rate throttle` — When checked, AetherSDR automatically reduces FFT and waterfall frame rates when network quality degrades, helping to maintain a stable connection on slower or congested links.

## What each control does

| Control | What it does | Persisted setting |
|---|---|---|
| Local / SmartLink / Manual mode buttons | Switch the panel among the three connection modes. | `ConnectionMode` |
| `Available radios` | Lists LAN radios discovered via mDNS/Flex discovery. | — |
| `Connect Selected Radio` | Connects to the highlighted LAN radio. | — |
| `No local radios found yet` | Callout shown when discovery is empty. | — |
| `Retry Discovery` | Re-runs LAN discovery. | — |
| `Remote with SmartLink` | Shortcut to the SmartLink page. | — |
| `Connect by IP` | Shortcut to the Manual page. | — |
| `Open Network Diagnostics` | Opens the network diagnostics dialog. | — |
| `SmartLink account: Email` | Your FlexRadio account email address. | `SmartLinkEmail` |
| `SmartLink account: Password` | Your SmartLink password. Not saved after the session ends. | — |
| `Sign In` | Authenticates with SmartLink and retrieves the list of remote radios. | — |
| `Sign Out` | Ends the current SmartLink session. | — |
| `Remote radios` | Lists the WAN radios available to your account after sign-in. | — |
| `Connect Remote Radio` | Starts a WAN connection to the selected remote radio. | — |
| `Radio IP address` | The IP address or hostname to connect to in Manual mode. Editable combo box that remembers the last three addresses you successfully connected to. | `ManualRadioIp` |
| `Advanced: Source path` | Picks the local network interface used for the manual connection. | `ManualBindSource` |
| `Use low bandwidth mode` | Enables reduced-rate streams for slow links. | `LowBandwidthMode` |
| `Connect by IP (manual)` | Starts the manual/VPN connection. | — |
| `Connect to last radio on start up` | When checked, auto-connects to the last used radio on startup. Defaults to checked. | `AutoConnectToLastRadio` |
| `Enable adaptive frame-rate throttle` | Automatically reduces FFT/waterfall frame rate when network quality degrades. | `AdaptiveThrottleEnabled` |
| `Disconnect` | Disconnects from the current radio. | — |

## Status indicators

| Indicator | Meaning |
|---|---|
| Status label | Current connection state: searching, connecting, connected, or errored. |
| Manual result label | Result text after probing a manual IP (success or error). |
| Source warning label | Warns when the selected source NIC is stale or unreachable. |

## Tips

- The connection panel now appears as a frameless dialog. Drag it by the title bar at the top.
- `SmartLinkEmail` is persisted, so your email address is pre-filled on the next launch. Your password is never stored.
- After signing in to SmartLink, the status label shows your name, callsign, or confirmation that you are signed in.
- The `Remote radios` list is sized for compact display; scroll within the list if the radio you want is not immediately visible.
- The `Radio IP address` field stores up to three recent addresses. If you previously used the `LastRoutedRadioIp` setting, AetherSDR imports it automatically the first time you open the Manual page after upgrading.
- On the Local page, you can quickly switch to SmartLink or Manual mode using the shortcut buttons.
- When switching to or from frameless mode, AetherSDR preserves the dialog geometry only if the dialog was visible at the time of the switch.
- The SmartLink login form now includes accessibility hints for password managers (macOS Passwords, Windows Authenticator, KDE Wallet). The email and password fields are labeled as a "SmartLink login form" so credential managers can correctly scope the account pair.

## Troubleshooting

- **`Available radios` list is empty** — Ensure the radio is powered on and on the same local network. Click `Retry Discovery` to refresh the list.
- **`Remote radios` list is empty after sign-in** — The remote radio may be powered off, not registered with SmartLink, or associated with a different FlexRadio account.
- **`Sign In` produces an error** — Check that your email and password are correct. Verify your credentials at the FlexRadio website.
- **Cannot connect by IP** — Ensure the radio is reachable on the network. Use `Open Network Diagnostics` to check connectivity.
- **AetherSDR connects to the wrong radio on startup** — Uncheck `Connect to last radio on start up` if you want to choose a radio manually each session.

## Related

- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Connect to a local LAN radio](../../getting-started/setup/connect-to-a-local-lan-radio.md)
- [Enable low-bandwidth mode for slow links](enable-low-bandwidth-mode-for-slow-links.md)
- [Operating remotely over SmartLink](../../operating/remote/remote-operation-smartlink.md)