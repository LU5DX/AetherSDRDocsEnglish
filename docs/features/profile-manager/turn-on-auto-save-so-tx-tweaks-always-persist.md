# Turn on auto-save so TX tweaks always persist

When auto-save is enabled, any changes you make to TX and microphone settings are written back to the active profile automatically, so you never lose a tweak by forgetting to save manually.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.
- At least one transmit or microphone profile must already exist on the radio for auto-save to have a profile to write to.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the **Auto-Save** tab.
3. Check **Auto-save profile changes**.
4. Click **Close**.

The setting takes effect immediately. AetherSDR sends the change to the radio; no restart is required.

To turn auto-save off, repeat the steps and uncheck **Auto-save profile changes**.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Auto-save profile changes** | Checkbox | When checked, TX and microphone setting changes are automatically saved to the active profile on the radio. When unchecked, changes are discarded unless you save manually. | `AutoSaveTransmitProfile` |

## Tips

- Auto-save applies to both TX and microphone settings, not just one category. If you want to experiment without overwriting your current profile, uncheck **Auto-save profile changes** first, make your changes, and evaluate before committing a manual save.
- The checkbox reflects the current state reported by the radio when the dialog opens. If another client changed the setting on the radio, the checkbox updates to match.

## Related

- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Profile Manager overview](overview.md)
