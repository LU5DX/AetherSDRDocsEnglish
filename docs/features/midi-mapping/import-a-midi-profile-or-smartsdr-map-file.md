# Import a MIDI profile or SmartSDR .map file

This page explains how to import a saved MIDI mapping profile into AetherSDR — either an AetherSDR profile XML file or a SmartSDR ".map" file — and apply it to your current MIDI controller setup.

## Before you start

- Have a MIDI controller connected to your radio (see [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)).
- Know which profile file you want to import — an AetherSDR profile XML or a SmartSDR .map file.

## Steps

1. Open the MIDI mapping dialog: **Settings > MIDI Mapping...**.
2. In the "Parameter Bindings" section, click **Import...**.
3. In the file dialog, locate and select your profile file (AetherSDR profile XML or SmartSDR .map file). The dialog starts in the last used import/export directory, or your Documents folder the first time.
4. Click **Open**. AetherSDR reads the file and reports how many bindings it imported.
5. In the **Profile:** combo box, select the imported profile.
6. Click **Load** to apply the imported bindings to your current mapping.

## What each control does

- **Import...** — Imports a profile file (AetherSDR profile XML or a SmartSDR .map file) into the profile store. New in v26.8.4.
- **Profile:** — Selects a saved MIDI mapping profile, including one you just imported.
- **Load** — Loads the currently selected profile into the active binding set.

The directory you last imported from or exported to is remembered and stored in the setting `MidiImportExportPath`.

## Tips

- After importing, click **Load** to make the imported bindings active. The import step alone only adds the profile to the store.
- You can import SmartSDR .map files directly — no conversion needed.

## Related

- [Overview](overview.md)
- [Export the current mapping as an AetherSDR profile XML](export-the-current-mapping-as-an-aethersdr-profile-xml.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Load a previously saved MIDI profile](load-a-previously-saved-midi-profile.md)
