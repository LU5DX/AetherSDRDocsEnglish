# Copy Assist — Speech to Speech Overview

Copy Assist provides real-time speech-to-text transcription for the active slice, powered by whisper.cpp. It decodes received voice audio into a scrolling, color-coded transcript, helping you capture and review QSO content without relying on notes.

## Before you start

- A FLEX-8600 radio must be connected and active.
- The whisper.cpp engine requires a model file; on first use, it will download the selected model automatically.
- GPU acceleration requires a compatible NVIDIA GPU with sufficient VRAM (GPU mode) or a CPU-only fallback (CPU mode).

## How it works

1. **Open the Copy Assist panel** via `View > Copy Assist` or press `Ctrl+Shift+T`.
2. **Enable transcription** by clicking the **Enable / Disable** toggle button. The engine state indicator will show "Downloading model" (first use) → "Loading model" → "Listening".
3. **Monitor the transcript** in real time as decoded text scrolls in the read-only **Transcript** field. Text is color-coded:
   - **Green** – high confidence
   - **Yellow** – medium confidence
   - **Red** – low confidence
4. **Track pipeline health** using the **Backlog indicator** — shows seconds of audio not yet transcribed. The indicator color escalates from amber to red as backlog grows.
5. **Fine-tune performance** by clicking the **Settings button** (gear icon) to open the modeless Copy Assist settings dialog, where you can adjust:
   - **Model tier** – choose `tiny`, `base`, `small`, or `medium` (larger = more accurate but slower/heavier)
   - **Compute device** – select `GPU (CUDA/Metal)` for faster inference with GPU or `CPU` for universal compatibility
6. **Clear the buffer** at any time by clicking the **Clear** button.

## What each control does

| Control | Type | Default | Behavior |
|---|---|---|---|
| **Enable / Disable** | toggle button | Disabled | Starts or stops the whisper.cpp engine on the active slice's audio. |
| **Transcript** | read-only text field | — | Scrolling text display of decoded speech. Color-coded by confidence (green/yellow/red). Contains a Clear button to empty the buffer. |
| **Model tier** | combo box | `tiny` | Selects whisper model size. Valid settings: `tiny`, `base`, `small`, `medium`. |
| **Compute device** | combo box | `GPU (CUDA/Metal)` | Selects inference device. Valid settings: `GPU` or `CPU`. |
| **Backlog indicator** | status indicator | 0.0s | Shows seconds of audio in the pipeline not yet transcribed. Color escalates amber → red as backlog grows. |
| **Settings button** | push button | — | Opens the modeless Copy Assist settings dialog for model tier, compute device, and engine configuration. |
| **Clear** | push button | — | Clears the current transcript buffer. |

## Tips

- Start with the `tiny` model for lowest latency and minimal resource usage. Switch to `base` or `small` if accuracy is insufficient and your system can handle the load.
- GPU mode is significantly faster but requires a compatible GPU. If you experience high backlog times, try switching to `GPU` (if available) or reducing model size.

## Related

- [Enable speech-to-text transcription on a slice](enable-speech-to-text-transcription-on-a-slice.md)
- [Change the whisper model tier for accuracy vs speed](change-the-whisper-model-tier-for-accuracy-vs-speed.md)
- [Choose GPU or CPU for speech recognition](choose-gpu-or-cpu-for-speech-recognition.md)
- [Read the live transcript with confidence-colored text](read-the-live-transcript-with-confidence-colored-text.md)
- [Clear the transcript buffer](clear-the-transcript-buffer.md)
