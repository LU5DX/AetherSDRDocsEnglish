# CWX overview

CWX is AetherSDR's built-in CW keyer interface. It lets you send typed text or pre-written macros through the FLEX-8600's keyer, control send speed, set inter-macro delay, and enable QSK full break-in — all without leaving the application.

## Before you start

- Connect to a FLEX-8600 radio. CWX requires an active radio connection.
- Set the active slice to CW, CWL, or CWU mode. The CWX panel appears in the main window central area when a CW-mode slice is active.

## How it works

CWX presents three views, selected by the buttons at the bottom of the panel: Send, Live, and Setup. The Speed: spinbox and the view-selector buttons are always visible regardless of which view is active.

**Send view** — Shows a scrolling history of previously sent buffers displayed as chat bubbles, with a text entry area at the bottom. Type your message and press Enter to send it. Characters are highlighted in the history as they are transmitted.

**Live view** — Shows the live send area. Use this when you want to monitor transmission as it happens.

**Setup view** — Shows the 12 F-key macro editors, the Delay: control, and the QSK toggle. Edit macro text here and configure keyer timing options.

**F1–F12 shortcuts** — When the active slice is in CW or CWL mode, pressing F1 through F12 on the keyboard sends the corresponding macro immediately, regardless of which view is currently shown.

**Escape** — Pressing Escape aborts the current CW transmission and clears the send buffer. This works application-wide whenever CWX is active.

## What each control does

| Control | Description | Persisted setting |
|---|---|---|
| Send | Switches to the send history and text entry view. | — |
| Live | Switches to the live send view. | — |
| Setup | Switches to the macro editor and QSK setup view. | — |
| Speed: | CW send speed in WPM. Range: 5–100 WPM. Default: 20 WPM. | `CwxSpeedWpm` |
| Send history scroll | Scrolling display of previous send buffers with per-character highlighting. Read-only. | — |
| Send text area | Text entry field. Press Enter to send the typed buffer. | — |
| F1 … F12 (macro buttons) | Sends the macro stored for that function key. Active via keyboard shortcut when slice is in CW or CWL mode. | `CwxMacro_F1` – `CwxMacro_F12` |
| F1 … F12 macro editors | Text fields in the Setup view for writing or editing each macro string. | `CwxMacro_F1` – `CwxMacro_F12` |
| Delay: | Inter-macro delay in milliseconds. Range: 0–2000 ms. Default: 5 ms. | `CwxDelay` |
| QSK | Enables QSK full break-in when checked. | `CwxQsk` |
| Prosigns legend | Read-only reference showing character shortcuts for common CW prosigns (=, +, (, &, $). | — |

## Tips

- Pressing Escape during a macro transmission clears the buffer immediately. Because the keyer state alternates rapidly between dits and dahs, Escape fires unconditionally rather than waiting for a specific transmit state, so it reliably stops sending.
- F1–F12 keyboard shortcuts only fire when the active slice is in CW or CWL mode. Switching the slice to a non-CW mode disables them automatically.

## Related

- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
- [Edit a CW macro string](edit-a-cw-macro-string.md)
- [Change CW send speed in WPM](change-cw-send-speed-in-wpm.md)
- [Enable QSK full break-in](enable-qsk-full-break-in.md)
- [Look up the prosign character shortcuts](look-up-the-prosign-character-shortcuts.md)
