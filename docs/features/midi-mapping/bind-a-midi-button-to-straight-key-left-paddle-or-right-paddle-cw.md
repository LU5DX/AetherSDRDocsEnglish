# Bind a MIDI Button to Straight Key, Left Paddle, or Right Paddle CW

Use this page to map a physical button on your MIDI controller to the straight key, left paddle, or right paddle CW inputs on your FLEX-8600. Once bound, pressing that button triggers the corresponding keying action as a momentary (gate) event.

## Before you start

- Your MIDI controller is connected to the computer and recognized by the operating system.
- AetherSDR was built with MIDI support (`HAVE_MIDI`).
- The MIDI Mapping dialog is not already in Learn mode from a previous session.

## Steps

1. Open `Settings > MIDI Mapping...`.
2. In the **Port:** combo box, select your MIDI controller from the list. If it does not appear, click Refresh.
3. Click Connect. The status indicator changes to show the port is open.
4. In the **Category** combo box, select `Phone/CW`.
5. In the **Parameter** combo box, select one of the following:
   - `Trigger straight key` — sends a straight key press
   - `Trigger CW Left Paddle` — sends a left paddle (dit) event
   - `Trigger CW Right Paddle` — sends a right paddle (dah) event
6. Click Learn. The button label changes to `Cancel Learn`.
7. Press and hold the physical button on your MIDI controller that you want to bind. AetherSDR detects the MIDI message and completes the binding automatically.
8. Confirm the new row appears in the Bindings table, showing the parameter name, MIDI Source, and Channel.
9. Repeat steps 5–8 for each additional CW input you want to bind.
10. Click Close.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| Port: | Combo box | Selects the MIDI input device | `MidiPort` |
| Refresh | Button | Rescans available MIDI ports | — |
| Connect | Button | Opens or closes the selected MIDI port | — |
| Auto-connect on startup | Checkbox | Reopens the MIDI port automatically on next launch | `MidiAutoConnect` |
| Category | Combo box | Filters the Parameter list; select `Phone/CW` for CW keying actions | — |
| Parameter | Combo box | Chooses the target action to bind; CW options are `Trigger straight key`, `Trigger CW Left Paddle`, `Trigger CW Right Paddle` | — |
| Learn | Button | Starts listening for the next MIDI message and binds it to the selected parameter; label becomes `Cancel Learn` while active | — |
| Bindings table | List | Shows all current bindings with per-row Invert, Relative, and delete controls | — |
| × (delete row) | Button | Removes that binding | — |
| Clear All | Button | Removes every binding | — |

## Tips

- These three CW actions are momentary (gate) type: the key is held for as long as the MIDI note or button remains active, then released. Use a pad or button that sends both Note On and Note Off messages for correct keying behavior.
- If you previously saved a mapping that used the legacy IDs `cw.key`, `cw.dit`, or `cw.dah`, AetherSDR migrates those automatically to the current IDs on load. No manual action is needed.
- Enable **Auto-connect on startup** so the port is ready the next time AetherSDR launches without requiring you to open this dialog.

## Troubleshooting

- **The `Phone/CW` category is missing from the Parameter list** — Confirm your build of AetherSDR is v0.9.7 or later. The three CW gate actions were added in that release.
- **Learn completes but the key does not fire when pressed** — Check that the port status shows the port is open (Connect was clicked and the status indicator confirms the connection). Also verify the MIDI controller is sending Note On/Off messages, visible in the Activity indicator.
- **The binding disappears after restarting AetherSDR** — The bindings are saved automatically when Learn completes. If the file was not written, check that AetherSDR has write permission to its settings directory.

## Related

- [Connect a MIDI controller](../../getting-started/setup/connect-a-midi-controller.md)
- [Record a new binding with Learn mode](record-a-new-binding-with-learn-mode.md)
- [Auto-connect MIDI controller on startup](../../getting-started/setup/auto-connect-midi-controller-on-startup.md)
- [Delete a binding](delete-a-binding.md)
- [Save the current mapping as a named profile](save-the-current-mapping-as-a-named-profile.md)
