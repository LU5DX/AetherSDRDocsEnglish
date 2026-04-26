# Load a previously saved MIDI profile

Loading a saved profile replaces the current bindings with those stored under that profile name, letting you switch between controller configurations without re-learning every binding.

## Before you start

- A MIDI profile must already exist. If you have not saved one yet, see [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md).
- Open the MIDI Controller Mapping dialog via `Settings > MIDI Mapping...`.

## Steps

1. In the **Profile:** combo box, select the name of the profile you want to load. If the list is empty, no profiles have been saved yet.
2. Click Load.

The current bindings are replaced with the bindings stored in the selected profile. The Bindings table updates immediately to show the loaded bindings.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| Profile: | Combo box | Picks a saved MIDI mapping profile to load or save. Editable. | — |
| Load | Button | Replaces current bindings with those from the selected profile. | — |
| Bindings table | List | Displays the bindings now active after the load. | — |

## Tips

- The Profile: combo box is editable. If you type a name that does not match a saved profile and click Load, nothing is loaded — no error is shown and the current bindings remain unchanged.
- After loading, the loaded bindings are immediately persisted as the active bindings. You do not need to click Save again to keep them active for the current session.

## Troubleshooting

- **Load is clicked but the Bindings table does not change** — The profile name in the Profile: combo box does not match any saved profile, or the name field is empty. Select a name from the dropdown list rather than typing it manually.
- **Profile: list is empty** — No profiles have been saved. See [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md).

## Related

- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [MIDI Controller Mapping overview](overview.md)
