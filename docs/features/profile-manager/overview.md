# Profile Manager overview

The Profile Manager lets you create, load, rename, and delete Global, Transmit, and Microphone profiles stored on the radio. Use it to save and recall complete radio states without reconfiguring settings by hand.

## Before you start

- AetherSDR must be connected to the radio. The Profile Manager is unavailable when disconnected.

## How it works

Open the Profile Manager from `Profiles > Profile Manager...`. The dialog contains four tabs — **Global**, **Transmit**, **Microphone**, and **Auto-Save** — each covering a separate profile category.

**Global, Transmit, and Microphone tabs** share the same layout:

- Type a name in **Profile name** to identify a new profile before saving, or select an existing entry in **Profile list** to fill the field automatically.
- The **Profile list** shows all profiles in that category. The currently active profile is highlighted.
- Click **Load** (or double-click a list entry) to apply the selected profile to the radio immediately.
- Click **Save** to write the radio's current state under the name shown in **Profile name**. If the name matches an existing profile, that profile is overwritten.
- Click **Delete** to remove the selected profile. A confirmation prompt appears before the profile is deleted.

**Auto-Save tab** controls whether transmit and microphone changes accumulate automatically:

- When **Auto-save profile changes** is checked, any change to TX or mic settings is written back to the active profile without a manual Save. This setting is stored as `AutoSaveTransmitProfile`.

Click **Close** to dismiss the dialog. Any changes already sent to the radio remain in effect.

## What each control does

| Control | Where | Behavior | Setting key |
|---|---|---|---|
| Global (tab) | Tab bar | Switches to global profile management. | — |
| Transmit (tab) | Tab bar | Switches to transmit profile management. | — |
| Microphone (tab) | Tab bar | Switches to microphone profile management. | — |
| Auto-Save (tab) | Tab bar | Switches to auto-save configuration. | — |
| Profile name | Global / Transmit / Microphone tabs | Name used when creating or overwriting a profile. Populated automatically when you select a list entry. | — |
| Profile list | Global / Transmit / Microphone tabs | All profiles for the active category. Active profile is highlighted. | — |
| Load | Global / Transmit / Microphone tabs | Applies the selected profile to the radio. Also triggered by double-clicking a list entry. | — |
| Save | Global / Transmit / Microphone tabs | Saves current radio state under the name in Profile name. | — |
| Delete | Global / Transmit / Microphone tabs | Deletes the selected profile after confirmation. | — |
| Auto-save profile changes | Auto-Save tab | When enabled, TX and mic changes are written back to the active profile automatically. | `AutoSaveTransmitProfile` |
| Close | Bottom of dialog | Closes the dialog. | — |

## Tips

- Load and Delete are disabled until you select a profile from the list. Select an entry first.
- The Profile list updates automatically if the radio reports a change while the dialog is open — you do not need to close and reopen it.
- The dynamic list under `Profiles >` in the menu bar shows active global profiles and lets you load them without opening the Profile Manager.

## Related

- [Save the current radio state as a new global profile](save-the-current-radio-state-as-a-new-global-profile.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [Create a separate mic profile per microphone](create-a-separate-mic-profile-per-microphone.md)
- [Rename or delete a microphone profile](rename-or-delete-a-microphone-profile.md)
- [Review the list of active global profiles](review-the-list-of-active-global-profiles.md)
