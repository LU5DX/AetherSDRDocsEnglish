# Enable QSK Full Break-in

QSK (full break-in) lets the radio switch between transmit and receive between individual CW elements, so you can hear signals in the gaps between your own dits and dahs. This page shows how to turn QSK on or off in the CWX panel.

## Before you start

- AetherSDR must be connected to the radio. The CWX panel requires an active radio connection.
- The active slice must be in CW, CWL, or CWU mode for the CWX panel to be visible.

## Steps

1. Open the CWX panel in the MainWindow central area.
2. Click **Setup** at the bottom of the panel. The Setup view shows the macro editors, the **Delay:** spinbox, and the **QSK** button.
3. Click **QSK** to toggle full break-in on. The button appears highlighted when enabled.
4. To disable QSK, click **QSK** again.

## What each control does

| Control | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|
| **QSK** | Enables or disables QSK (full break-in). Toggle button; highlighted when active. | — | On / Off | `CwxQsk` |
| **Delay:** | Sets the inter-macro delay in milliseconds. | 5 | 0–2000 ms | `CwxDelay` |

## Related

- [CWX overview](overview.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Change CW send speed in WPM](change-cw-send-speed-in-wpm.md)
- [Edit a CW macro string](edit-a-cw-macro-string.md)
