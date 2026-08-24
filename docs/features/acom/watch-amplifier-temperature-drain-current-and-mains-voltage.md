# Watch amplifier temperature, drain current and mains voltage

Monitor your ACOM linear amplifier's health telemetry — temperature, drain current, and mains voltage — to detect cooling issues, power supply problems, or abnormal operating conditions before they cause damage.

## Before you start

- Your ACOM amplifier must be connected to AetherSDR via serial or TCP.
- AetherSDR must be connected to a FLEX-8600 radio.

## Steps

1. Open the **Applet panel** at the bottom of the AetherSDR window.
2. Click the **ACOM** tile.
3. Read the **Temperature**, **Drain Current**, and **Mains Voltage** indicators in the ACOM Applet panel.

## What each control does

| Control | Behavior |
|---|---|
| **Forward Power** | Real-time forward power reading from the amplifier. |
| **SWR** | Real-time SWR reading. |
| **Temperature / Drain Current / Mains Voltage** | Amplifier health telemetry readouts. |
| **Operate / Standby** | Toggles the amplifier between Operate and Standby modes. Defaults to Standby. |

## Indicators

| Indicator | States | Meaning |
|---|---|---|
| **Operate/Standby state** | Operate, Standby, Fault | Current amplifier operating mode. |

## Tips

- High temperature readings may indicate insufficient cooling — check fan operation and airflow around the amplifier.
- Unusual drain current or mains voltage values can signal power supply issues or component degradation.

## Related

- [ACOM Amplifier overview](overview.md)
- [Monitor forward power and SWR at the amplifier output](../amp/monitor-forward-power-and-swr-at-the-amplifier-output.md)
- [Put the amplifier in Operate or Standby](put-the-amplifier-in-operate-or-standby.md)