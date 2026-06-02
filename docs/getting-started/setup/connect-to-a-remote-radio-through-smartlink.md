# Connect to a Remote Radio Through SmartLink

SmartLink lets you connect to a FLEX-8600 that is at a different location from your computer. Use this procedure when the radio is not on your local LAN and you have a FlexRadio SmartLink account.

## Before you start

- You have a FlexRadio SmartLink account (email and password).
- The FLEX-8600 at the remote station is powered on and registered to your SmartLink account.
- AetherSDR is running and no radio is currently connected.

## Steps

1. Open the Connection Panel. It appears automatically when no radio is connected. If a radio is already connected, go to `Settings > Connect to a Radio...` to open it.
2. Click **Remote with SmartLink** in the mode button row at the top of the panel. The panel switches to the SmartLink page. This sets `ConnectionMode` to `SmartLinkMode`.
3. In the **SmartLink account** group, enter your FlexRadio account email in the **Email** field. AetherSDR saves this value as `SmartLinkEmail`.
4. Enter your password in the **Password** field. The password is not saved after you close the application.
5. Click **Sign In**. AetherSDR authenticates with SmartLink. Wait for the status label to confirm you are signed in.
6. In the **Remote radios** list, click the radio you want to connect to.
7. Click **Connect Remote Radio**. AetherSDR establishes a WAN connection to the selected radio.

## What each control does

| Control | Description | Persisted key |
|---|---|---|
| **Remote with SmartLink** mode button | Switches the panel to SmartLink mode. | `ConnectionMode` |
| **Email** field | Your FlexRadio SmartLink account email address. | `SmartLinkEmail` |
| **Password** field | Your SmartLink password. Not saved between sessions. | — |
| **Sign In** | Authenticates with SmartLink and populates the **Remote radios** list. | — |
| **Sign Out** | Logs out of SmartLink and clears the radio list. | — |
| **Remote radios** list | Shows all FLEX-8600 radios registered to your SmartLink account that are currently online. The list has a fixed display height; if you have many radios, scroll within the list. | — |
| **Connect Remote Radio** | Starts a WAN connection to the radio selected in the **Remote radios** list. This button appears below the list, outside the radios group. | — |
| **Use low bandwidth mode** checkbox | Enables reduced-rate audio and data streams. Use this on slow or metered internet connections. | `LowBandwidthMode` |
| **Enable adaptive frame-rate throttle** checkbox | Automatically reduces FFT/waterfall frame rate when network quality degrades. This helps maintain performance on variable-speed links. | `AdaptiveThrottleEnabled` |
| **Connect to last radio on start up** checkbox | When checked, AetherSDR auto-connects to the last used radio on startup and on broadcast-discovery / routed-radio probe. When unchecked, the connection dialog opens and the user must pick a radio manually each session. Defaults to checked. Added in v0.9.7. | `AutoConnectToLastRadio` |
| **Open Network Diagnostics** | Opens the Network Diagnostics dialog to help troubleshoot connection issues. | — |
| **Source path** combo box (Advanced) | Picks the local network interface used for the manual connection. Available on the Manual page. | `ManualBindSource` |
| **Connect by IP (manual)** | Starts a manual or VPN connection to the IP address entered in the **Radio IP address** field. | — |

## Tips

- If the connection is sluggish or audio breaks up, enable **Use low bandwidth mode** before clicking **Connect Remote Radio**.
- For variable-speed network links (e.g., cellular), enable **Enable adaptive frame-rate throttle** to let AetherSDR automatically adjust FFT/waterfall frame rates when network quality changes.
- The status label below the controls shows the current connection state. If it shows an error, sign out and sign in again to refresh the SmartLink session.
- **Connect to last radio on start up** is checked by default so that existing users keep their previous behavior after upgrading. Uncheck it if you want to choose a radio manually at each startup.
- SmartLink login fields now include accessibility hints and object names that help password managers (macOS Passwords, Windows Authenticator, KDE Wallet) correctly associate your credentials with the SmartLink login form.

## Troubleshooting

- **Remote radios list is empty after signing in** — The remote radio may be offline or not registered to this account. Confirm the radio at the remote station is powered on and that you are signed in with the correct account.
- **Sign In does not respond** — Check your internet connection. If you are behind a restrictive firewall, SmartLink traffic may be blocked. Use the **Open Network Diagnostics** button to verify connectivity.
- **Status label shows an error after clicking Connect Remote Radio** — Another client may already hold the maximum number of connections allowed by the radio. Ask any other operators to disconnect, then retry.

## Related

- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Operating remotely over SmartLink](../../operating/remote/remote-operation-smartlink.md)
- [Disconnect from the current radio](disconnect-from-the-current-radio.md)
- Network Diagnostics