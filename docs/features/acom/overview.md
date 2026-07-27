# ACOM Amplifier overview

The ACOM Amplifier applet lets you monitor and control an ACOM linear amplifier connected via serial or TCP. It provides real-time telemetry and basic operating mode control, with automatic band tracking when the radio is tuned.

## How it works

The applet communicates with an ACOM amplifier over a serial or TCP connection. Once connected, it continuously receives telemetry data from the amplifier and displays it in real time. The applet also sends band-change commands to the amplifier when you change frequency on the radio, keeping the amplifier's band selection in sync.

## Opening the ACOM Amplifier applet

1. Locate the Applet Panel tray on the main window.
2. Click the ACOM tile to open the ACOM Amplifier applet.

## What each control does

| Control | Kind | Default | Behavior |
|---------|------|---------|----------|
| Forward Power | indicator | — | Real-time forward power reading from the amplifier. |
| SWR | indicator | — | Real-time SWR reading. |
| Temperature / Drain Current / Mains Voltage | indicator | — | Amplifier health telemetry readouts. |
| Operate / Standby | push button | Standby | Toggles the amplifier between Operate and Standby modes. The indicator shows current state: Operate, Standby, or Fault. |

## Related

- [Monitor forward power and SWR at the amplifier output](../amp/monitor-forward-power-and-swr-at-the-amplifier-output.md)
- [Put the amplifier in Operate or Standby](put-the-amplifier-in-operate-or-standby.md)
- [Watch amplifier temperature, drain current and mains voltage](watch-amplifier-temperature-drain-current-and-mains-voltage.md)
