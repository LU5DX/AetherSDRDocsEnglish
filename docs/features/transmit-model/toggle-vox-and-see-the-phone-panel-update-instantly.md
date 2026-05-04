# Toggle VOX and see the Phone panel update instantly

The `micStateChanged` signal notifies the UI whenever microphone or transmission-related settings change, ensuring the Phone panel always reflects the current radio state immediately — including VOX changes.

## Before you start

- Connect to a radio so that mic state is active and the Phone panel is visible.

## Steps

1. Open the **Phone** panel if it is not already visible.
2. Toggle the **VOX** control on or off.
3. Observe the Phone panel — it updates instantly to reflect the new VOX state without requiring a manual refresh.

## What each control does

| Control | Behavior |
|---|---|
| VOX toggle | Enables or disables Voice-Operated Transmit. Toggling this fires `micStateChanged`, which causes the Phone panel to redraw immediately with the updated state. |

## Tips

- The Phone panel also updates automatically when you switch microphone profiles, adjust mic level, change speech processor settings, or toggle DAX — all of these changes go through the same `micStateChanged` signal.
- If the Phone panel does not update after toggling VOX, check that the radio is still connected. On disconnect, mic state resets to defaults and the panel reflects those defaults.

## Related

- [Phone Panel Overview](phone-panel.md)
- [Microphone Settings](microphone-settings.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
