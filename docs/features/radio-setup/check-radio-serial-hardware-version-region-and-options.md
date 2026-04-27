# Check Radio Serial, Hardware Version, Region and Options

The Radio tab in Radio Setup shows identifying information reported directly by the radio — serial number, hardware version, regulatory region, and licensed options. Use this page to verify what hardware and options your radio has before troubleshooting or contacting support.

## Before you start

- AetherSDR must be connected to the radio. The Radio tab fields are populated from live radio data.

## Steps

1. Click `Settings > Radio Setup...`.
2. The dialog opens on the **Radio** tab by default.
3. Read the values in the **Radio Information** group:
   - **Radio SN** — the chassis serial number.
   - **HW Version** — the hardware version string reported by the radio.
   - **Region** — the radio's regulatory region (defaults to `USA` if the radio does not report one).
   - **Options** — the licensed options active on this radio (for example, `GPS`, `PGXL`).

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| Radio SN | Indicator (read-only) | Chassis serial number as reported by the radio. |
| HW Version | Indicator (read-only) | Hardware version string prefixed with `v`. |
| Region | Indicator (read-only) | Regulatory region. Displays `USA` if the radio reports none. |
| Options | Indicator (read-only) | Licensed radio options. |

All four fields are read-only. No persisted settings keys are associated with them.

## Tips

- If **Radio SN** is blank, the radio has not yet sent its chassis serial. Disconnect and reconnect to the radio.
- **Options** reflects what the radio itself reports. If you have recently purchased a license upgrade, power-cycle the radio and reconnect so it fetches the updated options.

## Related

- [Radio Setup overview](overview.md)
- [Set the radio nickname, callsign and station name](set-the-radio-nickname-callsign-and-station-name.md)
- [Upload a new firmware .ssdr to the radio](upload-a-new-firmware-ssdr-to-the-radio.md)
