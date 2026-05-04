# Reset mic state when switching between radios

When you switch between radios, AetherSDK automatically resets the microphone state to defaults and fires the `micStateChanged` signal so the Phone panel and all mic-related controls immediately reflect the new radio's state.

## Before you start

- Connect to at least one radio before switching.

## Steps

1. Switch to a different radio using your normal radio-selection control.
2. Observe that the Phone panel and mic-related controls update automatically — microphone selection, mic level, active mic profile, speech processor settings, and DAX state are all reset to defaults for the newly connected radio.

No manual action is required. The reset happens automatically on every radio switch and on disconnect.

## What each control does

| Control | Behavior |
|---|---|
| Mic State Change Signal (`micStateChanged`) | Fires whenever microphone selection, mic level, active mic profile, speech processor settings, or DAX state change. Also fires on radio disconnect, resetting all mic state to defaults. Keeps the Phone panel and mic-related panels in sync with the current radio. |

## Tips

- If the Phone panel appears to show stale mic settings after switching radios, disconnect and reconnect to force a full mic state reset.

## Related

- [phone-panel.md](phone-panel.md)
- [dax-settings.md](dax-settings.md)
- [speech-processor.md](speech-processor.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
