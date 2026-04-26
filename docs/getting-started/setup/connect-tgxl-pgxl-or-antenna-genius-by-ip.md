# Connect TGXL, PGXL or Antenna Genius by IP

This page explains how to manually connect a TGXL, PGXL, or Antenna Genius peripheral to AetherSDR using its IP address. Use this when the device is not discovered automatically on your network.

## Before you start

- AetherSDR must already be connected to a FLEX-8600 radio. The Peripherals tab is only available when a radio connection is active.
- You must know the IP address of the TGXL, PGXL, or Antenna Genius device.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Peripherals** tab.
3. Locate the row for the device you want to connect (TGXL, PGXL, or Antenna Genius).
4. Enter the device's IP address in the address field for that device.
5. Click **Connect** next to that device.

To disconnect a device, click **Disconnect** next to it.

## Tips

- If your peripheral is on a different subnet or reachable only through a VPN, enter its routable IP address directly in the address field before clicking **Connect**.
- Each device (TGXL, PGXL, Antenna Genius) has its own independent **Connect** / **Disconnect** control. You can connect them individually.

## Troubleshooting

- **Connect button does not respond or device shows no connection** — Verify the IP address is correct and that the device is powered on and reachable from your host. Try pinging the device IP from a terminal before retrying.
- **Peripherals tab is missing or greyed out** — The tab requires an active radio connection. Connect to the FLEX-8600 first, then reopen `Settings > Radio Setup...`.

## Related

- [Radio Setup overview](../../features/radio-setup/overview.md)
- [Manually connect to an AG over a remote network](manually-connect-to-an-ag-over-a-remote-network.md)
- [Change network MTU for VPN/remote setups](../../features/radio-setup/change-network-mtu-for-vpn-remote-setups.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
