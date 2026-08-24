# Copy Assist — Speech to Text

Real-time speech-to-text transcription for the active slice. Uses whisper.cpp to decode received voice audio into a scrolling, color-coded transcript (green = high confidence, red = low). Includes model selection, compute device picker, and confidence-based text coloring.

## Controls

### Enable / Disable

Starts or stops the whisper.cpp speech-to-text engine on the active slice's audio.

| Property | Value |
|---|---|
| Kind | Toggle button |
| Default | Disabled |

### Transcript

Scrolling, read-only transcript of decoded speech. Text is color-coded by whisper confidence: green (high), yellow (medium), red (low). Clear button empties the buffer.

| Property | Value |
|---|---|
| Kind | Text field |

### Model tier

Whisper model size. Larger models are more accurate but slower and use more VRAM/RAM.

| Property | Value |
|---|---|
| Kind | Combo box |
| Default | tiny |
| Valid range | tiny / base / small / medium |

### Compute device

Selects whether whisper runs on GPU (faster, needs VRAM) or CPU (slower, works everywhere).

| Property | Value |
|---|---|
| Kind | Combo box |
| Default | GPU (CUDA/Metal) |
| Valid range | GPU / CPU |

### Backlog indicator

Seconds of received audio not yet transcribed. Colour escalates amber→red as backlog grows.

| Property | Value |
|---|---|
| Kind | Indicator |
| Default | 0.0s |

### Settings button

Opens the modeless Copy Assist settings dialog for model tier, compute device and engine configuration.

| Property | Value |
|---|---|
| Kind | Push button |

### Clear

Clears the current transcript buffer.

| Property | Value |
|---|---|
| Kind | Push button |

## Indicators

### Engine status

Current state of the whisper.cpp speech-to-text engine.

| State | Meaning |
|---|---|
| Idle | Engine is not running |
| Downloading model | Model is being downloaded |
| Loading model | Model is being loaded into memory |
| Listening | Engine is actively transcribing |
| Error | Engine encountered an error |

### Backlog

Seconds of untranscribed audio in the pipeline buffer.