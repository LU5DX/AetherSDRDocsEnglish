# Monitor amplifier health and chain amplifiers

Monitor the ACOM linear amplifier's real-time telemetry and control its operating mode from within AetherSDR.

## Before you start

- The radio must be connected to AetherSDR.
- An ACOM amplifier must be connected and communicating (serial or TCP) with AetherSDR.

## Steps

1. Open the **Applet panel**.
2. Click the **ACOM** tile to open the ACOM Amplifier applet.

The applet shows the following real-time readings:

- **Forward Power** — real-time forward power output from the amplifier.
- **SWR** — real-time standing wave ratio at the amplifier output.
- **Temperature / Drain Current / Mains Voltage** — amplifier health telemetry.

## Select the amplifier operating mode

1. In the ACOM Amplifier applet, click **Operate** to place the amplifier in Operate (active transmit) mode.
2. Click **Standby** to place the amplifier in Standby (bypassed or idle) mode.

The **Operate/Standby state** indicator below the buttons shows the current mode: Operate, Standby, or Fault. The current mode button is highlighted.

## What each control does

| Control | Behavior |
|---------|----------|
| **Forward Power** | Indicator. Real-time forward power reading from the amplifier. |
| **SWR** | Indicator. Real-time SWR reading. |
| **Temperature / Drain Current / Mains Voltage** | Indicators. Amplifier health telemetry readouts. |
| **Operate / Standby** | Push button. Toggles the amplifier between Operate and Standby modes. Default state at power-on is Standby. |

## Tips

- The **Operate/Standby state** indicator may show **Fault** if the amplifier reports an error. The amplifier must be in a healthy state before it can enter Operate mode.
- ACOM amps automatically track the radio's band, so no manual band selection is required.

## Troubleshooting

- **Clicking Operate does nothing** — The amplifier may be in a Fault state. Check the temperature, drain current, and mains voltage readings in the ACOM applet. Resolve the fault condition on the amplifier itself before attempting to re-enter Operate.

## Related

- [Monitor forward power and SWR at the amplifier output](../amp/monitor-forward-power-and-swr-at-the-amplifier-output.md)
- [Watch amplifier temperature, drain current and mains voltage](watch-amplifier-temperature-drain-current-and-mains-voltage.md)