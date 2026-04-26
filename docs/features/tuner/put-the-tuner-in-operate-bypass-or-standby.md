# Put the tuner in OPERATE, BYPASS, or STANDBY

Use the OPERATE button in the Tuner applet to cycle the 4O3A Tuner Genius XL between its three relay states: OPERATE, BYPASS, and STANDBY.

## Before you start

- AetherSDR must be connected to the radio. The Tuner applet is hidden until a Tuner Genius XL is detected.
- The TUN tray button must be available on the right sidebar, which confirms the TGXL has been detected.

## Steps

1. Click the TUN tray button on the right sidebar to open the Tuner applet.
2. Locate the OPERATE button in the lower-right of the applet.
3. Click OPERATE to advance to the next state. Each click cycles one step forward: OPERATE → BYPASS → STANDBY → OPERATE.

## What each control does

| Button label | Color | Meaning |
|---|---|---|
| OPERATE | Green | Tuner network is in circuit and actively matching. |
| BYPASS | Orange | Tuner relay is bypassed; RF passes through without matching. |
| STANDBY | Default (blue-grey) | Tuner is in standby; relay network is neither in circuit nor actively bypassed. |

The button label and color update immediately when the TGXL confirms the state change.

## Tips

- The button always shows the **current** state, not the state you are about to select. A green OPERATE label means the tuner is already in OPERATE; clicking it will move to BYPASS.
- If you have just run an autotune, the tuner enters OPERATE automatically. You do not need to click OPERATE after a successful tune cycle.

## Troubleshooting

- **TUN tray button is not visible** — The TGXL has not been detected. Check the connection between the radio and the tuner and confirm the tuner is powered on.
- **Button label does not change after clicking** — The radio has not acknowledged the state change. Verify the radio connection is active via `Settings > Connect to Radio...` and try again.

## Related

- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
- [Tuner overview](overview.md)
