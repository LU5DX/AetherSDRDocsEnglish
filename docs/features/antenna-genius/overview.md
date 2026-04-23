# Antenna Genius Overview

The Antenna Genius applet lets you control a 4O3A Antenna Genius antenna switch from within AetherSDR. Use it to select antennas per radio port, follow band changes automatically, and see at a glance which antennas are permitted for TX on the current band.

## Before you start

- The Antenna Genius device must be powered on and reachable — either on the local LAN (for auto-discovery) or at a known IP address (for manual connection).
- The applet is hidden until a device is detected or a manual connection is made. Once visible, open it with the "AG" tray button on the right sidebar.

## How it works

AetherSDR listens for Antenna Genius devices on the LAN using UDP discovery. When a device is found, the applet appears and connects automatically. If your device is on a remote network, enter its IP address in the Manual IP field and press Enter; the address is saved as `AG_ManualIp` and used to connect on port 9007.

Once connected, the applet shows two port sections — Port A and Port B — each with a row of antenna buttons populated from the device's antenna list. Clicking an antenna button selects that antenna on the port; clicking it again deselects it (sets antenna to 0). If a device reports only one radio port, the Port B section is hidden.

Antenna buttons are colour-coded to show TX/RX permission on the current band:

- **Blue** — TX and RX permitted.
- **Amber** — RX only on this band.
- **Dim** — No permission on the current band.

An antenna already selected on the other port is disabled and cannot be selected on this port.

The status label at the top of the applet tracks the connection lifecycle, and the per-port indicators show the active band and selected antenna name in real time.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Device combo | Selects which discovered AG device to connect to. Populated by UDP discovery. Auto-selects the first device found. | — | — |
| Connect / Disconnect | Connects to the selected device, or to the Manual IP if no discovered device is selected. Becomes "Disconnect" when connected. | Connect | — |
| Manual IP | Enter an IPv4 or IPv6 address and press Enter to connect to port 9007. The address is saved for future sessions. An invalid entry shows a red "Invalid IP address" status. | — | `AG_ManualIp` |
| Port A antenna buttons | Click to select an antenna on Port A. Click again to deselect. Disabled if the antenna is in use on Port B. Colour reflects TX/RX permission (blue = TX+RX, amber = RX only, dim = no permission). | — | — |
| Port A AUTO | Toggle to enable band-follow on Port A. When active, the AG switches antennas automatically as the radio changes band. | — | — |
| Port B antenna buttons | Same behavior as Port A antenna buttons, for Port B. Hidden if the connected device has only one radio port. | — | — |
| Port B AUTO | Toggle to enable band-follow on Port B. | — | — |

### Status indicators

| Indicator | States | Meaning |
|---|---|---|
| Status label | No device found / Device found / Connected — \<name\> v\<version\> / Disconnected / Error: \<msg\> / Invalid IP address | Discovery and connection state of the Antenna Genius. |
| Port A band | Band name or — | Active band on Port A, derived from AG report or radio frequency. |
| Port A antenna | Antenna name / \<ant\>  TX:\<alt\> / \<ant\> [INHIBIT] / — | Selected antenna on Port A. Red when transmitting; orange when TX is routed to an alternate antenna or inhibit is active. |
| Port B band | Band name or — | Active band on Port B. |
| Port B antenna | Antenna name / \<ant\>  TX:\<alt\> / \<ant\> [INHIBIT] / — | Selected antenna on Port B. Same colour rules as Port A. |

## Related

- [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md)
- [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md)
- [Select an antenna for Port A or Port B](select-an-antenna-for-port-a-or-port-b.md)
- [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
- [Spot which antennas cannot TX on the current band (amber or dim)](spot-which-antennas-cannot-tx-on-the-current-band-amber-or-dim.md)
- [Swap radios that share the AG (antennas in use by the other port are locked out)](swap-radios-that-share-the-ag-antennas-in-use-by-the-other-port-are-locked-out.md)
