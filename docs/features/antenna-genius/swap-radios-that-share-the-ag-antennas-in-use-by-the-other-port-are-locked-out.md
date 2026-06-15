# Antenna Genius Applet

The Antenna Genius (AG) applet controls a 4O3A Antenna Genius switch. It discovers devices on the LAN, allows manual connection by IP, and lets you select antennas per radio port with band-aware TX/RX permission colouring and AUTO mode.

## Open the Applet

Click the AG tray button on the right sidebar. The applet opens as a narrow panel.

## Connect to an Antenna Genius

The applet supports two connection methods:

- **Auto-discover on the LAN**: The applet listens for UDP discovery broadcasts. When a device is found, it appears in the Device combo and is automatically selected and connected. The status label shows "Device found" during discovery and then "Connected — <name> v<version>" once connected.

- **Manual IP connection**: If the device is not on the local network, enter its IPv4 or IPv6 address in the Manual IP field and press Enter. The applet connects to port 9007. Invalid addresses produce a red "Invalid IP address" status. The last-used manual IP is stored in `AG_ManualIp` and restored on next launch.

To connect to a manually entered IP, press Enter after typing the address. To disconnect, click the Disconnect button (which replaces the Connect button when connected).

**Note**: ShackSwitch devices discovered on the LAN are excluded from automatic connection in the Antenna Genius applet. They are handled by the ShackSwitch applet instead. Select the correct Antenna Genius device from the Device combo and click Connect, or enter its IP in Manual IP and press Enter.

## Select an Antenna

Each radio port (Port A and Port B) has a row of antenna buttons. The antenna list is populated from the AG device.

- **To select an antenna**: Click its button on the port you want to assign it to. The button lights up.
- **To deselect an antenna**: Click a lit button again. The port shows no antenna ("—").
- **If a button is dimmed**: The antenna is already selected on the other port. Deselect it there first.
- **Button colours**: Blue = TX and RX permitted on the current band. Amber = RX only on the current band. Dim = no permission on the current band.

## Use AUTO Mode

Each port has an AUTO toggle button. When enabled, the AG follows the radio's band changes automatically, selecting the appropriate antenna for each band.

- **To enable AUTO**: Click the Port A AUTO or Port B AUTO toggle button. The button stays in the on position.
- **To disable AUTO**: Click the toggle button again.

Disable AUTO on a port before manually reassigning antennas if you need explicit control. If both radios are in AUTO mode, manual lockout resolution may be overridden immediately by the next band change.

## Read the Indicators

| Indicator | Displays | Notes |
|---|---|---|
| Status label | "No device found", "Device found", "Connected — <name> v<version>", "Disconnected", "Error: <msg>", or "Invalid IP address" | Red text indicates an error or invalid IP. |
| Port A band | Active band name or "—" | Band reported by the AG or derived from frequency. |
| Port A antenna | Selected antenna name | Red during TX, orange when TX is routed to an alternate antenna or inhibit is asserted. Shows "—" when no antenna is selected. |
| Port B band | Active band name or "—" | Same as Port A, for Port B. |
| Port B antenna | Selected antenna name | Same as Port A, for Port B. |

## Swap Radios That Share the AG (Antennas in Use by the Other Port Are Locked Out)

When two radios share one Antenna Genius, each radio connects to a separate port (Port A or Port B). Any antenna already selected on one port is locked out — its button is dimmed — on the other port. This section explains how to reassign antennas between ports so neither radio is blocked.

### Before you start

- The Antenna Genius applet must be visible. If the AG tray button is absent, connect to your device first — see [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md) or [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md).
- The status label must read "Connected — <name> v<version>". Do not attempt antenna changes while disconnected.
- Your AG device must report two radio ports. If it reports only one, the Port B section is hidden and this procedure does not apply.

### Steps

1. Click the AG tray button on the right sidebar to open the Antenna Genius applet.
2. Look at the Port A antenna buttons and the Port B antenna buttons. Buttons that are dimmed on one port are already selected on the other port and cannot be chosen until released.
3. To free a locked-out antenna, click its currently lit button on the port that holds it. Clicking a selected antenna button a second time deselects it (sets that port to no antenna). The button returns to its unlit state.
4. Once the antenna is deselected on the port that held it, its button becomes active on the other port.
5. Click the now-available antenna button on the port you want to assign it to. The button lights up and the antenna name appears in the port's antenna indicator at the top of that port's section.
6. Confirm the assignment: the antenna indicator next to "Port A" or "Port B" shows the antenna name. If the antenna supports TX on the current band the button is blue; if RX-only on the current band it is amber.

### Tips

- **Deselect before reassigning**: you must release the antenna from its current port before the button becomes available on the other port. There is no drag-and-drop swap — the release step is required.
- If both radios are in AUTO mode, the AG will follow each radio's band independently. In that case, manual lockout resolution may be overridden immediately by the next band change. Disable AUTO on the relevant port before making manual changes.

### Troubleshooting

- **An antenna button remains dimmed even after I clicked the other port's button to deselect it** — confirm the deselect took effect by checking that the antenna indicator for the other port now shows "—". If the indicator still shows the antenna name, the click may not have registered; click the lit button on the other port once more.
- **Port B section is not visible** — the connected AG device reports only one radio port. Port B sharing is not available on single-port devices.
- **Status label shows "Disconnected" or "Error: <msg>"** — antenna buttons cannot be changed while disconnected. Reconnect using Connect or by re-entering the IP in Manual IP and pressing Enter. Invalid addresses produce a red "Invalid IP address" status. The last-used manual IP is stored in `AG_ManualIp` and restored on next launch.
- **A ShackSwitch device appears in the Device combo but does not auto-connect** — ShackSwitch devices discovered on the LAN are excluded from automatic connection in the Antenna Genius applet. They are handled by the ShackSwitch applet instead. Select the correct Antenna Genius device from the Device combo and click Connect, or enter its IP in Manual IP and press Enter.

## Disconnecting Clears Antenna Buttons

When you disconnect from an Antenna Genius device, the antenna button grid is cleared immediately. All antenna buttons disappear from both Port A and Port B sections. This is expected behaviour — the antenna list is only available while connected to the device.

When you reconnect, the antenna buttons are rebuilt from the device's antenna list as soon as the response arrives. If the list is not yet available, the existing buttons remain in place until the fresh data arrives.

## Theme Support

As of v26.6.1, the Antenna Genius applet fully supports theming through the ThemeManager system. All widget colours (backgrounds, borders, text, accent colours, and status indicators) are now derived from the active theme rather than hard-coded. This means the applet's appearance automatically adapts when you switch themes in AetherSDR.

## Related

- [Select an antenna for Port A or Port B](select-an-antenna-for-port-a-or-port-b.md)
- [Spot which antennas cannot TX on the current band (amber or dim)](spot-which-antennas-cannot-tx-on-the-current-band-amber-or-dim.md)
- [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
- [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md)