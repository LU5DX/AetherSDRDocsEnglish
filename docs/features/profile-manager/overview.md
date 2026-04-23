# Profile Manager overview

The Profile Manager lets you create, load, rename, and delete Global, Transmit, and Microphone profiles stored on the radio. Use it to save and restore complete radio states without manually reconfiguring settings each session.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.

## How it works

Open the Profile Manager from `Profiles > Profile Manager...`. The dialog contains four tabs — **Global**, **Transmit**, **Microphone**, and **Auto-Save** — each covering a separate category of profiles stored on the Flex radio.

**Global, Transmit, and Microphone tabs** share the same layout: a text field at the top for entering a profile name, three action buttons (Load, Save, Delete), and a list of all profiles in that category below. The currently active profile is highlighted in the list. Selecting a profile in the list populates the **Profile name** field with that profile's name and enables the Load and Delete buttons. Double-clicking a profile in the list loads it immediately, equivalent to clicking Load.

**Auto-Save tab** contains a single checkbox that controls whether transmit and microphone setting changes are written back to the active profile automatically.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| Global (tab) | Tab | Manage global profiles stored on the radio. | — |
| Transmit (tab) | Tab | Manage transmit profiles stored on the radio. | — |
| Microphone (tab) | Tab | Manage microphone profiles stored on the radio. | — |
| Auto-Save (tab) | Tab | Control automatic saving of transmit and mic changes. | — |
| Profile name | Text field | Name used when saving a new profile. Populated automatically when you select a profile from the list. | — |
| Profile list | List | All profiles for the current category. The active profile is highlighted. | — |
| Load | Button | Sends the selected profile to the radio, making it active. Enabled only when a profile is selected in the list. | — |
| Save | Button | Saves the current radio state under the name in the **Profile name** field. If the field is empty, uses the selected list item's name. | — |
| Delete | Button | Deletes the selected profile after a confirmation prompt. Enabled only when a profile is selected in the list. | — |
| Auto-save profile changes | Checkbox | When checked, TX and Mic setting changes are automatically written back to the active profile. | `AutoSaveTransmitProfile` |
| Close | Button | Closes the Profile Manager dialog. | — |

## Tips

- Selecting a profile in the list fills the **Profile name** field. To save under a different name, edit the field before clicking Save — this creates a new profile rather than overwriting the selected one.
- The profile list updates automatically when the radio reports changes, so profiles saved or deleted from another client will appear without reopening the dialog.

## Related

- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Rename or delete a microphone profile](rename-or-delete-a-microphone-profile.md)
- [Create a separate mic profile per microphone](create-a-separate-mic-profile-per-microphone.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [Review the list of active global profiles](review-the-list-of-active-global-profiles.md)
