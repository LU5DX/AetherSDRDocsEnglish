# Fix TUNE not working after upgrading to firmware 4.2 (configure direct TGXL connection)

Firmware 4.2 broke the radio's internal path for sending the autotune command to the Tuner Genius XL. Since AetherSDR v0.9.2.1, the TUNE button can bypass the radio firmware entirely by connecting to the TGXL directly on port 9010. This page explains how to configure that direct connection.

## Before you start

- AetherSDR v0.9.2.1 or later is installed.
- Your TGXL is powered on and reachable from the computer running AetherSDR (not just from the radio).
- You know the TGXL's IP address.
- You are connected to the radio. The TUN tray button is visible in the right sidebar (the Tuner applet appears only when a Tuner Genius XL is detected).

## Steps

1. Open `Settings > Radio Setup...`.
2. Select the **Tuner** tab.
3. Enter your TGXL's IP address and confirm the port is set to **9010**.
4. Click **Apply** or **OK** to save.
5. In the right sidebar, click the **TUN** tray button to open the Tuner applet.
6. Click **TUNE**.

The button turns red and reads **TUNING...** while the autotune sweep runs. When complete, it flashes **SWR x.xx** for approximately 2.5 seconds, then returns to **TUNE**.

## Tips

- When a direct connection is active, AetherSDR sends the native `autotune` command directly to the TGXL over port 9010, bypassing the `tgxl autotune handle=<H>` path through the radio firmware that broke in 4.2.
- If no direct connection is configured, the TUNE button falls back to the radio firmware path. On firmware 4.2 that path may not work; configuring the direct connection is the reliable fix.
- With a direct connection active, the C1, L, and C2 relay bars also enable mousewheel adjustment, and the ANT 1 / ANT 2 / ANT 3 antenna switch row becomes visible if your TGXL has a 3x1 switch.

## Troubleshooting

- **TUNE button shows TUNING... but never returns an SWR result** — The TGXL may not be reachable on port 9010 from your computer. Verify the IP address in `Settings > Radio Setup...` under the Tuner tab, and confirm there is no firewall blocking port 9010 between your computer and the TGXL.
- **TUN tray button is not visible** — The Tuner applet is hidden until AetherSDR detects a Tuner Genius XL. Confirm the TGXL is powered on and the radio recognises it before opening the applet.
- **SWR result flashes a very high value after tuning** — The post-tune SWR capture window is 400 ms. If the TGXL reports the settled SWR outside that window, the displayed value may not reflect the final match. Try the tune again; the value shown is the lowest SWR seen in the capture window.

## Related

- [Connect TGXL, PGXL or Antenna Genius by IP](connect-tgxl-pgxl-or-antenna-genius-by-ip.md)
- [Run an autotune on the external TGXL](../../features/tuner/run-an-autotune-on-the-external-tgxl.md)
- [Read SWR immediately after a tune](../../features/tuner/read-swr-immediately-after-a-tune.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](../../features/tuner/put-the-tuner-in-operate-bypass-or-standby.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](../../features/tuner/fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)
- [Switch between three antennas on a TGXL 3x1](../../features/tuner/switch-between-three-antennas-on-a-tgxl-3x1.md)
- [Tuner overview](../../features/tuner/overview.md)
