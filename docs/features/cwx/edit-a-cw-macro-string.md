# Edit a CW macro string

The CWX panel stores up to 12 macro strings, one for each function key F1 through F12. This page shows how to open the macro editor and change the text that is sent when you press a macro button.

## Before you start

- AetherSDR must be connected to the radio. The CWX panel requires an active radio connection.
- The active slice must use CW, CWL, or CWU mode, or the CWX panel must already be open in the main window.

## Steps

1. In the CWX panel, click **Setup** in the bottom bar. The panel switches to the macro editor view.
2. Locate the row for the macro you want to change. Each row is labeled **F1** through **F12**.
3. Click inside the text field next to the function key label.
4. Edit the macro text. The field accepts plain text and prosign shortcuts. Refer to the Prosigns legend shown in the Setup view for the available shortcut characters (`=`, `+`, `(`, `&`, `$`).
5. Press Tab or click another field. The new text is saved immediately to the corresponding setting (`CwxMacro_F1` through `CwxMacro_F12`).

## What each control does

| Control | Behavior | Setting key | Default | Valid range |
|---|---|---|---|---|
| **F1** … **F12** macro text fields | Stores the CW text sent when that function key is pressed | `CwxMacro_F1` … `CwxMacro_F12` | — | Plain text with prosign shortcuts |
| **Delay:** | Inter-macro delay in milliseconds | `CwxDelay` | 5 ms | 0 – 2000 ms |
| **QSK** | Enables QSK (full break-in) | `CwxQsk` | — | On / Off |
| **Speed:** | CW send speed | `CwxSpeedWpm` | 20 WPM | 5 – 100 WPM |

## Tips

- To send a macro immediately after editing, click **Send** in the bottom bar to return to the send view, then press the corresponding F-key.
- Pressing **Setup** while **Live** is active turns off live sending and returns to the send view before showing the macro editor. Any text already keyed character-by-character is not retransmitted.
- Pressing Escape aborts any in-progress CW transmission without affecting stored macro text.

## How Send and Live interact (v0.9.2.1)

The behavior of the **Send** button changed in v0.9.2.1.

- If **Live** is **off** when you click **Send**, the panel submits the typed buffer immediately as before.
- If **Live** is **on** when you click **Send**, the panel first turns off live sending and returns to the normal send view. The buffer is **not** retransmitted. This prevents characters that were already keyed live, one at a time, from being sent again.

The **Live** button is now a toggle. Its checked state reflects the live-sending state held by the radio model, so the button stays in sync if the state changes from outside the panel (for example, from a macro or a remote command).

## Related

- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
- [Look up the prosign character shortcuts](look-up-the-prosign-character-shortcuts.md)
- [Change CW send speed in WPM](change-cw-send-speed-in-wpm.md)
- [Enable QSK full break-in](enable-qsk-full-break-in.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)