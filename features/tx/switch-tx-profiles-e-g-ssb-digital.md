# Switch TX profiles (e.g. SSB, Digital)

Use the TX Controls applet to switch between transmit profiles stored on the radio, such as profiles configured for SSB, digital modes, or other operating styles. Profiles are created and managed on the radio and loaded into AetherSDR automatically at connection time.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet is not active without a radio connection.
- At least one TX profile must exist on the radio. Use `Profiles > Profile Manager...` to view available profiles, or create them in SmartSDR.
- The TX Controls applet must be visible. If it is not shown, click the TX tray button in the right sidebar.

## Steps

1. Locate the **TX Profile** drop-down in the TX Controls applet. It appears directly below the **RF Power** and **Tune Pwr** sliders.
2. Click the **TX Profile** drop-down to expand it. The list is populated from the profiles stored on the radio.
3. Click the profile you want to load (for example, "SSB" or "Digital").

The radio loads the selected profile immediately. No confirmation step is required.

## What each control does

| Control | Kind | Behavior | Default | Valid values |
|---|---|---|---|---|
| TX Profile | Drop-down | Selects and loads a transmit profile from the radio. Sending a new selection loads that profile on the radio immediately. | Populated from radio at connection | Profiles returned by the radio |

## Tips

- Profile names are defined on the radio. If a profile you expect is missing, verify it exists in `Profiles > Profile Manager...`.
- You can also load a profile from the menu bar without opening the TX Controls applet: `Profiles` lists all available profiles below a separator. Click a profile name there to load it directly.
- Switching profiles mid-transmission is not recommended. Make changes while in receive.

## Related

- [TX Controls overview](overview.md)
- [Set RF output power](set-rf-output-power.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Make your first QSO with AetherSDR](../../getting-started/tutorials/first-qso.md)
