# Switch TX Profiles (e.g. SSB, Digital)

TX profiles store transmit settings such as microphone equalization, compression, and mode-specific audio processing. Switching profiles lets you quickly move between configurations — for example, from an SSB voice profile to a digital modes profile — without manually adjusting each setting.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet requires an active radio connection.
- TX profiles must already exist on the radio. To create or edit profiles, use `Profiles > Profile Manager...`.

## Steps

1. Click the **TX** tray button in the right sidebar to open the TX Controls applet.
2. Locate the **TX Profile** drop-down box near the top of the applet, below the RF Power and Tune Pwr sliders.
3. Click the **TX Profile** drop-down and select the profile name you want to load (for example, "SSB" or "Digital").

The radio loads the selected profile immediately. No additional confirmation is required.

## What each control does

| Control | Kind | Behavior | Default |
|---|---|---|---|
| **TX Profile** | Drop-down | Loads the selected transmit profile on the radio. The list is populated from the profiles stored on the radio. | None (populated at connection) |

## Tips

- You can also switch profiles from the menu bar. Open `Profiles` and click any profile name in the list below the separator. The active profile is shown with a check mark.
- Profile contents (equalization, compression, etc.) are stored on the radio, not in AetherSDR. Use `Profiles > Profile Manager...` to manage them.

## Troubleshooting

- **The TX Profile drop-down is empty** — No transmit profiles are stored on the radio. Open `Profiles > Profile Manager...` to create one.
- **The TX Profile drop-down is not responding** — AetherSDR is not connected to the radio. The TX Controls applet requires an active connection. Check your connection via `Settings > Connect to Radio...`.

## Related

- [TX Controls overview](overview.md)
- [Set RF output power](set-rf-output-power.md)
- [Make your first QSO with AetherSDR](../../getting-started/tutorials/first-qso.md)
