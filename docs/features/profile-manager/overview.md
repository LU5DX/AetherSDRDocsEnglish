# Profile Manager overview

The Profile Manager lets you create, load, and delete Global, Transmit, and Microphone profiles stored on the radio. Use it to save and recall complete radio states without reconfiguring settings by hand.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Profile Manager requires an active radio connection.

## How it works

Open the Profile Manager from `Profiles > Profile Manager...`. The dialog contains four tabs — **Global**, **Transmit**, **Microphone**, and **Auto-Save** — each operating independently on its respective profile category.

On the **Global**, **Transmit**, and **Microphone** tabs, the workflow is the same:

1. The **Profile list** shows all profiles stored on the radio for that category. The currently active profile is highlighted.
2. Selecting an entry in the **Profile list** populates the **Profile name** field with that entry's name and enables the **Load** and **Delete** buttons.
3. Type a new name into **Profile name** and click **Save** to store the current radio state under that name. If the field is empty when you click **Save**, the dialog uses the selected list item's name instead.
4. Select a profile and click **Load** (or double-click the entry) to apply it to the radio immediately.
5. Select a profile and click **Delete** to remove it. A confirmation prompt appears before the profile is removed.

The **Auto-Save** tab contains a single checkbox that controls automatic saving of transmit changes.

Click **Close** to dismiss the dialog.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Global** | Tab | Manages global profiles. | — |
| **Transmit** | Tab | Manages transmit profiles. | — |
| **Microphone** | Tab | Manages microphone profiles. | — |
| **Auto-Save** | Tab | Controls automatic profile saving. | — |
| **Profile name** | Text field | Name used when saving a new profile. If empty at save time, the selected list item's name is used. | — |
| **Profile list** | List | All profiles for the active category; the active profile is highlighted. | — |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. Also triggered by double-clicking a list entry. | — |
| **Save** | Button | Saves the current radio state under the name in **Profile name**. | — |
| **Delete** | Button | Deletes the selected profile after confirmation. Enabled only when a profile is selected. | — |
| **Auto-save profile changes** | Checkbox | When checked, TX and Mic setting changes are written back to the active profile automatically. | `AutoSaveTransmitProfile` |
| **Close** | Button | Closes the dialog. | — |

## Tips

- The **Profile list** updates automatically when the radio reports a change, so profiles saved or deleted elsewhere (for example, from SmartSDR on another client) appear without reopening the dialog.
- Load and Delete are disabled until you select a profile from the list. If the buttons appear greyed out, click a profile name first.

## Related

- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [Rename or delete a microphone profile](rename-or-delete-a-microphone-profile.md)
- [Create a separate mic profile per microphone](create-a-separate-mic-profile-per-microphone.md)
- [Review the list of active global profiles](review-the-list-of-active-global-profiles.md)
