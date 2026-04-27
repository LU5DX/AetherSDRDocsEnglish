# Autostart CAT servers with AetherSDR

Configure AetherSDR to start the rigctld TCP servers and/or PTY virtual serial ports automatically each time the application launches, so external logging and contest software is ready without manual intervention.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio before the CAT servers can operate. The autostart setting is saved regardless, but servers only become active once a radio connection is established.
- Decide whether you need TCP, PTY (Linux/macOS only), or both. TCP works on all platforms; PTY is for applications that expect a serial device path such as `/tmp/AetherSDR-CAT-A`.

## Steps

### Enable autostart for TCP servers

1. Open `Settings > Autostart rigctld with AetherSDR`.
2. Click the item to place a checkmark next to it.

AetherSDR will now start all four rigctld TCP servers automatically on the next launch. The base port persisted in `CatTcpPort` (default `4532`) is used; channels bind to port, port+1, port+2, and port+3.

### Enable autostart for PTY virtual serial ports

1. Open `Settings > Autostart CAT with AetherSDR`.
2. Click the item to place a checkmark next to it.

AetherSDR will now create the PTY symlinks under `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D` automatically on the next launch.

### Verify the current session without restarting

If you want the servers running immediately in the current session as well:

1. Click the `CAT` tray button on the right sidebar to open the CAT Control applet.
2. Click `Enable TCP` to start the TCP servers now.
3. Click `Enable TTY` to start the PTY symlinks now (Linux/macOS only).

The channel rows (A, B, C, D) will update from `(stopped)` to `:<port> (0 clients)` as each server comes up.

## What each control does

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| `Enable TCP` | Toggle button | Off | — | — | Starts or stops all four rigctld TCP servers on Base through Base+3. Also persists the current base port to `CatTcpPort`. |
| `Enable TTY` | Toggle button | Off | — | — | Starts or stops all four PTY symlinks under `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. |
| `Base` | Text field | `4532` | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Out-of-range values snap back to `4532`. If TCP servers are already running, they restart on the new port immediately. |
| A/B/C/D channel rows | Indicator | `(stopped)` | — | — | Shows the channel badge, TCP status (port and client count), and PTY path for each of the four channels. |

## Tips

- The `Enable TCP` toggle in the applet reflects the `AutoStartRigctld` setting. The `Enable TTY` toggle reflects the `AutoStartCAT` setting. Toggling either button in the applet updates the autostart preference at the same time, so you can use the applet buttons instead of the Settings menu if you prefer.
- If you change the `Base` port after enabling autostart, the new port is saved to `CatTcpPort` and the running servers restart on the new base immediately. The saved value is used on the next autostart as well.

## Troubleshooting

- **Servers do not start after launch even though autostart is enabled** — The radio must be connected before the servers become active. Confirm the connection state in the title bar and retry once connected.
- **PTY symlinks do not appear** — The `Enable TTY` autostart is only functional on Linux and macOS. On Windows, `Enable TTY` has no effect.
- **Port already in use** — If another application occupies a port in the Base–Base+3 range, the corresponding server will fail silently. Change the `Base` value in the CAT Control applet to an unused port range and re-enable TCP.

## Related

- [CAT Control overview](overview.md)
- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)
