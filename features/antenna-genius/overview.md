# Antenna Genius Overview

The Antenna Genius applet lets you connect to a 4O3A Antenna Genius antenna switch from within AetherSDR, select antennas for each radio port, and optionally let the switch follow band changes automatically. Use it when your station has a 4O3A Antenna Genius on the LAN or reachable over a remote network.

## Before you start

- Your 4O3A Antenna Genius must be powered on and reachable from the machine running AetherSDR (same LAN for auto-discovery, or any routable IP for manual connection).
- No radio connection is required to use the Antenna Genius applet.

## How it works

The applet is hidden until an Antenna Genius is detected or manually connected. Once present, open it with the **AG** tray button on the right sidebar.

On launch, AetherSDR sends a UDP broadcast to discover Antenna Genius devices on the local network. When the first device is found, it is added to the **Device combo** and AetherSDR connects to it automatically. The **Status label** updates throughout to reflect what is happening.

If no device is found automatically — for example, the switch is on a remote network — enter its IP address in **Manual IP** and press Enter. AetherSDR connects to that address on port 9007 and saves the address as `AG_ManualIp` for future sessions.

Once connected, the applet shows antenna buttons for **Port A** and, if the device reports two radio ports, **Port B**. Each button represents one antenna. Clicking a button selects that antenna on the port; clicking it again deselects it (sets antenna to 0). The button colour indicates TX/RX permission on the current band:

- **Blue** — antenna has TX and RX permission on the current band.
- **Amber** — antenna has RX permission only on the current band.
- **Dim** — no permission on the current band.

Antennas already selected on the opposite port are disabled so you cannot assign the same antenna to both ports simultaneously.

The **AUTO** button on each port enables band-follow mode: when the radio changes band, the Antenna Genius automatically switches to a suitable antenna for that port without manual intervention.

The **Port B** section is hidden automatically if the connected device reports only one radio port.

## What each control does

| Control | What it does | Persisted setting |
|---|---|---|
| **Device combo** | Selects which discovered AG device to connect to. Populated by UDP discovery. Auto-selects the first device found. | — |
| **Connect** / **Disconnect** | Connects to the selected device or the **Manual IP** address. Changes to **Disconnect** when connected. | — |
| **Manual IP** | Enter an IPv4 or IPv6 address and press Enter to connect to port 9007. Invalid addresses show a red "Invalid IP address" status. | `AG_ManualIp` |
| **Port A antenna buttons** | Click to select an antenna on Port A; click again to deselect. Disabled if the antenna is already in use on Port B. | — |
| **Port A AUTO** | Enables band-follow on Port A. The switch tracks radio band changes automatically. | — |
| **Port B antenna buttons** | Click to select an antenna on Port B; click again to deselect. Hidden if the device has only one radio port. | — |
| **Port B AUTO** | Enables band-follow on Port B. | — |

### Status indicators

| Indicator | What it shows |
|---|---|
| **Status label** | Discovery and connection state: `No device found`, `Device found`, `Connected — <name> v<version>`, `Disconnected`, `Error: <msg>`, or `Invalid IP address`. |
| **Port A band** | Active band on Port A, or `—` if not available. |
| **Port A antenna** | Selected antenna on Port A. Displays `<ant>  TX:<alt>` when TX is routed to an alternate antenna, or `<ant> [INHIBIT]` when TX inhibit is asserted. Red while transmitting, orange when TX is rerouted or inhibited. |
| **Port B band** | Active band on Port B, or `—`. |
| **Port B antenna** | Selected antenna on Port B, with the same TX/inhibit display rules as Port A. |

## Related

- [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md)
- [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md)
- [Select an antenna for Port A or Port B](select-an-antenna-for-port-a-or-port-b.md)
- [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
- [Spot which antennas cannot TX on the current band (amber or dim)](spot-which-antennas-cannot-tx-on-the-current-band-amber-or-dim.md)
- [Swap radios that share the AG (antennas in use by the other port are locked out)](swap-radios-that-share-the-ag-antennas-in-use-by-the-other-port-are-locked-out.md)
