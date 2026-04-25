# Connect to a Remote Radio Through SmartLink

SmartLink lets you connect to a FLEX-8600 that is at a different location from your computer. Use this procedure when the radio is not on your local LAN and you have a FlexRadio SmartLink account.

## Before you start

- You have a FlexRadio SmartLink account (email and password).
- The FLEX-8600 at the remote station is powered on and registered to your SmartLink account.
- AetherSDR is running and no radio is currently connected.

## Steps

1. Open the ConnectionPanel. It appears automatically when no radio is connected. If a radio is already connected, go to `Settings > Connect to Radio...` to open it.
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
| **Remote radios** list | Shows all FLEX-8600 radios registered to your SmartLink account that are currently online. | — |
| **Connect Remote Radio** | Starts a WAN connection to the radio selected in the **Remote radios** list. | — |
| **Use low bandwidth mode** checkbox | Enables reduced-rate audio and data streams. Use this on slow or metered internet connections. | `LowBandwidthMode` |

## Tips

- If the connection is sluggish or audio breaks up, enable **Use low bandwidth mode** before clicking **Connect Remote Radio**.
- The status label below the controls shows the current connection state. If it shows an error, sign out and sign in again to refresh the SmartLink session.

## Troubleshooting

- **Remote radios list is empty after signing in** — The remote radio may be offline or not registered to this account. Confirm the radio at the remote station is powered on and that you are signed in with the correct account.
- **Sign In does not respond** — Check your internet connection. If you are behind a restrictive firewall, SmartLink traffic may be blocked. Use `Settings > Connect to Radio...` to reopen the panel and try again.
- **Status label shows an error after clicking Connect Remote Radio** — Another client may already hold the maximum number of connections allowed by the radio. Ask any other operators to disconnect, then retry.

## Related

- [Log in to SmartLink to see remote radios](../../features/connection/log-in-to-smartlink-to-see-remote-radios.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Operating remotely over SmartLink](../../operating/remote/remote-operation-smartlink.md)
- [Disconnect from the current radio](disconnect-from-the-current-radio.md)
