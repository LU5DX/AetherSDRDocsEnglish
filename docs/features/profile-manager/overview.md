# Profile Manager overview

The Profile Manager lets you create, load, rename, and delete the three profile types stored on the FLEX-8600: Global, Transmit, and Microphone. Use it to save and restore complete radio states, switch between operating configurations, and control whether transmit changes are saved automatically.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager requires an active radio connection.
- The Profile Manager dialog remembers its size and position between sessions.

## How it works

Open the Profile Manager from `Profiles > Profile Manager...`. The dialog contains four tabs — **Global**, **Transmit**, **Microphone**, and **Auto-Save** — plus a **Close** button at the bottom.

**Global, Transmit, and Microphone tabs**

Each of these three tabs has the same layout:

- A **Profile name** text field at the top. Type a name here before saving or creating a new profile, or select an existing profile from the list to populate this field automatically.
- **Load**, **Save** (or **Create**), and **Delete** buttons. Load and Delete are disabled until you select a profile in the list. Selecting a profile also copies its name into the **Profile name** field.
- A **Profile list** showing all saved profiles for that category. The active profile is highlighted. Double-clicking a profile in the list loads it immediately, equivalent to selecting it and clicking **Load**.
- On the **Transmit** and **Microphone** tabs, an informational note below the buttons explains the autosave model for these profile types.

When you click **Save** on the **Global** tab, the radio saves the current state under the name in the **Profile name** field, overwriting an existing profile if one with that name already exists. If the field is empty, the currently selected profile name is used instead.

When you click **Create** on the **Transmit** or **Microphone** tab, the radio creates a new profile under the typed name. It cannot overwrite an existing transmit or microphone profile — if a profile with that name already exists, a dialog appears asking if you want to enable Auto-Save so your changes to the existing profile are captured automatically.

When you click **Delete**, a confirmation dialog appears before the profile is removed.

The profile list updates automatically when the radio reports a change, so additions or deletions made elsewhere are reflected without reopening the dialog.

**Auto-Save tab**

The Auto-Save tab contains a single checkbox and a short description. When **Auto-save profile changes** is checked, changes to TX and microphone settings are written back to the active profile automatically. This state is persisted as `AutoSaveTransmitProfile`. When unchecked, you must use **Save** or **Create** explicitly to preserve any changes.

The checkbox synchronizes automatically with the radio's auto-save state. Changes made from any source — the profile dialog's "Enable Auto-Save" confirmation, TCI clients, profile loads, or remote SmartSDR clients — are reflected in the checkbox without reopening the dialog.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| Global (tab) | Tab | Manages global profiles. | — |
| Transmit (tab) | Tab | Manages transmit profiles. | — |
| Microphone (tab) | Tab | Manages microphone profiles. | — |
| Auto-Save (tab) | Tab | Controls automatic profile saving. | — |
| Profile name | Text field | Name used when saving a new profile. Populated automatically when a profile is selected. | — |
| Profile list | List | All profiles for this category; active one highlighted. | — |
| Load | Button | Loads the selected profile onto the radio. Disabled when nothing is selected. | — |
| Save | Button | On the Global tab only. Saves the current radio state under the typed name, overwriting an existing profile if one with that name exists. | — |
| Create | Button | On the Transmit and Microphone tabs only. Creates a new profile under the typed name. Cannot overwrite an existing profile; if a name collision occurs, a dialog offers to enable Auto-Save. | — |
| Delete | Button | Deletes the selected profile after confirmation. Disabled when nothing is selected. | — |
| Auto-save profile changes | Checkbox | When enabled, TX and mic changes are written back to the active profile automatically. Synchronizes with the radio state from any source. | `AutoSaveTransmitProfile` |
| Close | Button | Closes the dialog. | — |

## Tips

- Double-clicking a profile in the list loads it immediately without needing to click **Load**.
- The **Profile name** field is filled in when you select a profile, so you can load or overwrite a profile without retyping its name.
- On the **Transmit** and **Microphone** tabs, the **Save** button is labelled **Create** because the radio cannot directly overwrite existing transmit or microphone profiles — changes are captured via Auto-Save while the profile is active.
- If you see a dialog when clicking **Create** on a transmit or microphone tab saying a profile already exists, you can click **Enable Auto-Save** to turn on automatic saving without switching to the **Auto-Save** tab.
- The Auto-Save checkbox updates automatically when auto-save is enabled or disabled by any means — a profile load, a TCI command, a remote client, or the confirmation dialog on the Transmit/Microphone tabs.

## Related

- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [Create a separate mic profile per microphone](create-a-separate-mic-profile-per-microphone.md)
- [Rename or delete a microphone profile](rename-or-delete-a-microphone-profile.md)
- [Review the list of active global profiles](review-the-list-of-active-global-profiles.md)