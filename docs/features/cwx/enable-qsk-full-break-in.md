# Enable QSK Full Break-in

QSK (full break-in) lets the radio receive between each dit and dah while transmitting CW. Enable it in the CWX Setup view so the radio switches to receive during the gaps in your sending.

## Before you start

- Connect to a FLEX-8600 radio. The CWX panel requires an active radio connection.
- Set the active slice to CW, CWL, or CWU mode so the CWX panel is available.

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

## Related

- [CWX overview](overview.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)
