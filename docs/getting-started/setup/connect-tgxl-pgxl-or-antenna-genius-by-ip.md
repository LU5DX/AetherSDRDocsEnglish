# Connect TGXL, PGXL or Antenna Genius by IP

This page explains how to manually connect a TGXL, PGXL, or Antenna Genius device to AetherSDR by entering its IP address. Use this when the device is not discovered automatically on your network.

## Before you start

- AetherSDR must already be connected to a FLEX-8600 radio. The Peripherals tab is not available without an active radio connection.
- Have the IP address of the TGXL, PGXL, or Antenna Genius device ready.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Peripherals** tab.
3. Locate the row for the device you want to connect (TGXL, PGXL, or Antenna Genius).
4. Enter the device's IP address in the address field for that device.
5. Click **Connect** for that device.

To disconnect a device, click **Disconnect** on its row.

## Troubleshooting

- **Connect has no effect or the device shows as unreachable** — Confirm the IP address is correct and that the device is powered on and reachable from the same network as the radio. If the radio and device are on separate subnets, ensure routing is in place.
- **Peripherals tab is missing or greyed out** — AetherSDR requires an active radio connection to display this tab. Connect to the radio first before opening Radio Setup.

## Related

- [Radio Setup overview](../../features/radio-setup/overview.md)
- [Manually connect to an AG over a remote network](manually-connect-to-an-ag-over-a-remote-network.md)
- [Change network MTU for VPN/remote setups](../../features/radio-setup/change-network-mtu-for-vpn-remote-setups.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
