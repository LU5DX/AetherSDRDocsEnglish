# Check Radio Serial, Hardware Version, Region and Options

Open the Radio tab in Radio Setup to view your FLEX-8600's chassis serial number, hardware version, regulatory region, and licensed options. All fields on this tab are read-only indicators — no values can be changed here.

## Before you start

- AetherSDR must be connected to the radio. These indicators are populated from the live radio connection.

## Steps

1. Click `Settings > Radio Setup...`.
2. The dialog opens on the **Radio** tab by default.
3. Locate the **Radio Information** group.
4. Read the values from the following indicators:
   - **Radio SN** — chassis serial number.
   - **HW Version** — hardware version string.
   - **Region** — regulatory region (default: `USA`).
   - **Options** — licensed options active on this radio.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| Radio SN | Indicator | Chassis serial number. Read-only. |
| HW Version | Indicator | Hardware version string. Read-only. |
| Region | Indicator | Radio regulatory region. Defaults to `USA`. Read-only. |
| Options | Indicator | Lists the licensed options active on the radio. Read-only. |
| Model | Indicator | Radio model string. Read-only. |
| FlexControl | Indicator | Detected state of connected FlexControl hardware. Read-only. |
| multiFLEX | Indicator | multiFLEX enabled state. Read-only. |

## Tips

- If **Radio SN** appears blank, the radio may not have reported its chassis serial yet. Disconnect and reconnect to the radio, then reopen Radio Setup.
- **Options** reflects what the radio firmware reports as licensed. If an expected option is missing, verify your license status through FlexRadio's licensing portal.

## Related

- [Set the radio nickname, callsign and station name](set-the-radio-nickname-callsign-and-station-name.md)
- [Upload a new firmware .ssdr to the radio](upload-a-new-firmware-ssdr-to-the-radio.md)
- [Radio Setup overview](overview.md)
