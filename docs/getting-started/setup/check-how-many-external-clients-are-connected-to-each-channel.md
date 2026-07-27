# Check how many external clients are connected to each channel

The CAT Control applet shows a live client count for each of the four rigctld TCP channels (A–D). Use this to confirm that your logging or contest software has successfully connected to the right channel.

## Before you start

- The radio must be connected. The CAT Control applet requires an active radio connection.
- Enable TCP must be active. If the servers are not running, all channels show `(stopped)` and no clients can connect. See [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md).

## Steps

1. Click the **CAT** tray button on the right sidebar to open the CAT Control applet.
2. Read the TCP status label on each channel row (A, B, C, D).

Each row displays one of the following states:

| Display | Meaning |
|---|---|
| `(stopped)` | The TCP server for that channel is not running. |
| `:<port> (0 clients)` | Server is running; no external client is connected. |
| `:<port> (1 client)` | One external client is connected on that port. |
| `:<port> (N clients)` | N external clients are connected on that port. |

The port shown is the base port for channel A, base+1 for B, base+2 for C, and base+3 for D. The default base port is `4532` (persisted as `CatTcpPort`).

## What each control does

| Control              | Default     | Valid range |
|----------------------|-------------|-------------|
| **Enable TCP**       | Off         | On / Off    |
| **Enable TTY**       | Off         | On / Off    |
| **Base**             | `4532`      | 1024–65535  |
| A/B/C/D channel rows | `(stopped)` | —           |

### Enable TCP

Starts or stops all four rigctld TCP servers on the base port through base+3. Also persists the current base port value to the `CatTcpPort` setting.

In v26.7.4, the **Enable TCP** button now displays "Enabled" or "Disabled" instead of "Enable CAT" to make the current state immediately readable. The same label is mirrored in both the docked and floating applet views. The button text updates dynamically when toggled or when the state is changed programmatically.

### Enable TTY

Starts or stops all four PTY symlinks. On Linux, symlinks are created under `$XDG_RUNTIME_DIR/aethersdr/cat-A` through `cat-D`. On macOS, symlinks are created under `~/Library/Caches/AetherSDR/cat-A` through `cat-D`.

In v26.5.3, the symlink location moved from `/tmp` to per-user runtime directories to fix a cross-user symlink vulnerability (GHSA-qxhr-cwrc-pvrm). Atomic symlink replacement via `symlink(.tmp) + rename(.tmp, final)` closes the TOCTOU window.

### Base

Base TCP port. Channels bind to port, port+1, port+2, and port+3. Default is `4532`. Valid range is 1024–65535. Out-of-range values snap back to `4532`. Servers restart with the new port if currently enabled.

### A/B/C/D channel rows

Each row shows:
- A slice-colour coded channel badge
- TCP status: `(stopped)`, `:<port> (1 client)`, or `:<port> (N clients)`
- PTY path showing the symlink location where logging software can open a serial device

In v26.7.4, each channel row includes a per-port enable checkbox. The checkbox uses a high-contrast style with a visible border and a filled accent colour when checked, making its on/off state readable against the dark applet background. The VFO selection for each channel persists across reconnections so that a previously chosen slice is not lost when reconnecting to a smaller radio.

## Tips

- The TCP status label changes colour when a client is connected: it adopts the slice colour for that channel, making it easier to spot at a glance which channels are in use.
- If you change the value in **Base** while the servers are running, all four servers restart automatically on the new ports. Any connected clients will be dropped and must reconnect.

## Troubleshooting

- **All rows show `(stopped)` even though Enable TCP is on** — The radio connection may have been lost. Check that AetherSDR is connected to the FLEX-8600, then toggle **Enable TCP** off and on again.
- **Client count stays at 0 after starting your logging software** — Confirm the software is pointing at the correct port. Channel A uses the base port (`4532` by default), B uses base+1, and so on. Check the value in the **Base** field and compare it to what your software is configured to connect to.
- **Server fails to start on the selected port** — Another application may already be listening on that port. Change the **Base** value to a free port range and click **Enable TCP** again.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Change the base TCP port](../../features/cat-control/change-the-base-tcp-port.md)
- [Autostart CAT servers with AetherSDR](../../features/cat-control/autostart-cat-servers-with-aethersdr.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](../../features/cat-control/enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [See how many TCI clients are connected](see-how-many-tci-clients-are-connected.md)