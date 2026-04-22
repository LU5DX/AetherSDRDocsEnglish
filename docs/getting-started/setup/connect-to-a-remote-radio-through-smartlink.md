# Connect to a Remote Radio through SmartLink

SmartLink lets you connect to a FLEX-8600 that is at a different location from your computer. Use this procedure when your radio is not on the same local network as AetherSDR.

## Before you start

- Your FLEX-8600 must be powered on and connected to the internet at the remote location, with SmartLink enabled in the radio's settings.
- You need a FlexRadio account (email and password) with SmartLink access for that radio.
- AetherSDR must not already be connected to a radio. If it is, disconnect first.

## Steps

1. Open the connection screen. It appears automatically when no radio is connected. You can also reach it via `Settings > Connect to Radio...`.
2. Click the **Remote with SmartLink** mode button at the top of the panel. The panel switches to the SmartLink page.
3. In the **SmartLink account** group, enter your FlexRadio account address in the **Email** field and your password in the **Password** field.
4. Click **Sign In**. AetherSDR authenticates with SmartLink and populates the **Remote radios** list with radios available to your account.
5. Select your radio in the **Remote radios** list.
6. Click **Connect Remote Radio**. AetherSDR establishes a WAN connection to the selected radio.

## What each control does

| Control | Description | Persisted setting |
|---|---|---|
| **Remote with SmartLink** mode button | Switches the panel to the SmartLink connection page. | `ConnectionMode` |
| **Email** field | Your FlexRadio account email address. | `SmartLinkEmail` |
| **Password** field | Your FlexRadio account password. Not saved between sessions. | — |
| **Sign In** | Authenticates with SmartLink and loads the remote radio list. | — |
| **Sign Out** | Logs out of SmartLink and clears the remote radio list. | — |
| **Remote radios** list | Shows all SmartLink-enabled radios available to the signed-in account. | — |
| **Connect Remote Radio** | Starts the WAN connection to the selected radio. | — |
| **Use low bandwidth mode** checkbox | Enables reduced-rate audio and data streams. Use this on slow or metered internet connections. | `LowBandwidthMode` |

## Tips

- Your email address (`SmartLinkEmail`) is saved between sessions. Your password is not — you must enter it each time.
- If you are on a slow or high-latency connection, check **Use low bandwidth mode** before clicking **Connect Remote Radio**.

## Troubleshooting

- **Remote radios list is empty after signing in** — The remote radio may not have SmartLink enabled, or it may be offline. Confirm the radio is powered on and that SmartLink is active in the radio's firmware settings.
- **Sign In fails** — Verify your email and password against your FlexRadio account. Check that your computer has internet access.
- **Connection drops or audio is broken** — Try enabling **Use low bandwidth mode** and reconnecting.

## Related

- [Log in to SmartLink to see remote radios](../../features/connection/log-in-to-smartlink-to-see-remote-radios.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Operating remotely over SmartLink](../../operating/remote/remote-operation-smartlink.md)
- [Disconnect from the current radio](disconnect-from-the-current-radio.md)
