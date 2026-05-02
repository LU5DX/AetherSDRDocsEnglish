# Set the TX audio low-cut frequency

Use the Low Cut control in the Phone applet to raise the lower edge of the TX audio passband, cutting rumble, breath noise, or low-frequency interference from your transmitted signal.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Make sure the Applet Panel is visible. If it is not, click `View > Applet Panel` to show it.

## Steps

1. Click the **PHNE** tray button on the right sidebar to open the Phone applet.
2. Locate the **Low Cut** section in the TX filter area at the bottom of the applet.
3. Click **<** to decrease the low-cut frequency or **>** to increase it. You can also scroll the mouse wheel over the value display to step in either direction.
4. Read the current value in the numeric display between the two buttons. The default is **50 Hz**.

## How the step buttons work

Each click of **<** or **>** snaps the low-cut frequency to the nearest multiple of 50 Hz in the chosen direction, rather than adding or subtracting a fixed 50 Hz from the current value. For example, if the current value is 87 Hz, clicking **>** sets it to 100 Hz and clicking **<** sets it to 50 Hz. If the value is already an exact multiple of 50 Hz, the buttons move it to the next multiple in the chosen direction.

This means a single click always lands on a clean 50 Hz boundary regardless of the starting value.

## What each control does

| Control               | Default | Valid range                             |
|-----------------------|---------|-----------------------------------------|
| **Low Cut** **<**     | —       | Snaps down to next lower 50 Hz multiple |
| **Low Cut** **>**     | —       | Snaps up to next higher 50 Hz multiple  |
| Low Cut value display | 50 Hz   | 0 Hz to (high-cut − 50 Hz), step 50 Hz |

## Tips

- The low-cut value cannot be set higher than the current high-cut frequency minus 50 Hz. If you are near that limit, lower the high-cut first or raise it to create room.
- For SSB voice, a typical low-cut of 100–200 Hz reduces low-frequency noise without noticeably affecting voice intelligibility.
- Because the buttons snap to multiples of 50 Hz, clicking once from any off-boundary value may move the frequency by less than 50 Hz. This is expected behaviour.

## Troubleshooting

- **Low Cut buttons do nothing** — Confirm the radio is connected. The TX filter controls require an active radio connection to send filter changes to the FLEX-8600.

## Related

- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
- [Phone overview](overview.md)
- [Enable VOX and set trigger threshold](enable-vox-and-set-trigger-threshold.md)