# Change Network MTU for VPN/Remote Setups

The Network MTU setting controls the maximum packet size the radio sends over the network. Lowering it prevents fragmentation when you connect through a VPN or other tunnel that reduces the available path MTU.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is not accessible when disconnected.
- Know the MTU of your VPN tunnel or network path. Common VPN MTUs are 1400–1450 bytes; a standard Ethernet path is 1500 bytes.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Locate the **Network MTU:** spinbox.
4. Set the value to match your network path MTU.
5. Click **Apply** to push the new MTU to the radio.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Network MTU:** | Outgoing packet size in bytes. Lower this when operating over a VPN or any link with a reduced MTU. | — | — | — |
| **Apply** | Sends the current Network tab configuration, including the MTU value, to the radio. | — | — | — |

## Tips

- If you are unsure what MTU to use, start at 1400 bytes and increase until you see packet loss or audio dropouts, then step back down by 10–20 bytes.
- The **Audio Buffer:** setting (found on the **Audio** tab) can help absorb jitter on VPN links independently of the MTU setting. See [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md).

## Troubleshooting

- **Apply has no visible effect** — Confirm the radio is still connected. If the connection dropped, reconnect via `Settings > Connect to Radio...` and repeat the steps.
- **Audio breaks up after changing MTU** — The new value may still be too large for the path. Lower **Network MTU:** by another 20–50 bytes and click **Apply** again.

## Related

- [Switch the radio between DHCP and static IP](switch-the-radio-between-dhcp-and-static-ip.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
