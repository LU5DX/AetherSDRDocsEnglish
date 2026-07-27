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

## Tips

- If you notice the **Backlog indicator** climbing (amber→red), switch to a smaller model tier to help the engine catch up.
- The model files are downloaded automatically when you switch to a tier for the first time. Expect a brief delay and internet connection required for the initial download.

## Related

- [Copy Assist — Speech to Text overview](overview.md)
- [Choose GPU or CPU for speech recognition](choose-gpu-or-cpu-for-speech-recognition.md)
- [Enable speech-to-text transcription on a slice](enable-speech-to-text-transcription-on-a-slice.md)
