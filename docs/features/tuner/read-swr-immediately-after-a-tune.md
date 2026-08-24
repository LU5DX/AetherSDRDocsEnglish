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

If you miss the flash, the SWR gauge continues to display the live TGXL-reported SWR value after tuning. The gauge scale only repaints when the scale-relevant inputs (power or amplifier state) actually change, so the displayed scale stays stable during normal operation.

## What each control does

| Control | Kind | Behavior | Valid range |
|---|---|---|---|
| Fwd Pwr | Meter | Displays TGXL-reported forward power. Scale is 0–200 W barefoot, 0–600 W with Aurora amplifier, 0–2000 W with PGXL amplifier. The bar rises quickly on RF bursts and decays over approximately 800 ms to prevent flickering from inter-packet noise. A white tick mark shows the peak forward power, which clears after 2.5 seconds of no new peaks. Has an accessible name of "Forward power" for screen readers. | See scale |
| SWR | Meter | Displays live TGXL-reported SWR continuously. Turns red above 2.5. The bar rises quickly and decays over approximately 800 ms. A white tick mark shows the peak SWR, which clears after 2.5 seconds of no new peaks. When forward power is below 5 W (noise floor), the gauge snaps to 1.0 (empty) to prevent idle noise from lighting up the bar. Has an accessible name of "SWR" for screen readers. | 1.0–3.0 |
| C1 | Meter | Shows the C1 relay bank position. Mousewheel scroll adjusts the relay position when a direct TGXL connection is active. Has an accessible name of "Tuner capacitor C1" for screen readers. | 0–255 |
| L | Meter | Shows the L relay bank position. Mousewheel scroll adjusts the relay position. Has an accessible name of "Tuner inductor L" for screen readers. | 0–255 |
| C2 | Meter | Shows the C2 relay bank position. Mousewheel scroll adjusts the relay position. Has an accessible name of "Tuner capacitor C2" for screen readers. | 0–255 |
| TUNE | Button | Starts autotune. Turns red and reads "TUNING..." during the sweep. Flashes "SWR x.xx" for 2.5 s after completion. Returns to "TUNE" afterward. When a direct TGXL connection (port 9010) is configured in Radio Setup → Tuner, the autotune command is sent directly to the TGXL, bypassing the radio's firmware path. Falls back to the radio path when no direct connection is available. | — |
| OPERATE | Button | Cycles through three states: OPERATE (green), BYPASS (orange), and STANDBY (default). Each click advances to the next state. | — |
| ANT 1, ANT 2, ANT 3 | Button | Selects the corresponding antenna port on the TGXL 3x1 switch. These buttons appear only when a direct TGXL connection is active and the antenna switch is present. | — |

## Tips

- The 400 ms capture window after tuning=0 exists because the TGXL's final settled SWR value often arrives over TCP slightly after the tune-complete signal. The value shown on the button reflects this settled reading, not a mid-sweep sample.
- If the capture window expires before a valid SWR reading arrives, AetherSDR falls back to the last live SWR value from the gauge.
- The peak hold tick on the gauges helps you see the highest power or SWR reached during a transmission, which clears automatically after 2.5 seconds.
- The slow decay on the gauge bars (800 ms) prevents annoying flickering that could occur from brief gaps between UDP packets.
- The SWR gauge automatically resets to 1.0 when forward power drops below 5 W, preventing idle noise from causing false SWR readings.
- The forward power gauge scale repaints only when the actual scale changes (for example, when an amplifier is connected or disconnected), reducing unnecessary redraws during routine telemetry updates.

## Troubleshooting

- **The TUNE button returns to "TUNE" without showing an SWR value** — The tuning state transition was not preceded by an active tune (for example, the model state changed externally). Click TUNE again to run a fresh autotune.
- **The SWR gauge reads above 2.5 (red) after the tune** — The tuner was unable to find a satisfactory match on the current band and antenna. Check the antenna connection and try again, or check the C1, L, and C2 relay positions.

## Related

- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)