# Save the current radio state as a new global profile

Use this page to capture the radio's current state and store it as a named global profile. Global profiles record overall radio configuration so you can return to a known setup later.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- Decide on a name for the new profile before you begin.

## Steps

1. Click `Profiles > Profile Manager...` to open the Profile Manager dialog.
2. Click the `Global (tab)` tab if it is not already selected.
3. In the `Profile name` field, type the name for the new profile.
4. Click `Save`.

The radio saves the current state under the name you typed. The `Profile name` field clears, and the radio pushes an updated list back to the `Profile list`.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| `Profile name` | Text field | Name used when saving a new profile. If left blank when Save is clicked and a profile is selected in the list, the selected profile's name is used instead. | — |
| `Profile list` | List | Shows all existing global profiles. The active profile is highlighted. | — |
| `Load` | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. | — |
| `Save` | Button | Saves the current radio state under the name typed in `Profile name`. | — |
| `Delete` | Button | Deletes the selected profile after a confirmation prompt. Enabled only when a profile is selected. | — |
| `Close` | Button | Closes the Profile Manager dialog. | — |

## Tips

- Clicking an existing profile in the `Profile list` populates the `Profile name` field with that profile's name. If you then click `Save`, the existing profile is overwritten with the current radio state.
- You can also double-click a profile in the `Profile list` to load it immediately without clicking `Load`.
- The `Profile list` updates automatically when the radio confirms the save. You do not need to close and reopen the dialog to see the new entry.

## Troubleshooting

- **Save has no effect and the profile does not appear in the list** — Confirm the radio is connected. Profile Manager requires an active radio connection; if the connection dropped, reconnect via `Settings > Connect to Radio...` and try again.
- **Clicking Save with an empty `Profile name` field does nothing** — Either type a name in `Profile name` or select an existing profile in the `Profile list` first (its name will fill the field automatically).

## Related

- [Profile Manager overview](overview.md)
- [Review the list of active global profiles](review-the-list-of-active-global-profiles.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
