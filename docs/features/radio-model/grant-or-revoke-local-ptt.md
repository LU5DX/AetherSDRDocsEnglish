# Grant or revoke local PTT

Each GUI client connected to the same radio carries a local PTT flag that determines whether that client holds local PTT rights. Use the Connected Client Info panel to see the current state for every connected client and to grant or revoke those rights.

## Before you start

- You must be connected to a radio with at least one other GUI client also connected.

## Steps

1. Open the Connected Client Info panel to view all currently connected clients.
2. Locate the client whose local PTT rights you want to change, then toggle the local PTT state for that client to grant or revoke access.

## What each control does

| Control | Behavior |
|---|---|
| Station name | Identifies the remote client by its station name. |
| Program | Shows the software the remote client is running. |
| Source IP/host | Displays the IP address or hostname the remote client is connecting from. |
| Local PTT state | Indicates whether the client currently holds local PTT rights. Toggle to grant or revoke. |
| TX antenna | Shows which transmit antenna the remote client is using. |
| Current TX frequency | Displays the frequency on which the remote client is transmitting. |

## Tips

- Check the local PTT state column before transmitting to confirm no other client already holds PTT rights on the same radio.
- A client shown as transmitting (non-idle TX frequency) should have its local PTT reviewed before you revoke access mid-transmission.

## Related

- [connected-clients.md](connected-clients.md)
- [ptt-overview.md](ptt-overview.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
