# Manually connect to an AG over a remote network

Use this procedure when your Antenna Genius is not on the same LAN segment as AetherSDR and UDP discovery cannot reach it. Entering the device's IP address directly bypasses discovery and connects to port 9007.

## Before you start

- You know the IPv4 or IPv6 address of the Antenna Genius on the remote network.
- The remote network allows TCP traffic to port 9007 on the Antenna Genius (VPN, port forward, or routed path).
- The Antenna Genius applet is visible. If the AG tray button is not shown on the right sidebar, AetherSDR has not yet detected any device. Proceed anyway — entering a manual IP will cause the applet to appear after a successful connection.

## Steps

1. Click the **AG** tray button on the right sidebar to open the Antenna Genius applet.
2. Locate the **Manual IP** field below the status label.
3. Type the IPv4 or IPv6 address of the Antenna Genius into the **Manual IP** field.
4. Press **Enter**.
   - AetherSDR validates the address. If it is malformed, the status label turns red and shows `Invalid IP address`. Correct the address and press **Enter** again.
   - If the address is valid, AetherSDR saves it to `AG_ManualIp` and attempts a connection to port 9007.
5. Watch the status label:
   - `Connected — <name> v<version>` confirms a successful connection. The **Connect / Disconnect** button changes to **Disconnect**.
   - `Error: <msg>` means the device was unreachable or refused the connection. Check the address, firewall rules, and that port 9007 is open.

## What each control does

| Control | Behavior | Default | Persisted key |
|---|---|---|---|
| **Manual IP** | Accepts an IPv4 or IPv6 address. Press **Enter** to initiate a connection to port 9007. An invalid address shows `Invalid IP address` in red. | *(blank, or last-used address)* | `AG_ManualIp` |
| **Connect / Disconnect** | While disconnected and no discovered device is selected in the device combo, clicking **Connect** also triggers a manual-IP connection attempt. Changes to **Disconnect** when connected. | Connect | — |
| Status label | Shows discovery and connection state: `No device found`, `Device found`, `Connected — <name> v<version>`, `Disconnected`, `Error: <msg>`, or `Invalid IP address`. | No device found | — |

## Tips

- AetherSDR restores the last-used manual IP from `AG_ManualIp` when it starts, so the field is pre-filled on subsequent launches.
- If a device is already selected in the device combo, clicking **Connect** connects to that discovered device rather than the manual IP. Clear or ignore the combo selection if you intend to use the manual IP path.
- Port B is hidden if the connected Antenna Genius reports only one radio port. This is normal for single-port devices.

## Troubleshooting

- **Status shows `Invalid IP address`** — The text in the **Manual IP** field is not a valid IPv4 or IPv6 address. Check for typos, stray spaces, or a hostname (hostnames are not accepted; use a numeric IP address).
- **Status shows `Error: <msg>` after a valid address** — The Antenna Genius is unreachable on port 9007. Verify the IP address is correct, that a VPN or route to the remote network is active, and that no firewall is blocking port 9007.
- **AG tray button is not visible** — The applet is hidden until a device is detected or connected. If you cannot see the tray button, see [Antenna Genius overview](../../features/antenna-genius/overview.md) for how to reveal the applet panel.

## Related

- [Antenna Genius overview](../../features/antenna-genius/overview.md)
- [Auto-discover an Antenna Genius on the LAN](../../features/antenna-genius/auto-discover-an-antenna-genius-on-the-lan.md)
- [Select an antenna for Port A or Port B](../../features/antenna-genius/select-an-antenna-for-port-a-or-port-b.md)
- [Enable AUTO mode so the AG follows radio band changes](../../features/antenna-genius/enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
