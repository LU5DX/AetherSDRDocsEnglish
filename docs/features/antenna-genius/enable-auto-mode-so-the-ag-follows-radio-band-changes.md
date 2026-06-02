# Enable AUTO mode so the AG follows radio band changes

AUTO mode tells the Antenna Genius to track your radio's active band and switch antennas automatically. This removes the need to manually select an antenna each time you change bands.

## Before you start

- The Antenna Genius applet must be visible. It is hidden until a device is discovered or manually connected. Use the AG tray button on the right sidebar to open it.
- The applet must show a "Connected — \<name\> v\<version\>" status. AUTO mode has no effect when disconnected.

## Steps

1. Click the AG tray button on the right sidebar to open the Antenna Genius applet.
2. Confirm the status label reads "Connected — \<name\> v\<version\>".
3. To enable band-follow on Port A, click **AUTO** under the Port A antenna buttons. The button highlights green when active.
4. To enable band-follow on Port B, click **AUTO** under the Port B antenna buttons. The button highlights green when active.
   - The Port B section is hidden if the connected device reports only one radio port.
5. To disable AUTO mode on either port, click the lit **AUTO** button again. It returns to its unlit state and the port reverts to manual antenna selection.

## What each control does

| Control | Behavior | Default |
|---|---|---|
| Device combo | Selects which discovered AG device to connect to. Auto-selects and connects when the first device is discovered. | empty |
| Connect / Disconnect | Connects to the selected device (or the Manual IP if none selected); becomes "Disconnect" when connected. | Connect |
| Manual IP | Enter an IP and press Enter to connect to port 9007. Invalid addresses produce a red "Invalid IP address" status. | empty |
| Port A antenna buttons | Click to select an antenna on Port A; click again to deselect (antenna=0). Disabled/dim if the antenna is already selected on Port B. Blue = TX+RX, amber = RX only, dim = no permission on current band. | none |
| Port A AUTO | Toggles band-follow on Port A. When active, the AG selects the antenna for Port A based on the radio's current band. | Off |
| Port B antenna buttons | Click to select an antenna on Port B; click again to deselect. Port B section hidden if the AG device reports only one radio port. | none |
| Port B AUTO | Toggles band-follow on Port B. When active, the AG selects the antenna for Port B based on the radio's current band. Hidden on single-port devices. | Off |

## What each indicator shows

| Indicator | States | Meaning |
|---|---|---|
| Status label | "No device found", "Device found", "Connected — \<name\> v\<version\>", "Disconnected", "Error: \<msg\>", "Invalid IP address" | Discovery/connection state of the Antenna Genius. |
| Port A band | Band name or "—" | Active band on Port A (AG-reported or frequency-derived). |
| Port A antenna | Antenna name, "\<ant\> TX:\<alt\>", "\<ant\> [INHIBIT]", "—" | Selected antenna; red when TXing, orange when TX routed to alt antenna or inhibit is asserted. |
| Port B band | Band name or "—" | Active band on Port B. |
| Port B antenna | Antenna name, "\<ant\> TX:\<alt\>", "\<ant\> [INHIBIT]", "—" | Selected antenna for Port B. |

## Tips

- You can run AUTO on one port and select antennas manually on the other. The two ports are independent.
- When AUTO is active, the Port A band and Port B band indicators update as you tune across bands, confirming the AG is tracking correctly.

## Troubleshooting

- **AUTO button does not respond to clicks** — The applet is not connected. Check that the status label reads "Connected — \<name\> v\<version\>" before enabling AUTO. If not connected, see the pages below.
- **Band indicator shows "—" after enabling AUTO** — The AG has not yet received a band report from the radio. Tune to a frequency within a recognized band to trigger an update.
- **A ShackSwitch device appears in the Device combo but the applet does not auto-connect to it** — ShackSwitch devices are handled by a separate applet and are intentionally skipped during Antenna Genius auto-connect. Use the ShackSwitch applet to connect to that device.

## Related

- [Antenna Genius overview](overview.md)
- [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md)
- [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md)
- [Select an antenna for Port A or Port B](select-an-antenna-for-port-a-or-port-b.md)