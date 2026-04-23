# Change Network MTU for VPN/Remote Setups

Adjust the outgoing network MTU that the Flex radio uses when sending data to clients. Lowering the MTU prevents fragmentation over VPNs and other links that have a smaller maximum packet size than a standard Ethernet connection.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is only available while a connection is active.
- Know the MTU of your VPN or remote link before changing this value. Your network administrator or VPN documentation should list it.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Locate the **Network MTU:** spinbox.
4. Set the value to match or stay below the MTU of your VPN or remote link.
5. Click **Apply** to push the new network configuration to the radio.

## What each control does

| Control | Kind | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|---|
| **Network MTU:** | Spinbox | Sets the outgoing MTU in bytes that the radio uses when sending packets. | — | — | — |
| **Apply** | Button | Pushes the current network configuration, including the MTU value, to the radio. | — | — | — |

No setting key is persisted in AetherSDR for this value; it is stored on the radio itself.

## Tips

- If you are also experiencing audio dropouts over a VPN, increase the **Audio Buffer:** value (50–1000 ms) on the **Audio** tab. A larger buffer absorbs the extra jitter that fragmented or re-ordered packets can cause on high-latency links.
- The **Enforce Private IP Connections:** toggle on the same tab restricts the radio to RFC 1918 peers. If your VPN assigns a public IP to your client interface, disable that toggle before connecting remotely.

## Troubleshooting

- **Audio cuts out or the connection drops shortly after changing the MTU** — the value may still be too large for the path. Reduce the MTU further in small steps (for example, by 50 bytes at a time) and click **Apply** after each change until the connection stabilises.
- **Apply has no visible effect** — confirm the radio is still connected. If the connection dropped, reconnect via `Settings > Connect to Radio...`, reopen `Settings > Radio Setup...`, navigate to the **Network** tab, re-enter the MTU value, and click **Apply** again.

## Related

- [Switch the radio between DHCP and static IP](switch-the-radio-between-dhcp-and-static-ip.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
