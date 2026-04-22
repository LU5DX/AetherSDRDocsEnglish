# Run an autotune on the external TGXL

This page explains how to trigger the 4O3A Tuner Genius XL automatic tune cycle from AetherSDR and read the result when it finishes.

## Before you start

- A Tuner Genius XL must be detected by the radio. The TUN tray button on the right sidebar appears only when the TGXL is present.
- The radio must be connected. The TunerApplet requires an active radio connection.
- The tuner should be in OPERATE state before running an autotune. If the button reads "BYPASS" or "STANDBY", see [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md).

## Steps

1. Click the TUN tray button on the right sidebar to open the Tuner applet.
2. Confirm the OPERATE button reads "OPERATE" (green). If it does not, click the button until it cycles to "OPERATE".
3. Click TUNE.
4. The TUNE button turns red and reads "TUNING..." while the tune cycle runs.
5. When the cycle finishes, the button briefly displays "SWR x.xx" — the settled post-tune SWR — for 2.5 seconds, then returns to "TUNE".

## What each control does

| Control | Description | Valid range |
|---|---|---|
| TUNE | Starts the autotune cycle. Turns red and reads "TUNING..." during the cycle. Flashes the final SWR result for 2.5 s when done. | — |
| Fwd Pwr | Displays TGXL-reported forward power during the tune. | 0–200 W barefoot, 0–600 W Aurora, 0–2000 W with PGXL |
| SWR | Displays TGXL-reported SWR in real time. | 1.0–3.0 (red above 2.5) |
| C1 | Shows the C1 relay bank position after tuning completes. | 0–255 |
| L | Shows the L relay bank position after tuning completes. | 0–255 |
| C2 | Shows the C2 relay bank position after tuning completes. | 0–255 |

## Tips

- The SWR result displayed after tuning reflects a settled value captured up to 400 ms after the tune cycle ends, not the SWR during the relay sweep. This gives a more accurate final reading.
- If you want to read the post-tune SWR independently of the 2.5-second flash, watch the SWR gauge directly after the TUNE button returns to "TUNE".

## Troubleshooting

- **TUN tray button does not appear** — The TGXL has not been detected by the radio. Verify the tuner is powered on and correctly connected to the FLEX-8600.
- **TUNE button returns to "TUNE" immediately without showing an SWR result** — The tune cycle may have been aborted or the TGXL did not report a settled SWR. Check the tuner's physical state and try again.
- **TUNE button shows "SWR 3.00" or a very high value** — The tuner could not find an acceptable match on the current frequency and antenna. Verify the antenna is connected and the band is within the tuner's matching range.

## Related

- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)
- [Tuner overview](overview.md)
