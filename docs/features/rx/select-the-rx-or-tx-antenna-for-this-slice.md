# Select the RX or TX antenna for this slice

The RX Controls applet lets you choose which antenna port the radio uses for receiving and transmitting on each slice independently. Change these when you have separate antennas for different bands or when you want to receive on a dedicated RX-only port.

## Before you start

- AetherSDR must be connected to the radio. The antenna controls are unavailable without a live connection.
- The antenna list is populated from the radio's own port configuration. Confirm your antennas are physically connected and named in the radio before proceeding.

## Steps

1. Open the RX Controls applet. It is always visible in the Applet Panel (right sidebar). If it is not visible, click the `RX` tray button on the right sidebar to show it.
2. If you have more than one slice, click the correct slice tab (A through H) at the top of the applet to bind the applet to the slice you want to change.
3. In the header row, locate the two small antenna labels. The blue label is the RX antenna; the red label is the TX antenna. Both default to `ANT1`.
4. **To change the RX antenna:** click the blue antenna label (e.g. `ANT1`). A menu opens listing all available antenna ports. The currently selected port has a checkmark. Click the port you want to use for receive.
5. **To change the TX antenna:** click the red antenna label (e.g. `ANT1`). A menu opens listing TX-capable ports. Ports whose names begin with `RX` are excluded because they are receive-only. Click the port you want to use for transmit.
6. The label updates immediately to show the newly selected antenna. The radio applies the change to the active slice.

## What each control does

| Control | Color | Default | Valid options | Behavior |
|---|---|---|---|---|
| RX antenna label | Blue | `ANT1` | All ports from the radio's antenna list | Click to open a menu; selecting an entry sets the receive antenna for this slice. |
| TX antenna label | Red | `ANT1` | All ports except those prefixed `RX` | Click to open a menu; selecting an entry sets the transmit antenna for this slice. RX-only ports are filtered out. |

## Tips

- RX and TX antennas are set per slice. Switching to a different slice tab changes which slice the applet controls; the antenna labels update to reflect that slice's current selections.
- If a port name begins with `RX` (for example, `RXANT` or `RX2`), it appears in the RX menu but is hidden from the TX menu.

## Troubleshooting

- **The antenna menu shows fewer ports than expected** — The list is pulled from the radio's `ant_list`. Ports that are not reported by the radio firmware will not appear. Verify the port is enabled in the radio's own configuration and that firmware 4.1.5 is running.
- **The TX antenna label is missing a port that the RX menu shows** — The port name likely starts with `RX`. Receive-only ports are intentionally excluded from the TX selection menu.

## Related

- [RX Controls overview](overview.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
