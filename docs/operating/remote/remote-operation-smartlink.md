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
4. In the **SmartLink account: Password** field, enter your password. The password is not saved between sessions.
5. Click **Sign In**. The status label updates to show the progress of authentication.
6. Once signed in, the **Remote radios** list populates with the radios available to your account. Select the radio you want to use.
7. If your link to the remote site is slow (satellite, cellular, or congested broadband), check **Use low bandwidth mode** before connecting.
8. Click **Connect Remote Radio**. The status label tracks the connection progress. When the connection succeeds, the main AetherSDR interface opens.

## What each control does

| Control | What it does | Persisted setting |
|---|---|---|
| **Remote with SmartLink** (mode button) | Switches the connection screen to SmartLink mode. | `ConnectionMode` |
| **SmartLink account: Email** | Your FlexRadio account email. | `SmartLinkEmail` |
| **SmartLink account: Password** | Your SmartLink password. Not saved after the session ends. | — |
| **Sign In** | Authenticates with SmartLink and populates the **Remote radios** list. | — |
| **Sign Out** | Logs out of SmartLink and clears the remote radio list. | — |
| **Remote radios** | Lists SmartLink WAN radios available to the signed-in account. | — |
| **Use low bandwidth mode** | Reduces stream data rates for slow or metered links. | `LowBandwidthMode` |
| **Connect Remote Radio** | Starts a WAN connection to the radio selected in **Remote radios**. | — |

## Tips

- `SmartLinkEmail` is persisted, so your email address is pre-filled the next time you open the connection screen. Your password is not persisted and must be entered each session.
- If the **Remote radios** list is empty after signing in, the remote radio may not have SmartLink enabled, or it may be offline.

## Troubleshooting

- **Remote radios list is empty after Sign In** — The radio at the remote location may be offline or SmartLink may not be enabled on it. Confirm the radio is powered on and registered to the same FlexRadio account.
- **Sign In fails or the status label shows an error** — Check that your email and password are correct. Verify that AetherSDR has outbound internet access and that no firewall or proxy is blocking the SmartLink connection.
- **Audio is choppy or drops frequently** — Enable **Use low bandwidth mode** before connecting to reduce stream rates for the link.

## Related

- [Connect to a Radio overview](../../features/connection/overview.md)
- [Log in to SmartLink to see remote radios](../../features/connection/log-in-to-smartlink-to-see-remote-radios.md)
- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Enable low-bandwidth mode for slow links](../../features/connection/enable-low-bandwidth-mode-for-slow-links.md)
- [Disconnect from the current radio](../../getting-started/setup/disconnect-from-the-current-radio.md)
- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)
