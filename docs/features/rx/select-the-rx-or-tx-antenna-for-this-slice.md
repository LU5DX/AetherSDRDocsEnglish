# Select the RX or TX antenna for this slice

This page explains how to change the receive or transmit antenna assigned to a slice. You might do this to switch between a beam and a vertical, or to route receive-only antenna ports to the RX path only.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet will not populate antenna lists without a live connection.
- The antenna list is supplied by the radio. Any antenna port that does not appear in the radio's `ant_list` will not be offered as a choice.

## Steps

1. Open the RX Controls applet. If it is not visible, click the **RX** tray button on the right sidebar.
2. If you have more than one slice, click the slice tab (A, B, C … H) for the slice you want to configure.
3. In the header row, locate the two small antenna labels. The **blue** label is the current RX antenna; the **red** label is the current TX antenna. Both default to **ANT1**.
4. To change the **RX antenna**: click the blue antenna label. A menu lists all available antennas from the radio. The current selection is checked. Click the antenna you want.
5. To change the **TX antenna**: click the red antenna label. A menu lists TX-capable antennas only — ports whose names begin with **RX** are excluded. Click the antenna you want.
6. The label updates immediately to reflect your selection. The change takes effect on the radio at once.

## What each control does

| Control | Label colour | Default | Valid values | Behavior |
|---|---|---|---|---|
| RX antenna | Blue | ANT1 | All ports in the radio's `ant_list` | Sets the receive antenna for this slice. |
| TX antenna | Red | ANT1 | Ports in `ant_list` that do not begin with `RX` | Sets the transmit antenna for this slice. |

Neither control has a persisted setting key — antenna selections are held by the radio and restored by the radio on reconnect.

## Tips

- Ports whose names start with `RX` (case-insensitive) are RX-only and are filtered out of the TX antenna menu. If an antenna you expect to transmit from is missing from the TX list, check whether its name begins with `RX` in the radio's antenna configuration.
- You can assign different RX and TX antennas to each slice independently. Each slice tab has its own pair of antenna controls.

## Related

- [RX Controls overview](overview.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
