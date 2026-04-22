# Fine-tune the C1/L/C2 relays with the mousewheel

After an autotune, you can nudge the C1, L, and C2 relay positions by hand. This lets you optimize the match without running a full autotune cycle.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- A 4O3A Tuner Genius XL must be detected; the TUN tray button appears on the right sidebar only when one is present.
- The TGXL must be connected via a direct TGXL connection. Mousewheel scrolling on the relay bars is disabled when only a radio-mediated connection is active.
- The Tuner applet must be open. Click the TUN tray button to show it.

## Steps

1. Confirm the relay bars are scroll-enabled. If a direct TGXL connection is active, the C1, L, and C2 bars respond to the mousewheel. If they do not respond, see Troubleshooting below.
2. Hover the mouse pointer over the C1 bar.
3. Scroll the mousewheel up to increase the C1 relay position, or down to decrease it. Each scroll step adjusts the position by one unit. Valid range: 0–255.
4. Hover over the L bar and scroll to adjust the L relay position. Valid range: 0–255.
5. Hover over the C2 bar and scroll to adjust the C2 relay position. Valid range: 0–255.
6. Monitor the SWR gauge while adjusting to confirm the match is improving.

## What each control does

| Control | Kind | Default | Valid range | Behavior |
|---------|------|---------|-------------|----------|
| C1 | Relay bar | 0 | 0–255 | Displays and adjusts the C1 relay bank position. Scroll up increments, scroll down decrements. |
| L | Relay bar | 0 | 0–255 | Displays and adjusts the L relay bank position. Scroll up increments, scroll down decrements. |
| C2 | Relay bar | 0 | 0–255 | Displays and adjusts the C2 relay bank position. Scroll up increments, scroll down decrements. |
| SWR | Meter | — | 1.0–3.0 (red above 2.5) | Shows TGXL-reported SWR in real time as you adjust the relays. |

## Tips

- Adjust one relay at a time and watch the SWR gauge settle before moving to the next. The interaction between C1, L, and C2 means changing one affects the others.
- If the SWR is far from 1:1, run a full autotune first, then use the mousewheel for fine correction.

## Troubleshooting

- **Scrolling the mousewheel over a relay bar has no effect** — A direct TGXL connection is not active. Check your TGXL network or USB connection. Mousewheel scrolling is enabled only when the direct connection is present.
- **The TUN tray button is not visible** — No Tuner Genius XL has been detected. Verify the TGXL is powered on and reachable from the same network as AetherSDR.

## Related

- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
