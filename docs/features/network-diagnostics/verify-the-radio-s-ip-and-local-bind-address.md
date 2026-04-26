# Verify the Radio's IP and Local Bind Address

Use the Network Diagnostics dialog to confirm which IP address AetherSDR is targeting on the radio and which local network interface it is using for the connection.

## Before you start

- AetherSDR must be running. The dialog can be opened whether or not a radio is connected.

## Steps

1. Click `Settings > Network...`.
2. In the **Network Diagnostics** dialog, locate the **Network Status** group.
3. Read **Target Radio IP**. This shows the IP address of the connected radio. If no radio is connected, it displays `Not connected`.
4. Read **Selected Source**. This shows the local NIC or bind path AetherSDR is using for the connection.
5. Optionally read **Local TCP** and **Local UDP** to see the exact local endpoints for each protocol.
6. Click `Close` when finished.

## What each control does

| Indicator | Meaning |
|---|---|
| **Status** | Overall link state. |
| **Target Radio IP** | IP address of the connected radio. Displays `Not connected` when no radio is present. |
| **Selected Source** | Local NIC or bind path used for the connection. |
| **Local TCP** | Local TCP endpoint for the radio connection. |
| **Local UDP** | Local UDP endpoint for the radio connection. |

## Tips

- You do not need an active radio connection to open the dialog. **Target Radio IP** will show `Not connected` rather than an address when the radio is offline, which can itself confirm a connection has not been established.
- **Selected Source** is the bind path chosen at connect time. If AetherSDR is routing traffic through an unexpected interface, check this value first before investigating elsewhere.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
