# Auto-discover an Antenna Genius on the LAN

AetherSDR listens for 4O3A Antenna Genius devices on your local network using UDP discovery. When a device is found, the Antenna Genius applet appears automatically and connects without any manual steps.

## Before you start

- Your Antenna Genius must be powered on and connected to the same LAN as the computer running AetherSDR.
- The applet panel must be visible. If it is not, click `View > Applet Panel` to show it.

## Steps

1. Launch AetherSDR. Discovery starts immediately in the background — no action required.
2. When a device is found, the **AG** tray button appears in the right sidebar. Click **AG** to open the Antenna Genius applet.
3. Check the status label below the device selector. It will read **Device found**, then change to **Connected — \<name\> v\<version\>** once the automatic connection completes.
4. Confirm the correct device is shown in the **Device combo**. If more than one Antenna Genius is on the LAN, use the combo to select the one you want, then click **Connect**.

## What each control does

| Control | What it does | Default | Setting key |
|---|---|---|---|
| **Device combo** | Lists all Antenna Genius units discovered via UDP. Auto-selects and connects to the first device found. | — | — |
| **Connect / Disconnect** | Connects to the selected device in the combo, or disconnects if already connected. Label switches between **Connect** and **Disconnect** to reflect current state. | Connect | — |
| **Manual IP** | Enter an IPv4 or IPv6 address and press Enter to connect directly to port 9007. Used when the device is not on the local LAN. The last-used value is restored on next launch. Invalid addresses produce a red **Invalid IP address** status. | — | `AG_ManualIp` |
| **Port A antenna buttons** | Click to select an antenna on Port A; click again to deselect (antenna=0). Buttons are disabled/dim if the antenna is already selected on Port B. Colour indicates permission: blue = TX+RX, amber = RX only, dim = no permission on current band. | — | — |
| **Port A AUTO** | Toggle to enable band-follow on Port A. When active, the Antenna Genius automatically switches antennas as the radio changes bands. | — | — |
| **Port B antenna buttons** | Click to select an antenna on Port B; click again to deselect. Same colouring rules as Port A. This section is hidden when the connected device reports only one radio port. | — | — |
| **Port B AUTO** | Toggle to enable band-follow on Port B. Hidden when the device reports only one radio port. | — | — |
| Status label | Shows discovery and connection state: **No device found**, **Device found**, **Connected — \<name\> v\<version\>**, **Disconnected**, **Error: \<msg\>**, or **Invalid IP address**. | No device found | — |

## Indicators

| Indicator | States | Meaning |
|---|---|---|
| **Port A band** | Band name or **—** | Active band on Port A, as reported by the Antenna Genius or derived from the radio frequency. |
| **Port A antenna** | Antenna name, **\<ant\> TX:\<alt\>**, **\<ant\> [INHIBIT]**, or **—** | Selected antenna for Port A. Shows red when transmitting, orange when TX is routed to an alternate antenna or inhibit is asserted. |
| **Port B band** | Band name or **—** | Active band on Port B. |
| **Port B antenna** | Antenna name, **\<ant\> TX:\<alt\>**, **\<ant\> [INHIBIT]**, or **—** | Selected antenna for Port B. |

## Tips

- If your network has more than one Antenna Genius, the **Device combo** lists all discovered units. AetherSDR connects automatically only to the first discovered device. Select a different entry and click **Connect** to switch.
- Port B controls are hidden automatically when the connected device reports only one radio port. This visibility is set dynamically based on device information received from either a UDP beacon or the device info response after a manual IP connection.
- Antenna buttons are colour-coded to show TX/RX permissions: blue buttons allow both transmit and receive on the current band, amber buttons allow receive only, and dimmed buttons indicate no permission on the current band.
- The antenna button grid is cleared entirely when disconnected to keep the display consistent. When reconnecting, the buttons are rebuilt from the device's antenna list only after the list is fully loaded — the grid will not appear blank while waiting for the response.

## Troubleshooting

- **Status label stays at "No device found"** — Verify the Antenna Genius is powered on and on the same subnet. Firewalls or managed switches that block UDP broadcast traffic will prevent discovery. If the device is on a different network, use **Manual IP** instead.
- **Status label shows "Invalid IP address"** — The text entered in **Manual IP** could not be parsed as a valid IPv4 or IPv6 address. Correct the address and press Enter again.
- **Status label shows "Error: \<msg\>"** — The connection attempt was made but the device refused or dropped it. Check that no other client is holding an exclusive connection to the Antenna Genius.

## Related

- [Antenna Genius overview](overview.md)
- [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md)
- [Select an antenna for Port A or Port B](select-an-antenna-for-port-a-or-port-b.md)
- [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md)