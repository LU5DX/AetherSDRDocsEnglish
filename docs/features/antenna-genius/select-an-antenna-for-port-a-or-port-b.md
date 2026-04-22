# Select an antenna for Port A or Port B

Use the Antenna Genius applet to choose which antenna the 4O3A Antenna Genius switch routes to Port A or Port B on your radio. Selecting an antenna here sends the command immediately to the switch.

## Before you start

- The Antenna Genius applet must be visible in the applet panel. It appears automatically when a device is discovered or connected. If it is not visible, click the AG tray button on the right sidebar.
- The Antenna Genius must be connected. The status label must read "Connected — &lt;name&gt; v&lt;version&gt;". If it reads "No device found" or "Disconnected", see [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md) or [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md).
- The antenna list must be populated. The antenna buttons appear automatically after a successful connection.

## Steps

1. Click the AG tray button on the right sidebar to open the Antenna Genius applet.
2. Locate the Port A or Port B section. Port B is hidden if the connected device reports only one radio port.
3. Click the antenna button you want to select. The button highlights to show it is active.
4. To deselect the current antenna on a port, click its active button again. The port returns to no antenna selected (antenna 0).

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Port A antenna buttons | Click to select an antenna on Port A. Click the active button again to deselect. | Blue = TX and RX permitted on the current band. Amber = RX only on the current band. Dim = no permission on the current band. Disabled if the antenna is already selected on Port B. |
| Port A AUTO | Toggle to enable band-follow on Port A. The switch selects antennas automatically as the radio changes bands. | See [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md). |
| Port B antenna buttons | Click to select an antenna on Port B. Click the active button again to deselect. | Same color coding as Port A. Disabled if the antenna is already selected on Port A. Hidden if the device has only one radio port. |
| Port B AUTO | Toggle to enable band-follow on Port B. | See [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md). |
| Port A antenna indicator | Shows the name of the currently selected antenna for Port A. Displays `<ant>  TX:<alt>` when TX is routed to an alternate antenna, or `<ant> [INHIBIT]` when transmit is inhibited. | Turns red while transmitting, orange when TX is rerouted or inhibit is active. |
| Port B antenna indicator | Same as Port A antenna indicator, for Port B. | Same color behavior. |

## Tips

- An antenna button that is dim on the current band is still clickable, but that antenna has no TX or RX permission configured for this band on the Antenna Genius. Check your AG band/antenna permission settings if this is unexpected.
- If an antenna you want to assign to Port A is greyed out and unclickable, it is already selected on Port B. Deselect it from Port B first.

## Troubleshooting

- **Antenna buttons do not appear** — The applet is connected but has not received an antenna list from the device. Try clicking Disconnect and then Connect to re-establish the session.
- **Clicking a button has no effect** — The device may have dropped the connection. Check the status label. If it does not show "Connected — &lt;name&gt; v&lt;version&gt;", reconnect using the Connect button.
- **Port B section is not visible** — The connected Antenna Genius device reports only one radio port. Port B controls are hidden automatically in this case.

## Related

- [Antenna Genius overview](overview.md)
- [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md)
- [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md)
- [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
- [Spot which antennas cannot TX on the current band (amber or dim)](spot-which-antennas-cannot-tx-on-the-current-band-amber-or-dim.md)
- [Swap radios that share the AG (antennas in use by the other port are locked out)](swap-radios-that-share-the-ag-antennas-in-use-by-the-other-port-are-locked-out.md)
