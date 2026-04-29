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

## How Send and Live interact

In v0.9.2.1 the **Send** and **Live** buttons no longer act as a simple mutually exclusive group. Their behavior depends on the current state of the panel:

- **Live** is a toggle. Click it once to enable live character-by-character keying; click it again to disable it. The button's checked state always reflects the model's live state, even if the state was changed externally.
- **Send** behaves differently depending on whether **Live** is active when you click it:
  - If **Live** is currently **off**, clicking **Send** submits the typed buffer immediately.
  - If **Live** is currently **on**, clicking **Send** first turns live mode off and returns the panel to the normal send view. The buffer is **not** retransmitted, because some characters may already have been keyed character-by-character.
- Clicking **Setup** always turns live mode off before switching to the Setup view.

## Related

- [CWX overview](overview.md)
- [Send a typed CW buffer live](send-a-typed-cw-buffer-live.md)
- [Trigger a CW macro with F1–F12](trigger-a-cw-macro-with-f1-f12.md)