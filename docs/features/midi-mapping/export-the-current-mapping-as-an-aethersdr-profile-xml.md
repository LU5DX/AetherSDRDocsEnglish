# Export the current mapping as an AetherSDR profile XML

This page shows you how to save your current MIDI bindings as an AetherSDR profile XML file that you can share or back up.

## Before you start

- Open the MIDI Controller Mapping dialog via `Settings > MIDI Mapping...`.
- Have at least one MIDI binding configured. If your bindings table is empty, export will produce a profile with no bindings.

## Steps

1. Click **Export...**.
2. In the file dialog, choose where to save the profile XML file.
3. Enter a filename and click Save.

The dialog reports how many bindings were exported. The remembered directory is stored under `MidiImportExportPath` and will be used the next time you open the Export or Import file dialog.

## What each control does

| Control | Behavior | Persisted setting |
|---|---|---|
| **Export...** | Exports the current bindings as an AetherSDR profile XML file. | `MidiImportExportPath` (remembered directory) |

## Tips

- The exported file is plain XML, so you can open it in any text editor to inspect or transfer bindings manually.
- AetherSDR can also import a SmartSDR `.map` file if you are migrating from a FlexRadio setup — use **Import...** in the same dialog.

## Related

- [Import a MIDI profile or SmartSDR .map file](import-a-midi-profile-or-smartsdr-map-file.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Load a previously saved MIDI profile](load-a-previously-saved-midi-profile.md)
- [MIDI Controller Mapping overview](overview.md)
