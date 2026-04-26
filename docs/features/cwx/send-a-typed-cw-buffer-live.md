# Send a typed CW buffer live

Use the CWX panel to type a CW message and transmit it immediately. This is the fastest way to send free-text CW without pre-writing a macro.

## Before you start

- Connect to a FLEX-8600 radio. The CWX panel requires an active radio connection.
- Set the active slice to CW, CWL, or CWU mode. The CWX panel appears in the main window when a CW mode slice is active.

## Steps

1. In the CWX panel, click **Send** to make sure the send view is active. The **Send** button is in the bottom bar of the panel.
2. Click inside the **Send text area** — the text field at the bottom of the send view. The placeholder text reads "Type CW message...".
3. Type your message. Use standard ASCII characters. Refer to the prosign legend displayed in the panel for prosign shortcuts (=, +, (, &, $).
4. Press **Enter** to transmit the buffer. The radio begins sending immediately.
5. To abort transmission at any time, press **Escape**. This clears the buffer and stops the send.

After transmission, the sent text appears in the **Send history scroll** area above the text field as a timestamped bubble.

## What each control does

| Control | What it does | Setting key |
|---|---|---|
| **Send** | Switches to the send view showing the history and text field. | — |
| **Live** | Switches to the live send view. | — |
| **Setup** | Switches to the macro editor and QSK setup view. | — |
| **Speed:** | Sets CW send speed in WPM. Range: 5–100 WPM. Default: 20 WPM. | `CwxSpeedWpm` |
| Send text area | Type your CW message here. Press Enter to send. | — |
| Send history scroll | Displays previous sent buffers with timestamps. Read-only. | — |
| **Delay:** | Sets inter-macro delay in milliseconds. Range: 0–2000 ms. Default: 5 ms. Available in Setup view. | `CwxDelay` |
| **QSK** | Enables QSK (full break-in). Available in Setup view. | `CwxQsk` |
| Prosigns legend | Shows character shortcuts for common CW prosigns. Read-only. | — |

## Tips

- F1–F12 send pre-written macros while a CW mode slice is active. The keyboard shortcuts work application-wide in CW and CWL modes. See [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md).
- Pressing **Escape** clears the buffer unconditionally. On an idle CWX panel it is a harmless no-op, so pressing it is always safe.
- Adjust **Speed:** in the bottom bar without switching views. The spinbox is visible in both the send and setup views.

## Troubleshooting

- **CWX panel does not appear** — Confirm the active slice is set to CW, CWL, or CWU mode. The panel requires a CW mode slice and an active radio connection.
- **Pressing Enter does nothing** — Click inside the Send text area first to give it focus, then press Enter.
- **Escape does not stop transmission** — Escape fires an application-wide shortcut. If a dialog or text widget captures the key first, click away from it and press Escape again.

## Related

- [CWX overview](overview.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
- [Edit a CW macro string](edit-a-cw-macro-string.md)
- [Change CW send speed in WPM](change-cw-send-speed-in-wpm.md)
- [Enable QSK full break-in](enable-qsk-full-break-in.md)
- [Look up the prosign character shortcuts](look-up-the-prosign-character-shortcuts.md)
