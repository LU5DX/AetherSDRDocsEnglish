# Toggle the PA temperature between Celsius and Fahrenheit

This page shows you how to switch the PA temperature gauge in the Meters applet between Celsius and Fahrenheit, and explains how the choice persists across sessions.

## Before you start

- Connect to your FLEX-8600 radio.
- The Meters applet is hidden by default. Ensure the MTR tray button is enabled on the right sidebar.

## Steps

1. Click the MTR tray button on the right sidebar to open the Meters applet.
2. Locate the "Radio Hardware" header in the applet.
3. Click the temperature unit button (labeled "°C" or "°F") next to the header to toggle between Celsius and Fahrenheit.

The PA Temp gauge re-scales instantly and shows the live temperature in the selected unit. Your choice is saved automatically.

## What each control does

| Control | Default | Behavior | Setting key |
|---------|---------|----------|-------------|
| PA Temp gauge | °C | Displays the PATEMP meter reading from the radio. Scale range is 0–120 °C or 32–248 °F. Red zone above 70 °C / 158 °F. | None |
| °C / °F toggle button | °C | Toggles the PA temperature display between Celsius and Fahrenheit. The gauge label shows the live value with the selected unit. | `MtrApplet` (tempFahrenheit field) |

## Tips

- The gauge scale and tick marks snap immediately to the new unit — there is no animation across the °C-to-°F jump.
- The toggle button's tooltip tells you which unit you'll switch to next (e.g., "Click to show in Fahrenheit").
- The choice persists across restarts and is stored in the `MtrApplet` settings object under the `tempFahrenheit` field.

## Related

- [Watch PA temperature during long overs](watch-pa-temperature-during-long-overs.md)
- [Check the radio's live DC supply voltage](check-the-radio-s-live-dc-supply-voltage.md)
- [Monitor the main cooling fan speed](monitor-the-main-cooling-fan-speed.md)
- [Meters overview](overview.md)
