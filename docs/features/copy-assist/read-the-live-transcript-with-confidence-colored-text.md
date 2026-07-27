# Read the live transcript with confidence-colored text

Read the scrolling speech-to-text transcript in the Copy Assist panel, where each word is color-coded by the whisper.cpp engine's confidence level.

## Before you start

- The radio must be connected and an active slice must be receiving audio.
- The Copy Assist panel must be open (`View > Copy Assist`, or press `Ctrl+Shift+T`).

## Steps

1. In the Copy Assist panel, click **Enable** to start the speech-to-text engine on the active slice's audio.
2. Wait for the engine status indicator to show "Listening".
3. Speak into the microphone or receive audio on the active slice.
4. Read the transcript. Each word or phrase is shown in a color that represents the whisper engine's confidence:
   - **Green** — high confidence
   - **Yellow** — medium confidence
   - **Red** — low confidence

## What each control does

| Control | Behavior |
|---------|----------|
| **Enable / Disable** | Toggle button. Starts or stops the whisper.cpp speech-to-text engine on the active slice's audio. Default: Disabled. |
| **Transcript** | Scrolling, read-only text field. Shows decoded speech with confidence-based coloring. |
| **Model tier** | Combo box. Selects whisper model size: tiny (default), base, small, or medium. Larger models improve accuracy but use more VRAM/RAM and are slower. |
| **Compute device** | Combo box. Selects GPU (CUDA/Metal) or CPU for whisper processing. Default: GPU (CUDA/Metal). |
| **Backlog indicator** | Shows seconds of received audio not yet transcribed. Escalates from amber to red as backlog grows. |
| **Settings button** | Opens the Copy Assist settings dialog for model tier, compute device, and engine configuration. |
| **Clear** | Empties the current transcript buffer. |

## Tips

- The backlog indicator shows how far behind the engine is. If it stays red for more than a few seconds, a smaller model tier or CPU compute may help on lower-end hardware.

## Related

- [Copy Assist — Speech to Text overview](overview.md)
- [Enable speech-to-text transcription on a slice](enable-speech-to-text-transcription-on-a-slice.md)
- [Change the whisper model tier for accuracy vs speed](change-the-whisper-model-tier-for-accuracy-vs-speed.md)
- [Choose GPU or CPU for speech recognition](choose-gpu-or-cpu-for-speech-recognition.md)
- [Clear the transcript buffer](clear-the-transcript-buffer.md)
