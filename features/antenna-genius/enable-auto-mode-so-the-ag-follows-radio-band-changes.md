# Enable AUTO mode so the AG follows radio band changes

AUTO mode tells the Antenna Genius to select antennas automatically as the radio changes bands, instead of requiring you to pick an antenna manually. Enable it separately for Port A and Port B.

## Before you start

- The Antenna Genius applet must be visible. It appears only after a device is discovered or you connect manually. Open it by clicking the AG tray button on the right sidebar.
- The applet must show a status of **Connected — \<name\> v\<version\>**. AUTO mode cannot be enabled while disconnected.

## Steps

1. Click the AG tray button on the right sidebar to open the Antenna Genius applet.
2. Confirm the status label reads **Connected —** followed by the device name and version.
3. To enable band-following on Port A, click **AUTO** under the Port A antenna buttons. The button highlights green when active.
4. To enable band-following on Port B, click **AUTO** under the Port B antenna buttons. The button highlights green when active.
5. To turn AUTO mode off for a port, click the highlighted **AUTO** button again. The button returns to its inactive appearance and you can select antennas manually.

## What each control does

| Control | Location | Behavior | Default |
|---|---|---|---|
| Port A AUTO | Below the Port A antenna buttons | Toggles band-follow mode for Port A. When active, the AG selects the antenna for Port A as the radio changes bands. | Off |
| Port B AUTO | Below the Port B antenna buttons | Toggles band-follow mode for Port B. When active, the AG selects the antenna for Port B as the radio changes bands. | Off |

> **Note:** The Port B section is hidden if the connected AG device reports only one radio port.

## Tips

- AUTO mode is applied per port. You can run Port A in AUTO while leaving Port B in manual, or vice versa.
- When AUTO is active, the antenna buttons for that port still update to reflect the currently selected antenna and its TX/RX permission colouring. Watch the Port A and Port B antenna indicators to confirm the AG is tracking band changes correctly.

## Troubleshooting

- **AUTO button has no effect or does not stay highlighted** — The applet is not connected. Check that the status label reads **Connected —** and not **Disconnected**, **No device found**, or **Error: \<msg\>**. Connect first, then enable AUTO.
- **Port B AUTO is not visible** — The connected device has only one radio port. Port B controls are hidden automatically in this case.

## Related

- [Antenna Genius overview](overview.md)
- [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md)
- [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md)
- [Select an antenna for Port A or Port B](select-an-antenna-for-port-a-or-port-b.md)
- [Spot which antennas cannot TX on the current band (amber or dim)](spot-which-antennas-cannot-tx-on-the-current-band-amber-or-dim.md)
