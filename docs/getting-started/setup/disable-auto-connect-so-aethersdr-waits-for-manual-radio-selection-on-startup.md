# Disable auto-connect so AetherSDR waits for manual radio selection on startup

By default, AetherSDR reconnects to the last used radio every time it starts. Disabling this makes AetherSDR open the connection dialog on startup instead, so you can choose a radio manually each session.

## Before you start

- AetherSDR must be running.
- No radio connection is required to change this setting.

## Steps

1. Click `Settings > Connect to Radio...`.
2. In the "Connect to a Radio" panel, scroll to the bottom of the page.
3. Locate the checkbox labelled "Connect to last radio on start up".
4. Uncheck "Connect to last radio on start up".

The setting is saved immediately to `AutoConnectToLastRadio`. The next time AetherSDR starts, it will open the connection dialog automatically instead of reconnecting to the last radio.

## What each control does

| Control | Default | Persisted setting | Behavior |
|---|---|---|---|
| "Connect to last radio on start up" checkbox | Checked (True) | `AutoConnectToLastRadio` | When checked, AetherSDR auto-connects to the last used radio on startup. When unchecked, the connection dialog opens on startup and you must select a radio manually. |

## Tips

- This setting also suppresses the automatic connection attempt that occurs during broadcast discovery and routed-radio probing, not only the initial startup reconnect.
- If you share the computer across multiple stations or switch between radios frequently, leaving this unchecked avoids connecting to the wrong radio by accident.

## Troubleshooting

- **AetherSDR still auto-connects after unchecking the box** — Confirm you unchecked the box inside `Settings > Connect to Radio...` and not a different dialog. The checkbox label is exactly "Connect to last radio on start up". Quit and relaunch AetherSDR to verify the change takes effect.

## Related

- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Disconnect from the current radio](disconnect-from-the-current-radio.md)
