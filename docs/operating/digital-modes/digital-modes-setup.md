# DAX Audio

The **DAX Audio** applet shows per-channel RX meters and gain sliders for DAX 1-4 plus a single TX meter, with a master Enable toggle that persists as `AutoStartDAX`. In v0.9.7 (Linux), DAX RX latency drops from ~400 ms to ~200 ms via a native PipeWire `pw_stream` source path, replacing the previous PulseAudio client.

> **Note for Windows users:** AetherSDR does not ship a built-in DAX bridge on Windows. The DAX Audio applet displays an informational message only. Use TCI or FlexRadio's SmartSDR DAX drivers instead. See Help > Configuring Data Modes for setup instructions.

## Opening DAX Audio

Click the **DAX Audio** button in the toolbar.

## DAX Audio Layout

The DAX Audio window contains controls for enabling the DAX audio bridge, setting per-channel RX gain, TX gain, and viewing slice assignments.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **DAX Enable** | off | on/off | `AutoStartDAX` | Starts the DAX audio bridge; emits `daxToggled`. Button label reflects current state: "Enabled" when active, "Disabled" when off. Master switch for all DAX RX and TX streams. |
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

### Windows Platform Behavior

On Windows, the DAX Audio applet displays only an informational note: "No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX." No controls, meters, or indicators are built. The applet's internal state setters (`setDaxEnabled`, `setDaxRxLevel`, `setDaxTxLevel`) are guarded and do nothing.

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

# SpotHub

The **SpotHub** dialog is the central hub for connecting to DX spot sources — DX cluster, Reverse Beacon Network, WSJT-X, SpotCollector, POTA and FreeDV — and configuring how spots are displayed on the panadapter.

## Opening SpotHub

Click the **SpotHub** button in the toolbar, or press `Ctrl+Shift+S`.

## SpotHub Layout

The SpotHub dialog contains a multi-tab interface. Each source tab provides connection controls, a data console, and a spot color picker. A separate **Display** tab controls panadapter spot visualization, Signal History tunables, and DXCC coloring.

### Cluster Tab

The **Cluster** tab provides a telnet connection to a DX cluster.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Server:** | — | — | `ClusterHost` | Hostname of DX cluster to connect to. |
| **Port:** | — | 1–65535 | `ClusterPort` | Telnet port on DX cluster. |
| **Callsign:** | — | — | `ClusterCallsign` | Login callsign sent to cluster. |
| **Connect / Disconnect** | Connect | — | — | Toggles telnet connection to the cluster. |
| **Auto-connect on startup** | — | — | `ClusterAutoConnect` | Auto-connects cluster on launch. |
| **Cluster Console** | — | — | — | Read-only telnet console of raw cluster traffic. |
| **Send** | — | — | — | Sends a typed command to the cluster. |
| **Spot Color:** | — | — | `ClusterSpotColor` | Opens a color picker for cluster spots. |

### RBN Tab

The **RBN** tab provides a Reverse Beacon Network telnet source with rate limiting.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Server:** | — | — | `RbnHost` | RBN telnet hostname. |
| **Port:** | — | 1–65535 | `RbnPort` | RBN telnet port. |
| **Callsign:** | — | — | `RbnCallsign` | Login callsign to RBN. |
| **Rate Limit:** | — | — | `RbnRateLimit` | Caps RBN spots per second. |
| **Connect / Disconnect (RBN)** | Connect | — | — | Toggles RBN connection. |
| **Auto-connect on startup (RBN)** | — | — | `RbnAutoConnect` | Starts RBN automatically. |
| **RBN Console** | — | — | — | Read-only console of RBN traffic. |
| **Send (RBN)** | — | — | — | Sends command to RBN. |
| **Spot Color: (RBN)** | — | — | `RbnSpotColor` | Color picker for RBN spots. |

### WSJT-X Tab

The **WSJT-X** tab provides an UDP listener for WSJT-X decodes with filters and colors.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Address:** | — | — | `WsjtxAddress` | UDP bind address for WSJT-X messages. |
| **Port:** | — | 1–65535 | `WsjtxPort` | UDP port for WSJT-X. |
| **Start / Stop** | — | — | — | Starts or stops UDP listener. |
| **Auto-start on startup (WSJT-X)** | — | — | `WsjtxAutoStart` | Auto-starts listener on launch. |
| **CQ** | — | — | `WsjtxFilterCQ` | Show only CQ calls from WSJT-X. |
| **CQ POTA** | — | — | `WsjtxFilterPOTA` | Show CQ POTA calls. |
| **Calling Me** | — | — | `WsjtxFilterCallingMe` | Show only decodes addressed to your callsign. |
| **CQ color / POTA color / Calling Me color / Default color** | — | — | `WsjtxColorCQ` / `WsjtxColorPOTA` / `WsjtxColorCallingMe` / `WsjtxColorDefault` | Color pickers for each WSJT-X spot category. |
| **WSJT-X Decodes** | — | — | — | Console of decoded transmissions. |
| **Spot Life:** | — | — | `WsjtxSpotLife` | Seconds WSJT-X spots remain on panadapter. |

### SpotCollector Tab

The **SpotCollector** tab provides an UDP listener for Ham Radio Deluxe SpotCollector broadcasts.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **UDP Port:** | — | 1–65535 | `SpotCollectorPort` | UDP port SpotCollector broadcasts on. |
| **Start / Stop (SpotCollector)** | — | — | — | Starts or stops UDP listener. |
| **Auto-start on startup (SpotCollector)** | — | — | `SpotCollectorAutoStart` | Auto-starts listener on launch. |
| **SpotCollector Spots** | — | — | — | Console of received SpotCollector spots. |

### POTA Tab

The **POTA** tab polls api.pota.app for current activations.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Server:** | api.pota.app (HTTP polling) | — | — | Shows fixed POTA endpoint. |
| **Poll Interval:** | — | — | `PotaPollInterval` | Seconds between POTA polls. |
| **Start / Stop (POTA)** | — | — | — | Starts or stops POTA polling. |
| **Auto-start on startup (POTA)** | — | — | `PotaAutoStart` | Auto-starts POTA on launch. |
| **POTA Activations** | — | — | — | Console of activation feed. |
| **Spot Color: (POTA)** | — | — | `PotaSpotColor` | Color picker for POTA spots. |

### FreeDV Tab

The **FreeDV** tab provides a WebSocket feed of FreeDV QSO reporter spots. This tab is only available when AetherSDR is built with WebSocket support.

| Control | Default | Range | Setting Key | Behavior |
|---------|---------|-------|-------------|----------|
| **Server:** | qso.freedv.org (WebSocket) | — | — | Shows fixed FreeDV endpoint. |
| **Start / Stop (FreeDV)** | — | — | — | Connects or disconnects the FreeDV WebSocket. |
|