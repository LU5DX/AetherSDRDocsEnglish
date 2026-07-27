# Put the amplifier in Operate or Standby

Toggle the ACOM linear amplifier between the Operate (active transmit) and Standby (bypassed or idle) state from within AetherSDR.

## Before you start

- The radio must be connected to AetherSDR.
- An ACOM amplifier must be connected and communicating (serial or TCP) with AetherSDR.

## Steps

1. Open the **Applet panel**.
2. Click the **ACOM** tile to open the ACOM Amplifier applet.
3. Click the **Operate / Standby** button to toggle between the two modes.

   - The button label shows the current mode. When the amplifier is in Operate, the button reads **Operate**; clicking it switches to Standby, and vice versa.
   - The **Operate/Standby state** indicator below the button confirms the current mode: Operate, Standby, or Fault.

## What each control does

| Control | Behavior |
|---------|----------|
| **Operate / Standby** | Push button. Toggles the amplifier between Operate and Standby modes. Default state at power-on is Standby. |

## Tips

- The **Operate/Standby state** indicator may show **Fault** if the amplifier reports an error. The amplifier must be in a healthy state before it can enter Operate mode.

## Troubleshooting

- **Clicking Operate / Standby does nothing** — The amplifier may be in a Fault state. Check the temperature, drain current, and mains voltage readings in the ACOM applet. Resolve the fault condition on the amplifier itself before attempting to re-enter Operate.

## Related

- [ACOM Amplifier overview](overview.md)
- [Monitor forward power and SWR at the amplifier output](../amp/monitor-forward-power-and-swr-at-the-amplifier-output.md)
- [Watch amplifier temperature, drain current and mains voltage](watch-amplifier-temperature-drain-current-and-mains-voltage.md)
