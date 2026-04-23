# CWX overview

CWX is AetherSDR's CW keying panel. It lets you type and send live CW text, trigger pre-written macro strings with function keys, and configure QSK and inter-macro delay — all routed through the connected Flex radio.

## Before you start

- AetherSDR must be connected to a Flex radio. CWX requires an active radio connection.
- The active slice must be in CW, CWL, or CWU mode for CWX to appear automatically in the main window area.

## How it works

CWX is a panel fixed at 250 pixels wide that appears in the MainWindow central area. It has three views, selected by buttons in the bottom bar: Send, Live, and Setup. The bottom bar also holds the Speed control, which is always visible regardless of the active view.

**Send view** shows a scrolling history of previously sent buffers, displayed as chat-style bubbles that accumulate from the bottom up. Each bubble shows the text and a timestamp. Below the history is a text entry area where you type the next message. Pressing Enter sends the typed buffer to the radio.

**Live view** shows the live send area. Switch to it by clicking Live in the bottom bar.

**Setup view** shows the 12 F-key macro editors, the Delay control, and the QSK toggle. Edit a macro's text in its field; the value is saved immediately and used the next time that macro fires.

**F1–F12 keys** fire macros application-wide whenever the active slice is in CW or CWL mode. Pressing Escape clears the current send buffer and aborts transmission.

## What each control does

| Control | View | Behavior | Setting key |
|---|---|---|---|
| Send | Bottom bar | Switches to the Send view. Shows typed-buffer entry and send history. | — |
| Live | Bottom bar | Switches to the Live view. | — |
| Setup | Bottom bar | Switches to the macro editor and QSK setup. | — |
| Speed: | Bottom bar | CW sending speed in WPM. Range: 5–100 WPM. Default: 20 WPM. | `CwxSpeedWpm` |
| Send history scroll | Send view | Scrolling display of previous send buffers with per-character highlighting and timestamps. Read-only. | — |
| Send text area | Send view | Type CW text here. Press Enter to send the buffer to the radio. | — |
| F1 … F12 (macros) | Send/Live view | Sends the stored macro string for that function key. Also triggered by the corresponding keyboard key when the active slice is in CW or CWL mode. | `CwxMacro_F1` – `CwxMacro_F12` |
| F1 … F12 macro editors | Setup view | Text fields for writing or editing each macro string. | `CwxMacro_F1` – `CwxMacro_F12` |
| Delay: | Setup view | Inter-macro delay in milliseconds. Range: 0–2000 ms. Default: 5 ms. | `CwxDelay` |
| QSK | Setup view | Toggle. Enables QSK (full break-in) CW operation. | `CwxQsk` |
| Prosigns legend | Setup view | Read-only reference showing character shortcuts for common CW prosigns (=, +, (, &, $). | — |

## Tips

- Pressing Escape aborts an in-progress CW transmission by clearing the send buffer. This works application-wide during CW or CWL operation and does not interfere with normal UI Escape behavior such as closing dialogs.
- F1–F12 macro shortcuts are only active when the current slice mode is CW or CWL. They have no effect in other modes.

## Related

- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
- [Edit a CW macro string](edit-a-cw-macro-string.md)
- [Change CW send speed in WPM](change-cw-send-speed-in-wpm.md)
- [Enable QSK full break-in](enable-qsk-full-break-in.md)
- [Look up the prosign character shortcuts](look-up-the-prosign-character-shortcuts.md)
