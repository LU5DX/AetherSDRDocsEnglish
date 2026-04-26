# Read SWR Immediately After a Tune

After clicking TUNE, the Tuner applet captures the final settled SWR from the 4O3A Tuner Genius XL and displays it briefly on the TUNE button so you can confirm the match without looking at the SWR gauge.

## Before you start

- A Tuner Genius XL must be detected by AetherSDR. The TUN tray button on the right sidebar appears only when the TGXL is present.
- The Tuner applet must be open. Click the TUN tray button to open it if it is not already visible.
- The tuner must be in OPERATE state (OPERATE button shows green). See [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md).

## Steps

1. Click TUNE. The button turns red and its label changes to `TUNING...`.
2. Wait. When the autotune cycle completes, the button label changes to `SWR x.xx`, where `x.xx` is the settled SWR reported by the TGXL.
3. Read the SWR value directly from the TUNE button. The value is displayed for 2.5 seconds, then the button returns to `TUNE`.

## What each control does

| Control | Kind | Behavior | Valid range |
|---------|------|----------|-------------|
| TUNE | Button | Starts autotune. Label cycles: `TUNE` → `TUNING...` → `SWR x.xx` (flashes for 2.5 s) → `TUNE`. | — |
| SWR | Meter | Displays TGXL-reported SWR in real time throughout the session. Red above 2.5. | 1.0–3.0 |

## Tips

- The `SWR x.xx` value on the TUNE button reflects the settled post-tune reading, not a mid-sweep sample. AetherSDR waits 400 ms after the tune cycle ends before freezing the value, giving the TGXL time to report its final settled SWR over TCP.
- If you miss the 2.5-second flash, the SWR gauge shows the current live SWR at all times.

## Troubleshooting

- **TUNE button returns to `TUNE` without showing an SWR value** — The tuning cycle may have been aborted before a valid SWR reading arrived. Click TUNE again to run a new autotune.
- **TUN tray button is not visible** — AetherSDR has not detected a Tuner Genius XL. Check the TGXL connection and that the radio firmware is 4.1.5.

## Related

- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
