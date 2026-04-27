# Create a separate mic profile per microphone

The Microphone tab in Profile Manager lets you save, load, and delete microphone profiles stored on the radio. By saving a named profile for each physical microphone, you can switch mic settings instantly without manually re-entering EQ, level, and processing values.

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- Configure the radio's mic settings for the first microphone before saving. The profile captures the current state at the moment you click Save.

## Steps

1. Open `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. Set up your radio's microphone settings (level, EQ, processing) for the first microphone if you have not already done so.
4. Click in the **Profile name** field and type a name for this microphone — for example, `Desk Mic`.
5. Click **Save**. The profile appears in the **Profile list**.
6. Connect or select your second microphone and adjust the radio's mic settings to suit it.
7. Click in the **Profile name** field, clear any existing text, and type a name for the second microphone — for example, `Headset`.
8. Click **Save**. The second profile now appears in the **Profile list** alongside the first.
9. To switch between microphones in future sessions, select the profile name in the **Profile list** and click **Load**, or double-click the profile name.
10. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Microphone (tab)** | Tab | Shows mic profiles stored on the radio. | — |
| **Profile name** | Text field | Name used when saving a new mic profile. Populated automatically when you select an item in the list. | — |
| **Profile list** | List | All mic profiles on the radio; the active profile is highlighted. | — |
| **Load** | Button | Loads the selected profile onto the radio. Enabled only when a profile is selected. | — |
| **Save** | Button | Saves the current radio mic state under the name in **Profile name**. If **Profile name** is empty, uses the selected list item's name. | — |
| **Delete** | Button | Deletes the selected profile after confirmation. Enabled only when a profile is selected. | — |
| **Close** | Button | Closes the Profile Manager dialog. | — |

## Tips

- Selecting a profile in the **Profile list** copies its name into the **Profile name** field. If you want to overwrite an existing profile with updated settings, simply select it and click **Save** without changing the name.
- The **Profile list** updates automatically when the radio reports a change, so a newly saved profile appears without reopening the dialog.
- To keep mic settings for the active profile current without manual saves, enable **Auto-save profile changes** on the **Auto-Save** tab. See [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md) for details. Note that `AutoSaveTransmitProfile` applies to both TX and mic settings.

## Troubleshooting

- **Load and Delete are greyed out** — No profile is selected in the **Profile list**. Click a profile name to select it.
- **Save does nothing** — Both the **Profile name** field and the **Profile list** selection are empty. Type a name in **Profile name** before clicking **Save**.
- **Profile list is empty** — No microphone profiles have been saved on this radio yet. Follow the steps above to create the first one.

## Related

- [Rename or delete a microphone profile](rename-or-delete-a-microphone-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)
