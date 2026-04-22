# Connect TGXL, PGXL or Antenna Genius by IP

This page explains how to manually connect a TGXL, PGXL, or Antenna Genius peripheral to AetherSDR using an IP address. Use this when the device is not discovered automatically on your network.

## Before you start

- AetherSDR must already be connected to your FLEX-8600 radio.
- You must know the IP address of the TGXL, PGXL, or Antenna Genius device.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Peripherals** tab.
3. Locate the row for the device you want to connect (TGXL, PGXL, or Antenna Genius).
4. Enter the device's IP address in the address field for that device.
5. Click **Connect** next to that device.

To disconnect a device, click **Disconnect** next to it.

## What each control does

| Control | Description |
|---|---|
| **Connect** (per device) | Opens a connection to the device at the entered IP address. |
| **Disconnect** (per device) | Closes the current connection to that device. |

## Troubleshooting

- **Connect does nothing or the device shows as unavailable** — Confirm the IP address is correct and that the device is powered on and reachable from your host machine. If the radio and device are on different subnets, ensure routing between them is configured. See [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md).
- **Antenna Genius does not appear in the Peripherals tab** — The Peripherals tab is only built after the tab is first selected. Click the tab once to trigger the UI build, then try again.

## Related

- [Change network MTU for VPN/remote setups](../../features/radio-setup/change-network-mtu-for-vpn-remote-setups.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Manually connect to an AG over a remote network](manually-connect-to-an-ag-over-a-remote-network.md)
