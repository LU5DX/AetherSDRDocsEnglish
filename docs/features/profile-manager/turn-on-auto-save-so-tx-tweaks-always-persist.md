# Turn on auto-save so TX tweaks always persist

When auto-save is enabled, any changes you make to TX and microphone settings are written back to the active profile automatically, so nothing is lost when you switch profiles or restart.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.
- At least one transmit or microphone profile must exist on the radio for auto-save to have a profile to write to.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the `Auto-Save (tab)` tab.
3. Check `Auto-save profile changes`.

AetherSDR sends the change to the radio immediately. No additional save step is required. To disable auto-save, uncheck `Auto-save profile changes`.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| `Auto-save profile changes` | When checked, TX and microphone setting changes are automatically saved to the active profile on the radio. When unchecked, changes are discarded unless you manually save a profile. | `AutoSaveTransmitProfile` |

## Tips

- Auto-save applies to the currently active transmit and microphone profiles. If no profile is active on the radio, there is nothing for auto-save to write to. Load a profile first using the `Transmit (tab)` or `Microphone (tab)` tab before enabling auto-save.
- To manually save a specific state without enabling auto-save, use the `Save` button on the `Transmit (tab)` or `Microphone (tab)` tab instead.

## Related

- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Create a separate mic profile per microphone](create-a-separate-mic-profile-per-microphone.md)
- [Profile Manager overview](overview.md)
