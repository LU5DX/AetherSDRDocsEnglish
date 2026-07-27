# Choose GPU or CPU for speech recognition

Select whether the whisper.cpp speech-to-text engine uses your system's GPU or CPU for transcription. GPU processing is faster but requires VRAM; CPU processing works on any system but is slower.

## Before you start

- Copy Assist must be open: `View > Copy Assist` (Ctrl+Shift+T)
- A radio must be connected

## Steps

1. Open the Copy Assist settings dialog by clicking **Settings** in the Copy Assist panel.
2. Locate the **Compute device** combo box.
3. Select either **GPU** or **CPU** from the dropdown.
4. Close the settings dialog.

The new compute device is used the next time you enable transcription.

## What each control does

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| Compute device | GPU (CUDA/Metal) | GPU / CPU | Selects whether whisper runs on GPU (faster, needs VRAM) or CPU (slower, works everywhere) |

## Tips

- If you see high backlog values (amber/red) with GPU selected, try switching to a smaller model tier first before falling back to CPU.
- On systems with limited GPU memory (e.g., integrated graphics), CPU mode may be more stable.

## Related

- [Copy Assist — Speech to Text overview](overview.md)
- [Enable speech-to-text transcription on a slice](enable-speech-to-text-transcription-on-a-slice.md)
- [Change the whisper model tier for accuracy vs speed](change-the-whisper-model-tier-for-accuracy-vs-speed.md)
