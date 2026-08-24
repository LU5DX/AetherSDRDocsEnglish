# CWX Panel

The CWX panel provides a complete CW operating interface. It allows you to type CW text, send it live character-by-character, store and send up to 12 F-key macros, control speed and QSK, and view a scrolling history of sent transmissions with visual feedback for aborted sends.

## Opening the CWX Panel

1. Ensure AetherSDR is connected to the radio.
2. Open the CWX panel from the main window menu or toolbar.

## Panel Views

The CWX panel has three views, selected by the buttons at the bottom of the panel:

- **Send (view)** — Shows the live send area with history and text field.
- **Live (view)** — Shows the live send view for character-by-character sending.
- **Setup (view)** — Shows the macro editor and QSK setup.

## Controls

### Speed

- **Control:** Speed spinbox
- **Setting key:** `CwxSpeedWpm`
- **Behavior:** Sets CW send speed in WPM.

### Send History

- **Control:** Send history scroll indicator
- **Behavior:** Shows previous send buffers with character highlighting. Each entry appears as a chat bubble with a timestamp.

### Send Text Area

- **Control:** Text field
- **Behavior:** Type CW characters. Press Enter to send the buffer.

### F1 through F12 Macros

- **Controls:** Push buttons (in Send and Live views) and text fields (in Setup view)
- **Setting key:** `CwxMacro_F1` through `CwxMacro_F12`
- **Behavior:** In Send and Live views, pressing an F-key sends the pre-written macro. In Setup view, the text fields allow editing the macro content.

### Delay

- **Control:** Spinbox
- **Setting key:** `CwxDelay`
- **Behavior:** Inter-macro delay in milliseconds.
- **Valid range:** 0 – 2000 ms
- **Default:** 5 ms

### QSK

- **Control:** Toggle button
- **Setting key:** `CwxQsk`
- **Behavior:** Enables QSK (full break-in).

### Prosigns Legend

- **Control:** Indicator
- **Behavior:** Shows shortcuts for common CW prosigns: `=`, `+`, `(`, `&`, `$`.

## Editing a CW Macro String

The CWX panel stores up to 12 macro strings, one for each function key F1 through F12. This section shows how to open the macro editor and change the text that is sent when you press a macro button.

### Before you start

- AetherSDR must be connected to the radio. The CWX panel requires an active radio connection.
- The TX slice must use a CW mode (CW, CWL, or CWU), or the CWX panel must already be open in the main window.

### Steps

1. In the CWX panel, click **Setup** in the bottom bar. The panel switches to the macro editor view.
2. Locate the row for the macro you want to change. Each row is labeled **F1** through **F12**.
3. Click inside the text field next to the function key label.
4. Edit the macro text. The field accepts plain text and prosign shortcuts. Refer to the Prosigns legend shown in the Setup view for the available shortcut characters (`=`, `+`, `(`, `&`, `$`).
5. Press Tab or click another field. The new text is saved immediately to the corresponding setting (`CwxMacro_F1` through `CwxMacro_F12`).

### Tips

- To send a macro immediately after editing, click **Send** in the bottom bar to return to the send view, then press the corresponding F-key.
- Pressing **Setup** while **Live** is active turns off live sending and returns to the send view before showing the macro editor. Any text already keyed character-by-character is not retransmitted.
- Pressing Escape aborts any in-progress CW transmission without affecting stored macro text.

## Function Key Shortcut Behavior

The CWX panel registers application-wide shortcuts for F1 through F12 and Escape. These shortcuts are enabled and disabled by the main window based on the TX slice's operating mode, not on panel visibility.

- When the TX slice uses a CW mode (CW, CWL, or CWU), the shortcuts are enabled.
- When the TX slice uses any other mode (such as SSB or AM for the DVK panel), the shortcuts are disabled.
- The shortcuts fire regardless of whether the CWX panel is visible, as long as the TX slice is in a CW mode.
- This prevents shortcut conflicts with the DVK panel, which registers its own set of F1 through F12 shortcuts for voice macros.

## Send and Live Interaction

- If **Live** is off when you click **Send**, the panel submits the typed buffer immediately.
- If **Live** is on when you click **Send**, the panel first turns off live sending and returns to the normal send view. The buffer is not retransmitted. This prevents characters that were already keyed live, one at a time, from being sent again.
- The **Live** button is a toggle. Its checked state reflects the live-sending state held by the radio model, so the button stays in sync if the state changes from outside the panel (for example, from a macro or a remote command).

## Context Menu on Send History Bubbles

Right-click any bubble in the send history scroll area to open a context menu with two options:

- **Resend** — Sends the entire text from that bubble again. The bubble reappears at the bottom of the history as a new entry with the current timestamp.
- **Clear History** — Removes all history bubbles from the scroll area. The spacer at the bottom of the history layout remains.

## Aborted Transmission Display

When you press Escape during a CW transmission, the bubble for that transmission in the send history scroll area shows a visual strikeout on the unsent portion of the text.

- The sent portion of the text appears in normal style.
- The unsent portion appears with a strikethrough line.

This makes it clear which characters were actually transmitted before the abort.

## Related

- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
- [Look up the prosign character shortcuts](look-up-the-prosign-character-shortcuts.md)
- [Change CW send speed in WPM](change-cw-send-speed-in-wpm.md)
- [Enable QSK full break-in](enable-qsk-full-break-in.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)