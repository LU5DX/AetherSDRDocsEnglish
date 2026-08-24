# Enable speech-to-text transcription on a slice

Real-time speech-to-text transcribes received voice audio from the active slice using the whisper.cpp engine. The transcript appears in the Copy Assist panel with color-coded confidence levels.

## Before you start

- Connect to a FLEX-8600 radio and have at least one slice active
- Ensure the radio is receiving audio (a signal should be present on the slice)

## Steps

1. Open the Copy Assist panel: `View > Copy Assist` or press `Ctrl+Shift+T`.
2. Click **Enable / Disable** to start the whisper.cpp speech-to-text engine.
   - The engine status indicator changes from "Idle" to "Downloading model" (if needed), then "Loading model", then "Listening".
   - If no model is available, the engine automatically downloads the selected model tier (default: `tiny`).
3. Speak into the radio's microphone or receive a transmission on the active slice.
   - Decoded text appears in the **Transcript** field, color-coded by confidence (green = high, yellow = medium, red = low).
   - The **Backlog** indicator shows seconds of audio not yet transcribed; stays near `0.0s` under normal operation.

To stop transcription, click **Enable / Disable** again. The engine status returns to "Idle".

## What each control does

| Control | Default | Behavior | Setting key |
|---------|---------|----------|-------------|
| Enable / Disable | Disabled | Starts or stops the whisper.cpp speech-to-text engine on the active slice's audio | None |
| Transcript | — | Scrolling, read-only transcript of decoded speech. Text is color-coded by confidence: green (high), yellow (medium), red (low). Clear button empties the buffer | None |
| Model tier | `tiny` | Whisper model size. Larger models are more accurate but slower and use more VRAM/RAM | None |
| Compute device | GPU (CUDA/Metal) | Selects whether whisper runs on GPU (faster, needs VRAM) or CPU (slower, works everywhere). Hidden on hosts without a GPU | None |
| Backlog indicator | 0.0s | Seconds of received audio not yet transcribed. Colour escalates amber→red as backlog grows | None |
| Settings button | — | Opens the modeless Copy Assist settings dialog for model tier, compute device and engine configuration | None |
| Clear | — | Clears the current transcript buffer | None |

## Engine status

The engine status indicator shows the current state of the whisper.cpp speech-to-text engine:

| State | Meaning |
|-------|---------|
| Idle | Engine is stopped |
| Downloading model | Model is being fetched |
| Loading model | Model is being loaded into memory |
| Listening | Engine is actively transcribing |
| Error | A failure occurred during operation |

## Compute device selection

The compute device picker is shown whenever a GPU exists, so you can select a GPU (or several) or force CPU. On hosts without a GPU, the selector is hidden and the CPU is always used.

When the radio starts, the engine uses the platform default compute device until the asynchronous GPU probe completes. On macOS, the first GPU query can take several seconds to compile the embedded Metal shader library, so the initial device selection is resolved in the background.

## Context carry

The context-carry feature is only available when the whisper backend is active. If you switch to the sherpa-onnx or remote backend, the context-carry toggle is disabled because those backends do not implement this behavior.

## Tips

- The transcript scrolls automatically as new text appears. Use the **Clear** button to empty the buffer at any time.
- If the compute device is set to GPU but there isn't enough VRAM, the engine may fail to load. Switch to CPU in the settings dialog or choose a smaller model tier.
- Clearing the transcript also clears any carried decode context, so the next transcription session starts from a fresh prompt.

## Related

- [Copy Assist — Speech to Text overview](overview.md)
- [Change the whisper model tier for accuracy vs speed](change-the-whisper-model-tier-for-accuracy-vs-speed.md)
- [Choose GPU or CPU for speech recognition](choose-gpu-or-cpu-for-speech-recognition.md)
- [Clear the transcript buffer](clear-the-transcript-buffer.md)
- [Read the live transcript with confidence-colored text](read-the-live-transcript-with-confidence-colored-text.md)