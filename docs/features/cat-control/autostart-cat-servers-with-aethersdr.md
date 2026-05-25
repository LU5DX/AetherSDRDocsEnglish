# Autostart CAT servers with AetherSDR

Configure AetherSDR to start the rigctld TCP servers and/or PTY virtual serial ports automatically each time the application launches, so external logging and contest software is ready without manual intervention.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio before the CAT servers can operate. The autostart setting is saved regardless, but servers only become active once a radio connection is established.
- Decide whether you need TCP, PTY (Linux/macOS only), or both. TCP works on all platforms; PTY is for applications that expect a serial device path.
- PTY symlink paths are located in per-user runtime directories for security:
  - Linux: `$XDG_RUNTIME_DIR/aethersdr/cat-A` through `cat-D`
  - macOS: `~/Library/Caches/AetherSDR/cat-A` through `cat-D`

## Steps

### Enable autostart for TCP servers

1. Open `Settings > Autostart rigctld with AetherSDR`.
2. Click the item to place a checkmark next to it.

AetherSDR will now start all four rigctld TCP servers automatically on the next launch. The base port persisted in `CatTcpPort` (default `4532`) is used; channels bind to port, port+1, port+2, and port+3.

### Enable autostart for PTY virtual serial ports

1. Open `Settings > Autostart CAT with AetherSDR`.
2. Click the item to place a checkmark next to it.

AetherSDR will now create the PTY symlinks under the per-user runtime paths automatically on the next launch:
- Linux: `$XDG_RUNTIME_DIR/aethersdr/cat-A` through `cat-D`
- macOS: `~/Library/Caches/AetherSDR/cat-A` through `cat-D`

### Verify the current session without restarting

If you want the servers running immediately in the current session as well:

1. Click the `CAT` tray button on the right sidebar to open the CAT Control applet.
2. Click `Enable TCP` to start the TCP servers now.
3. Click `Enable TTY` to start the PTY symlinks now (Linux/macOS only).

The channel rows (A, B, C, D) will update from `(stopped)` to `:<port> (0 clients)` as each server comes up. Each channel row also displays the current PTY path.

## What each control does

| Control              | Kind          | Default     |
|----------------------|---------------|-------------|
| `Enable TCP`         | Toggle button | Off         |
| `Enable TTY`         | Toggle button | Off         |
| `Base`               | Text field    | `4532`      |
| A/B/C/D channel rows | Indicator     | `(stopped)` |

The per-channel PTY path indicator shows:
- `stopped` when no PTY is active
- The full symlink path (e.g., `/run/user/1000/aethersdr/cat-A` on Linux or `~/Library/Caches/AetherSDR/cat-A` on macOS) when the PTY is running

## Tips

- The `Enable TCP` toggle in the applet reflects the `AutoStartRigctld` setting. The `Enable TTY` toggle reflects the `AutoStartCAT` setting. Toggling either button in the applet updates the autostart preference at the same time, so you can use the applet buttons instead of the Settings menu if you prefer.
- If you change the `Base` port after enabling autostart, the new port is saved to `CatTcpPort` and the running servers restart on the new base immediately. The saved value is used on the next autostart as well.
- In v26.5.3, AetherSDR includes a native Hamlib NET rigctl implementation, replacing the need for a standalone rigctld bridge. Slices A–H each expose a TTY (per-user runtime path) and a TCP port (4532–4539).
- PTY symlink creation uses atomic replacement (symlink + rename) to prevent TOCTOU race conditions (GHSA-qxhr-cwrc-pvrm).

## Troubleshooting

- **Servers do not start after launch even though autostart is enabled** — The radio must be connected before the servers become active. Confirm the connection state in the title bar and retry once connected.
- **PTY symlinks do not appear** — The `Enable TTY` autostart is only functional on Linux and macOS. On Windows, `Enable TTY` has no effect. On Linux, verify that `$XDG_RUNTIME_DIR` is set (typically `/run/user/<uid>`).
- **Port already in use** — If another application occupies a port in the Base–Base+3 range, the corresponding server will fail silently. Change the `Base` value in the CAT Control applet to an unused port range and re-enable TCP.
- **Channel badge colours appear incorrect** — Slice colours are managed dynamically. If badges show unexpected colours, disconnect and reconnect to the radio so that slice colour assignments are refreshed.

## Related

- [CAT Control overview](overview.md)
- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)