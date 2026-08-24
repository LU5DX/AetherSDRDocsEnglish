# Enable QSK Full Break-in

QSK (full break-in) lets the radio receive between each dit and dah while transmitting CW. Enable it in the CWX Setup view so the radio switches to receive during the gaps in your sending.

## Before you start

- Connect to a FLEX-8600 radio. The CWX panel requires an active radio connection.
- Set the TX slice to CW, CWL, or CWU mode so the CWX panel is available.

## Steps

1. Open the CWX panel in the main window.
2. Click **Setup** at the bottom of the panel to switch to the Setup view.
3. Click **QSK** to toggle it on. The button highlights when active.

To turn QSK off, click **QSK** again.

## What each control does

| Control | Behavior | Default | Setting key |
|---------|----------|---------|-------------|
| **QSK** | Toggles QSK (full break-in) on or off. | Off | `CwxQsk` |
| **Delay:** | Inter-macro delay in milliseconds. | 5 | `CwxDelay` |
| **Speed:** | CW speed in WPM. | 20 | `CwxSpeedWpm` |
| **Send (view)** | Switches to the live send area with history and text field. | – | – |
| **Live (view)** | Switches to the live send view. | – | – |
| **Setup (view)** | Switches to the macro editor and QSK setup. | – | – |
| **Send history scroll** | Shows previous send buffers with character highlighting. | – | – |
| **Send text area** | Type CW characters; Enter sends the buffer. | – | – |
| **F1 … F12 (macros)** | Sends the pre-written macro for that function key. | – | `CwxMacro_F1..F12` |
| **F1 … F12 macro editors** | Setup view editors for each macro. | – | `CwxMacro_F1..F12` |
| **Prosigns legend** | Shows shortcuts for common CW prosigns (=, +, (, &, $). | – | – |

## How Send and Live interact

The **Send** and **Live** buttons do not act as a simple mutually exclusive group. Their behavior depends on the current state of the panel:

- **Live** is a toggle. Click it once to enable live character-by-character keying; click it again to disable it. The button's checked state always reflects the model's live state, even if the state was changed externally.
- **Send** behaves differently depending on whether **Live** is active when you click it:
  - If **Live** is currently **off**, clicking **Send** submits the typed buffer immediately.
  - If **Live** is currently **on**, clicking **Send** first turns live mode off and returns the panel to the normal send view. The buffer is **not** retransmitted, because some characters may already have been keyed character-by-character.
- Clicking **Setup** always turns live mode off before switching to the Setup view.

## History bubble behavior

Each sent message appears as a history bubble in the **Send history scroll** area. Bubbles display the CW text and a timestamp. As characters are sent, the bubble updates to show which characters have been transmitted.

### Aborted bubbles (Escape key)

Press **Escape** during transmission to abort the current buffer. The bubble for the aborted message shows:
- Characters that were already sent appear normally.
- Characters that were not yet sent appear with strikeout formatting (a line through the text).

This visual distinction helps you see what made it to the air and what was cut off.

### History bubble context menu

Right-click any bubble to open a context menu with the following actions:

- **Resend** — Sends the selected message again and adds a new history bubble with the current timestamp.
- **Clear History** — Removes all history bubbles from the scroll area.

## F1–F12 and Escape shortcut behavior

The F1–F12 function keys and the **Escape** key are available as application-wide shortcuts. The shortcuts are enabled or disabled by the TX slice's mode, not by panel visibility. This ensures the keys fire whether the CWX panel is visible or not, while preventing conflicts with the DVK (Digital Voice Keyer) panel.

- When the TX slice is in CW, CWL, or CWU mode: F1–F12 trigger the corresponding CW macros, and **Escape** aborts the current send buffer.
- When the TX slice is in a voice mode: F1–F12 trigger DVK macros instead.
- The shortcuts are automatically managed by the MainWindow based on the TX slice's mode.

## Speed step configuration

The CWX panel supports speed modifier prefixes in macros. The **Speed:** spinbox step value determines how much the speed changes when using speed modification characters. To configure the step:

1. Right-click the **Speed:** spinbox to open the context menu.
2. Select **Speed step...** to open the Speed Step dialog.
3. Enter a value between 1 and 20 WPM.
4. Click **OK**.

The step value is saved and persists between sessions.

## Related

- [CWX overview](overview.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)