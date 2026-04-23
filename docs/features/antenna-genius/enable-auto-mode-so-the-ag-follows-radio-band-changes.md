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
| Port A AUTO | Toggles band-follow on Port A. When active, the AG selects the antenna for Port A based on the radio's current band. | Off |
| Port B AUTO | Toggles band-follow on Port B. When active, the AG selects the antenna for Port B based on the radio's current band. Hidden on single-port devices. | Off |

## Tips

- You can run AUTO on one port and select antennas manually on the other. The two ports are independent.
- When AUTO is active, the Port A band and Port B band indicators update as you tune across bands, confirming the AG is tracking correctly.

## Troubleshooting

- **AUTO button does not respond to clicks** — The applet is not connected. Check that the status label reads "Connected — \<name\> v\<version\>" before enabling AUTO. If not connected, see the pages below.
- **Band indicator shows "—" after enabling AUTO** — The AG has not yet received a band report from the radio. Tune to a frequency within a recognized band to trigger an update.

## Related

- [Antenna Genius overview](overview.md)
- [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md)
- [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md)
- [Select an antenna for Port A or Port B](select-an-antenna-for-port-a-or-port-b.md)
