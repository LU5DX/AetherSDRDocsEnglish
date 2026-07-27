# Switch to a saved transmit profile

Switch the radio to a previously saved transmit profile—loading its mic, processor, EQ, and filter settings—without affecting global or mic-only profiles.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- At least one transmit profile must exist on the radio. If none exist, create one using **Profiles > Profile Manager...** and the **Save** or **Create** button on the Transmit tab.

## Steps

1. Open the **Profile Manager** by selecting **Profiles > Profile Manager...**.
2. Click the **Transmit** tab.
3. In the profile list, click the profile you want to load.
4. Click **Load**.

The radio switches to the selected transmit profile. The active profile name appears highlighted in the list.

## Tips

- To load a profile without opening the Profile Manager, use the **Profile Switcher** tile in the Applet panel. See [Cycle through transmit profiles quickly](cycle-through-transmit-profiles-quickly.md).
- Enable **Auto-Save** on the Auto-Save tab so any changes you make to TX settings are written back to the active profile automatically.

## Related

- [Profile Manager overview](../profile-manager/overview.md)
- [Profile Switcher overview](overview.md)
- [Cycle through transmit profiles quickly](cycle-through-transmit-profiles-quickly.md)
- [Turn on auto-save so TX tweaks always persist](../profile-manager/turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [See which profile is currently active](see-which-profile-is-currently-active.md)
