# Switch TX Profiles (e.g. SSB, Digital)

Use the TX Profile selector to load a named transmit profile from the radio. Profiles store microphone settings, equalizer values, and other transmit parameters, letting you switch quickly between modes such as SSB and Digital.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet requires an active radio connection.
- At least one transmit profile must already exist on the radio. Create or manage profiles via `Profiles > Profile Manager...`.

## Steps

1. Click the **TX** tray button in the right sidebar to open the TX Controls applet.
2. Locate the **TX Profile** drop-down near the middle of the applet.
3. Click the drop-down and select the profile name you want to load (for example, "SSB" or "Digital").

The radio loads the selected profile immediately. No confirmation step is required.

## What each control does

| Control | Kind | Behavior | Default | Valid values |
|---|---|---|---|---|
| **TX Profile** | Drop-down | Selects and loads a transmit profile from the radio. The list is populated by the radio. | — | Populated from the radio's profile list |

## Tips

- You can also load a profile from the menu bar without opening the TX Controls applet. Go to `Profiles` and click the profile name in the checkable list below the separator.
- To create, edit, or delete profiles, go to `Profiles > Profile Manager...`.

## Troubleshooting

- **TX Profile drop-down is empty** — No transmit profiles exist on the radio. Open `Profiles > Profile Manager...` to create one.
- **TX Profile drop-down is not responding** — AetherSDR is not connected to the radio. Connect first via `Settings > Connect to Radio...`.

## Related

- [TX Controls overview](overview.md)
- [Set RF output power](set-rf-output-power.md)
- [Run a Two-Tone Tune](run-a-two-tone-tune.md)
