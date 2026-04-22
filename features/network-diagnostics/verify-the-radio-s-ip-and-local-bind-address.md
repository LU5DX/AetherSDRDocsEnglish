# Verify the Radio's IP and Local Bind Address

Open the Network Diagnostics dialog to confirm which IP address AetherSDR has connected to and which local network interface it is using for that connection.

## Before you start

- AetherSDR must be running. The dialog can be opened whether or not a radio is connected, but the fields will be empty or show "Not connected" until a connection is established.

## Steps

1. Click `Settings > Network...`.
2. Locate the **Network Status** group at the top-left of the dialog.
3. Read the **Target Radio IP** field. This shows the IP address of the radio AetherSDR has connected to. If no connection is active, the field reads `Not connected`.
4. Read the **Selected Source** field. This shows the local network interface or bind path AetherSDR is using for the connection.
5. Optionally check **Local TCP** and **Local UDP** to see the exact local endpoints for each protocol.
6. Click `Close` when finished.

## What each control does

| Indicator | Meaning |
|---|---|
| **Status** | Overall link state of the connection to the radio. |
| **Target Radio IP** | IP address of the connected radio. Shows `Not connected` when no connection is active. |
| **Selected Source** | Local network interface or bind path used to reach the radio. |
| **Local TCP** | Local TCP endpoint (address and port). |
| **Local UDP** | Local UDP endpoint (address and port). |

## Tips

- The **Network Status** group refreshes every second, so values update in place without reopening the dialog.
- If **Target Radio IP** shows the wrong address, close the dialog and use `Settings > Connect to Radio...` to select the correct radio before reconnecting.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Watch the first-UDP-packet timestamp after connect](../../getting-started/setup/watch-the-first-udp-packet-timestamp-after-connect.md)
