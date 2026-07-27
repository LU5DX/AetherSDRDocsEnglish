# Create a separate mic profile per microphone

The Microphone tab in Profile Manager lets you save, load, and delete microphone profiles stored on the radio. By saving a named profile for each physical microphone, you can switch mic settings instantly without manually re-entering EQ, level, and processing values.

**Note:** For microphone profiles, the radio only supports creating new profiles — it cannot overwrite an existing mic profile directly. To update an existing profile with new settings, make that profile active and enable **Auto-Save** (see the steps below and the *Turn on auto-save* related article).

## Before you start

- AetherSDR must be connected to the radio. Profile Manager requires an active radio connection.
- Configure the radio's mic settings for the first microphone before saving. The profile captures the current state at the moment you click Create.

## Steps

1. Open `Profiles > Profile Manager...`.
2. Click the **Microphone** tab.
3. Set up your radio's microphone settings (level, EQ, processing) for the first microphone if you have not already done so.
4. Click in the **Profile name** field and type a name for this microphone — for example, `Desk Mic`.
5. Click **Create**. The profile appears in the **Profile list**.
6. Connect or select your second microphone and adjust the radio's mic settings to suit it.
7. Click in the **Profile name** field, clear any existing text, and type a name for the second microphone — for example, `Headset`.
8. Click **Create**. The second profile now appears in the **Profile list** alongside the first.
9. To switch between microphones in future sessions, select the profile name in the **Profile list** and click **Load**, or double-click the profile name.
10. Click **Close** when finished.

## What each control does

| Control              | Kind       | Behavior                                                                                                                                                                                                                                                |
|----------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Microphone (tab)** | Tab        | Shows mic profiles stored on the radio.                                                                                                                                                                                                                 |
| **Profile name**     | Text field | Name used when saving a new mic profile. Populated automatically when you select an item in the list. **Create** is disabled when the field is empty. Editing the field clears any result message shown below the buttons.                              |
| **Profile list**     | List       | All mic profiles on the radio; the active profile is highlighted.                                                                                                                                                                                       |
| **Load**             | Button     | Loads the selected profile onto the radio. Enabled only when a profile is selected. Double-clicking a profile also loads it.                                                                                                                            |
| **Create**           | Button     | Creates a new mic profile under the name in **Profile name**. Disabled when the **Profile name** field is empty. The radio does not support overwriting an existing mic profile — use Auto-Save to capture changes to an active profile.                |
| **Delete**           | Button     | Deletes the selected profile after confirmation. Enabled only when a profile is selected.                                                                                                                                                               |
| **Close**            | Button     | Closes the Profile Manager dialog.                                                                                                                                                                                                                      |

### Additional note (visible on the Microphone tab)

A label below the buttons reads:

> Updates to existing profiles save automatically — enable Auto-Save (Auto-Save tab) so changes follow the active profile. Create makes a new profile; it does not overwrite an existing one.

## Result messages

After clicking **Create**, a message line appears below the buttons indicating the outcome:

- **Success** — The profile was created on the radio. The message is shown in blue text.
- **Error** — The radio rejected the operation (for example, a duplicate name or a time-out). The message is shown in red text.
- **In progress** — While waiting for the radio to respond (maximum 15 seconds), a brief "creating…" message may appear.

The result line clears automatically when you start typing in the **Profile name** field, or when you load a different profile.

## Tips

- Selecting a profile in the **Profile list** copies its name into the **Profile name** field.
- The **Profile list** updates automatically when the radio reports a change, so a newly created profile appears without reopening the dialog.
- To keep mic settings for the active profile current without manual re-creation, enable **Auto-save profile changes** on the **Auto-Save** tab. See [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md) for details. Note that `AutoSaveTransmitProfile` applies to both TX and mic settings.

### If you try to create a profile with an existing name

If you type a name that already exists in the profile list and click **Create**, AetherSDR shows a prompt:

> A Mic profile named "Desk Mic" already exists.  
> The radio can't overwrite Mic profiles directly — updates are captured by Auto-Save while the profile is active. Auto-Save is currently OFF.  
> Would you like to enable Auto-Save now so your changes to "Desk Mic" are captured?

Click **Enable Auto-Save** to turn on auto-saving immediately, then make the existing profile active and apply your changes — they will be saved automatically. The Auto-Save checkbox on the **Auto-Save** tab stays in sync with the radio's auto-save state even if changes originate outside this dialog (for example, from another TCI client or a remote SmartSDR client).

## Troubleshooting

- **Load and Delete are greyed out** — No profile is selected in the **Profile list**. Click a profile name to select it.
- **Create is greyed out** — The **Profile name** field is empty. Type a name before clicking **Create**.
- **Create does nothing** — Both the **Profile name** field and the **Profile list** selection are empty. Type a name in **Profile name** before clicking **Create**.
- **Profile list is empty** — No microphone profiles have been saved on this radio yet. Follow the steps above to create the first one.
- **Error message appears after Create** — The radio may have rejected the operation. Check that the name is unique and that the radio connection is stable. If the error persists, try again; if the radio does not respond within 15 seconds, the dialog shows a time-out error.

## Related

- [Rename or delete a microphone profile](rename-or-delete-a-microphone-profile.md)
- [Turn on auto-save so TX tweaks always persist](turn-on-auto-save-so-tx-tweaks-always-persist.md)
- [Switch to a saved transmit profile](switch-to-a-saved-transmit-profile.md)