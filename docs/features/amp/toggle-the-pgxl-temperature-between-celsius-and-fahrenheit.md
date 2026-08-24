# Toggle the PGXL temperature between Celsius and Fahrenheit

Switch the amplifier temperature readout in the Amplifier applet between Celsius and Fahrenheit. The unit you choose is remembered the next time AetherSDR starts.

## Before you start

- A Power Genius XL amplifier must be detected by AetherSDR.
- The Amplifier applet must be visible. If it isn't, click the **AMP** tray button on the right sidebar.

## Steps

1. Locate the temperature button in the Amplifier applet. It shows the current temperature and unit, for example `45.6 °C`.
2. Click the temperature button to switch to the other unit. The display updates immediately and the tooltip announces the unit the next click would switch to.
3. The chosen unit is saved automatically. No further action is needed.

## What each control does

| Control | Default | Persisted setting | Behavior |
| :--- | :--- | :--- | :--- |
| Temp (C/F button) | °C | `AmpApplet` (`tempFahrenheit` field) | Shows the amplifier temperature and toggles between Celsius and Fahrenheit on click. Displays `tempA/tempB °C` when both sensors report, or `tempA °C` otherwise. |

## Tips

- The temperature button also shows both sensors when the PGXL reports two temperature readings (for example `45.6/47.2 °C`).
- The unit choice is stored per-app, not per-radio, so it carries over across radio reconnects.

## Related

- [Watch PGXL temperature, drain current, and mains voltage](watch-pgxl-temperature-drain-current-and-mains-voltage.md)
- [Amplifier overview](overview.md)
