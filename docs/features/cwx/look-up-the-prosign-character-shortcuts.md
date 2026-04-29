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

## How Send and Live interact

In v0.9.2.1 the **Send** button behavior changed. Its action now depends on whether **Live** is currently on:

- **Live is off:** Clicking **Send** submits the current buffer immediately, exactly as in previous versions.
- **Live is on:** Clicking **Send** first turns Live mode off and returns the panel to the normal send view. The buffer is *not* re-transmitted. This prevents characters that were already keyed one-by-one in Live mode from being sent again.

The **Live** button is now a toggle. Clicking it a second time turns Live mode off without navigating away from the send view. The button state stays in sync with the model — if something outside the panel changes the Live state, the button updates to match.

Clicking **Setup** always turns Live mode off before showing the macro editor view.

## Tips

- Prosign shortcuts work in both the live send text area and in the F-key macro editors. Type them as you would any other character.
- To send a macro that contains a prosign, edit the macro string in the Setup view using the same shortcut characters, then trigger it with the corresponding F-key from the Send view.
- If you switch from Live mode to Send mode and want to transmit the buffer contents, turn Live off first (click **Live** to toggle it off), then click **Send**.

## Related

- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Edit a CW macro string](edit-a-cw-macro-string.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)