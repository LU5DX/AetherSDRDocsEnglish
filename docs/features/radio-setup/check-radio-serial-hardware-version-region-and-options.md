# Check Radio Serial, Hardware Version, Region and Options

View the read-only identification fields your FLEX-8600 reports: chassis serial number, hardware version string, regulatory region, and licensed options. Use this page to confirm the radio's identity before filing a support request or verifying a hardware upgrade.

## Before you start

- AetherSDR must be connected to the radio. These fields are populated from a live radio connection.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Radio** tab. It is the first tab and opens by default.
3. In the **Radio Information** group, read the following indicators:
   - **Radio SN** — chassis serial number.
   - **HW Version** — hardware version string.
   - **Region** — regulatory region (default: `USA`).
   - **Options** — licensed options active on this radio.

## What each control does

| Label | Kind | Behavior | Default |
|---|---|---|---|
| Radio SN | Indicator | Chassis serial number. Read-only. | — |
| HW Version | Indicator | Hardware version string. Read-only. | — |
| Region | Indicator | Radio regulatory region. Read-only. | USA |
| Options | Indicator | Licensed radio options active on this unit. Read-only. | — |
| FlexControl | Indicator | Detected state of FlexControl hardware. Read-only. | — |
| multiFLEX | Indicator | multiFLEX enabled state. Read-only. | — |

## Tips

- All four fields are read-only. Nothing on this page changes the radio hardware or license state.
- If **Radio SN** is blank, the radio firmware has not yet reported the chassis serial. Disconnect and reconnect to trigger a fresh status response.

## Related

- [Radio Setup overview](overview.md)
- [Set the radio nickname, callsign and station name](set-the-radio-nickname-callsign-and-station-name.md)
- [Upload a new firmware .ssdr to the radio](upload-a-new-firmware-ssdr-to-the-radio.md)
