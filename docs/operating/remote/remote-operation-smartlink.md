# Operating Remotely over SmartLink

SmartLink is FlexRadio's cloud relay service that lets you connect to a FLEX-8600 at a remote location over the internet. Use this page when your radio and computer are on different networks and you have a FlexRadio account.

## Before you start

- Your FLEX-8600 must be powered on and connected to the internet at the remote site.
- You must have a FlexRadio account (email and password) with SmartLink access enabled on that account.
- AetherSDR must be installed and running on your local machine.

## Steps

1. Open the connection screen. It appears automatically before any radio is connected. If you are already connected, go to `Settings > Connect to Radio...` to reopen it.
2. Click **Remote with SmartLink** in the row of mode buttons at the top of the panel. The panel switches to the SmartLink page.
3. In the **SmartLink account** group, enter your FlexRadio account email in the **SmartLink account: Email** field and your password in the **SmartLink account: Password** field.
4. Click **Sign In**. AetherSDR authenticates with SmartLink. The status label updates to reflect the sign-in result.
5. After a successful sign-in, the **Remote radios** list populates with radios available to your account.
6. Select the radio you want to use in the **Remote radios** list.
7. Click **Connect Remote Radio**. AetherSDR opens a WAN connection to the selected radio.

## What each control does

| Control | Description | Persisted setting key |
|---|---|---|
| **Remote with SmartLink** (mode button) | Switches the connection panel to the SmartLink page. | `ConnectionMode` |
| **SmartLink account: Email** | Your FlexRadio account email address. | `SmartLinkEmail` |
| **SmartLink account: Password** | Your FlexRadio account password. Not saved between sessions. | — |
| **Sign In** | Authenticates with SmartLink and fetches the list of remote radios. | — |
| **Sign Out** | Logs out of SmartLink and clears the remote radio list. | — |
| **Remote radios** | Lists WAN radios available to the signed-in account. | — |
| **Connect Remote Radio** | Starts a WAN connection to the selected radio. | — |
| **Use low bandwidth mode** | Reduces stream data rates for slow or congested internet links. | `LowBandwidthMode` |

## Tips

- The **SmartLink account: Password** field is not saved. You will need to enter it each time you sign in.
- If the **Remote radios** list is empty after signing in, confirm that the radio at the remote site is powered on, connected to the internet, and that SmartLink is enabled in its SmartSDR settings.
- On a slow internet connection, check **Use low bandwidth mode** before clicking **Connect Remote Radio** to reduce audio and spectrum stream bandwidth.

## Troubleshooting

- **Sign In fails or returns an error** — Verify your FlexRadio account email and password. Confirm your machine has a working internet connection. Check the status label below the sign-in form for a specific error message.
- **Remote radios list is empty after signing in** — The radio at the remote site may be offline, may not have SmartLink enabled, or may not be associated with your FlexRadio account. Confirm the remote station is on and reachable, then click **Sign Out** and sign in again to refresh the list.
- **Connection drops or is slow** — Enable **Use low bandwidth mode** and reconnect. Also check that neither site has a firewall blocking the SmartLink relay ports.

## Related

- [Log in to SmartLink to see remote radios](../../features/connection/log-in-to-smartlink-to-see-remote-radios.md)
- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- [Connect to a local LAN radio](../../getting-started/setup/connect-to-a-local-lan-radio.md)
- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)
