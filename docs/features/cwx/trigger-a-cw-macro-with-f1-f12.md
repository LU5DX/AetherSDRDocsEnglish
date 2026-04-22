# Trigger a CW macro with F1–F12

Press a function key to send a pre-written CW string without typing. Each of the twelve F-key slots holds one macro; pressing the key transmits that macro at the current speed.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in CW or CWL mode. Function key macros do not fire in other modes.
- Each macro slot must contain text. See [Edit a CW macro string](edit-a-cw-macro-string.md) if the slots are empty.

## Steps

1. Open the CWX panel. It appears in the main window area when the active slice is in CW or CWL mode.
2. Press **F1** through **F12** on the keyboard. AetherSDR sends the macro stored in the corresponding slot at the speed shown in **Speed:**.
3. To stop transmission early, press **Escape**. This clears the send buffer immediately.

## What each control does

| Control | Behavior | Setting key | Default | Valid range |
|---|---|---|---|---|
| **F1** … **F12** (macro buttons) | Clicking a button in the CWX panel sends that macro. Pressing the matching function key on the keyboard does the same. | `CwxMacro_F1` … `CwxMacro_F12` | *(empty)* | Any CW-encodable text or prosigns |
| **Speed:** | CW send speed in WPM, applied to all macro transmissions. | `CwxSpeedWpm` | 20 WPM | 5–100 WPM |
| **Delay:** | Inter-macro delay in milliseconds. | `CwxDelay` | 5 ms | 0–2000 ms |
| **QSK** | Enables QSK full break-in. | `CwxQsk` | off | on / off |

## Tips

- The F-key shortcuts are application-wide. The CWX panel does not need to be focused for the keys to fire, but the active slice must be in CW or CWL mode.
- Pressing **Escape** during a macro transmission clears the buffer. Because the radio alternates between transmitting and ready during each dit and dah, the abort takes effect at the next gap — typically within one element.
- You can also click the **F1** … **F12** buttons inside the CWX panel directly instead of using the keyboard.

## Troubleshooting

- **Pressing F1–F12 does nothing** — Confirm the active slice is in CW or CWL mode. The macros are suppressed in all other modes (SSB, AM, FM, etc.).
- **Macro fires but transmits nothing** — The macro slot is empty. Open the Setup view and enter text in the corresponding macro editor. See [Edit a CW macro string](edit-a-cw-macro-string.md).
- **Wrong speed** — Adjust **Speed:** in the bottom bar of the CWX panel. The value persists as `CwxSpeedWpm`.

## Related

- [Edit a CW macro string](edit-a-cw-macro-string.md)
- [Change CW send speed in WPM](change-cw-send-speed-in-wpm.md)
- [Enable QSK full break-in](enable-qsk-full-break-in.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Look up the prosign character shortcuts](look-up-the-prosign-character-shortcuts.md)
