# Switch between three antennas on a TGXL 3x1

Select which of the three antenna ports on a 4O3A Tuner Genius XL 3x1 switch is active. This lets you change antennas without touching any physical switch.

## Before you start

- AetherSDR must be connected to a Flex radio.
- A Tuner Genius XL must be detected; the TUN tray button appears on the right sidebar only when one is present.
- A direct TGXL connection must be active. The antenna switch row is hidden if the TGXL is not connected directly or does not report an antenna switch.

## Steps

1. Click the TUN tray button on the right sidebar to open the Tuner applet.
2. Confirm that the antenna row is visible at the bottom of the applet. If the row is not shown, the direct TGXL connection is not active or this TGXL does not have a 3x1 switch — see Before you start above.
3. Click `ANT 1`, `ANT 2`, or `ANT 3` to select the corresponding antenna port.

## What each control does

| Label | Behavior |
|-------|----------|
| `ANT 1` | Switches the TGXL 3x1 to antenna port 1. |
| `ANT 2` | Switches the TGXL 3x1 to antenna port 2. |
| `ANT 3` | Switches the TGXL 3x1 to antenna port 3. |

The entire antenna row is hidden unless the direct TGXL connection is active and the TGXL reports that an antenna switch is present.

None of these controls have persisted setting keys; the selected port is held by the TGXL hardware.

## Troubleshooting

- **ANT 1 / ANT 2 / ANT 3 buttons are not visible** — The direct TGXL connection is not active, or this TGXL unit does not have a 3x1 switch fitted. Verify the direct connection in your TGXL hardware setup. The row appears automatically once a direct connection is active and the TGXL reports an antenna switch.

## Related

- [Tuner overview](overview.md)
- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
