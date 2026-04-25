# Change network MTU for VPN/remote setups

Lowering the network MTU prevents IP fragmentation when your radio traffic passes through a VPN tunnel or a WAN link with a smaller path MTU than Ethernet's default. Set this value on the radio so that outgoing packets fit inside the tunnel without being dropped or reassembled.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is not accessible while disconnected.
- Know the MTU of your VPN tunnel or remote link. A common starting point for OpenVPN is 1400 bytes; WireGuard tunnels often use 1420 bytes.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Locate the **Network MTU:** spinbox.
4. Set the value in bytes to match your tunnel's MTU.
5. Click **Apply** to push the new MTU to the radio.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Network MTU:** | Outgoing MTU in bytes sent by the radio. Lower this when packets are fragmented or dropped over a VPN or WAN path. | — | — | — |
| **Apply** | Pushes the current network configuration, including the MTU value, to the radio. | — | — | — |

## Tips

- If audio stutters or panadapter data drops intermittently over a VPN, also increase **Audio Buffer:** (found on the **Audio** tab) to compensate for added jitter. That setting accepts values between 50 and 1000 ms.
- The **IP Address / Mask / MAC Address** fields on the same tab are read-only and confirm which interface the radio is using.

## Troubleshooting

- **Apply has no visible effect** — Verify the radio is still connected. If the connection dropped, close and reopen `Settings > Radio Setup...`, reconnect, and apply again.
- **Audio still drops after lowering MTU** — The MTU controls outgoing radio packets. Also check that your host OS network interface MTU is set to the same value or lower, and consider raising **Audio Buffer:** on the **Audio** tab.

## Related

- [Switch the radio between DHCP and static IP](switch-the-radio-between-dhcp-and-static-ip.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
