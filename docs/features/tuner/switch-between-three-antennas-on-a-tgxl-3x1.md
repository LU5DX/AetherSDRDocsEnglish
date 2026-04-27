# Switch between three antennas on a TGXL 3x1

This page explains how to select antenna ports 1, 2, or 3 on a 4O3A Tuner Genius XL with a 3x1 antenna switch. Use this when you have multiple antennas connected to the TGXL and need to route the radio to a specific port.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- A Tuner Genius XL must be detected; the TUN tray button appears on the right sidebar only when a TGXL is present.
- A direct TGXL connection must be active. The antenna switch row is hidden unless both a direct connection is active and the TGXL reports that an antenna switch is present.

## Steps

1. Click the TUN tray button on the right sidebar to open the Tuner applet.
2. Confirm that the antenna switch row is visible at the bottom of the applet. If it is not visible, the TGXL either has no direct connection or does not have a 3x1 switch fitted — see Before you start above.
3. Click ANT 1, ANT 2, or ANT 3 to select the corresponding antenna port.

## What each control does

| Button | Behavior |
|--------|----------|
| ANT 1 | Selects antenna port 1 on the TGXL 3x1 switch. |
| ANT 2 | Selects antenna port 2 on the TGXL 3x1 switch. |
| ANT 3 | Selects antenna port 3 on the TGXL 3x1 switch. |

None of these buttons have a persisted setting key. The selection is sent directly to the TGXL.

## Troubleshooting

- **The ANT 1 / ANT 2 / ANT 3 buttons are not visible** — The antenna switch row is hidden unless a direct TGXL connection is active and the TGXL reports an antenna switch. Verify your TGXL connection. If the TGXL model does not include a 3x1 switch, these buttons will never appear.

## Related

- [Tuner overview](overview.md)
- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
