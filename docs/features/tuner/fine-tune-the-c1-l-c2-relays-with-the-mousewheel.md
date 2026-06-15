## Fine-tune the C1/L/C2 relays with the mousewheel

After an autotune, you can nudge the C1, L, and C2 relay bank positions one step at a time using the mousewheel. This lets you manually walk the tuner through adjacent relay positions to chase a lower SWR without triggering a full retune.

## Before you start

- A Tuner Genius XL (TGXL) must be detected by AetherSDR. The Tuner applet is hidden until that happens.
- A **direct TGXL connection** must be active. Mousewheel scrolling on the relay bars is disabled when AetherSDR is communicating with the TGXL only through the radio (non-direct mode).
- Open the Tuner applet by clicking the **TUN** tray button on the right sidebar.

## Steps

1. Confirm the Tuner applet is visible. If not, click the **TUN** tray button.
2. Verify a direct TGXL connection is active. If the relay bars do not respond to scrolling, the direct connection is not established — see [Tuner overview](overview.md).
3. Position your mouse cursor over the **C1** bar.
4. Scroll the mousewheel up to increase the C1 relay position by one step, or down to decrease it by one step.
5. Repeat on the **L** bar to adjust the inductance relay bank.
6. Repeat on the **C2** bar to adjust the second capacitor relay bank.
7. Watch the **SWR** gauge after each step to assess the effect.

## What each control does

| Control | What it shows | Valid range | Default | Setting key |
|---------|--------------|-------------|---------|-------------|
| **C1** | C1 relay bank position | 0–255 | 0 | — |
| **L** | L relay bank position | 0–255 | 0 | — |
| **C2** | C2 relay bank position | 0–255 | 0 | — |
| **SWR** | TGXL-reported SWR | 1.0–3.0 (red above 2.5) | — | — |
| **Fwd Pwr** | TGXL-reported forward power | 0–200 W barefoot, 0–600 W Aurora, 0–2000 W with PGXL | — | — |

## Notes about power and SWR display

- The forward power gauge auto-scales based on your radio and amplifier configuration:
  - **Barefoot (no amp):** 0–200 W, yellow above 80 W, red above 125 W
  - **Aurora (500 W amp):** 0–600 W, yellow above 400 W, red above 500 W
  - **PGXL:** 0–2000 W, yellow above 1000 W, red above 1500 W
- Scale labels and threshold colors update automatically when you change amplifier settings in Radio Setup.
- The power gauge uses slow release ballistics: the bar rises quickly on RF bursts but decays over approximately 800 ms, preventing flicker from inter-packet noise.
- A peak hold indicator (white tick) marks the highest forward power seen. The peak clears after 2.5 seconds with no new peak.
- When power drops below the detection threshold, the PWR and SWR labels remain visible for 800 ms before returning to their default text, preventing blinking during brief pauses in transmission.
- The SWR gauge automatically snaps to 1.0 when forward power is below 5 W. This prevents the gauge from pegging at a high value due to idle noise when no signal is present. The reading updates normally when forward power is 5 W or higher.

## Tips

- Scrolling adjusts the relay position one step per wheel detent. There is no coarse/fine mode; each scroll event sends one increment or decrement to the TGXL.
- If you want to return to a known-good position, run a fresh autotune using the **TUNE** button rather than stepping back manually.

## Troubleshooting

- **Scrolling the mousewheel over a relay bar does nothing** — The direct TGXL connection is not active. Mousewheel scroll is enabled only when the direct connection is present. Check the connection state in the Tuner overview.
- **Relay bar values change but SWR does not update** — The **SWR** gauge reflects TGXL-reported values via the direct connection. If the meter is frozen, the direct connection may have dropped.
- **Power gauge stays stuck at a value** — The slow release ballistics keep the bar visible for 800 ms. If it remains stuck longer, the direct connection may have dropped.
- **SWR gauge shows 1.0 even with a mismatch** — Check your forward power. The SWR gauge holds at 1.0 when forward power is below 5 W. Key the transmitter or increase drive until the power reading exceeds 5 W.

## Related

- [Tuner overview](overview.md)
- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](put-the-tuner-in-operate-bypass-or-standby.md)