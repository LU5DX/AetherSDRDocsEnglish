# Look up the prosign character shortcuts

The CWX panel includes a built-in prosigns legend so you can find the correct shortcut characters to type when composing CW messages or macros.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in CW, CWL, or CWU mode so the CWX panel is visible.

## Steps

1. Locate the CWX panel in the main window central area.
2. Click "Setup" at the bottom of the CWX panel.
3. Read the prosigns legend displayed in the Setup view. It shows the shortcut characters for common CW prosigns: `=`, `+`, `(`, `&`, and `$`.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| "Send" | Shows the live send area with history and text input field. | — |
| "Live" | Shows the live send view. | — |
| "Setup" | Shows the macro editor, QSK setup, and the prosigns legend. | — |
| Prosigns legend | Read-only display of shortcut characters for common CW prosigns (`=`, `+`, `(`, `&`, `$`). | — |
| Speed: | CW send speed in WPM. Valid range: 5–100 WPM. Default: 20 WPM. | `CwxSpeedWpm` |
| Delay: | Inter-macro delay in ms. Valid range: 0–2000 ms. Default: 5 ms. | `CwxDelay` |
| QSK | Enables QSK full break-in. | `CwxQsk` |
| F1 … F12 macro editors | Text fields for each macro in the Setup view. | `CwxMacro_F1` – `CwxMacro_F12` |

## Tips

- Use the prosign shortcut characters directly when typing in the send text area or when editing macro strings. For example, type `=` in your macro text where you want the BT prosign sent.
- The prosigns legend is always accessible in the Setup view without affecting any in-progress transmission.

## Related

- [CWX overview](overview.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Edit a CW macro string](edit-a-cw-macro-string.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
