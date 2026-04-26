# Watch the first-UDP-packet timestamp after connect

The **First UDP Packet** indicator in Network Diagnostics shows whether AetherSDR has received any UDP data from the radio since the current connection was established. Use it to confirm that the UDP data path is open — a missing first packet means audio, FFT, and waterfall data cannot flow, even if the TCP command channel is up.

## Before you start

- AetherSDR must be running. The radio does not need to be connected; the dialog opens regardless.
- For the indicator to show a meaningful result, connect to a radio first — see [Connect to a local LAN radio](connect-to-a-local-lan-radio.md).

## Steps

1. Click `Settings > Network...`.
2. The **Network Diagnostics** dialog opens.
3. Locate the **Network Status** group in the upper-left area of the dialog.
4. Read the **First UDP Packet** row.
   - **Yes** — at least one UDP packet has arrived from the radio since connect.
   - **No** — no UDP packet has been received yet on the current connection.
5. Click **Close** to dismiss the dialog.

## What each control does

| Indicator | Meaning |
|---|---|
| **First UDP Packet** | Shows **Yes** or **No**. Resets each time a new connection is made. Reports whether any UDP packet from the radio has been received on the current session. |
| **Status** | Overall link state of the connection. |
| **Local UDP** | The local UDP endpoint AetherSDR is listening on. If this is blank or unexpected, UDP traffic cannot arrive at all. |
| **Target Radio IP** | IP address of the connected radio. Shows `Not connected` when no radio is connected. |

## Tips

- The indicator is updated once per second. Allow a few seconds after connecting before concluding that no UDP traffic is arriving.
- If **First UDP Packet** stays **No** while **Status** shows a connected state, check **Local UDP** to confirm a port is bound. A firewall blocking the UDP port is the most common cause.
- **First UDP Packet** resets to **No** on every new connection. Disconnect and reconnect to retest after changing network settings.

## Troubleshooting

- **First UDP Packet shows "No" after several seconds connected** — The TCP command path is up but UDP is blocked. Verify that your firewall permits inbound UDP from the radio's IP. Check **Local UDP** to confirm AetherSDR has bound a port. On a routed or VPN network, confirm the path is symmetric — see [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md).
- **First UDP Packet shows "Yes" but audio is silent** — UDP is arriving; the problem is downstream of the network layer. Check **RX Buffer Now**, **Underruns (total / last sec)**, and **Audio Arrival Gap** in the **Audio Playback** group — see [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md).

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Verify the radio's IP and local bind address](../../features/network-diagnostics/verify-the-radio-s-ip-and-local-bind-address.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
