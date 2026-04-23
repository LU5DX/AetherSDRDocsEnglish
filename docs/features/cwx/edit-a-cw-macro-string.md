# Edit a CW macro string

The CWX panel stores up to 12 macro strings, one for each function key F1–F12. This page explains how to open the macro editor and write or change a macro string so it transmits the correct CW text when triggered.

## Before you start

- AetherSDR must be connected to a Flex radio. The CWX panel requires a radio connection.
- The active slice must be in CW, CWL, or CWU mode for the CWX panel to appear.

## Steps

1. Open the CWX panel. It appears in the main window central area when the active slice is in a CW mode.
2. Click **Setup** in the bottom bar of the CWX panel. The view switches to the macro editor.
3. Locate the macro slot you want to edit. Each slot is labeled **F1** through **F12** on the left side.
4. Click inside the text field to the right of the function key label for that slot.
5. Clear the existing text if needed, then type your new macro string.
6. Press Tab or click elsewhere. The new text is saved immediately to the corresponding setting key (`CwxMacro_F1` through `CwxMacro_F12`).

## What each control does

| Control | Behavior | Setting key | Default | Valid range |
|---|---|---|---|---|
| **F1** … **F12** macro editors | Text fields in the Setup view. Each holds the string sent when that function key is pressed or its macro button is clicked. | `CwxMacro_F1` … `CwxMacro_F12` | — | Any CW-legal text or prosign shortcut |
| **Delay:** | Inter-macro delay in milliseconds. | `CwxDelay` | 5 ms | 0–2000 ms |
| **QSK** | Enables QSK (full break-in) when checked. | `CwxQsk` | — | On / Off |
| **Speed:** | CW send speed in words per minute, applies to all macros. | `CwxSpeedWpm` | 20 WPM | 5–100 WPM |

## Tips

- The Prosigns legend displayed in the panel shows shortcut characters for common CW prosigns (such as `=`, `+`, `(`, `&`, `$`). Use these characters in your macro strings to send the corresponding prosigns.
- Pressing Escape aborts an in-progress CW transmission. This works even during a macro send.
- To test a macro after editing, click **Send** or **Live** in the bottom bar to leave the Setup view, then press the corresponding function key.

## Related

- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
- [Look up the prosign character shortcuts](look-up-the-prosign-character-shortcuts.md)
- [Change CW send speed in WPM](change-cw-send-speed-in-wpm.md)
- [Enable QSK full break-in](enable-qsk-full-break-in.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
