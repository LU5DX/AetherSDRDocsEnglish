# Toggle VOX and see the Phone panel update instantly

The `micStateChanged` signal notifies the UI whenever microphone settings change — including VOX state — so the Phone panel reflects the current radio state immediately without requiring a manual refresh.

## Before you start

- Connect to a radio. The Phone panel is only active when a radio connection is established.

## Steps

1. Open the Phone panel.
2. Toggle the **VOX** control on or off.
3. Observe the Phone panel — it updates instantly to reflect the new VOX state.

## What each control does

| Control | Behavior |
|---|---|
| **VOX** | Enables or disables voice-operated transmit. Toggling this control fires `micStateChanged`, which causes the Phone panel to redraw immediately with the updated state. |

## Tips

- If the Phone panel does not update after toggling VOX, check that the radio is still connected. When the radio disconnects, mic state resets to defaults and the panel reflects those defaults instead of your previous settings.

## Related

- [phone-panel.md](phone-panel.md)
- [mic-settings.md](mic-settings.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
