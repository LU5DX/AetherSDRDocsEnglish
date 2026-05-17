# Profile Import/Export overview

The Profile Import/Export feature lets you save radio profiles (Global, Transmit, and Microphone) to files on your local machine and restore them later. This is useful for backing up your radio configuration, transferring settings between radios, or sharing profiles with other operators.

## Before you start

- A radio connection is required to export profiles from or import profiles to the radio.
- The feature requires AetherSDR v26.5.2.1 or later.

## How it works

The Profile Import/Export dialog has two tabs: **Export** and **Import**.

### Export tab

1. Open the dialog: **Profiles > Import/Export Profiles...**
2. Click the **Export** tab if not already selected.
3. Select the checkboxes next to the profiles you want to export.
4. Choose a file path using the file path chooser.
5. Click **Export** to save the selected profiles to the chosen file.

### Import tab

1. Open the dialog: **Profiles > Import/Export Profiles...**
2. Click the **Import** tab.
3. Browse for the profile file on your local machine — available files are shown.
4. Select which profiles to restore using the checkboxes.
5. Click **Import** to push the selected profiles to the radio.

## What each control does

| Control | Kind | Behavior | Notes |
|---------|------|----------|-------|
| **Export** (tab) | tab | Shows a list of radio profiles with checkboxes for selection and a file path chooser. Clicking **Export** saves the selected profiles to the chosen file. | New in v26.5.2.1. |
| **Import** (tab) | tab | Shows available profile files on the local machine. Select which profiles to restore and click **Import** to push them to the radio. | — |

## Related

- [Profile Manager](profile-manager.md) — view, create, edit, and delete transmit profiles
