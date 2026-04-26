# Set CW break-in delay

The CW break-in delay controls how long the radio waits after the last keyed element before returning to receive. Adjusting this prevents premature receiver recovery during fast exchanges.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in a CW mode. The Phone/CW applet automatically shows CW controls only when a CW mode is selected.

## Steps

1. If the Phone/CW applet is not visible, click the **P/CW** tray button on the right sidebar to show it.
2. Locate the **Delay** slider in the CW sub-panel.
3. Drag the **Delay** slider to the desired value. The valid range is 0–2000 ms in steps of 10.
4. To enable full break-in (QSK) with no delay, click **Breakin** so it is active.

## What each control does

| Control | Kind | Default | Valid range | Persisted key |
|---|---|---|---|---|
| **Delay** | Slider | — | 0–2000 ms (step 10) | — |
| **Breakin** | Toggle button | — | On / Off | — |

- **Delay** — Sets the time the radio waits after the last keyed element before switching back to receive.
- **Breakin** — Toggles full break-in (QSK). When active, the radio returns to receive immediately between keyed elements regardless of the **Delay** setting.

## Tips

- A **Delay** value of 0 ms with **Breakin** active gives true QSK behavior.
- Increase **Delay** if your receiver is recovering too quickly and disturbing your keying rhythm during pile-ups.

## Related

- [Phone/CW overview](overview.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
