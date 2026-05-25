# CAT Control

The **CAT Control** applet runs up to four `rigctld`-compatible TCP servers (and PTY symlinks on Linux/macOS) so external logging and contest software can control one slice per channel. AetherSDR implements a native Hamlib NET `rigctl` protocol, eliminating the need for a standalone `rigctld` bridge.

## Opening CAT Control

Click the **CAT Control** button in the toolbar, or press `Ctrl+Shift+C`.

## CAT Control Layout

The CAT Control window contains controls for enabling TCP and TTY servers, configuring the base port, and monitoring per-channel status.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Enable TCP** | off | on/off | `CatTcpPort` | Starts/stops all four `rigctld` TCP servers on `Base..Base+3`. Also persists the current base port. |
| **Enable TTY** | off | on/off | — | Starts/stops all four PTY symlinks under `$XDG_RUNTIME_DIR/aethersdr/cat-A..D` (Linux) or `~/Library/Caches/AetherSDR/cat-A..D` (macOS). |
| **Base** | 4532 | 1024–65535 | `CatTcpPort` | Base TCP port; channels bind to port, port+1, port+2, port+3. Out-of-range values snap back to 4532; servers restart with new port if currently enabled. |

### Per-Channel Status

Each channel (A/B/C/D) displays its status in a row:

| Channel | TCP Status | PTY Path |
|---------|------------|----------|
| **A** | (stopped) | Path to symlink or "stopped" |
| **B** | (stopped) | Path to symlink or "stopped" |
| **C** | (stopped) | Path to symlink or "stopped" |
| **D** | (stopped) | Path to symlink or "stopped" |

The **TCP Status** shows:
- `(stopped)` when the server is not running
- `:<port> (1 client)` when one client is connected
- `:<port> (N clients)` when multiple clients are connected

The **PTY Path** shows the symlink path logging software can open as a serial device:
- Linux: `$XDG_RUNTIME_DIR/aethersdr/cat-A` through `cat-D`
- macOS: `~/Library/Caches/AetherSDR/cat-A` through `cat-D`
- Displays "stopped" when the TTY server is not running

## Security Notes

In v26.5.3, the PTY symlink location moved from `/tmp` to per-user runtime directories to fix a cross-user symlink vulnerability (GHSA-qxhr-cwrc-pvrm). Atomic symlink replacement via `symlink(.tmp) + rename(.tmp, final)` closes the TOCTOU window.