# Watch the first-UDP-packet timestamp after connect

The **First UDP Packet** indicator in Network Diagnostics confirms that the radio's UDP data stream has reached your machine after a connection is established. Use it to verify that the UDP path is open and that packets are flowing, not just the TCP control channel.

## Before you start

- AetherSDR must be running.
- A connection attempt to the radio must have been made. The indicator is most useful immediately after connecting.

## Steps

1. Click `Settings > Network...` to open the Network Diagnostics dialog.
2. In the **Network Status** group, locate the **First UDP Packet** row.
3. Read the value. It shows either **Yes** or **No**.

## What each control does

| Indicator | Meaning | Notes |
|---|---|---|
| **First UDP Packet** | Shows **Yes** if at least one UDP packet has been received from the radio since connect; **No** otherwise. | Resets each time a new connection is made. |

## Tips

- The dialog refreshes once per second. If the value changes from **No** to **Yes** shortly after connecting, the UDP path opened successfully.
- If **First UDP Packet** remains **No** while **Status** shows connected, the TCP control channel is up but UDP traffic is blocked. Check firewalls and router NAT rules for the UDP port used by the radio.
- **First UDP Packet** only indicates that one packet arrived. Check **Audio**, **FFT**, and **Waterfall** rates in the **Incoming Stream Rates** group to confirm sustained data flow.

## Troubleshooting

- **First UDP Packet stays "No" after connecting** — The TCP handshake succeeded but no UDP packets have arrived. A firewall or NAT rule is likely blocking the UDP stream. Verify that your firewall permits inbound UDP from the radio's IP. On a routed or VPN path, confirm that UDP is not filtered between the two endpoints.

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Verify the radio's IP and local bind address](../../features/network-diagnostics/verify-the-radio-s-ip-and-local-bind-address.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
