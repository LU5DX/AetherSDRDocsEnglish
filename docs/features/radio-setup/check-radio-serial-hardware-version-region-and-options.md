# Check Radio Serial, Hardware Version, Region and Options

View the read-only hardware details reported by your connected FLEX-8600: chassis serial number, hardware version string, regulatory region, and licensed options.

## Before you start

- AetherSDR must be connected to the radio. These fields are populated from the live radio connection and are blank otherwise.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Radio** tab (it opens by default).
3. Locate the **Radio Information** group near the top of the tab.
4. Read the values shown for **Radio SN**, **HW Version**, **Region**, and **Options**.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| **Radio SN** | Indicator (read-only) | Chassis serial number reported by the radio. |
| **HW Version** | Indicator (read-only) | Hardware version string reported by the radio. |
| **Region** | Indicator (read-only) | Regulatory region programmed into the radio. Displays `USA` if the radio reports no region. |
| **Options** | Indicator (read-only) | Licensed options active on this radio (for example, `GPS`, `GPS, PGXL`). |

## Tips

- All four fields are read-only. There are no controls to change them from AetherSDR; they reflect what the radio firmware reports.
- If **Radio SN** is blank, the radio connection may not yet be fully established. Close and reopen the dialog after the connection stabilises.

## Related

- [Radio Setup overview](overview.md)
- [Set the radio nickname, callsign and station name](set-the-radio-nickname-callsign-and-station-name.md)
- [Upload a new firmware .ssdr to the radio](upload-a-new-firmware-ssdr-to-the-radio.md)
