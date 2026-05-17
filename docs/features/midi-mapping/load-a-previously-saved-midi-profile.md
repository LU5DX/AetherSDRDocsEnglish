# Load a previously saved MIDI profile

Loading a saved profile replaces the current bindings with those stored under that profile name, letting you switch between controller configurations without re-learning every binding.

## Before you start

- A MIDI profile must already exist. If you have not saved one yet, see [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md).
- Open the MIDI Controller Mapping dialog via `Settings > MIDI Mapping...`.

## Steps

1. In the **Profile:** combo box, select the name of the profile you want to load. If the list is empty, no profiles have been saved yet.
2. Click **Load**.

The current bindings are replaced with the bindings stored in the selected profile. The Bindings table updates immediately to show the loaded bindings.

## What each control does

| Control        | Kind      | Behavior                                                        |
|----------------|-----------|-----------------------------------------------------------------|
| Profile:       | Combo box | Picks a saved MIDI mapping profile to load or save. Editable.   |
| Load           | Button    | Replaces current bindings with those from the selected profile. |
| Bindings table | List      | Displays the bindings now active after the load.                |

## Category filter options

The **Category** combo box filters the **Parameter** list to show only controls from a specific group. Available categories:

- All
- RX
- TX
- Phone/CW
- EQ
- Global
- Mode
- Band
- Filter
- Slice
- Display
- Frequency

Selecting a category limits the **Parameter** combo box to entries in that group, making it easier to find the control you want to bind.

## Parameter options

The **Parameter** combo box contains all available parameters for binding. In v26.5.2.1, three new momentary (Gate) actions were added in the Phone/CW category:

- **Trigger straight key** (id: `cwkey`)
- **Trigger CW Left Paddle** (id: `cwdit`)
- **Trigger CW Right Paddle** (id: `cwdah`)

Legacy dotted IDs (`cw.key`, `cw.dit`, `cw.dah`) are automatically migrated to the new format when loading old profiles.

## Tips

- The **Profile:** combo box is editable. If you type a name that does not match a saved profile and click Load, nothing is loaded — no error is shown and the current bindings remain unchanged.
- After loading, the loaded bindings are immediately persisted as the active bindings. You do not need to click Save again to keep them active for the current session.

## Troubleshooting

- **Load is clicked but the Bindings table does not change** — The profile name in the **Profile:** combo box does not match any saved profile, or the name field is empty. Select a name from the dropdown list rather than typing it manually.
- **Profile: list is empty** — No profiles have been saved. See [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md).

## Related

- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [MIDI Controller Mapping overview](overview.md)