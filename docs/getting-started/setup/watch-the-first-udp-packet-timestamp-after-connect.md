# Watch the first-UDP-packet timestamp after connect

Use the Network Diagnostics dialog to confirm that the radio's UDP data stream has reached your machine after connecting. The **First UDP Packet** indicator tells you whether any UDP traffic has arrived since the current session began.

## Before you start

- AetherSDR must be running. The dialog can be opened whether or not a radio is connected, but **First UDP Packet** is only meaningful after a connection attempt.
- You must have already initiated a connection to a FLEX-8600 radio.

## Steps

1. Click `Settings > Network...`.
2. In the **Network Diagnostics** dialog, locate the **Network Status** group.
3. Read the **First UDP Packet** indicator. It shows `Yes` if at least one UDP packet has been received since connect, or `No` if none has arrived yet.
4. Click `Close` to dismiss the dialog.

## What each control does

| Indicator | Meaning |
|---|---|
| **First UDP Packet** | Shows `Yes` or `No`. Updates once per second. Reflects whether any UDP packet from the radio has been received in the current session. |
| **Status** | Overall link state. |
| **Local UDP** | The local UDP endpoint AetherSDR is listening on. Useful for confirming the correct port is bound. |
| **Target Radio IP** | IP address of the connected radio. |

## Tips

- The dialog refreshes all indicators once per second. If **First UDP Packet** stays `No` for several seconds after connecting, UDP traffic is not reaching the host — check firewall rules, routing, and that the local UDP endpoint shown in **Local UDP** is reachable from the radio.
- On a VPN or routed link, TCP may connect successfully while UDP is blocked separately. **First UDP Packet** showing `No` with **Status** showing a connected state is a reliable sign of this split.
- **First UDP Packet** resets on each new connection. Disconnect and reconnect if you want to re-verify delivery after changing network settings.

## Troubleshooting

- **First UDP Packet stays "No" after connecting** — UDP is not arriving at the local endpoint. Verify that no firewall is blocking UDP on the port shown in **Local UDP**, and that the radio can route back to your machine's IP. On a VPN connection, confirm the VPN passes UDP in both directions.
- **First UDP Packet shows "Yes" but audio is silent** — UDP is arriving, but a different problem affects playback. Check the **Audio Playback** group for underruns or buffer issues, and see the audio diagnostics page.

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Verify the radio's IP and local bind address](../../features/network-diagnostics/verify-the-radio-s-ip-and-local-bind-address.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Pick the local network interface used for a manual connection](pick-the-local-network-interface-used-for-a-manual-connection.md)
