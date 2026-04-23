# Watch the First-UDP-Packet Timestamp After Connect

The **First UDP Packet** indicator in Network Diagnostics confirms whether the radio has successfully opened the UDP data path to your machine. Checking it immediately after connecting helps you distinguish a healthy link from a one-sided connection where TCP negotiated but no UDP stream arrived.

## Before you start

- AetherSDR must be running.
- You must have attempted a connection to a FLEX-8600 radio. The indicator is meaningful only after a connect attempt; it does not require the connection to be fully established.

## Steps

1. Open `Settings > Network...`.
2. In the **Network Diagnostics** dialog, locate the **Network Status** section.
3. Read the **First UDP Packet** field.
   - **Yes** — at least one UDP packet has arrived from the radio since the last connect.
   - **No** — no UDP packet has been received yet.
4. Click **Close** to dismiss the dialog.

## What each control does

| Indicator | Meaning |
|---|---|
| **First UDP Packet** | Shows **Yes** or **No**. Indicates whether the first UDP packet from the radio has been received since the current connection was established. The value resets on each new connect. |
| **Status** | Overall link state of the connection to the radio. |
| **Local UDP** | The local endpoint AetherSDR is listening on for incoming UDP traffic. |
| **Target Radio IP** | The IP address of the radio AetherSDR is connected to. |

## Tips

- If **First UDP Packet** remains **No** after several seconds, the radio's UDP stream is not reaching your machine. Check firewall rules on the host: the radio sends UDP to the port shown in **Local UDP**, and that port must be reachable from the radio's IP shown in **Target Radio IP**.
- The dialog refreshes once per second, so **First UDP Packet** will update to **Yes** within one second of the first packet arriving.
- **First UDP Packet** alone does not confirm a healthy stream. After it reads **Yes**, also check **Latency (RTT)** and the per-category rates (Audio, FFT, Waterfall) to confirm data is flowing normally.

## Troubleshooting

- **First UDP Packet stays "No" after connecting** — The UDP path from the radio to your machine is blocked. Verify no firewall or NAT rule is dropping inbound UDP on the port shown in **Local UDP**. On a VPN or routed network, confirm the radio can reach your machine's IP at that port.
- **First UDP Packet shows "Yes" but audio is silent** — UDP is arriving but the audio stream may not be active. Check the **Audio** rate in the Incoming Stream Rates section and the **RX Buffer Now** and **Underruns** fields in Audio Playback.

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Verify the radio's IP and local bind address](../../features/network-diagnostics/verify-the-radio-s-ip-and-local-bind-address.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](../../features/network-diagnostics/check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
