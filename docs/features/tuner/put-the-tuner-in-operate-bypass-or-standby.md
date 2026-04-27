# Put the tuner in OPERATE, BYPASS, or STANDBY

Use the OPERATE button in the Tuner applet to cycle the 4O3A Tuner Genius XL through its three relay states: OPERATE, BYPASS, and STANDBY.

## Before you start

- AetherSDR must be connected to the radio. The Tuner applet is hidden until a Tuner Genius XL is detected.
- The TUN tray button must be available in the right sidebar, indicating the TGXL has been detected.

## Steps

1. Click the TUN tray button on the right sidebar to open the Tuner applet.
2. Locate the OPERATE button in the lower-right area of the applet.
3. Click OPERATE to advance to the next state. Each click cycles one step forward:
   - OPERATE → BYPASS
   - BYPASS → STANDBY
   - STANDBY → OPERATE

## What each control does

| Button | Color when active | Meaning |
|---|---|---|
| OPERATE | Green | Tuner relays are in circuit and active. |
| BYPASS | Orange | Tuner is energized but the matching network is bypassed. |
| STANDBY | Default (blue-grey) | Tuner is not operating. |

The button label and color update immediately when the TGXL acknowledges the state change.

## Tips

- The button always shows the **current** state, not the next state. A green OPERATE label means the tuner is already in OPERATE.
- Clicking once from STANDBY returns the tuner to OPERATE and restores the green color. You do not need to pass through BYPASS to get back to OPERATE.

## Troubleshooting

- **The TUN tray button is not visible** — The Tuner applet is hidden until a Tuner Genius XL is detected on the network. Verify the TGXL is powered on and connected. See [Tuner overview](overview.md).
- **The button label does not change after clicking** — The label updates only when the TGXL confirms the new state. If the label stays the same, check the connection between AetherSDR and the TGXL.

## Related

- [Tuner overview](overview.md)
- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)
