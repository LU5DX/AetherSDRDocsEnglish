The diff contains no user-visible changes to the documented behaviour covered by this page. The changes are internal (auto-connect guard for ShackSwitch, applet wiring, SWR sweep infrastructure, and private constants) and are already reflected in the existing documentation (the ShackSwitch row, auto-connect tip, and related troubleshooting entries). No documentation update is warranted.

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
| Status label | Displays the current discovery or connection state. Does not show "Connected" when the connected device is a ShackSwitch; that state is reflected in the ShackSwitch row instead. | No device found | No device found, Device found, Connected — \<name\> v\<version\>, Disconnected, Error: \<msg\>, Invalid IP address | — |

## ShackSwitch row (Settings > Radio Setup… > Remote Peripherals)

V0.9.4 adds a dedicated **ShackSwitch** row (Row 4) in the Remote Peripherals tab alongside the existing Antenna Genius row.

| Control | What it does | Default | Valid values | Setting key |
|---|---|---|---|---|
| **Manual IP** (ShackSwitch) | IP address used to connect to a ShackSwitch directly. | _(blank)_ | IPv4 address | `SS_ManualIp` |
| **Connect / Disconnect** | Connects to the ShackSwitch on port 9007 using the AG control protocol, or disconnects. | Connect | — | — |
| Status | Shows whether a ShackSwitch is currently connected. | Disconnected | Connected, Disconnected | — |
| **⚙ Web UI** | Opens the ShackSwitch web interface in your default browser. Uses the IP from `SS_ManualIp` (or the live peer address if a ShackSwitch is connected). Reads the web port from the device beacon (`webPort` field); falls back to `SS_WebPort`, then to port 5000. | — | — | `SS_WebPort` (fallback) |

## Tips

- AetherSDR saves the last-used address to `AG_ManualIp` when you press Enter. The field is pre-filled with that address the next time you open the applet.
- If the Device combo contains a discovered device, clicking Connect connects to that device, not the Manual IP. Clear or ignore the combo selection if you want the Manual IP to take effect via the Connect button. Pressing Enter in the Manual IP field always uses the typed address regardless of the combo state.
- Port B is hidden automatically if the connected Antenna Genius reports only one radio port.
- Auto-connect on discovery applies only to Antenna Genius devices. If a ShackSwitch is discovered on the same network, it is not auto-connected from this applet; it is handled by the ShackSwitch applet instead.
- The **⚙ Web UI** button for the ShackSwitch determines the web port in this order: (1) the `webPort` value advertised in the device beacon, if greater than 1024; (2) the `SS_WebPort` setting; (3) port 5000. Set `SS_WebPort` in application settings if your ShackSwitch uses a non-standard web port and is not yet connected.

## Troubleshooting

- **Status label shows "Invalid IP address"** — The text entered in **Manual IP** is not a valid IPv4 or IPv6 address. Correct the address and press Enter again.
- **Status label shows "Error: \<msg\>"** — AetherSDR reached the network layer but could not complete the connection. Verify that port 9007 is open and the Antenna Genius is powered on and reachable at the address you entered.
- **AG tray button never appears** — The applet remains hidden until a connection is established. Check the status label inside the applet panel for error details. If the panel itself is not visible, enable it via `View > Applet Panel`.
- **A discovered device is not auto-connecting** — If the first device discovered on the LAN is a ShackSwitch, the Antenna Genius applet will not auto-connect to it. The ShackSwitch applet handles that device. Check whether a separate Antenna Genius device is present on your network.
- **AG row shows Disconnected even though a device is connected** — If the connected device is a ShackSwitch, the AG row intentionally does not show "Connected". Check the ShackSwitch row for the actual connection state.
- **⚙ Web UI button does nothing** — The `SS_ManualIp` field is empty and no ShackSwitch is currently connected. Enter the ShackSwitch IP address in the ShackSwitch Manual IP field first.

## Related

- [Antenna Genius overview](../../features/antenna-genius/overview.md)
- [Auto-discover an Antenna Genius on the LAN](../../features/antenna-genius/auto-discover-an-antenna-genius-on-the-lan.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Select an antenna for Port A or Port B](../../features/antenna-genius/select-an-antenna-for-port-a-or-port-b.md)
- [Enable AUTO mode so the AG follows radio band changes](../../features/antenna-genius/enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
<!-- docmesh:llm version=v0.9.4 date=2026-05-01 -->