# Save the current mapping as a named profile

Save your current MIDI bindings under a name so you can reload them later. This is useful when you switch between controllers or want to keep separate mappings for different operating modes.

## Before you start

- Open the MIDI Controller Mapping dialog via `Settings > MIDI Mapping...`.
- Have at least one binding in the Bindings table. Saving an empty mapping is allowed but rarely useful.

## Steps

1. In the **Profile:** combo box, type a name for the profile. The combo box is editable — click it and type directly.
2. Click Save.

The profile is stored immediately. The **Profile:** combo box is refreshed and the new name appears in the list.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| Profile: | Combo box (editable) | Type a new name or select an existing one. Accepts free-form text. | — |
| Save | Push button | Saves the current bindings under the name shown in **Profile:**. If a profile with that name already exists, it is overwritten. | — |
| Load | Push button | Loads the bindings from the profile selected in **Profile:**. Replaces all current bindings. | — |

## Tips

- Profile names are trimmed of leading and trailing spaces before saving. A name that is empty or whitespace-only will not be saved.
- To overwrite an existing profile, select its name from the **Profile:** combo box and click Save again.

## Troubleshooting

- **Clicking Save does nothing** — The **Profile:** field is blank or contains only spaces. Type a name before clicking Save.
- **A profile name you typed is not in the list after saving** — The name may have been whitespace-only. Confirm the field shows visible characters, then click Save again.

## Related

- [Load a previously saved MIDI profile](load-a-previously-saved-midi-profile.md)
- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Delete a binding](delete-a-binding.md)
- [MIDI Controller Mapping overview](overview.md)
