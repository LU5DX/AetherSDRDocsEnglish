# See all stations connected to this Flex radio

The Connected Client Info panel shows every other GUI client currently connected to the same radio, including which station is transmitting, on what antenna, and at what frequency.

## Steps

1. Open the client list view in AetherSDR to display the **Connected Client Info** table.
2. Review the rows — each row represents one connected client session.

## What each control does

| Control | Behavior |
|---|---|
| Station Name | The human-readable name of the remote station. |
| Program | The software client the remote station is running. |
| Source IP / Host | The IP address or hostname from which the remote client is connected. |
| Local PTT State | Indicates whether that client currently holds local PTT rights. |
| TX Antenna | The antenna the remote client is using for transmit. |
| Current TX Frequency | The frequency the remote client is currently set to transmit on. |

## Tips

- Check **Local PTT State** before transmitting to confirm no other client holds PTT rights on the radio at the same time.
- If a station's row disappears, that client has disconnected from the radio.

## Related

- [connect-to-flex-radio.md](connect-to-flex-radio.md)
- [transmit-settings.md](transmit-settings.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
