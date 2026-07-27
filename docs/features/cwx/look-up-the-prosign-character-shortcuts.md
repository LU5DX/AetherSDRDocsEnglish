# Look up the prosign character shortcuts

The CWX panel includes a built-in prosigns legend that shows which keyboard characters to type in order to send common CW prosigns. Use this reference when composing a typed buffer or writing a macro.

## Before you start

- AetherSDR must be connected to the radio.
- The CWX panel must be open. It appears automatically when the TX slice is in CW, CWL, or CWU mode.

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
| Speed: | Spinbox | CW speed in WPM. | `CwxSpeedWpm` |
| Delay: | Spinbox | Inter-macro delay. | `CwxDelay` |
| QSK | Toggle button | Enables QSK (full break-in). | `CwxQsk` |
| Send (view) | Push button | Shows the live send area with history and text field. | — |
| Live (view) | Push button | Shows the live send view. | — |
| Setup (view) | Push button | Shows the macro editor and QSK setup. | — |
| Send history scroll | Indicator | Shows previous send buffers with character highlighting. | — |
| F1 … F12 (macros) | Push buttons | Sends the pre-written macro for that function key. | `CwxMacro_F1` – `CwxMacro_F12` |

## How Send and Live interact

In v0.9.2.1 the **Send** button behavior changed. Its action now depends on whether **Live** is currently on:

- **Live is off:** Clicking **Send** submits the current buffer immediately, exactly as in previous versions.
- **Live is on:** Clicking **Send** first turns Live mode off and returns the panel to the normal send view. The buffer is *not* re-transmitted. This prevents characters that were already keyed one-by-one in Live mode from being sent again.

The **Live** button is now a toggle. Clicking it a second time turns Live mode off without navigating away from the send view. The button state stays in sync with the model — if something outside the panel changes the Live state, the button updates to match.

Clicking **Setup** always turns Live mode off before showing the macro editor view.

## Send history bubble actions

The send history scroll area displays each sent buffer as a bubble with a timestamp. You can interact with these bubbles using right-click:

- **Right-click a history bubble** to open a context menu with two options:
  - **Resend:** Sends the same text again as if you typed it fresh. The text appears as a new bubble in the history.
  - **Clear History:** Removes all history bubbles from the scroll area. This action cannot be undone.

## Aborting a transmission with Escape

Pressing **Escape** during a CW transmission aborts the sending process. When you abort a transmission:

- All unsent characters in the current buffer are displayed with strikethrough formatting in the history bubble.
- Characters that were already sent appear normally, without strikethrough.
- The bubble's timestamp shows when the transmission was started.

This visual distinction helps you identify which parts of a message were actually transmitted versus canceled mid-send.

## Keyboard shortcuts in the CWX panel

The CWX panel registers the F1 through F12 keys and the Escape key as application-wide shortcuts. The F1–F12 shortcuts are enabled or disabled based on the TX slice's mode, managed by MainWindow. They fire regardless of whether the CWX panel is visible, as long as the TX slice is in CW, CWL, or CWU mode. When the TX slice switches to a different mode (such as SSB), the shortcuts are automatically disabled to prevent conflicts with other panels like the DVK panel.

- **F1 – F12:** Sends the corresponding macro string.
- **Escape:** Aborts the current CW transmission. Unsent characters appear with strikethrough in the history bubble.

## Tips

- Prosign shortcuts work in both the live send text area and in the F-key macro editors. Type them as you would any other character.
- To send a macro that contains a prosign, edit the macro string in the Setup view using the same shortcut characters, then trigger it with the corresponding F-key from the Send view.
- If you switch from Live mode to Send mode and want to transmit the buffer contents, turn Live off first (click **Live** to toggle it off), then click **Send**.
- The F1–F12 keyboard shortcuts are active whenever the TX slice is in a CW mode, regardless of whether the CWX panel is visible. If you cannot trigger a macro with an F-key, check that the TX slice is in CW, CWL, or CWU mode.
- To resend a previous buffer, right-click the history bubble and select **Resend**. The original text is preserved and sent again as a new entry in the history.
- To clear the send history, right-click any bubble and select **Clear History**, or right-click the history area background if no bubbles are present.
- If you abort a transmission with Escape, the history bubble shows the unsent portion with strikethrough formatting for clear visual feedback.

## Related

- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Edit a CW macro string](edit-a-cw-macro-string.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)