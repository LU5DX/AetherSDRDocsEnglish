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

## Tips

- The **Speed:** spinbox is visible in all three views (Send, Live, and Setup). You do not need to switch views to change speed.
- Press Escape at any time to abort a transmission in progress without changing the speed setting.

## Related

- [CWX overview](overview.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
- [Enable QSK full break-in](enable-qsk-full-break-in.md)
