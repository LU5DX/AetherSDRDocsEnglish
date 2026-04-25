# Create a separate mic profile per microphone

Use the Profile Manager to save a dedicated microphone profile for each physical microphone you use. Switching microphones then takes one load action instead of manually adjusting mic settings each time.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- Configure the radio's mic settings (gain, EQ, etc.) for the microphone you want to save before opening the dialog.

## Steps

1. Open `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. In the **Profile name** field, type a name that identifies the microphone (for example, `Heil PR-40` or `Desk Mic`).
4. Click **Save**. The profile appears in the **Profile list**.
5. Repeat steps 3–4 for each additional microphone, adjusting the radio's mic settings before each save.
6. To switch to a saved microphone profile, select it in the **Profile list** and click **Load**, or double-click its entry in the list.
7. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Microphone** (tab) | Tab | Shows mic profiles stored on the radio. | — |
| **Profile name** | Text field | Name used when saving a new mic profile. Select an existing profile to populate this field automatically. | — |
| **Profile list** | List | All mic profiles on the radio; the currently active one is highlighted. | — |
| **Load** | Button | Loads the selected profile onto the radio. Also activated by double-clicking a list entry. Enabled only when a profile is selected. | — |
| **Save** | Button | Saves the current radio mic state under the name in **Profile name**. If **Profile name** is empty and a profile is selected, saves under that profile's name. | — |
| **Delete** | Button | Deletes the selected profile after confirmation. Enabled only when a profile is selected. | — |
| **Close** | Button | Closes the dialog. | — |

## Tips

- When you select a profile in the **Profile list**, its name appears automatically in the **Profile name** field. Edit the text before clicking **Save** to save a copy under a new name without overwriting the original.
- If you want mic changes to be written back to the active profile automatically whenever you adjust them, enable **Auto-save profile changes** on the **Auto-Save** tab. This is controlled by the `AutoSaveTransmitProfile` setting.

## Troubleshooting

- **Load and Delete are greyed out** — no profile is selected in the **Profile list**. Click a profile name to select it.
- **Save does nothing** — both the **Profile name** field is empty and no profile is selected. Type a name in **Profile name** and click **Save** again.
- **Profile list is empty after saving** — the radio pushes the updated list back via status. If the list does not refresh, close and reopen the dialog to force a re-query.

## Related

- [Profile Manager overview](overview.md)
- [Rename or delete a microphone profile](rename-or-delete-a-microphone-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
