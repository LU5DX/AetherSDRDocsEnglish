# Run an Autotune on the External TGXL

This page explains how to start an automatic tuning cycle on a connected 4O3A Tuner Genius XL. Use autotune to find the best C1/L/C2 relay combination for your current frequency and antenna.

## Before you start

- A Tuner Genius XL must be detected by AetherSDR. The TUN tray button appears on the right sidebar only when a TGXL is present.
- The radio must be connected. The Tuner applet requires an active radio connection.
- The TGXL should be in OPERATE state (button shows "OPERATE" in green). Autotune will not produce a useful result if the tuner is in BYPASS or STANDBY.

## Steps

1. Click the TUN tray button on the right sidebar to open the Tuner applet.
2. Confirm the OPERATE button shows "OPERATE" (green). If it shows "BYPASS" or "STANDBY", click it until "OPERATE" appears.
3. Click TUNE.
4. Wait while the button turns red and reads "TUNING...". Do not transmit manually during this time.
5. When tuning completes, the button briefly displays the result — for example, "SWR 1.42" — for approximately 2.5 seconds, then returns to "TUNE".
6. Check the SWR gauge to confirm the final settled SWR value.

## What each control does

| Control | Description | Valid range |
|---|---|---|
| TUNE | Starts the autotune cycle. Turns red and reads "TUNING..." while active. Flashes the post-tune SWR for 2.5 seconds when complete, then resets to "TUNE". Since v0.9.2.1, when a direct TGXL connection (port 9010) is configured, sends the native "autotune" command directly to the TGXL instead of routing through the radio's firmware path. Configure this in **Radio Setup → Tuner**. Falls back to the radio path when no direct connection is available. | — |
| OPERATE | Cycles the tuner state: OPERATE (green) → BYPASS (orange) → STANDBY → OPERATE. Must be in OPERATE for a meaningful tune. | — |
| ANT 1, ANT 2, ANT 3 | Selects antenna port 1, 2, or 3 on the TGXL 3x1 switch. Row hidden unless direct TGXL connection is active and the antenna switch is present. | — |
| PWR | Displays TGXL-reported forward power. Scale depends on your configuration: 0–200 W barefoot (yellow > 80 W, red > 125 W), 0–600 W Aurora (yellow > 400 W, red > 500 W), 0–2000 W with PGXL (yellow > 1000 W, red > 1500 W). Labels update live; text clears 800 ms after power drops below threshold to prevent blinking. | 0–2000 W |
| SWR | Displays TGXL-reported SWR. Gauge turns red above 2.5. Labels update live; text clears 800 ms after SWR drops below threshold to prevent blinking. | 1.0–3.0 |
| C1 | Shows the C1 relay bank position; mousewheel scroll adjusts the relay when direct TGXL connection is active. | 0–255 |
| L | Shows the L relay bank position; mousewheel scroll adjusts the relay when direct TGXL connection is active. | 0–255 |
| C2 | Shows the C2 relay bank position; mousewheel scroll adjusts the relay when direct TGXL connection is active. | 0–255 |

## Tips

- The SWR displayed on the TUNE button after tuning reflects a settled value captured up to 400 ms after the tuning cycle ends. This is the final TGXL-reported figure, not a mid-sweep reading.
- If you need to read the post-tune SWR after the 2.5-second flash has expired, watch the SWR gauge directly.
- The PWR gauge features "ballistic" behavior: the bar rises quickly on RF bursts but decays over approximately 800 ms, providing a smooth reading.
- A peak hold marker (white tick) appears on the PWR gauge at the highest forward power level observed. It clears automatically after 2.5 seconds of no new peaks.

## Troubleshooting

- **The TUN tray button does not appear** — AetherSDR has not detected a TGXL. Check that the tuner is powered on and communicating with the radio or directly with AetherSDR.
- **TUNE button returns to "TUNE" immediately without showing an SWR result** — The tuner may not have been in OPERATE state, or the tuning cycle completed with no valid SWR data returned. Confirm the OPERATE button shows "OPERATE" (green) before clicking TUNE.
- **SWR gauge reads red (above 2.5) after tuning** — The tuner could not find a satisfactory match. Check antenna connections and confirm you are within a band the antenna covers.

## Related

- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)
- [Tuner overview](overview.md)