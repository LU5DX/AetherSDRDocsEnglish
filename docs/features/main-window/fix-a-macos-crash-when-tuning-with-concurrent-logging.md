# Fix a macOS crash when tuning with concurrent logging

AetherSDR's Main Window coordinates tuning and all background audio processing. On macOS, adjusting frequency while concurrent logging was active could trigger a crash in the audio engine's scope emission path.

## Before you start

- Update to AetherSDR v0.9.7 or later. This release contains the fix.
- Connect to your FlexRadio hardware (LAN or SmartLink WAN) before tuning.

## Steps

1. Launch AetherSDR. The Main Window opens automatically.
2. Tune normally using the frequency entry or VFO controls. The crash no longer occurs when logging runs concurrently.

## What each control does

| Control | Behavior |
|---|---|
| Frequency / VFO tuning | Adjusts the slice frequency. In v0.9.7, the audio engine's TX post-chain scope emission is now properly throttled (≤ ~120 Hz) and thread-safe, preventing a crash when the logging subsystem is active at the same time. |

## Tips

- No settings changes are needed. The fix is applied automatically at startup when the audio engine initialises the Quindar tone and final limiter components.
- If you previously worked around the crash by disabling logging during tuning, you can re-enable logging safely after updating.

## Related

- [main-window.md](main-window.md)
- [audio-engine.md](audio-engine.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
