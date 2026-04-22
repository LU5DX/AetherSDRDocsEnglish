# Change CW send speed in WPM

Adjust the CWX send speed so the radio transmits at the words-per-minute rate you want. The speed setting takes effect immediately and is saved across sessions.

## Before you start

- AetherSDR must be connected to the radio. CWX requires an active radio connection.
- The active slice must be in CW, CWL, or CWU mode, or the CWX panel must already be open.

## Steps

1. Locate the CWX panel in the main window central area.
2. Find the **Speed:** spinbox in the bottom bar of the CWX panel.
3. Click the spinbox and type a value, or use the up/down arrows to adjust the speed.
4. The new speed takes effect immediately. No confirmation step is required.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---------|-------------|---------|-------------|-------------|
| **Speed:** | CW send speed in words per minute. | 20 WPM | 5–100 WPM | `CwxSpeedWpm` |

## Tips

- The **Speed:** spinbox is always visible in the bottom bar regardless of which view is active (Send, Live, or Setup). You do not need to switch views to change speed.
- Speed changes apply to both typed buffers and F-key macros.

## Related

- [CWX overview](overview.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
