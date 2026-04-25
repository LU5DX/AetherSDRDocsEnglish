# Verify the Radio's IP and Local Bind Address

Use the Network Diagnostics dialog to confirm which IP address AetherSDR has connected to and which local network interface it is using to reach the radio.

## Before you start

- AetherSDR must be running. The dialog can be opened whether or not a radio is connected, but the indicators will show live data only when connected.

## Steps

1. Click `Settings > Network...`.
2. In the **Network Diagnostics** dialog, locate the **Network Status** group.
3. Read **Target Radio IP** — this shows the IP address of the connected radio. If no connection is active, it displays `Not connected`.
4. Read **Selected Source** — this shows the local NIC or bind path AetherSDR is using for the connection.
5. If you need to confirm the exact local endpoints, read **Local TCP** and **Local UDP** — these show the local TCP and UDP addresses and ports in use.
6. Click `Close` when finished.

## What each control does

| Indicator | Meaning |
|---|---|
| **Status** | Overall link state of the connection to the radio. |
| **Target Radio IP** | IP address of the connected radio. Shows `Not connected` when no radio is connected. |
| **Selected Source** | Local NIC or bind path being used for the connection. |
| **Local TCP** | Local TCP endpoint (address and port). |
| **Local UDP** | Local UDP endpoint (address and port). |

## Tips

- The dialog refreshes all indicators once per second, so values update live while you watch.
- If **Target Radio IP** shows `Not connected` and you expect a connection, check your connection settings via `Settings > Connect to Radio...`.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
