# Change the whisper model tier for accuracy vs speed

The Copy Assist panel uses a whisper.cpp model to transcribe received audio. Larger models produce more accurate transcriptions but use more VRAM/RAM and process audio more slowly. This page shows you how to switch between model tiers to balance accuracy against speed.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- Copy Assist must be visible (open it with `View > Copy Assist` or press `Ctrl+Shift+T`).

## Steps

1. In the Copy Assist panel, click the **Settings button** (gear icon). This opens the Copy Assist settings dialog.
2. In the dialog, locate the **Model tier** combo box.
3. Click the combo box and select one of:
   - **tiny** — Fastest, lowest accuracy, least memory used.
   - **base** — Reasonable speed with moderate accuracy.
   - **small** — Good accuracy, noticeably slower.
   - **medium** — Highest accuracy, slowest performance, most VRAM/RAM required.
4. Close the settings dialog. The new model tier takes effect immediately after the underlying engine reloads.

## What each control does

| Control | Default | Valid range | Behavior |
|---------|---------|-------------|----------|
| Model tier combo box | `tiny` | tiny / base / small / medium | Selects the whisper model size. Larger models improve accuracy but increase latency and memory usage. |
| Compute device combo box | `GPU (CUDA/Metal)` | GPU / CPU | Selects whether whisper runs on GPU (faster, needs VRAM) or CPU (slower, works everywhere). |
| Backlog indicator | `0.0s` | — | Seconds of received audio not yet transcribed. Colour escalates amber→red as backlog grows. |

## Choosing a compute device

By default, AetherSDR runs whisper on the GPU if one is available. You can force CPU or explicitly select a specific GPU in the Copy Assist settings dialog.

### Steps

1. Open the Copy Assist settings dialog via the **Settings button**.
2. Locate the **Compute device** combo box.
3. Choose:
   - **GPU (CUDA/Metal)** — Uses a CUDA or Metal GPU. Faster, but requires sufficient VRAM.
   - **CPU** — Runs entirely on the CPU. Slower, but works on any system.

> **Note:** On macOS, the first GPU query may take several seconds because the Metal shader library is compiled on demand. This happens in the background and does not block the Copy Assist panel.

## Context-carry behavior

The **Context-carry** toggle in the Copy Assist panel continues the decoded prompt across the transcript. This is only available with the whisper backend; when using Sherpa or remote backends, the toggle is disabled.

## Tips

- If you notice the **Backlog indicator** climbing (amber→red), switch to a smaller model tier or to CPU to help the engine catch up.
- The model files are downloaded automatically when you switch to a tier for the first time. Expect a brief delay and internet connection required for the initial download.
- If transcription is consistently inaccurate, try a larger model tier first before changing the compute device.
- When the **Backlog indicator** stays high on GPU, consider switching to CPU—some systems have GPU memory pressure even when the GPU is nominally available.

## Related

- [Copy Assist — Speech to Text overview](overview.md)
- [Choose GPU or CPU for speech recognition](choose-gpu-or-cpu-for-speech-recognition.md)
- [Enable speech-to-text transcription on a slice](enable-speech-to-text-transcription-on-a-slice.md)