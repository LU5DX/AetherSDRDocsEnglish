# Change CW Send Speed in WPM

Adjust the CW keying speed so the radio sends at the WPM rate you need. The speed setting is available at all times from the bottom bar of the CWX panel.

## Before you start

- Connect to a FLEX-8600 radio. The CWX panel requires an active radio connection.
- Open the CWX panel. It appears in the main window area when the active slice is in CW, CWL, or CWU mode.

## Steps

1. Locate the **Speed:** spinbox in the bottom bar of the CWX panel.
2. Click the spinbox and type a value, or use the up/down arrows to adjust the speed.
3. The new speed takes effect immediately. The value is saved as `CwxSpeedWpm`.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| **Speed:** | 20 | 5–100 WPM | `CwxSpeedWpm` | Sets the CW keying speed in words per minute. |
| **Delay:** | 0 | 0–10000 ms | `CwxDelay` | Sets the inter-macro delay in milliseconds. |
| **QSK** | Off | – | `CwxQsk` | Toggles QSK (full break-in) on or off. |

## How the Send, Live, and Setup buttons behave

The three view buttons in the top bar of the CWX panel changed behavior in v0.9.2.1.

| Button | Kind | Behavior |
|---|---|---|
| **Send (view)** | Push button | If **Live** mode is currently off, clicking **Send** submits the typed buffer immediately and stays in the Send view. If **Live** mode is currently on, clicking **Send** first turns Live mode off and returns the panel to the normal typing view without retransmitting any text that was already keyed character-by-character. |
| **Live (view)** | Toggle button | Toggles Live mode on or off. When toggled on, the panel switches to the Send view and the radio begins keying characters as you type them. Turning Live off does not clear the buffer. Navigating to **Setup** while Live is on automatically turns Live off. |
| **Setup (view)** | Push button | Shows the macro editor and QSK setup. Opening Setup always turns Live mode off before displaying the Setup view. |

> **Note:** Prior to v0.9.2.1, **Send** was a checkable button that acted as part of a mutually exclusive toggle group with **Live** and **Setup**. It is now a plain push button whose action depends on whether Live mode is active when you click it.

## Live mode state is preserved on reconnect

When a model is attached to the CWX panel (for example, after connecting to the radio), the **Live** button is updated to reflect the current Live state reported by the radio. This means if Live mode was active before a disconnect, the button will show the correct state when the connection is restored.

## Send history context menu

Each entry in the send history scroll area supports a right-click context menu with two actions:

- **Resend** – Re-sends the selected text buffer. A new history entry is added to the scroll.
- **Clear History** – Removes all history entries from the scroll area. Does not affect the radio.

## Aborted transmissions shown with strikeout

If you press Escape while the radio is sending a CW buffer, the transmission is aborted. In the send history scroll area, the history bubble for that transmission shows the sent portion in normal text and the unsent portion with strikeout formatting. This makes it clear which characters were actually transmitted before the abort.

## Keyboard shortcuts

The CWX panel registers global application shortcuts for the F1–F12 keys and the Escape key. These shortcuts activate when the active slice is in CW, CWL, or CWU mode, regardless of whether the CWX panel is visible. This prevents shortcut conflicts with other panels, such as the DVK macro panel, which uses the same F1–F12 keys for its own purposes. The enable state is managed by the MainWindow based on the active slice's mode.

| Shortcut | Behavior |
|---|---|
| **F1–F12** | Sends the corresponding macro (F1–F12) when the active slice is in CW or CWL mode. |
| **Escape** | Clears the current text buffer (aborts any transmission in progress). |

## Tips

- The **Speed:** spinbox is visible in all three views (Send, Live, and Setup). You do not need to switch views to change speed.
- Press Escape at any time to abort a transmission in progress without changing the speed setting.
- If you are in Live mode and want to type ahead without transmitting, click **Send** to exit Live mode before continuing to type. The panel will not re-send any characters that were already transmitted.
- The Prosigns legend shows shortcuts for common CW prosigns: = (BT), + (AR), ( (KN), & (AS), $ (SK).
- Right-click any history bubble to resend that text or clear the entire history.
- After aborting a transmission, inspect the history bubble to see which characters were sent (normal text) and which were not (strikeout text).

## Related

- [CWX overview](overview.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
- [Enable QSK full break-in](enable-qsk-full-break-in.md)