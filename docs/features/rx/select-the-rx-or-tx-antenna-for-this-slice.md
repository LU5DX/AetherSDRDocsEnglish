# Select the RX or TX antenna for this slice

Each slice has an independent RX antenna and TX antenna. Use the RX Controls applet to change either without affecting other slices.

## Before you start

- Connect to a FLEX-8600 radio. The antenna controls require an active radio connection.
- Open the RX Controls applet. It is always visible in the Applet Panel (right sidebar). If the panel is hidden, click the `RX` tray button on the right sidebar to show it.
- If you have more than one slice, select the correct slice using the A–H tab row at the top of the applet.

## Steps

### Change the RX antenna

1. Locate the blue antenna label in the header row of the RX Controls applet. It shows the current RX antenna (for example, `ANT1`).
2. Click the blue label. A menu opens listing all antennas reported by the radio.
3. Click the antenna you want to use for receive. A checkmark appears next to the current selection.

### Change the TX antenna

1. Locate the red antenna label in the header row, immediately to the right of the blue RX antenna label. It shows the current TX antenna (for example, `ANT1`).
2. Click the red label. A menu opens listing TX-capable antennas. Antenna ports with names beginning with `RX` are not shown, as they are receive-only.
3. Click the antenna you want to use for transmit.

## What each control does

| Control | Color | Default | Valid values | Behavior |
|---|---|---|---|---|
| RX antenna button | Blue label | ANT1 | Antenna names from the radio's `ant_list` | Opens a menu; selecting an entry sets the RX antenna for this slice. |
| TX antenna button | Red label | ANT1 | Antenna names from the radio's `ant_list`, excluding ports prefixed `RX` | Opens a menu; selecting an entry sets the TX antenna for this slice. RX-only ports are filtered out. |

## Tips

- The RX and TX antenna selections are per-slice. Changing the antenna on slice A does not affect slice B.
- The available antenna names come from the radio's reported `ant_list`. If an expected antenna is missing, verify the hardware connection and the radio firmware.
- RX-only ports (those whose names begin with `RX`) appear in the RX antenna menu but are excluded from the TX antenna menu.

## Troubleshooting

- **An antenna I expect is not listed** — The list is populated from the radio's `ant_list` at connection time. Reconnect to the radio and check that the antenna port is enabled in the radio's own configuration.
- **A port I want for TX does not appear in the TX menu** — Ports whose names begin with `RX` are filtered out of the TX antenna menu. These ports are hardware receive-only and cannot transmit.

## Related

- [RX Controls overview](overview.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
