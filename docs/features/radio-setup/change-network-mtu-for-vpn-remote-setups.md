# Change Network MTU for VPN/Remote Setups

The Network MTU setting controls the maximum packet size the radio sends over the network. Lowering it prevents packet fragmentation on VPN tunnels and other links with reduced path MTU, which can otherwise cause audio dropouts or connection instability during remote operation.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is not accessible while disconnected.
- Know the MTU of your VPN tunnel or remote link. A common starting point for OpenVPN is 1400 bytes; WireGuard tunnels often use 1420 bytes.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the `Network` tab.
3. Locate the `Network MTU:` spinbox.
4. Set the value to match or stay below the MTU of your VPN or remote link.
5. Click `Apply` to push the new network configuration to the radio.

## What each control does

| Control | Kind | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|---|
| `Network MTU:` | Spinbox | Sets the outgoing packet MTU in bytes on the radio. | — | — | — |
| `Apply` | Push button | Sends the current Network tab configuration to the radio. | — | — | — |

No persisted `AppSettings` key is associated with `Network MTU:`. The value is stored on the radio, not in AetherSDR's local settings.

## Tips

- If you are also experiencing audio jitter over a VPN, consider increasing `Audio Buffer:` (50–1000 ms) on the `Audio` tab after adjusting the MTU. A larger buffer compensates for the added latency and jitter common on remote links.
- The `Enforce Private IP Connections:` toggle on the same tab rejects connections from non-RFC1918 addresses. Disable it only if your VPN assigns public-range addresses to tunnel endpoints.

## Troubleshooting

- **Audio drops or frequent disconnections after changing MTU** — The value may still be too large for the path. Reduce `Network MTU:` by 20–40 bytes and click `Apply` again. Repeat until the link is stable.
- **`Apply` has no visible effect** — Confirm the radio is still connected. The `Network` tab requires an active radio connection; if the radio disconnected between opening the dialog and clicking `Apply`, reconnect and retry.

## Related

- [Switch the radio between DHCP and static IP](switch-the-radio-between-dhcp-and-static-ip.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
