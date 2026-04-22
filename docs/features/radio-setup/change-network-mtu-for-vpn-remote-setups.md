# Change Network MTU for VPN/Remote Setups

Adjust the MTU value the radio uses for outgoing packets. Lowering the MTU prevents packet fragmentation when connecting over a VPN or WAN link where the path MTU is smaller than the default.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is only accessible with an active radio connection.
- Know the MTU of your VPN tunnel or remote network path. A common starting value for OpenVPN or WireGuard tunnels is 1400 bytes; consult your VPN provider or router documentation if unsure.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Locate the **Network MTU:** spinbox.
4. Set the value to match your network path MTU.
5. Click **Apply** to push the new MTU to the radio.

## What each control does

| Control | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Network MTU:** | Sets the outgoing packet MTU in bytes on the radio. | — | — | — |
| **Apply** | Pushes the current network configuration, including the MTU value, to the radio. | — | — | — |

## Tips

- If you also experience audio dropouts or choppy audio over the same VPN link, consider increasing **Audio Buffer:** (50–1000 ms) on the **Audio** tab to absorb jitter introduced by the tunnel.

## Troubleshooting

- **Audio or data stream drops after changing MTU** — The new value may be too low or too high for the path. Verify the MTU of every hop between the radio and your client, then set **Network MTU:** to the lowest MTU found on that path. Click **Apply** again after each adjustment.
- **Apply has no visible effect** — Confirm the radio is still connected. The **Network** tab requires an active radio connection. If the connection dropped, reconnect and retry.

## Related

- [Switch the radio between DHCP and static IP](switch-the-radio-between-dhcp-and-static-ip.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
