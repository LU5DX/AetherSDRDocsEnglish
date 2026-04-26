# Invert a knob or treat it as an endless encoder

After creating a MIDI binding, you can reverse its direction with Invert or tell AetherSDR to treat the control as an endless encoder with Relative. Both options are set per binding in the Bindings table.

## Before you start

- A MIDI controller must be connected and at least one binding must already exist. See [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md) and [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md).
- Open `Settings > MIDI Mapping...` to reach the MIDI Controller Mapping dialog.

## Steps

1. Open `Settings > MIDI Mapping...`.
2. Locate the binding you want to change in the Bindings table.
3. To reverse the control direction, check the Invert checkbox in that binding's row.
4. To treat the control as an endless encoder, check the Relative checkbox in that binding's row.
5. Either checkbox can be checked or unchecked independently. Changes take effect immediately.
6. Click Close when finished.

## What each control does

| Control | Column in Bindings table | Behavior | Default |
|---|---|---|---|
| Invert | Invert | Reverses the direction of the control for that binding. Turn clockwise to decrease, counter-clockwise to increase, or vice versa. | Unchecked |
| Relative | Relative | Treats the control as an endless encoder. Use this when your hardware knob sends incremental (relative) values rather than absolute positions (0–127). | Unchecked |

## Tips

- Use Relative when your knob sends small increment/decrement values rather than an absolute position. If a knob jumps erratically when turned, enabling Relative usually corrects it.
- Invert and Relative can be combined on the same binding. For example, a Relative encoder that increments in the wrong direction can have both options checked.
- Changes to Invert and Relative are saved automatically when you save a profile. Use Save under Profile: to preserve them.

## Troubleshooting

- **Checking Relative makes a knob stop responding** — The knob may be sending absolute values (0–127). Uncheck Relative and leave the binding in absolute mode.
- **Control still moves in the wrong direction after checking Invert** — Confirm you checked Invert on the correct row. Each binding row has its own Invert checkbox; scroll horizontally if the column is not visible.

## Related

- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Delete a binding](delete-a-binding.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
