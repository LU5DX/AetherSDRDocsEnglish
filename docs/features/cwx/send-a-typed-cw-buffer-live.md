# Send a typed CW buffer live

The CWX panel lets you type a message and transmit it immediately in Morse code. Use this when you need to send free-form CW text that is not already stored in a macro.

## Before you start

- Connect to a FLEX-8600 radio. The CWX panel requires an active radio connection.
- Set the active slice to CW, CWL, or CWU mode. The CWX panel appears in the main window when a CW mode is active.

## Steps

1. Locate the CWX panel in the main window central area.
2. Click **Send** in the bottom bar to show the send view. The send history scroll and text entry area will be visible.
3. Click the **Send text area** (the text field at the bottom of the send view, showing the placeholder "Type CW message...").
4. Type your message. Use standard alphanumeric characters. Refer to the Prosigns legend in the panel for shortcuts to common CW prosigns.
5. Press **Enter** to transmit the buffer. The radio begins sending immediately. The sent text appears as a bubble in the send history scroll above.
6. To stop transmission at any time, press **Escape**. This clears the buffer and aborts the current send.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| **Send** | Shows the send view with history and text entry. | Active on open | — | — |
| **Live** | Shows the live send view. | — | — | — |
| **Setup** | Shows the macro editor and QSK controls. | — | — | — |
| **Speed:** | CW send speed in WPM. | 20 | 5–100 | `CwxSpeedWpm` |
| Send history scroll | Displays previously sent buffers with character highlighting. Scrolls upward as new buffers are sent. | — | — | — |
| Send text area | Text field where you type the CW message. Press Enter to send. | — | — | — |
| **Delay:** | Inter-macro delay in milliseconds. | 5 | 0–2000 | `CwxDelay` |
| **QSK** | Enables QSK full break-in. | Off | On/Off | `CwxQsk` |
| Prosigns legend | Displays shortcuts for common CW prosigns. | — | — | — |

## Tips

- Adjust **Speed:** in the bottom bar before or between sends. The `CwxSpeedWpm` value is persisted and restored on next launch.
- The send history scroll pushes older bubbles upward as you send more buffers, so recent transmissions remain visible at the bottom.
- Pressing **Escape** is safe even when the radio is idle — clearing an empty buffer has no effect.
- F1–F12 keyboard shortcuts trigger macros when the active slice is in CW or CWL mode. They do not interfere with typed text entry in the send text area.

## Troubleshooting

- **CWX panel does not appear** — Confirm the active slice is set to CW, CWL, or CWU mode, and that AetherSDR is connected to the radio.
- **Pressing Enter does nothing** — Click the send text area first to give it focus, then press Enter.
- **F-key presses fire macros instead of appearing as typed text** — F1–F12 are application-wide shortcuts when a CW mode slice is active. Type text using letter and number keys only; function keys are reserved for macros.

## Related

- [CWX overview](overview.md)
- [Change CW send speed in WPM](change-cw-send-speed-in-wpm.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
- [Edit a CW macro string](edit-a-cw-macro-string.md)
- [Enable QSK full break-in](enable-qsk-full-break-in.md)
- [Look up the prosign character shortcuts](look-up-the-prosign-character-shortcuts.md)
