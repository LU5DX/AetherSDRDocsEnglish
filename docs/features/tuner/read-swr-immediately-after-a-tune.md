# Read SWR Immediately After a Tune

After an autotune completes, AetherSDR briefly displays the final settled SWR value directly on the TUNE button, giving you an instant pass/fail reading without looking at the SWR gauge.

## Before you start

- The Tuner applet must be visible. If it is not, click the TUN tray button on the right sidebar. The TUN tray button appears only when a Tuner Genius XL is detected.
- The radio must be connected.

## Steps

1. Click TUN on the right sidebar to open the Tuner applet.
2. Click TUNE.
3. Watch the TUNE button. It turns red and reads TUNING... while the autotune sweep runs.
4. When tuning finishes, the button returns to its normal style and briefly displays `SWR x.xx`, where `x.xx` is the final settled SWR value reported by the TGXL.
5. Read the SWR value from the button label. The display reverts to TUNE after 2.5 seconds.

## What each control does

| Control | Kind | Behavior | Valid range |
|---|---|---|---|
| TUNE | Button | Starts autotune. Label cycles: TUNE → TUNING... → SWR x.xx → TUNE. | — |
| SWR | Meter | Displays live TGXL-reported SWR continuously. | 1.0–3.0 (red above 2.5) |

## Tips

- The post-tune SWR shown on the TUNE button is captured after a short settling window following the end of the sweep. This ensures the value reflects the tuner's final relay position, not a mid-sweep reading.
- If you miss the 2.5-second display, the SWR meter shows the current live SWR at all times.

## Troubleshooting

- **The TUNE button reverts to TUNE without showing an SWR value** — The TGXL did not return a valid SWR reading. Check that the tuner is in OPERATE mode (not BYPASS or STANDBY) and that the antenna is connected.
- **The SWR meter reads above 2.5 (red) after tuning** — The autotune did not find an acceptable match on the current frequency. Try a different antenna or check the feedline.

## Related

- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
- [Tuner overview](overview.md)
