# Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio

The CAT Control applet runs up to four rigctld-compatible TCP servers (and PTY symlinks on Linux/macOS), one per slice channel (A–H), so external logging and contest software can control the radio over a network socket or serial-style path. In v26.5.3, the applet uses a native Hamlib NET rigctl implementation, replacing the need for a standalone rigctld bridge. Use this page to start those servers and point your logging software at the correct port.

## Before you start

- AetherSDR must be connected to the radio. The CAT applet requires an active radio connection.
- Decide which base port to use. The default is `4532`. Channels A, B, C, and D bind to base, base+1, base+2, and base+3 respectively.
- Make sure no other application (including a standalone rigctld instance) is already listening on those ports.

## Steps

1. Click the **CAT** tray button on the right sidebar to open the CAT Control applet. The applet is hidden by default.
2. Check the value in the **Base** field. The default is `4532`. Change it if needed (valid range: 1024–65535). Press Enter or click away to confirm; out-of-range values snap back to `4532`.
3. Click **Enable TCP**. The button highlights green when active.
4. Verify the channel rows. Each row labelled A, B, C, or D should update from `(stopped)` to `:<port> (0 clients)` once the servers are listening.
5. In your logging or contest software (N1MM, Log4OM, WSJT-X, or similar), configure the CAT connection as **rigctld (net)** and enter `localhost` (or the AetherSDR machine's IP address) and the port for the channel you want to control — for example, `4532` for channel A or `4533` for channel B.
6. When the external software connects, the channel row updates to `:<port> (1 client)`.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Enable TCP** | Off | On / Off | — | Starts or stops all four rigctld TCP servers. Also writes the current base port to `CatTcpPort`. |
| **Base** | `4532` | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Channel A uses this port; B, C, and D use base+1, base+2, base+3. If servers are already running, they restart on the new ports immediately. |
| **Enable TTY** | Off | On / Off | — | Starts or stops PTY symlinks for serial-style access. The symlink path is shown per channel. On Linux, paths are under `$XDG_RUNTIME_DIR/aethersdr/cat-A` through `cat-D`. On macOS, paths are under `~/Library/Caches/AetherSDR/cat-A` through `cat-D`. Not needed for TCP-based software. |
| Channel rows (A–D) | `(stopped)` | — | — | Shows each channel's TCP status and connected client count. Badge colour matches the slice colour. The PTY path is shown when enabled. |

## Security update in v26.5.3

In v26.5.3, the PTY symlink location moved from `/tmp` to per-user runtime directories (`$XDG_RUNTIME_DIR/aethersdr/` on Linux, `~/Library/Caches/AetherSDR/` on macOS). This change fixes a cross-user symlink vulnerability (GHSA-qxhr-cwrc-pvrm). Atomic symlink replacement (creating a temporary symlink then renaming it) closes the TOCTOU race window.

## Tips

- If you only use one logging program at a time, channel A on port `4532` is sufficient. Channels B–D exist for running multiple programs simultaneously against different slices.
- To have the TCP servers start automatically every time AetherSDR launches, use `Settings > Autostart rigctld with AetherSDR`.
- Changing the **Base** value while **Enable TCP** is active restarts all running servers on the new ports immediately. Update your logging software's port setting to match before reconnecting.
- For PTY access, external software opens the path shown in the channel row, which is the same location where the actual symlink is created.

## Troubleshooting

- **Channel row stays `(stopped)` after clicking Enable TCP** — Another process is likely already listening on that port. Choose a different base port, or stop the conflicting application.
- **Logging software shows "connection refused"** — Confirm **Enable TCP** is on (button is green) and that you are using the correct port number for the channel. If AetherSDR is on a remote machine, use that machine's IP address rather than `localhost`.
- **Client count does not increment** — The software connected but immediately disconnected. Check that your logging software is set to **rigctld** (network) mode, not a direct serial or Hamlib mode that expects a different protocol.

## Related

- [CAT Control overview](overview.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)