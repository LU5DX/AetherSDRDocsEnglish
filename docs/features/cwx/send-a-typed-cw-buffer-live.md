# Send a typed CW buffer live

Use the CWX panel to type a CW message and transmit it immediately. This is the fastest way to send free-text CW without pre-writing a macro.

## Before you start

- Connect to a FLEX-8600 radio. The CWX panel requires an active radio connection.
- Set the active slice to CW, CWL, or CWU mode. The CWX panel appears in the main window when a CW mode slice is active.

## Steps

1. In the CWX panel, make sure **Live** is off. If **Live** is active (button checked), click it to toggle it off before typing a buffered message.
2. Click inside the **Send text area** — the text field at the bottom of the send view. The placeholder text reads "Type CW message...".
3. Type your message. Use standard ASCII characters. Refer to the prosign legend displayed in the panel for prosign shortcuts (=, +, (, &, $).
4. Click **Send** or press **Enter** to transmit the buffer. The radio begins sending immediately.
5. To abort transmission at any time, press **Escape**. This clears the buffer and stops the send. When aborted, the history bubble shows sent characters in normal text and unsent characters with strikeout formatting.

After transmission, the sent text appears in the **Send history scroll** area above the text field as a timestamped bubble.

## Resend or clear history

Right-click any history bubble to open a context menu with two options:

- **Resend** — Transmits the same text again. The text appears as a new timestamped bubble in the history.
- **Clear History** — Removes all history bubbles from the scroll area.

## How Send behaves depending on Live mode

The **Send** button behaves differently depending on whether **Live** is currently on:

- **Live is off** — Clicking **Send** submits the contents of the text field as a buffer and transmits it.
- **Live is on** — Clicking **Send** first turns **Live** off and returns the panel to the send view. The buffer is *not* retransmitted; this prevents text that was already keyed character-by-character in live mode from being sent a second time. After clicking **Send** in this state, type your message and click **Send** again to transmit.

## Aborted transmission visual indicators

When you press **Escape** during transmission, the history bubble shows which characters were sent and which were not:

- **Sent characters** — Appear in normal text.
- **Unsent characters** — Appear with strikeout formatting (crossed out). This provides clear visual feedback about exactly what was transmitted and what was aborted.

The strikeout formatting works correctly for single-line messages (callsigns, RST, serial numbers). For multi-line wrapped messages, the strikeout may not align perfectly on continuation lines.

## What each control does

| Control | What it does | Setting key |
|---|---|---|
| **Send** (view) | Shows the live send area with history and text field. | — |
| **Live** (view) | Shows the live send view. | — |
| **Setup** (view) | Shows the macro editor and QSK setup. | — |
| **Speed:** | Sets CW send speed in WPM. | `CwxSpeedWpm` |
| Send text area | Type your CW message here. Press Enter to send. | — |
| Send history scroll | Displays previous sent buffers with character highlighting. Read-only. Right-click a bubble for Resend or Clear History. | — |
| **F1 … F12** (macros) | Sends the pre-written macro for that function key. | `CwxMacro_F1..F12` |
| **F1 … F12** macro editors | Setup view editors for each macro. | `CwxMacro_F1..F12` |
| **Delay:** | Sets inter-macro delay in milliseconds. Available in Setup view. | `CwxDelay` |
| **QSK** | Enables QSK (full break-in). Available in Setup view. | `CwxQsk` |
| Prosigns legend | Shows character shortcuts for common CW prosigns (=, +, (, &, $). Read-only. | — |

## Keyboard shortcuts

F1–F12 and Escape shortcuts fire when a CW mode slice is active, regardless of whether the CWX panel is visible. This lets you trigger macros even when another panel is focused.

- **F1–F12** — Send the pre-written macro for that function key while a CW mode slice is active.
- **Escape** — Clears the buffer unconditionally and aborts any ongoing transmission. On an idle CWX panel it is a harmless no-op, so pressing it is always safe.

## Tips

- F1–F12 send pre-written macros while a CW mode slice is active. See [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md).
- Pressing **Escape** clears the buffer unconditionally. On an idle CWX panel it is a harmless no-op, so pressing it is always safe.
- Adjust **Speed:** in the bottom bar without switching views. The spinbox is visible in both the send and setup views.
- When you reconnect to a radio, the **Live** button reflects the radio's current live state automatically.
- Right-click a history bubble to resend past text or clear the entire history.

## Troubleshooting

- **CWX panel does not appear** — Confirm the active slice is set to CW, CWL, or CWU mode. The panel requires a CW mode slice and an active radio connection.
- **Clicking Send does not transmit** — If **Live** was on, the first click on **Send** only turns **Live** off. Click **Send** a second time (or press **Enter**) to transmit the buffer.
- **Pressing Enter does nothing** — Click inside the Send text area first to give it focus, then press Enter.
- **Escape does not stop transmission** — Escape fires an application-wide shortcut. If a dialog or text widget captures the key first, click away from it and press Escape again.
- **F1–F12 macros do not trigger** — Ensure the active slice is in CW, CWL, or CWU mode. The shortcuts are controlled by the active slice mode, not by panel visibility.
- **Aborted bubble shows no strikeout** — Verify you pressed Escape during active transmission. The strikeout only appears for text that was not yet sent when abort occurred.

## Related

- [CWX overview](overview.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
- [Edit a CW macro string](edit-a-cw-macro-string.md)
- [Change CW send speed in WPM](change-cw-send-speed-in-wpm.md)
- [Enable QSK full break-in](enable-qsk-full-break-in.md)
- [Look up the prosign character shortcuts](look-up-the-prosign-character-shortcuts.md)