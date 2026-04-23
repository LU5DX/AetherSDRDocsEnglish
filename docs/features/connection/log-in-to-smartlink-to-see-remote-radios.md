# Log in to SmartLink to see remote radios

SmartLink lets you see and connect to a Flex radio that is at a different location from your computer. This page covers signing in to your SmartLink account so that remote radios appear in the list.

## Before you start

- You have a FlexRadio SmartLink account (email and password).
- The computer running AetherSDR has internet access.
- AetherSDR is open and no radio is currently connected (the connection panel is visible).

## Steps

1. Open the connection panel. If it is not already visible, go to `Settings > Connect to Radio...`.
2. Click **Remote with SmartLink**. This switches the panel to the SmartLink page.
3. In the **SmartLink account** group, enter your FlexRadio account email in the **Email** field.
4. Enter your password in the **Password** field. The password is not saved between sessions.
5. Click **Sign In**.
6. Wait for the status label to update. When authentication succeeds, your name, callsign, or "Signed in to SmartLink" appears above the radio list.
7. The **Remote radios** list populates with the radios available to your account.

To end the session, click **Sign Out**.

## What each control does

| Control | What it does | Persisted setting |
|---|---|---|
| **Remote with SmartLink** mode button | Switches the panel to the SmartLink page. | `ConnectionMode` |
| **Email** field | Your FlexRadio account email address. | `SmartLinkEmail` |
| **Password** field | Your FlexRadio account password. Not saved between sessions. | — |
| **Sign In** | Authenticates with SmartLink and requests the radio list. | — |
| **Sign Out** | Logs out of SmartLink and clears the radio list. | — |
| **Remote radios** list | Lists the SmartLink WAN radios available to your account after sign-in. | — |

## Tips

- Your email address is saved in `SmartLinkEmail` and pre-filled on the next launch. Your password is never persisted; you must re-enter it each session.
- If you see your name and callsign in the status label but the **Remote radios** list is empty, the radio at the remote station may be offline or not registered to your account.

## Troubleshooting

- **Sign In does nothing or the status label shows an error** — Check that your email and password are correct. Verify that the computer has internet access. The SmartLink service requires outbound HTTPS connectivity.
- **Remote radios list is empty after sign-in** — The remote radio may be powered off or its internet connection may be down. Confirm the radio is online at the remote location.
- **Email field is blank on launch** — `SmartLinkEmail` was not saved. Enter the address and sign in; it will be saved for future sessions after a successful interaction with the panel.

## Related

- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Connect to a local LAN radio](../../getting-started/setup/connect-to-a-local-lan-radio.md)
- [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md)
- [Enable low-bandwidth mode for slow links](enable-low-bandwidth-mode-for-slow-links.md)
- [Operating remotely over SmartLink](../../operating/remote/remote-operation-smartlink.md)
