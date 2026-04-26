# Fine-tune the C1/L/C2 relays with the mousewheel

Use the mousewheel over the C1, L, or C2 relay bars to step relay positions up or down by hand. This lets you nudge the tuner network after an autotune or set a starting point manually.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- A 4O3A Tuner Genius XL must be detected; the TUN tray button appears on the right sidebar only when one is present.
- The TGXL must be connected via a direct TGXL connection. Mousewheel scrolling on the relay bars is disabled when only a radio-mediated connection is active.

## Steps

1. Click the TUN tray button on the right sidebar to open the Tuner applet.
2. Confirm that the C1, L, and C2 relay bars are visible in the lower-left section of the applet.
3. Hover the mouse pointer over the C1, L, or C2 bar you want to adjust.
4. Scroll the mousewheel up to increment the relay position, or scroll down to decrement it.
5. Repeat for each bar you want to adjust.

## What each control does

| Control | What it shows | Valid range | Default |
|---------|---------------|-------------|---------|
| C1 | C1 relay bank position | 0–255 | 0 |
| L | L relay bank position | 0–255 | 0 |
| C2 | C2 relay bank position | 0–255 | 0 |

None of these controls persist a setting key; the values reflect the live state reported by the TGXL.

## Tips

- Mousewheel adjustment is available only when a direct TGXL connection is active. If scrolling the bars has no effect, check your TGXL connection status.
- The relay bars update in real time as the TGXL acknowledges each step. Watch the SWR gauge while scrolling to find a lower SWR manually.
- To reset to a known network state, run an autotune first, then use the mousewheel to fine-tune from the result.

## Troubleshooting

- **Scrolling the relay bar does nothing** — The direct TGXL connection is not active. Mousewheel input is disabled when only a radio-mediated connection is present. Verify the direct TGXL connection and try again.

## Related

- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)
