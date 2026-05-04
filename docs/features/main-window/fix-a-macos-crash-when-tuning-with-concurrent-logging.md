# Fix a macOS crash when tuning with concurrent logging

AetherSDR's main window coordinates tuning and background audio processing simultaneously. On macOS, a race condition between the tuning path and concurrent logging could cause a crash; v0.9.5.1 resolves this automatically with no user action required.

## Before you start

- Update to AetherSDR v0.9.5.1 or later. The fix is applied at startup with no configuration needed.

## Steps

1. Launch AetherSDR. The main window opens automatically and applies the updated audio engine logic on startup.
2. Tune normally using the panadapter or slice controls. The crash that previously occurred on macOS when logging was active during tuning no longer occurs.

## What changed in v0.9.5.1

| Area | Previous behavior | New behavior |
|---|---|---|
| TX EQ audio tap | Tap ran only when the EQ stage was enabled; bypassed EQ skipped the tap entirely | Tap always runs, so the TX FFT analyzer reflects live mic input even when EQ is bypassed in the CHAIN widget |
| NR2 wisdom validation | Checked only whether the wisdom file existed on disk | Also attempts to import the wisdom file; if import fails, logs a warning and schedules regeneration |
| NR2 wisdom on enable | Called `generateWisdom()` on the audio worker thread if wisdom was missing | Imports existing wisdom only; full generation is never triggered on the audio worker thread (which could block or crash) |
| DAX TX routing (macOS) | Platform routing policy was handled inline | Extracted into a dedicated `DaxTxPolicy` header with explicit platform and mode enumerations, fixing the macOS crash path |

## Tips

- If you see a log warning such as `NR2 FFTW wisdom exists but could not be imported`, let AetherSDR complete the background wisdom regeneration before enabling NR2. The main window status area indicates when wisdom generation is in progress.
- The TX FFT analyzer in the EQ editor now shows live microphone signal at all times, regardless of whether the EQ stage is active in the CHAIN widget.

## Related

- [NR2 Noise Reduction Setup](nr2-noise-reduction.md)
- [DAX TX Routing](dax-tx-routing.md)
- [AetherSDR Main Window](main-window.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
