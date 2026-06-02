# DAX Audio

The **DAX Audio** applet shows per-channel RX meters and gain sliders for DAX 1-4 plus a single TX meter, with a master Enable toggle that persists as `AutoStartDAX`. In v0.9.7 (Linux), DAX RX latency drops from ~400 ms to ~200 ms via a native PipeWire `pw_stream` source path, replacing the previous PulseAudio client.

## Opening DAX Audio

Click the **DAX Audio** button in the toolbar.

## DAX Audio Layout

The DAX Audio window contains controls for enabling the DAX audio bridge, setting per-channel RX gain, TX gain, and viewing slice assignments.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **DAX Enable** | off | on/off | `AutoStartDAX` | Starts the DAX audio bridge; emits `daxToggled`. Button label is "Enable"; master switch for all DAX RX and TX streams. |
| **DAX 1 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain1` | Combined meter/slider; drag to set RX gain on DAX channel 1. Emits `daxRxGainChanged(1, g)` and persists. |
| **DAX 2 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain2` | Combined meter/slider; drag to set RX gain on DAX channel 2. |
| **DAX 3 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain3` | Combined meter/slider; drag to set RX gain on DAX channel 3. |
| **DAX 4 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain4` | Combined meter/slider; drag to set RX gain on DAX channel 4. |
| **TX gain+meter** | 0.5 | 0.0–1.0 | `DaxTxGain` | Combined meter/slider for the DAX TX stream. |

### Slice Assignment Indicators

Each DAX channel shows which slice (if any) is currently routed to it.

| Indicator | States | Meaning |
|-----------|--------|---------|
| **DAX 1 assignment** | —, Slice A..H | The slice (if any) currently assigned to this DAX channel. |
| **DAX 2 assignment** | —, Slice A..H | The slice (if any) currently assigned to this DAX channel. |
| **DAX 3 assignment** | —, Slice A..H | The slice (if any) currently assigned to this DAX channel. |
| **DAX 4 assignment** | —, Slice A..H | The slice (if any) currently assigned to this DAX channel. |
| **TX assignment** | —, Slice A..H | The slice currently holding TX privileges (drives DAX TX). |

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