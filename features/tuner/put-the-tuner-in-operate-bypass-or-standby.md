# Put the tuner in OPERATE, BYPASS, or STANDBY

The OPERATE button cycles the 4O3A Tuner Genius XL through its three relay states: OPERATE, BYPASS, and STANDBY. Use this to engage or disengage the tuner network without leaving the applet.

## Before you start

- AetherSDR must be connected to the radio. The Tuner applet is hidden until a Tuner Genius XL is detected.
- Open the Tuner applet by clicking the "TUN" tray button on the right sidebar.

## Steps

1. Locate the "OPERATE" button in the lower-right area of the Tuner applet.
2. Click the button once to advance to the next state. Each click cycles one step forward: OPERATE → BYPASS → STANDBY → OPERATE.

## What each control does

| Button label | Color | Meaning |
|---|---|---|
| OPERATE | Green | The tuner network is engaged. Relay settings are active. |
| BYPASS | Orange | The tuner is energized but the matching network is bypassed. |
| STANDBY | Default (blue-grey) | The tuner is in standby. RF passes without tuner involvement. |

The button label and color update immediately to reflect the new state as reported by the TGXL.

## Tips

- Each click advances exactly one step. To go from STANDBY directly to BYPASS, you must pass through OPERATE first.
- The current state shown on the button reflects what the TGXL has confirmed, not just what was requested. If the label does not change after a click, the TGXL has not acknowledged the command yet.

## Troubleshooting

- **The "TUN" tray button is not visible** — The Tuner applet only appears when a Tuner Genius XL is detected. Verify the TGXL is connected and powered, and that AetherSDR is connected to the radio.
- **Button label does not change after clicking** — The applet reflects state reported by the TGXL. A slow or interrupted connection between the radio and the TGXL may delay or prevent acknowledgement. Check the TGXL connection and try again.

## Related

- [Tuner overview](overview.md)
- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
