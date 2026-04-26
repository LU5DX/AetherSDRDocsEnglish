# Look up the prosign character shortcuts

The CWX panel includes a built-in prosigns legend that shows which keyboard characters to type in order to send common CW prosigns. Use this reference when composing a typed buffer or writing a macro.

## Before you start

- AetherSDR must be connected to the radio.
- The CWX panel must be open. It appears automatically when the active slice is in CW, CWL, or CWU mode.

## Steps

1. In the CWX panel, click **Setup** in the bottom bar.
2. Locate the prosigns legend displayed in the Setup view. It is a read-only indicator — no interaction is required.
3. Note the character shortcuts shown (=, +, (, &, $) and use them when typing in the send text area or editing a macro.

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| Prosigns legend | Indicator (read-only) | Displays the keyboard shortcuts for common CW prosigns: `=`, `+`, `(`, `&`, `$`. | — |
| Send text area | Text field | Type your CW message here, using prosign shortcuts where needed. Press Enter to send. | — |
| F1 … F12 macro editors | Text fields | Enter prosign shortcuts directly into macro text in the Setup view. | `CwxMacro_F1` – `CwxMacro_F12` |

## Tips

- Prosign shortcuts work in both the live send text area and in the F-key macro editors. Type them as you would any other character.
- To send a macro that contains a prosign, edit the macro string in the Setup view using the same shortcut characters, then trigger it with the corresponding F-key from the Send view.

## Related

- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Edit a CW macro string](edit-a-cw-macro-string.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
