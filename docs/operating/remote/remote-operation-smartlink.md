# Operating Remotely over SmartLink

SmartLink lets you connect to a FLEX-8600 that is at a different location from your computer. This page covers how to sign in to your SmartLink account and connect to a remote radio from AetherSDR's connection screen.

## Before you start

- Your FLEX-8600 must be powered on and connected to the internet at the remote location, with SmartLink enabled in its firmware.
- You must have a FlexRadio SmartLink account (email and password).
- AetherSDR must not already be connected to a radio. If it is, disconnect first.

## Steps

1. Open the connection screen. It appears automatically when no radio is connected. You can also reach it via `Settings > Connect to Radio...`.
2. Click **Remote with SmartLink**. This selects the SmartLink mode and shows the SmartLink account and remote radio controls.
3. In the **SmartLink account: Email** field, enter your FlexRadio account email address.
4. In the **SmartLink account: Password** field, enter your password. The password is not saved between sessions. The field is tagged with accessibility names for password managers (macOS Passwords, Windows Authenticator, KDE Wallet).
5. Click **Sign In**. The status label updates to show the progress of authentication.
6. Once signed in, the **Remote radios** list populates with the radios available to your account. Select the radio you want to use.
7. If your link to the remote site is slow (satellite, cellular, or congested broadband), check **Use low bandwidth mode** before connecting.
8. Click **Connect Remote Radio**. The status label tracks the connection progress. When the connection succeeds, the main AetherSDR interface opens.

## What each control does

| Control | What it does | Persisted setting |
|---|---|---|
| **Local / SmartLink / Manual** (mode buttons) | Switches the connection screen among the three connection modes. Each button is identified in the accessibility tree to support automated testing. | `ConnectionMode` |
| **Remote with SmartLink** (mode button) | Switches the connection screen to SmartLink mode. | `ConnectionMode` |
| **SmartLink account: Email** | Your FlexRadio account email. | `SmartLinkEmail` |
| **SmartLink account: Password** | Your SmartLink password. Not saved after the session ends. | — |
| **Sign In** | Authenticates with SmartLink and populates the **Remote radios** list. | — |
| **Sign Out** | Logs out of SmartLink and clears the remote radio list. | — |
| **Remote radios** | Lists SmartLink WAN radios available to the signed-in account. The list has a fixed display height; if you have many remote radios, scroll within the list to see all of them. | — |
| **Use low bandwidth mode** | Reduces stream data rates for slow or metered links. | `LowBandwidthMode` |
| **Enable adaptive frame-rate throttle** | Automatically reduces FFT/waterfall frame rate when network quality degrades. | `AdaptiveThrottleEnabled` |
| **Connect Remote Radio** | Starts a WAN connection to the radio selected in **Remote radios**. | — |
| **Connect to last radio on start up** | When checked, AetherSDR auto-connects to the last used radio on startup and on broadcast-discovery / routed-radio probe. When unchecked, the connection dialog opens and the user must pick a radio manually each session. Defaults to checked. | `AutoConnectToLastRadio` |
| **Disconnect** | Disconnects from the current radio and returns to the connection screen. | — |

## Connecting by IP (Manual mode)

If your radio is on a VPN or a routed network that is not visible via LAN discovery, use Manual mode instead of SmartLink.

1. Click **Connect by IP** on the Local page, or click the **Manual** mode button at the top of the connection screen.
2. In the **Radio IP address** field, type the IP address of the radio. The field accepts IPv4 and IPv6 addresses. AetherSDR normalizes the address when you connect.
3. The **Radio IP address** control is a drop-down as well as a text field. It stores up to three recently used addresses (saved as `RecentConnectByIpAddresses`). To reuse a previous address, click the drop-down arrow and select it from the list.
4. If needed, select the local network interface to use in **Advanced: Source path**. A **Source warning label** appears beneath the selector if the chosen interface is stale or unreachable.
5. Click **Connect by IP (manual)**. The **Manual result label** shows whether the probe succeeded or failed.

## Managing radio nicknames

Right-click any radio in the **Available radios** list on the Local page to set a custom nickname. This is useful for distinguishing between multiple radios that report similar discovery names. The nickname is saved keyed by serial number and appears on future discovery sweeps. This feature is available only for radios that do not have an on-radio name store (such as HL2 or simulator radios); FlexRadio radios set their name from Radio Setup while connected and are not affected by client-side nicknames.

## Tips

- `SmartLinkEmail` is persisted, so your email address is pre-filled the next time you open the connection screen. Your password is not persisted and must be entered each session.
- If the **Remote radios** list is empty after signing in, the remote radio may not have SmartLink enabled, or it may be offline.
- The **Radio IP address** drop-down remembers up to three recent addresses across sessions. If you previously used the `LastRoutedRadioIp` setting (from a version before v0.9.7), AetherSDR imports it automatically into the recent-address list on first launch.
- **Connect to last radio on start up** is checked by default. If you work with multiple radios and want to choose explicitly each session, uncheck it.
- The SmartLink login form is identified in the accessibility tree as "SmartLink account login", making it easier for password managers to associate the credential fields with this specific login form.
- The **Enable adaptive frame-rate throttle** checkbox is unchecked by default. When enabled, AetherSDR automatically lowers the FFT and waterfall frame rate when network quality degrades, helping maintain a stable connection on variable-quality links.
- The **Available radios** list on the Local page has a fixed maximum height so that the list scrolls internally when many radios are discovered. On small displays (for example, a 1024×600 panel), this prevents the Connect button and lower radios from becoming unreachable. The list shows a vertical scrollbar as needed.
- Right-click context menus on the **Available radios** list are read by screen readers and reported as "available local radios" with an accessible description of "Discovered FlexRadio radios on the local network".

## Troubleshooting

- **Remote radios list is empty after Sign In** — The radio at the remote location may be offline or SmartLink may not be enabled on it. Confirm the radio is powered on and registered to the same FlexRadio account.
- **Sign In fails or the status label shows an error** — Check that your email and password are correct. Verify that AetherSDR has outbound internet access and that no firewall or proxy is blocking the SmartLink connection.
- **Audio is choppy or drops frequently** — Enable **Use low bandwidth mode** before connecting to reduce stream rates for the link. For variable-quality connections, also enable **Enable adaptive frame-rate throttle** to automatically adjust display update rates.
- **Manual connection fails or the Manual result label shows an error** — Confirm the IP address is correct and reachable from this machine. Check that the selected source interface in **Advanced: Source path** is active; dismiss any **Source warning label** by selecting a valid interface.
- **AetherSDR connects to the wrong radio on startup** — Uncheck **Connect to last radio on start up** so the connection screen opens on every launch and you can select the intended radio.
- **Connection dialog appears with incorrect geometry after exiting full-screen or frameless mode** — If you had the connection dialog in frameless mode and it was hidden when the window was restored, the dialog preserves its position only when it was visible at the time of restoration. This prevents the dialog from appearing off-screen.
- **Available radios list only shows a few entries and does not scroll** — The list has a maximum height of 240 pixels. If more radios are discovered than fit, the vertical scrollbar appears automatically. Use the scroll wheel or drag the scrollbar to see the rest of the list.

## Related

- [Connect to a Radio overview](../../features/connection/overview.md)
- [Log in to SmartLink to see remote radios](../../features/connection/log-in-to-smartlink-to-see-remote-radios.md)
- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- [Disconnect from the current radio](../../getting-started/setup/disconnect-from-the-current-radio.md)
- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)