# Verify the Radio's IP and Local Bind Address

Use this page to confirm which IP address AetherSDR has connected to on your FLEX-8600 and which local network interface it is using for that connection.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but the fields will show meaningful values only after a connection attempt has been made.

## Steps

1. Click `Settings > Network...`.
2. In the **Network Diagnostics** dialog, locate the **Network Status** group at the top left.
3. Read **Target Radio IP** — this shows the IP address of the radio AetherSDR connected to. If no connection has been made, the field displays `Not connected`.
4. Read **Selected Source** — this shows the local network interface or bind path AetherSDR used to reach the radio.
5. Read **Local TCP** and **Local UDP** to see the exact local endpoints for each protocol.
6. Click Close when done.

## What each control does

| Indicator | Meaning |
|---|---|
| **Status** | Overall link state of the current connection. |
| **Target Radio IP** | IP address of the connected radio. Displays `Not connected` if no connection is active. |
| **Selected Source** | Local NIC or bind path used to reach the radio. |
| **Local TCP** | Local TCP endpoint (address and port). |
| **Local UDP** | Local UDP endpoint (address and port). |

## Tips

- The dialog refreshes all values once per second. If you have just connected, wait a moment for the fields to populate.
- **Selected Source** is useful when the host has multiple network interfaces. Confirm it shows the interface on the same subnet as the radio, not a VPN or secondary adapter.

## Troubleshooting

- **Target Radio IP shows `Not connected`** — No connection to the radio is active. Use `Settings > Connect to Radio...` to discover and connect to your FLEX-8600, then reopen the dialog.
- **Selected Source shows an unexpected interface** — Your operating system routed the connection through a different NIC than intended. Check your routing table or disable unused network interfaces, then reconnect.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
