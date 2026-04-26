# Switch TX profiles (e.g. SSB, Digital)

Use the TX profile selector to load a named transmit profile stored on the radio — for example, switching from an SSB voice profile to a Digital modes profile without re-entering microphone, EQ, or compressor settings manually.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet is not functional without an active radio connection.
- Transmit profiles must already exist on the FLEX-8600. Create or manage them via `Profiles > Profile Manager...`.

## Steps

1. Click the **TX** tray button in the right sidebar to open the TX Controls applet, if it is not already visible.
2. Locate the **TX Profile** drop-down box in the TX Controls applet. It appears below the **RF Power** and **Tune Pwr** sliders.
3. Click the **TX Profile** drop-down and select the profile you want to load (for example, "SSB" or "Digital").

The radio loads the selected profile immediately. No confirm step is required.

## What each control does

| Control | Kind | Behavior | Default | Valid values |
|---|---|---|---|---|
| **TX Profile** | Drop-down | Loads the selected transmit profile on the radio. The list is populated from the profiles stored on the radio. | — | Profiles returned by the radio |

## Tips

- You can also load a profile from the menu bar. Go to `Profiles` and click any profile name listed below the separator. The checkmark moves to the newly loaded profile.
- To create, rename, or delete profiles, use `Profiles > Profile Manager...`.

## Troubleshooting

- **TX Profile drop-down is empty** — The radio has no global transmit profiles defined. Open `Profiles > Profile Manager...` to create one.
- **Selecting a profile has no effect** — Confirm the radio connection is active. The profile selector does not send a command when AetherSDR is disconnected from the radio.

## Related

- [TX Controls overview](overview.md)
- [Set RF output power](set-rf-output-power.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Make your first QSO with AetherSDR](../../getting-started/tutorials/first-qso.md)
