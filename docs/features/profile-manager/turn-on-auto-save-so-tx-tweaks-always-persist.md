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

The setting takes effect immediately. AetherSDR sends the change to the radio and persists your preference as `AutoSaveTransmitProfile`.

## What each control does

| Control | Description | Persisted key |
|---|---|---|
| **Auto-save profile changes** | When checked, TX and microphone setting changes are automatically saved to the active profile. When unchecked, changes are not written back until you save manually from the **Transmit** or **Microphone** tab. | `AutoSaveTransmitProfile` |

## Tips

- To save the current transmit state under a specific name instead of relying on auto-save, use the **Transmit** tab and click **Save** with a name entered in the **Profile name** field.
- Auto-save applies to both TX and microphone settings, not only one or the other.

## Related

- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Create a separate mic profile per microphone](create-a-separate-mic-profile-per-microphone.md)
