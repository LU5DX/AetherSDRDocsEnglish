# Change Network MTU for VPN/Remote Setups

The Network MTU setting controls the maximum transmission unit size (in bytes) the radio uses for outgoing network packets. Lowering it prevents packet fragmentation when the radio's traffic passes through a VPN tunnel or other link with a reduced path MTU.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is not available while disconnected.
- Know the MTU of your VPN tunnel or remote link. A common starting value for OpenVPN or WireGuard tunnels is 1400 bytes.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Locate the **Network MTU:** spinbox.
4. Set the value to match or stay below your tunnel's MTU.
5. Click **Apply** to push the new MTU to the radio.

## What each control does

| Control | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Network MTU:** | Sets the outgoing MTU in bytes for radio network traffic. | — | — | — |
| **Apply** | Pushes the current Network tab configuration, including the MTU value, to the radio. | — | — | — |

## Tips

- Changes take effect on the radio immediately after you click **Apply**. You do not need to disconnect and reconnect.
- If audio cuts out or the panadapter stalls intermittently over a VPN, also consider increasing **Audio Buffer:** (50–1000 ms) on the **Audio** tab to absorb added jitter.

## Troubleshooting

- **Apply has no visible effect** — Confirm AetherSDR is still connected to the radio. The Network tab requires an active radio connection. Disconnect and reconnect, then try again.
- **Audio still drops after lowering MTU** — Packet loss and jitter from the VPN may also require a larger audio buffer. See [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md).

## Related

- [Switch the radio between DHCP and static IP](switch-the-radio-between-dhcp-and-static-ip.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
