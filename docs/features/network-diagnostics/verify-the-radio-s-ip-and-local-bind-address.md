# Verify the Radio's IP and Local Bind Address

Use this page to confirm which IP address AetherSDR has connected to and which local network interface it is using to reach the radio.

## Before you start

- AetherSDR must be running. The dialog can be opened whether or not a radio is connected.
- If you want to see a live IP address, connect to your Flex radio first.

## Steps

1. Click `Settings > Network...`.
2. The Network Diagnostics dialog opens. Locate the **Network Status** group in the upper-left area.
3. Read the **Target Radio IP** indicator. This shows the IP address of the connected radio. If no radio is connected, it reads `Not connected`.
4. Read the **Selected Source** indicator. This shows the local network interface or bind path AetherSDR is using for the connection.
5. Read **Local TCP** and **Local UDP** to see the exact local endpoints assigned for each protocol.
6. Click Close when finished.

## What each control does

| Indicator | What it shows |
|---|---|
| **Status** | Overall link state of the connection to the radio. |
| **Target Radio IP** | IP address of the connected radio. Shows `Not connected` when no radio is connected. |
| **Selected Source** | The local NIC or bind path used for the connection. |
| **Local TCP** | The local TCP endpoint (address and port) for the control connection. |
| **Local UDP** | The local UDP endpoint (address and port) for the stream connection. |

## Tips

- The **Selected Source** field is useful when your machine has multiple network interfaces. Confirm it shows the interface on the same subnet as the radio.
- **Target Radio IP** and **Selected Source** update once per second. If you just connected, wait a moment for the display to refresh.

## Troubleshooting

- **Target Radio IP shows `Not connected`** — No radio connection is active. Go to `Settings > Connect to Radio...` to discover and connect to a Flex radio on the network.
- **Selected Source shows an unexpected interface** — AetherSDR may have bound to the wrong NIC. Check your operating system's routing table and confirm the radio's subnet is reachable from the expected interface.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
