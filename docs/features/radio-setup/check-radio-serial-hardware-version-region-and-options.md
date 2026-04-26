# Check radio serial, hardware version, region and options

The Radio tab in Radio Setup displays read-only hardware identity fields reported directly by the radio: chassis serial number, hardware version, regulatory region, and licensed options. Use this page when you need to confirm what hardware you have connected or verify which options are active.

## Before you start

- AetherSDR must be connected to the radio. These fields are populated by the radio at connection time and are read-only.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Radio** tab if it is not already selected.
3. In the **Radio Information** group, read the following fields:
   - **Radio SN** — chassis serial number.
   - **HW Version** — hardware version string reported by the radio.
   - **Region** — regulatory region (defaults to `USA` if the radio reports none).
   - **Options** — licensed options active on this radio.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| Radio SN | Indicator | Chassis serial number. Read-only; set by the radio. |
| HW Version | Indicator | Hardware version string. Read-only; set by the radio. |
| Region | Indicator | Regulatory region. Defaults to `USA` if the radio reports an empty value. |
| Options | Indicator | Licensed options active on this radio (for example, GPS, PGXL). Read-only; set by the radio. |

## Troubleshooting

- **All fields show blank or dashes** — the radio has not yet reported its identity. Confirm the radio is fully connected and online, then close and reopen `Settings > Radio Setup...`.
- **Region shows `USA` but the radio is configured for a different region** — the radio firmware reported an empty region string; AetherSDR substitutes `USA` as the default display value. Check the radio firmware and region settings in SmartSDR if the displayed value is unexpected.

## Related

- [Radio Setup overview](overview.md)
- [Set the radio nickname, callsign and station name](set-the-radio-nickname-callsign-and-station-name.md)
- [Upload a new firmware .ssdr to the radio](upload-a-new-firmware-ssdr-to-the-radio.md)
