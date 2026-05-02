# Connect TGXL, PGXL, Antenna Genius, or ShackSwitch by IP

Use this page to manually connect a TGXL, PGXL, Antenna Genius, or ShackSwitch device to AetherSDR when automatic discovery has not picked up the device.

## Before you start

- AetherSDR must already be connected to a FLEX-8600 radio. The Peripherals tab is only available when a radio connection is active.
- Have the IP address of the TGXL, PGXL, Antenna Genius, or ShackSwitch device ready.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Peripherals** tab.
3. Locate the row for the device you want to connect (TGXL, PGXL, Antenna Genius, or ShackSwitch).
4. Enter the device's IP address in the field for that device.
5. Click **Connect** for that device.

To disconnect a device, click **Disconnect** on its row.

## Peripherals tab — device rows

| Device | Default port | Notes |
|---|---|---|
| TGXL | 9010 | Required to recover TUNE on firmware 4.2+. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort`. If the IP field is empty and the radio has already discovered the TGXL, the discovered IP is pre-filled. |
| PGXL | 9008 | Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| Antenna Genius (AG) | 9007 | Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row shows **Connected** status only when the connected device is a non-ShackSwitch Antenna Genius. Auto-connect on discovery is suppressed for ShackSwitch units; those are handled by the ShackSwitch row instead. |
| ShackSwitch | 9007 | Uses the AG UDP/TCP protocol. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. ShackSwitch is detected by the `ShackSwitch` field in the AG broadcast beacon, or by a serial number starting with `G0JKN`. Auto-discovery via UDP also works without manually entering an IP. The row is hidden if an Antenna Genius (non-ShackSwitch) is the connected device. When a ShackSwitch is detected, the saved `AG_ManualIp` value is cleared so the AG row does not auto-connect to the ShackSwitch on the next startup. |

## Opening the ShackSwitch web interface

Each ShackSwitch row includes a **⚙ Web UI** button. Clicking it opens the ShackSwitch device's local web configuration interface in the system browser.

AetherSDR determines the port for the web interface as follows:

1. If the connected ShackSwitch beacon advertises a `webPort` greater than 1024, that port is used.
2. Otherwise, the value stored in `SS_WebPort` is used.
3. If neither is available, port 5000 is used as the fallback.

The button uses the IP address stored in `SS_ManualIp`. If that field is empty and a ShackSwitch is currently connected, the live peer address is used instead. The button does nothing if no IP address can be determined.

The `webPort` value is populated from the AG discovery beacon's `webport` field. If a beacon arrives after the initial connection is established, AetherSDR updates the connected device record with the latest `webPort` and other fields automatically — no reconnection is required.

## Related

- [Radio Setup overview](../../features/radio-setup/overview.md)
- [Manually connect to an AG over a remote network](manually-connect-to-an-ag-over-a-remote-network.md)
- [Change network MTU for VPN/remote setups](../../features/radio-setup/change-network-mtu-for-vpn-remote-setups.md)

---

# Radio Setup — Firmware Update (v0.9.3 changes)

## Selecting a firmware file

In v0.9.3 the **Browse .ssdr...** button has been renamed to **Select Installer...**. The button now accepts three file types in addition to pre-extracted firmware:

| File type | Extension | Notes |
|---|---|---|
| SmartSDR WiX installer | `.msi` | FlexRadio v4.2 and later |
| SmartSDR self-extracting installer | `.exe` | Older SmartSDR releases |
| Extracted firmware file | `.ssdr` | As in previous AetherSDR versions |

The firmware stager detects the format automatically from the first 8 bytes of the file (OLE/MSI magic versus PE/COFF MZ header) and extracts the `.ssdr` payload without requiring any external tools.

### To stage firmware from a local installer

1. Download the SmartSDR installer from flexradio.com.
2. Open `Settings > Radio Setup...`.
3. Click the **Radio** tab.
4. Click **Select Installer...**.
5. In the file picker, select the `.msi`, `.exe`, or `.ssdr` file.
6. AetherSDR extracts and stages the firmware. Watch the progress bar and status line for progress and any errors.
7. When staging is complete, click **Upload Firmware** to send the firmware to the radio.

## Check for Update behavior change

When **Check for Update** finds a newer firmware version, AetherSDR now displays an informational message rather than offering an in-app download:

> Update available: v*X.Y.Z*  
> Download the SmartSDR installer from flexradio.com,  
> then click 'Select Installer...' to stage it.

Download the installer from flexradio.com independently, then use **Select Installer...** as described above.
<!-- docmesh:llm version=V0.9.4 date=2026-05-01 -->