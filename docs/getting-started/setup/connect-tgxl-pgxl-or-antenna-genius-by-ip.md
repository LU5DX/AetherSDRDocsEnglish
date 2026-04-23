# Connect TGXL, PGXL or Antenna Genius by IP

This page explains how to manually connect a TGXL, PGXL, or Antenna Genius peripheral to AetherSDR using an IP address. You would do this when the device is not automatically detected on your network.

## Before you start

- AetherSDR must already be connected to your Flex radio.
- You must know the IP address of the TGXL, PGXL, or Antenna Genius device.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Peripherals** tab.
3. Locate the row for the device you want to connect (TGXL, PGXL, or Antenna Genius).
4. Enter the device's IP address in the address field for that device.
5. Click **Connect** next to that device.
6. Verify the connection state changes to show the device is connected. To disconnect at any time, click **Disconnect** next to the device.

## Troubleshooting

- **Connect does nothing or the device shows no connection** — Confirm the IP address is correct and that the device is powered on and reachable from the host running AetherSDR. Check that no firewall is blocking traffic between the host and the peripheral's IP address.
- **Device disconnects immediately after connecting** — Verify that your radio firmware is version 4.1.5 and that the peripheral's firmware is compatible with SmartSDR protocol v1.4.0.0.

## Related

- [Radio Setup overview](../../features/radio-setup/overview.md)
- [Change network MTU for VPN/remote setups](../../features/radio-setup/change-network-mtu-for-vpn-remote-setups.md)
- [Manually connect to an AG over a remote network](manually-connect-to-an-ag-over-a-remote-network.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
