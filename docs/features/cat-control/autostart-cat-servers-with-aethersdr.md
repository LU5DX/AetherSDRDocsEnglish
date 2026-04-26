# Autostart CAT servers with AetherSDR

Configure AetherSDR to start its CAT TCP servers and/or PTY serial ports automatically each time the application launches, so external logging and contest software is ready without manual intervention.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. CAT Control requires a radio connection.
- Decide whether you need TCP servers (for software such as N1MM, Log4OM, or WSJT-X), PTY serial ports (Linux/macOS only), or both.
- Confirm the base TCP port you want to use. The default is `4532`. See [Change the base TCP port](change-the-base-tcp-port.md) if you need a different value.

## Steps

### Autostart TCP servers

1. Click `Settings > Autostart rigctld with AetherSDR`.

   A checkmark appears next to the item. On the next launch, AetherSDR will start all four rigctld TCP servers on ports `Base` through `Base+3` automatically.

2. To verify the servers started, click the **CAT** tray button on the right sidebar to open the CAT Control applet. Each channel row (A, B, C, D) should show a port and client count instead of `(stopped)`.

### Autostart PTY serial ports (Linux/macOS only)

1. Click `Settings > Autostart CAT with AetherSDR`.

   A checkmark appears next to the item. On the next launch, AetherSDR will create PTY symlinks at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D` automatically.

2. To verify, open the CAT Control applet via the **CAT** tray button. The PTY path column in each channel row will show the active symlink path when running.

### Disable autostart

1. Click the same menu item again (`Settings > Autostart rigctld with AetherSDR` or `Settings > Autostart CAT with AetherSDR`).

   The checkmark is removed. The servers or PTY ports will no longer start on launch.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| `Settings > Autostart rigctld with AetherSDR` | Off | On / Off | `AutoStartRigctld` | When checked, starts all four rigctld TCP servers on launch. |
| `Settings > Autostart CAT with AetherSDR` | Off | On / Off | `AutoStartCAT` | When checked, creates PTY symlinks on launch (Linux/macOS). |
| Base (in CAT Control applet) | `4532` | 1024–65535 | `CatTcpPort` | Base TCP port. Channels bind to `Base`, `Base+1`, `Base+2`, `Base+3`. Out-of-range values revert to `4532`. |

## Tips

- Autostart only brings up the servers; it does not open the CAT Control applet panel. The applet remains hidden until you click the **CAT** tray button.
- If you change the base port in the `Base` field while TCP servers are running, they restart automatically on the new ports. You do not need to toggle `Enable TCP` off and on.
- The TCP autostart setting (`AutoStartRigctld`) and the PTY autostart setting (`AutoStartCAT`) are independent. You can enable one, both, or neither.

## Troubleshooting

- **Channel rows still show `(stopped)` after launch with autostart enabled** — Autostart requires a radio connection before servers can bind. If AetherSDR launched but has not yet connected to the radio, the servers will not start. Connect to the radio, then toggle `Enable TCP` manually in the CAT Control applet.
- **PTY paths do not appear on Windows** — PTY serial port creation is a Linux/macOS feature. The `Settings > Autostart CAT with AetherSDR` item has no effect on Windows.
- **Port binding fails at launch** — Another application may already be using port `4532` (or your configured base port). Change the base port in the `Base` field of the CAT Control applet and relaunch.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)
