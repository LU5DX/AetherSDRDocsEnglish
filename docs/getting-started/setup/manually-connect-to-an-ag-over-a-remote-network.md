# Manually connect to an AG over a remote network

Use this page to connect AetherSDR to an Antenna Genius that is not on the local LAN — for example, across a VPN or a routed network — by entering its IP address directly. UDP discovery only works on the local subnet, so a manual IP entry is required for remote devices.

## Before you start

- The Antenna Genius must be reachable from your machine at TCP port 9007. Confirm this with your network or VPN configuration before proceeding.
- The Antenna Genius applet is hidden until a device is discovered or manually connected. If you do not see the AG tray button in the right sidebar, that is expected — it will appear after a successful connection.

## Steps

1. Open the applet panel. If it is not visible, click `View > Applet Panel`.
2. Look for the AG tray button in the right sidebar. If the applet is already open, skip to step 4.
3. If no AG tray button is visible yet, proceed through the remaining steps — the button appears once a connection is established.
4. In the Antenna Genius applet, locate the **Manual IP** field (labelled "Manual IP:").
5. Type the IPv4 or IPv6 address of the remote Antenna Genius into the **Manual IP** field.
6. Press **Enter**. AetherSDR validates the address and connects to port 9007.
7. Watch the status label beneath the device combo. A successful connection shows `Connected — <name> v<version>`. An unreachable or refused connection shows `Error: <msg>`.

## What each control does

| Control | What it does | Default | Valid values | Setting key |
|---|---|---|---|---|
| **Manual IP** | Stores and uses an IP address to connect directly, bypassing UDP discovery. Pressing Enter triggers the connection attempt. | _(blank)_ | IPv4 or IPv6 address | `AG_ManualIp` |
| **Connect / Disconnect** | Connects to the selected device in the Device combo, or to the Manual IP address if no discovered device is selected. Becomes Disconnect when connected. | Connect | — | — |
| Status label | Displays the current discovery or connection state. | No device found | No device found, Device found, Connected — \<name\> v\<version\>, Disconnected, Error: \<msg\>, Invalid IP address | — |

## Tips

- AetherSDR saves the last-used address to `AG_ManualIp` when you press Enter. The field is pre-filled with that address the next time you open the applet.
- If the Device combo contains a discovered device, clicking Connect connects to that device, not the Manual IP. Clear or ignore the combo selection if you want the Manual IP to take effect via the Connect button. Pressing Enter in the Manual IP field always uses the typed address regardless of the combo state.
- Port B is hidden automatically if the connected Antenna Genius reports only one radio port.

## Troubleshooting

- **Status label shows "Invalid IP address"** — The text entered in **Manual IP** is not a valid IPv4 or IPv6 address. Correct the address and press Enter again.
- **Status label shows "Error: \<msg\>"** — AetherSDR reached the network layer but could not complete the connection. Verify that port 9007 is open and the Antenna Genius is powered on and reachable at the address you entered.
- **AG tray button never appears** — The applet remains hidden until a connection is established. Check the status label inside the applet panel for error details. If the panel itself is not visible, enable it via `View > Applet Panel`.

## Related

- [Antenna Genius overview](../../features/antenna-genius/overview.md)
- [Auto-discover an Antenna Genius on the LAN](../../features/antenna-genius/auto-discover-an-antenna-genius-on-the-lan.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Select an antenna for Port A or Port B](../../features/antenna-genius/select-an-antenna-for-port-a-or-port-b.md)
- [Enable AUTO mode so the AG follows radio band changes](../../features/antenna-genius/enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
