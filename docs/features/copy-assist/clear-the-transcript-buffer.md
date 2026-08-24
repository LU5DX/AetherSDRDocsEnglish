# Copy Assist — Speech to Text

The Copy Assist panel provides real-time speech-to-text transcription for the active slice. It uses the whisper.cpp engine to decode received voice audio into a scrolling transcript that is color-coded by confidence: green for high confidence, yellow for medium, and red for low. The panel includes a settings dialog for selecting the model tier and compute device.

## Enable or disable transcription

The Copy Assist panel runs independently for the active slice. When enabled, it decodes received audio and displays the transcript in real time.

### Before you start

- Verify the Copy Assist panel is open (**View > Copy Assist**, or press Ctrl+Shift+T).
- Confirm a slice is active and receiving audio.

### Steps

1. Open the **Copy Assist** panel: **View > Copy Assist** (Ctrl+Shift+T).
2. Locate the **Enable / Disable** toggle button at the top of the panel.
3. Click the button to start the speech-to-text engine. The engine status indicator changes from **Idle** to **Listening** when decoding is active.
4. Click the button again to stop the engine. The engine status indicator returns to **Idle**.

### Engine status

The indicator shows the current state of the whisper.cpp engine:

| State | Meaning |
|-------|---------|
| Idle | Engine is stopped. |
| Downloading model | The selected model is being downloaded on first use. |
| Loading model | The model file is being loaded into memory. |
| Listening | Engine is actively decoding the slice's audio. |
| Error | Engine failed to start or encountered a runtime error. |

## Read the live transcript with confidence-colored text

The transcript displays decoded speech as it is produced. Each line is color-coded by the confidence score whisper assigned to the decoded text.

### Color coding

| Color | Confidence | Meaning |
|-------|-----------|---------|
| Green | High | The engine is highly confident in the decoded text. |
| Yellow | Medium | The engine is moderately confident — text may contain errors. |
| Red | Low | The engine is not confident — verify the text against the audio. |

### Steps

1. Enable transcription as described above.
2. Watch the transcript field for decoded speech.
3. Use the color coding to judge reliability:
   - Green text can be trusted as accurate.
   - Yellow text is likely correct but may contain minor errors.
   - Red text should be verified against the received audio.
4. The transcript scrolls automatically as new text is decoded.

## Select the model tier and compute device

The settings dialog controls which whisper model is used and where the decoding runs.

### Before you start

- The Copy Assist panel must be open.
- For GPU decoding, a compatible CUDA or Metal GPU must be present.

### Model tier

The model size determines accuracy and resource usage.

| Model | Accuracy | Speed | Memory |
|-------|----------|-------|--------|
| tiny | Lowest | Fastest | Minimal |
| base | Low | Fast | Low |
| small | Medium | Moderate | Moderate |
| medium | High | Slow | High |

### Compute device

| Device | Speed | Requirements |
|--------|-------|--------------|
| GPU (CUDA/Metal) | Fast | Compatible GPU with sufficient VRAM |
| CPU | Slower | Works on all systems |

On first launch, AetherSDR probes for a GPU asynchronously and selects GPU decoding when available, otherwise it falls back to CPU. You can override this choice at any time in the settings dialog.

### Steps

1. Open the **Copy Assist** panel.
2. Click the **Settings button** (⚙) at the top of the panel. The Copy Assist settings dialog opens as a modeless window.
3. Select a **Model tier** from the dropdown:
   - Choose a larger model (medium > small > base > tiny) for better accuracy when CPU/VRAM allows.
   - Choose a smaller model for faster decoding on limited hardware.
4. Select a **Compute device**:
   - **GPU (CUDA/Metal)** — faster decoding; requires sufficient VRAM for the selected model.
   - **CPU** — works everywhere; slower for large models.
5. The engine applies the new settings on the next decoding run. If the engine is listening, stop and re-enable it to apply the changes immediately.

### Context carry

The Copy Assist settings dialog includes a **Context carry** option that is available only when the whisper backend is active. When enabled, decoded context from previous segments is carried into subsequent decoding to improve accuracy. This option is disabled when the sherpa-onnx or remote backend is active because those backends do not implement context carry.

## Monitor the backlog

The backlog indicator shows how many seconds of received audio have not yet been transcribed.

### Behavior

- The indicator displays the backlog in seconds (for example, `0.0s`).
- Normal operation: backlog stays near zero.
- Escalation: as the backlog grows, the indicator color changes:
  - Amber — backlog is building; the engine is falling behind.
  - Red — backlog is significant; decoding quality may suffer.

### Steps

1. Enable transcription.
2. Watch the backlog indicator next to the transcript.
3. If the backlog climbs and stays high:
   - Select a smaller model tier to increase decoding speed.
   - Switch the compute device to GPU if currently on CPU.
   - Check the engine status — an **Error** state may indicate the engine stopped.

## Clear the transcript buffer

Clear the accumulated transcript between contacts or to start fresh.

### Before you start

- The Copy Assist panel must be open (**View > Copy Assist**, or press Ctrl+Shift+T).
- Transcription does not need to be active to clear the buffer.

### Steps

1. Open the **Copy Assist** panel: **View > Copy Assist** (Ctrl+Shift+T).
2. Find the **Clear** button at the bottom of the Copy Assist panel.
3. Click **Clear**. The transcript text field empties immediately, and any carried decode context is flushed so the new transcript starts from a clean prompt.

### Tips

- Clearing does not stop transcription — the engine continues listening and will begin filling the buffer from where it left off.
- The clearance is instant; no confirmation dialog appears.

## Troubleshooting

- **Engine stays in Idle after Enable** — Verify a slice is active and receiving audio. Check the engine status indicator for an **Error** state.
- **Engine shows Error** — Try switching the compute device to CPU, or select a smaller model tier. Verify the model file downloaded completely.
- **Backlog climbs continuously** — The engine cannot keep up with the audio. Select a smaller model or switch to GPU decoding.
- **No transcript appears but audio is audible** — Check the transcript color coding; low-confidence text may be sparse. Try a larger model tier for better accuracy.
- **GPU option is missing** — No compatible CUDA or Metal GPU was detected. Only CPU decoding is available.
- **Context carry is greyed out** — The active backend (sherpa-onnx or remote) does not implement context carry. Switch to the whisper backend to enable it.
- **Clear button does not respond** — Ensure the panel is open via **View > Copy Assist**. If the button still doesn't respond, try closing and reopening the panel.

## Related

- [Enable speech-to-text transcription on a slice](enable-speech-to-text-transcription-on-a-slice.md)
- [Read the live transcript with confidence-colored text](read-the-live-transcript-with-confidence-colored-text.md)