# Read SWR Immediately After a Tune

After an autotune completes, the TUNE button briefly displays the final settled SWR so you can confirm the match without looking at the SWR gauge.

## Before you start

- A 4O3A Tuner Genius XL must be connected and detected. The TUN tray button appears on the right sidebar only when a TGXL is present.
- The Tuner applet must be open. Click the TUN tray button to open it.
- The tuner should be in OPERATE state (OPERATE button shows green).

## Steps

1. Click TUNE.
2. Wait. The button turns red and reads "TUNING..." while the autotune sweep runs.
3. When tuning finishes, the button restores to its normal style and briefly reads "TUNING..." for up to 400 ms while AetherSDR captures the final settled SWR value from the TGXL.
4. The button then displays the result as "SWR x.xx" — for example, "SWR 1.34". Read this value directly from the button.
5. After 2.5 seconds, the button label returns to "TUNE".

If you miss the flash, the SWR gauge continues to display the live TGXL-reported SWR value after tuning.

## What each control does

| Control | Kind | Behavior | Valid range |
|---|---|---|---|
| TUNE | Button | Starts autotune. Turns red and reads "TUNING..." during the sweep. Flashes "SWR x.xx" for 2.5 s after completion. Returns to "TUNE" afterward. | — |
| SWR | Meter | Displays live TGXL-reported SWR continuously. Turns red above 2.5. | 1.0–3.0 |

## Tips

- The 400 ms capture window after tuning=0 exists because the TGXL's final settled SWR value often arrives over TCP slightly after the tune-complete signal. The value shown on the button reflects this settled reading, not a mid-sweep sample.
- If the capture window expires before a valid SWR reading arrives, AetherSDR falls back to the last live SWR value from the gauge.

## Troubleshooting

- **The TUNE button returns to "TUNE" without showing an SWR value** — The tuning state transition was not preceded by an active tune (for example, the model state changed externally). Click TUNE again to run a fresh autotune.
- **The SWR gauge reads above 2.5 (red) after the tune** — The tuner was unable to find a satisfactory match on the current band and antenna. Check the antenna connection and try again, or check the C1, L, and C2 relay positions.

## Related

- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)
