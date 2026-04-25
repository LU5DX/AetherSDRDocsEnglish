# Log in to SmartLink to see remote radios

SmartLink lets you reach a FLEX-8600 at a remote location over the internet. This page covers how to sign in to your FlexRadio SmartLink account so that AetherSDR can list the radios available to it.

## Before you start

- You must have a FlexRadio account with SmartLink access. If you do not have one, create it at the FlexRadio website before continuing.
- The remote radio must already be registered with SmartLink and powered on.
- AetherSDR must not already be connected to a radio. The connection panel appears automatically when no radio is connected.

## Steps

1. Open the connection panel. If AetherSDR is already showing the main interface, go to `Settings > Connect to Radio...`.
2. Click `Remote with SmartLink`. The panel switches to the SmartLink page.
3. Under **SmartLink account**, enter your FlexRadio account email in the `SmartLink account: Email` field.
4. Enter your password in the `SmartLink account: Password` field. The password is not saved between sessions.
5. Click `Sign In`. AetherSDR authenticates with SmartLink and, if successful, populates the `Remote radios` list with the radios available to your account.

## What each control does

| Control | What it does | Persisted setting |
|---|---|---|
| `Remote with SmartLink` mode button | Switches the panel to the SmartLink page. | `ConnectionMode` |
| `SmartLink account: Email` | Your FlexRadio account email address. | `SmartLinkEmail` |
| `SmartLink account: Password` | Your SmartLink password. Not saved after the session ends. | — |
| `Sign In` | Authenticates with SmartLink and retrieves the list of remote radios. | — |
| `Remote radios` | Lists the WAN radios available to your account after sign-in. | — |
| `Sign Out` | Ends the current SmartLink session. | — |

## Tips

- `SmartLinkEmail` is persisted, so your email address is pre-filled on the next launch. Your password is never stored.
- After signing in, the status label below the account group shows your name, callsign, or confirmation that you are signed in, depending on what your account profile contains.

## Troubleshooting

- **`Remote radios` list is empty after sign-in** — The remote radio may be powered off, not registered with SmartLink, or associated with a different FlexRadio account. Confirm the radio is on and registered under the same account you used to sign in.
- **`Sign In` produces an error** — Check that your email and password are correct. A typo in the email field is a common cause because the field has no auto-correct. Verify your credentials at the FlexRadio website.
- **The SmartLink page is not reachable** — Firewall or VPN software on this machine may be blocking outbound SmartLink traffic. Use `Open Network Diagnostics` (available on the Local page) to check connectivity, or see [Connect by IP across a VPN or routed network](../../getting-started/setup/connect-by-ip-across-a-vpn-or-routed-network.md) if your setup requires a direct IP path instead.

## Related

- [Connect to a remote radio through SmartLink](../../getting-started/setup/connect-to-a-remote-radio-through-smartlink.md)
- [Connect to a local LAN radio](../../getting-started/setup/connect-to-a-local-lan-radio.md)
- [Enable low-bandwidth mode for slow links](enable-low-bandwidth-mode-for-slow-links.md)
- [Operating remotely over SmartLink](../../operating/remote/remote-operation-smartlink.md)
