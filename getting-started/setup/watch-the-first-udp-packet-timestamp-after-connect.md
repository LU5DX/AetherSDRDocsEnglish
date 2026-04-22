# Watch the First-UDP-Packet Timestamp After Connect

Use the **First UDP Packet** indicator in Network Diagnostics to confirm that the UDP data path from the radio has been established after connecting.

## Before you start

- AetherSDR must be running.
- You do not need an active radio connection to open the dialog, but the indicator is only meaningful after a connection attempt.

## Steps

1. Click `Settings > Network...` to open the Network Diagnostics dialog.
2. Locate the **Network Status** group at the top left of the dialog.
3. Read the **First UDP Packet** row.
   - It displays **Yes** once the first UDP packet has been received from the radio since the current connection was established.
   - It displays **No** if no UDP packet has arrived yet.
4. Click `Close` to dismiss the dialog.

## What each control does

| Indicator | Meaning |
|---|---|
| **First UDP Packet** | Shows **Yes** or **No**. **Yes** means at least one UDP packet has been received from the radio since connect. **No** means the UDP path has not yet carried any data. |

## Tips

- The indicator resets each time you reconnect. If you disconnect and reconnect, reopen the dialog to see the updated state.
- If the indicator stays **No** while **Status** shows a connected state, the TCP control path is up but the UDP stream path is blocked. Check firewall rules and confirm the local UDP endpoint shown in **Local UDP** is reachable from the radio.
- On a VPN or routed network, UDP is often blocked while TCP passes. See the Related section for guidance on those setups.

## Troubleshooting

- **First UDP Packet shows "No" indefinitely after connecting** — The radio can reach AetherSDR over TCP (commands work) but UDP packets are not arriving. Check that any firewall on the Linux host permits inbound UDP on the port shown in **Local UDP**. On a routed or VPN path, confirm UDP is not filtered between the radio and the client machine.

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Verify the radio's IP and local bind address](../../features/network-diagnostics/verify-the-radio-s-ip-and-local-bind-address.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
