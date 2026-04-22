# Load a previously saved MIDI profile

Load a named MIDI mapping profile to restore a complete set of bindings you saved earlier. This is useful when switching between controllers or operating positions.

## Before you start

- At least one profile must already exist. If you have not yet saved a profile, see [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md).
- Open the MIDI Controller Mapping dialog via `Settings > MIDI Mapping...`.

## Steps

1. In the **Profile:** combo box, select the name of the profile you want to load. If the list is empty, no profiles have been saved yet.
2. Click **Load**.

The existing bindings are cleared and replaced with the bindings stored in the selected profile. The bindings table updates immediately to reflect the loaded profile.

## Tips

- Loading a profile overwrites all current bindings without a confirmation prompt. If you want to keep your current bindings, save them as a profile first before loading another.
- The **Profile:** combo box is editable. Type a name or select one from the drop-down list.

## Troubleshooting

- **Clicking Load does nothing** — The **Profile:** field may be empty or contain only whitespace. Select a profile name from the drop-down list before clicking Load.
- **The Profile: list is empty** — No profiles have been saved yet. See [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md).
- **Bindings table is empty after loading** — The selected profile was saved with no bindings, or the profile data could not be read. Save a new profile with the correct bindings and try again.

## Related

- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Delete a binding](delete-a-binding.md)
- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
