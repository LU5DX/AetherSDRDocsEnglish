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
2. Click the master `Enable` button (labeled `Disabled` by default) to start all CAT servers now. The button text changes to `Enabled` and the per-channel rows become editable.
3. In each channel row you wish to use, click the checkbox next to the channel badge to enable that channel's TCP server and/or PTY symlink.

The channel rows (A, B, C, D) will update from `(stopped)` to `:<port> (0 clients)` as each server comes up. Each channel row also displays the current PTY path.

## Per-channel enable checkboxes

In v26.7.4, each channel row (A, B, C, D) gained an individual enable checkbox. These checkboxes have a high-contrast style that uses a filled accent colour when checked, making the on/off state readable at a glance against the dark applet background.

- When the master `Enable` button is turned off, all per-channel checkboxes are disabled and the servers stop.
- When the master `Enable` button is turned on, you can independently enable or disable each channel by clicking its checkbox.
- Each checkbox controls both the TCP server and PTY symlink for that channel simultaneously.

## CAT Control applet overview

The CAT Control applet runs up to four rigctld-compatible TCP servers (and PTY symlinks on Linux/macOS) so external logging and contest software can control one slice per channel. Slices A–H each expose a TTY (per-user runtime path) and a TCP port (4532–4539).

## What each control does

| Control                | Kind          | Default         | Setting Key | Notes |
|------------------------|---------------|-----------------|-------------|-------|
| `Enable` master button | Toggle button | `Disabled`      | `CatEnabled` | Starts/stops all CAT servers. Button text changes to `Enabled` when active. |
| Per-channel checkboxes | Checkbox      | Unchecked       | None        | High-contrast style; visible only when master `Enable` is on. |
| `Base`                 | Text field    | `4532`          | `CatTcpPort` | Base TCP port; channels bind to port, port+1, port+2, port+3. Out-of-range values snap back to 4532. |
| A/B/C/D channel rows   | Indicator     | `(stopped)`     | None        | Each row shows channel badge, TCP status, PTY path. |

### Per-channel TCP status indicator

| State                | Meaning |
|----------------------|---------|
| `(stopped)`          | Server not running |
| `:<port> (1 client)` | Server active with 1 connected client |
| `:<port> (N clients)`| Server active with N connected clients |

### Per-channel PTY path indicator

| State                  | Meaning |
|------------------------|---------|
| `stopped`              | No PTY active |
| `<path>`               | Symlink path when PTY is running (e.g., `/run/user/1000/aethersdr/cat-A` on Linux or `~/Library/Caches/AetherSDR/cat-A` on macOS) |

## VFO selection persistence

The VFO combos in each channel row are bounded by the radio's slice-receiver count. If you reconnect to a smaller radio, a previously-chosen slice that no longer exists is preserved in settings and reappears when the slices return. Only a genuine, representable selection (including a deliberate `—`) is persisted.

## Tips

- The master `Enable` button in the applet is linked to the `Autostart rigctld with AetherSDR` and `Autostart CAT with AetherSDR` settings. Toggling the button updates both autostart preferences at the same time, so you can use the applet button instead of the Settings menu if you prefer.
- If you change the `Base` port after enabling CAT servers, the new port is saved to `CatTcpPort` and the running servers restart on the new base immediately. The saved value is used on the next autostart as well.
- In v26.5.3, AetherSDR includes a native Hamlib NET rigctl implementation, replacing the need for a standalone rigctld bridge. Slices A–H each expose a TTY (per-user runtime path) and a TCP port (4532–4539).
- PTY symlink creation uses atomic replacement (symlink + rename) to prevent TOCTOU race conditions (GHSA-qxhr-cwrc-pvrm).

## Troubleshooting

- **Servers do not start after launch even though autostart is enabled** — The radio must be connected before the servers become active. Confirm the connection state in the title bar and retry once connected.
- **Per-channel checkboxes are greyed out** — Click the master `Enable` button first to enable CAT servers before configuring individual channels.
- **PTY symlinks do not appear** — The PTY feature is only functional on Linux and macOS. On Windows, PTY has no effect. On Linux, verify that `$XDG_RUNTIME_DIR` is set (typically `/run/user/<uid>`).
- **Port already in use** — If another application occupies a port in the Base–Base+3 range, the corresponding server will fail silently. Change the `Base` value in the CAT Control applet to an unused port range and re-enable.
- **Channel badge colours appear incorrect** — Slice colours are managed dynamically. If badges show unexpected colours, disconnect and reconnect to the radio so that slice colour assignments are refreshed.

## Related

- [CAT Control overview](overview.md)
- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)