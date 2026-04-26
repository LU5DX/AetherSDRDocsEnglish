# Run an Autotune on the External TGXL

This page explains how to start an automatic tune cycle on a 4O3A Tuner Genius XL connected to your FLEX-8600. Use autotune to find the best C1/L/C2 relay combination for your current frequency and antenna.

## Before you start

- A Tuner Genius XL must be detected by AetherSDR. The TUN tray button on the right sidebar appears only when a TGXL is present.
- The radio must be connected. The Tuner applet is unavailable without an active radio connection.
- Set your operating frequency before tuning. The TGXL tunes to the current transmit frequency.
- Ensure the tuner is not in STANDBY. The OPERATE button must show "OPERATE" (green) before autotune will be effective.

## Steps

1. Click the **TUN** tray button on the right sidebar to open the Tuner applet.
2. Confirm the OPERATE button shows "OPERATE" (green). If it shows "BYPASS" or "STANDBY", click it until it cycles back to "OPERATE".
3. Click **TUNE**.
4. The button turns red and reads "TUNING..." while the tune cycle runs.
5. When the cycle completes, the button briefly displays "SWR x.xx" — the settled post-tune SWR — for approximately 2.5 seconds, then returns to "TUNE".

## What each control does

| Control | Description | Valid range |
|---|---|---|
| **TUNE** | Starts the autotune cycle. Turns red and reads "TUNING..." during tuning; flashes the final SWR result for 2.5 s when done. | — |
| **Fwd Pwr** | Displays TGXL-reported forward power during the tune pulse. | 0–200 W (barefoot), 0–600 W (Aurora), 0–2000 W (with PGXL) |
| **SWR** | Displays TGXL-reported SWR in real time. | 1.0–3.0 (red above 2.5) |
| **C1** | Shows the C1 relay bank position after tuning. | 0–255 |
| **L** | Shows the L relay bank position after tuning. | 0–255 |
| **C2** | Shows the C2 relay bank position after tuning. | 0–255 |

## Tips

- The SWR value flashed on the TUNE button after a cycle is the settled reading captured up to 400 ms after the TGXL reports tuning complete. This gives the tuner time to report its final value rather than a mid-sweep reading.
- Watch the C1, L, and C2 relay bars to confirm the TGXL has switched to a new network after the tune. If all three remain at 0, the tuner may not have engaged.

## Troubleshooting

- **TUN tray button is not visible** — The TGXL has not been detected. Check the physical connection between the FLEX-8600 and the TGXL and verify the radio firmware is 4.1.5.
- **TUNE button returns to "TUNE" immediately without flashing an SWR result** — The tuning cycle completed but no valid SWR reading arrived from the TGXL. Check the TGXL's connection and that the tuner is in OPERATE, not BYPASS or STANDBY.
- **Button reads "TUNING..." but never finishes** — The TGXL did not report end of tune. Check RF continuity — an open or shorted antenna can cause the tuner to time out.

## Related

- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)
