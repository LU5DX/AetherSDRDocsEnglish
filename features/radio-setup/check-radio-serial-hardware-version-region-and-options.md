# Check Radio Serial, Hardware Version, Region and Options

Open the Radio tab in Radio Setup to view your FLEX-8600's chassis serial number, hardware version string, regulatory region, and licensed options. These are read-only values reported by the radio firmware.

## Before you start

- AetherSDR must be connected to the radio. The Radio tab fields are blank until a connection is established.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Read the values in the **Radio Information** group:
   - **Radio SN** — chassis serial number.
   - **HW Version** — hardware version string reported by the radio.
   - **Region** — regulatory region (defaults to `USA` if the radio does not report one).
   - **Options** — licensed options active on this radio.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| Radio SN | Indicator (read-only) | Chassis serial number as reported by the radio. |
| HW Version | Indicator (read-only) | Hardware version string. Displayed with a leading `v`. |
| Region | Indicator (read-only) | Regulatory region. Default: `USA`. |
| Options | Indicator (read-only) | Licensed radio options string from the radio firmware. |
| FlexControl | Indicator (read-only) | Detected state of connected FlexControl hardware. |
| multiFLEX | Indicator (read-only) | multiFLEX enabled state. |

## Tips

- All four values are read from the radio at connection time and cannot be changed from this dialog.
- License details (subscription tier, expiration date, Radio ID, and licensed firmware version) are shown in the **License Info** group on the same tab.

## Related

- [Set the radio nickname, callsign and station name](set-the-radio-nickname-callsign-and-station-name.md)
- [Upload a new firmware .ssdr to the radio](upload-a-new-firmware-ssdr-to-the-radio.md)
- [Radio Setup overview](overview.md)
