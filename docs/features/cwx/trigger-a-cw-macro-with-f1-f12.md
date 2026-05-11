# Trigger a CW macro with F1–F12

Press a function key to send a pre-written CW macro string through the radio without typing. This is useful for contest exchanges, CQ calls, or any text you send repeatedly.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in CW or CWL mode. Function keys F1–F12 are silently ignored in all other modes.
- Each macro must have text stored in its slot. See [Edit a CW macro string](edit-a-cw-macro-string.md) if the slots are empty.

## Steps

1. Open the CWX panel. It appears automatically when the active slice is in CW or CWL mode.
2. Press the function key (F1 through F12) on your keyboard that corresponds to the macro you want to send. The macro fires immediately.
3. To stop transmission mid-send, press Escape. This clears the send buffer and halts output.

To send a macro using the on-screen buttons instead of the keyboard:

1. Click **Setup** in the bottom bar of the CWX panel.
2. Click the **F1** through **F12** button next to the macro you want to send.

## What each control does

| Control | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|
| F1 … F12 (keyboard) | Sends the macro stored for that function key. Only active when the CWX panel is visible and the slice mode is CW or CWL. | — | — | `CwxMacro_F1` … `CwxMacro_F12` |
| F1 … F12 (on-screen buttons) | Same as the keyboard keys; sends the corresponding macro. | — | — | `CwxMacro_F1` … `CwxMacro_F12` |
| Speed: | CW send speed in WPM, applied to all macro sends. | 20 WPM | 5–100 WPM | `CwxSpeedWpm` |
| Delay: | Inter-macro delay in milliseconds. | 5 ms | 0–2000 ms | `CwxDelay` |
| QSK | Enables full break-in (QSK) mode. | Off | On / Off | `CwxQsk` |

## How Send and Live interact

The **Send** button behavior changed in v0.9.2.1. Its action now depends on whether **Live** mode is currently active:

- **Live is off** — Clicking **Send** submits the contents of the send text area immediately, exactly as pressing Enter does.
- **Live is on** — Clicking **Send** first turns off Live mode and returns the panel to the normal send view. The buffer is **not** retransmitted. This prevents text that was already keyed character-by-character in Live mode from being sent a second time.

The **Live** button is now a toggle. Clicking it again while Live is active turns Live mode off. When a connected model changes the live state externally (for example, from another panel or a radio event), the **Live** button updates automatically to reflect the current state.

Clicking **Setup** always turns off Live mode before showing the macro editor view.

## Tips

- The F1–F12 shortcuts are application-wide. They work only when the CWX panel is visible. If you switch to another panel that also uses F1–F12 (such as the DVK panel), the shortcuts are disabled to avoid ambiguity.
- Pressing Escape during a macro send is the fastest way to abort. Because the radio transitions between transmit and ready states rapidly during CW, Escape works regardless of the radio's current transmit state.
- Adjust **Speed:** in the bottom bar before sending if you need to change the WPM for the current session.
- If you were sending live and want to re-send the same text, type it again in the send text area after clicking **Send** to exit Live mode, then click **Send** a second time (or press Enter).

## Troubleshooting

- **Pressing F1–F12 does nothing** — Confirm the active slice is in CW or CWL mode and the CWX panel is visible. The shortcuts are disabled when the panel is hidden or another panel using F1–F12 is visible. If another application has captured the function keys, bring AetherSDR to the foreground.
- **Macro sends but produces no audio or RF** — The macro text for that slot may be empty. Click **Setup** and check the text field next to the F-key in question. See [Edit a CW macro string](edit-a-cw-macro-string.md).
- **Transmission does not stop after pressing Escape** — Click inside the AetherSDR window to ensure it has keyboard focus, then press Escape again.
- **Clicked Send but the buffer was not transmitted** — If Live mode was active when you clicked **Send**, the panel exits Live mode without sending. Click **Send** once more (or press Enter) to transmit the buffer.

## Related

- [Edit a CW macro string](edit-a-cw-macro-string.md)
- [Change CW send speed in WPM](change-cw-send-speed-in-wpm.md)
- [Enable QSK full break-in](enable-qsk-full-break-in.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)