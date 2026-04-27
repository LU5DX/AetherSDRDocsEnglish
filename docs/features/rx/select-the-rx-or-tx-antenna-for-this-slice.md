# Select the RX or TX antenna for this slice

The RX Controls applet lets you choose which antenna port the FLEX-8600 uses for receiving and transmitting on each slice independently. Use this when you have multiple antennas connected and need to route a specific slice to a specific port.

## Before you start

- AetherSDR must be connected to the radio. The antenna controls are unavailable without a live connection.
- The antenna list is populated from the radio's own port configuration. Confirm your antennas are connected and recognized by the radio before changing these settings.

## Steps

1. Open the RX Controls applet. If it is not visible, click the **RX** tray button on the right sidebar.
2. If you have more than one slice, click the slice tab (A through H) for the slice you want to change.
3. **To change the RX antenna:** Click the blue antenna label near the top of the applet (shows the current RX antenna, e.g. **ANT1**). A menu appears listing all available antenna ports. Click the port you want. A checkmark shows the current selection.
4. **To change the TX antenna:** Click the red antenna label next to the RX antenna label (also shows the current TX antenna, e.g. **ANT1**). A menu appears listing TX-capable antenna ports. Click the port you want.

## What each control does

| Control | Default | Valid values | Behavior |
|---|---|---|---|
| **ANT1** (RX antenna, blue label) | ANT1 | Antenna ports from the radio's ant_list | Opens a menu; selecting an entry sets the RX antenna for this slice. |
| **ANT1** (TX antenna, red label) | ANT1 | TX-capable ports from the radio's ant_list | Opens a menu; selecting an entry sets the TX antenna for this slice. Ports whose names begin with `RX` are excluded. |

## Tips

- The RX antenna label is shown in blue; the TX antenna label is shown in red. This is the only visual distinction between the two controls, as they appear side by side in the header row.
- Antenna ports whose names begin with `RX` are filtered out of the TX antenna menu. They will still appear in the RX antenna menu.
- Each slice has its own independent RX and TX antenna assignment. Changing the antenna on slice A does not affect slice B.

## Troubleshooting

- **An expected antenna port does not appear in the menu** — The list comes directly from the radio's ant_list. Verify the port is configured and recognized in the radio's own settings. AetherSDR cannot add ports that the radio has not reported.
- **The TX antenna menu is missing a port that appears in the RX antenna menu** — Ports whose names begin with `RX` are intentionally excluded from the TX antenna menu because the radio treats them as receive-only.
- **Both labels are greyed out or unresponsive** — AetherSDR is not connected to the radio. Reconnect via `Settings > Connect to Radio...`.

## Related

- [RX Controls overview](overview.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
