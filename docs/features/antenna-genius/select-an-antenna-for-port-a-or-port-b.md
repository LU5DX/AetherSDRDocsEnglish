# Select an antenna for Port A or Port B

Use the Antenna Genius applet to assign a specific antenna to Port A or Port B on your 4O3A Antenna Genius switch. This lets you control which physical antenna each radio port uses without leaving AetherSDR.

## Before you start

- The Antenna Genius applet must be visible. It is hidden until a device is connected or discovered. See [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md) or [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md).
- The status label must read **Connected — \<name\> v\<version\>** before antenna buttons appear.
- Open the applet by clicking the **AG** tray button on the right sidebar.

## Steps

1. Click the **AG** tray button to open the Antenna Genius applet.
2. Confirm the status label reads **Connected —** followed by the device name and version.
3. Under the **Port A** heading, locate the antenna buttons populated from the device's antenna list.
4. Click the button for the antenna you want to assign to Port A. The button highlights to show it is selected.
5. To deselect the current antenna on Port A, click the same button again. The port returns to no antenna selected (antenna 0).
6. If your device has two radio ports, the **Port B** section is visible below the separator. Repeat steps 3–5 under the **Port B** heading to assign an antenna to Port B.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Port A antenna buttons | Click to select an antenna on Port A; click again to deselect. | Blue = TX and RX permitted on the current band. Amber = RX only. Dim = no permission on the current band. Disabled if the antenna is already selected on Port B. |
| Port A band | Displays the active band on Port A, derived from the radio frequency. | Shows **—** when no band is identified. |
| Port A antenna | Displays the currently selected antenna name for Port A. | Shows **\<ant\>  TX:\<alt\>** when TX is routed to an alternate antenna, and **\<ant\> [INHIBIT]** when transmit is inhibited. Turns red during TX, orange on alternate TX or inhibit. |
| Port A AUTO | Toggle. Enables band-follow on Port A so the switch tracks radio band changes automatically. | See [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md). |
| Port B antenna buttons | Click to select an antenna on Port B; click again to deselect. | Same antenna list as Port A. Hidden if the device reports only one radio port. |
| Port B band | Displays the active band on Port B. | Shows **—** when no band is identified. |
| Port B antenna | Displays the currently selected antenna name for Port B. | Same state display as Port A antenna. |
| Port B AUTO | Toggle. Enables band-follow on Port B. | Hidden when Port B section is hidden. |

## Tips

- An antenna already selected on one port is disabled and dimmed on the other port's button grid. You cannot assign the same antenna to both ports simultaneously.
- Amber-highlighted antenna buttons are available for receive but will not carry TX on the current band. Switch to a blue button before transmitting.

## Troubleshooting

- **Port B section is not visible** — The connected device reports only one radio port. Port B is hidden automatically in this case and is not available.
- **Antenna buttons are not shown** — The device is not yet connected, or the antenna list has not loaded. Confirm the status label reads **Connected —** and wait a moment for the list to populate.
- **Clicking an antenna button has no effect** — The button may be disabled because that antenna is already selected on the other port. Choose a different antenna or deselect it on the other port first.

## Related

- [Antenna Genius overview](overview.md)
- [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md)
- [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md)
- [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
- [Spot which antennas cannot TX on the current band (amber or dim)](spot-which-antennas-cannot-tx-on-the-current-band-amber-or-dim.md)
- [Swap radios that share the AG (antennas in use by the other port are locked out)](swap-radios-that-share-the-ag-antennas-in-use-by-the-other-port-are-locked-out.md)
