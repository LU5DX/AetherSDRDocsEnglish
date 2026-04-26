# Turn on auto-save so TX tweaks always persist

Enable auto-save so that any changes you make to transmit and microphone settings are written back to the active profile automatically, without needing to save manually after each adjustment.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.
- At least one transmit profile must exist on the radio for auto-save to have a profile to write to.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the **Auto-Save** tab.
3. Check **Auto-save profile changes**.
4. Click **Close**.

The setting takes effect immediately. AetherSDR sends the change to the radio and persists your choice in `AutoSaveTransmitProfile`.

## What each control does

| Control | Description | Persisted setting |
|---|---|---|
| **Auto-save profile changes** | When checked, TX and microphone setting changes are written automatically to the active profile. When unchecked, changes are discarded unless you save manually. | `AutoSaveTransmitProfile` |

## Tips

- To disable auto-save, return to `Profiles > Profile Manager...`, click the **Auto-Save** tab, and uncheck **Auto-save profile changes**.
- If you want a clean baseline before enabling auto-save, load the desired profile first using the **Transmit** tab, then enable auto-save.

## Related

- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Profile Manager overview](overview.md)
