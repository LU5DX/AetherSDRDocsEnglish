# Invert a knob or treat it as an endless encoder

Once a MIDI binding exists, you can reverse its direction with Invert or switch it to relative mode so an endless encoder works correctly instead of jumping to absolute positions.

## Before you start

- A MIDI controller must be connected and at least one binding must already exist. See [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md) and [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md).
- Open `Settings > MIDI Mapping...` to reach the MIDI Controller Mapping dialog.

## Steps

1. Open `Settings > MIDI Mapping...`.
2. Locate the binding you want to change in the Bindings table.
3. To reverse the control direction, check the **Invert** checkbox in that binding's row.
4. To treat the control as an endless encoder, check the **Relative** checkbox in that binding's row.
5. Click **Close** to dismiss the dialog. Changes take effect immediately and are saved automatically.

## What each control does

| Control | Where | What it does |
|---|---|---|
| Invert | Bindings table, per row | Reverses the direction of the MIDI control for that binding. |
| Relative | Bindings table, per row | Treats the control as an endless encoder rather than an absolute position source. |

## Tips

- Invert and Relative are independent. You can enable both on the same binding — for example, a reversed endless encoder.
- If a knob sends CC values in the range 0–127 and you notice it always snaps to a fixed position when you turn it, the control is likely sending absolute values. Enable Relative to fix this.
- Changes to Invert and Relative are persisted immediately when Learn completes or when the dialog saves bindings. You do not need to use Save under Profile: to preserve these per-binding flags, but saving a named profile will capture them.

## Troubleshooting

- **Invert or Relative checkboxes are not visible** — The Bindings table is empty. You must record at least one binding first. See [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md).
- **Enabling Relative has no effect on the hardware knob behavior** — The connected controller may be sending absolute CC values (0–127) rather than relative/signed values. Relative mode in AetherSDR expects the controller itself to be configured for relative encoding. Check your controller's own settings or documentation.

## Related

- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [Delete a binding](delete-a-binding.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
