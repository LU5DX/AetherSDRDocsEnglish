# Reset mic state when switching between radios

When you switch between radios, AetherSDR automatically resets the microphone state to defaults and emits a `micStateChanged` signal so the Phone panel and all mic-related controls reflect the newly connected radio's state.

## Steps

1. Switch to a different radio using the radio selector. AetherSDR disconnects from the current radio, resets mic selection, mic level, active mic profile, speech processor settings, and DAX state to defaults, then reconnects to the selected radio.
2. Verify the Phone panel and mic-related panels have updated to show the new radio's mic state.

## What each control does

| Control | Behavior |
|---|---|
| Mic State Changed (`micStateChanged`) | Fires whenever microphone selection, microphone level, active mic profile, speech processor settings, or DAX state change — including on radio disconnect, when all mic state is reset to defaults. Drives updates in the Phone panel and any mic-related UI panels. |

## Tips

- You do not need to manually reconfigure mic settings after switching radios. The reset runs automatically on disconnect and the UI updates as soon as the new radio connects.
- If the Phone panel does not reflect the correct mic state after switching, disconnect and reconnect to the radio to force the reset.

## Related

- [Phone panel](../panels/phone-panel.md)
- [Microphone settings](../settings/microphone-settings.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
