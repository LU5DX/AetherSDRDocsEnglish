# Switch between three antennas on a TGXL 3x1

This page explains how to select one of three antenna ports on a 4O3A Tuner Genius XL with a 3x1 antenna switch. Use this when you have multiple antennas connected to the TGXL and want to switch between them from AetherSDR.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio.
- A TGXL must be detected; the TUN tray button appears on the right sidebar only when a Tuner Genius XL is present.
- The TGXL must be connected via a direct TGXL connection. The antenna switch row is hidden when only a radio-mediated connection is active.
- The TGXL must report an antenna switch (models without a 3x1 switch never expose the antenna ports).

## Steps

1. Click the TUN tray button on the right sidebar to open the Tuner applet.
2. Confirm that the antenna switch row is visible at the bottom of the applet. If it is not visible, see "Before you start" above.
3. Click `ANT 1`, `ANT 2`, or `ANT 3` to select the corresponding antenna port on the TGXL 3x1 switch.

## What each control does

| Control | Behavior |
|---------|----------|
| `ANT 1` | Selects antenna port 1 on the TGXL 3x1 switch. |
| `ANT 2` | Selects antenna port 2 on the TGXL 3x1 switch. |
| `ANT 3` | Selects antenna port 3 on the TGXL 3x1 switch. |

None of these controls have a persisted setting key. The selection is sent directly to the TGXL.

## Tips

- The antenna switch row is hidden automatically when the direct TGXL connection is not active or when the connected TGXL model does not include a 3x1 switch. If you cannot see `ANT 1`, `ANT 2`, or `ANT 3`, check your direct connection to the TGXL.
- The active antenna port is tracked by the TGXL. AetherSDR reads the reported value on connection and highlights the current selection accordingly.

## Troubleshooting

- **The ANT 1 / ANT 2 / ANT 3 buttons do not appear** — The antenna switch row is only shown when a direct TGXL connection is active and the TGXL reports that an antenna switch is present. Verify that your TGXL is connected directly (not only via the radio) and that your TGXL model includes the 3x1 switch option.
- **Clicking an antenna button has no effect** — The command is sent only when a direct connection is established. If the TUN applet is open but the row appeared unexpectedly, the connection may have dropped. Close and reopen the applet to check connection state.

## Related

- [Tuner overview](overview.md)
- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)
