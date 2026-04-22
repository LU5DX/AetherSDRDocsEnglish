# Auto-discover an Antenna Genius on the LAN

AetherSDR listens for 4O3A Antenna Genius devices on the local network using UDP discovery. When a device is found, the Antenna Genius applet appears automatically and connects without any manual configuration.

## Before you start

- Your Antenna Genius must be powered on and connected to the same LAN segment as the computer running AetherSDR.
- The applet panel must be visible. If it is not, click `View > Applet Panel` to show it.

## Steps

1. Launch AetherSDR. Discovery starts immediately in the background — no manual action is required.
2. When a device is found, the **AG** tray button appears on the right sidebar. Click **AG** to open the Antenna Genius applet.
3. Check the status label below the device selector. It reads **Device found** when discovery succeeds, then transitions to **Connected — \<name\> v\<version\>** once the automatic connection completes.
4. Confirm the **Device combo** shows your device by name and IP address.
5. If the status label reads **Connected — \<name\> v\<version\>** and the **Connect / Disconnect** button now shows **Disconnect**, the applet is connected and ready.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Device combo | Lists all devices found by UDP discovery. Auto-selects and connects to the first device discovered. | Empty until discovery finds a device | — |
| Connect / Disconnect | Connects to the selected device in the combo; becomes **Disconnect** when connected. | **Connect** | — |
| Manual IP | Enter an IPv4 or IPv6 address and press Enter to connect directly to port 9007. Used when the device is not on the local LAN. | Empty (restores last-used value on relaunch) | `AG_ManualIp` |
| Status label | Shows current discovery and connection state. | **No device found** | — |

## Tips

- AetherSDR auto-connects to the first discovered device. If you have more than one Antenna Genius on the LAN, use the **Device combo** to select the correct one before clicking **Connect**.
- If Port B controls are not visible after connecting, the device has reported only one radio port. This is normal.
- The value in **Manual IP** is saved as `AG_ManualIp` and restored the next time AetherSDR starts, so you do not need to re-enter it after a restart.

## Troubleshooting

- **Status label stays "No device found"** — The Antenna Genius may be on a different network segment or subnet that blocks UDP broadcast traffic. Use the **Manual IP** field to connect directly by IP address instead. See [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md).
- **Status label shows "Invalid IP address"** — The text entered in **Manual IP** is not a valid IPv4 or IPv6 address. Correct the address and press Enter again.
- **Status label shows "Error: \<msg\>"** — The device was reachable but the connection failed. Check that the Antenna Genius firmware is running and that no firewall is blocking port 9007.
- **AG tray button does not appear** — Discovery has not yet found a device. Wait a few seconds; if the button still does not appear, verify the device is powered on and on the same LAN, or use **Manual IP** to connect directly.

## Related

- [Antenna Genius overview](overview.md)
- [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md)
- [Select an antenna for Port A or Port B](select-an-antenna-for-port-a-or-port-b.md)
- [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
