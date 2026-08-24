# Panadapter Applet

The Panadapter applet is a container for a single panadapter display (FFT spectrum + waterfall) with a title bar offering drag grip, pop-out, maximize, and close controls. An optional CW decode panel can appear underneath for off-air Morse decoding. A 3D FFT spectrum view is also available for visualizing signal history as a scrolling 3D surface.

## Controls

| Control | Kind | Default | Range | Setting Key | Behavior | Notes |
|---------|------|---------|-------|-------------|----------|-------|
| Slice title | indicator | "Slice A" | Slice A..Slice H | *none* | Shows which slice is bound to this panadapter. | |
| ⬈ / ↩ (pop-out/dock) | push_button | | | *none* | Pops the panadapter out into a floating window or docks it back. Hidden in single-pan mode. | Floating window is frameless. Drag via the in-app title strip, resize via the bottom-right size grip. On macOS, every float/dock cycle resets GPU resources prevents spectrum from going stale. |
| □ (maximize) | push_button | | | *none* | Maximizes this panadapter in a multi-pan layout. Hidden in single-pan mode. |
| × (close) | push_button | | | *none* | Closes this panadapter. Hidden in single-pan mode. |
| Spectrum / waterfall | drag_handle | | | *none* | Click activates the panadapter; drag to tune, scroll to zoom. | |
| CW stats label | indicator | | | *none* | Shows detected CW pitch and speed (e.g. "700 Hz 20 WPM"). | |
| Sens (CW decoder sensitivity) | slider | 30 | 0-100 | CwDecoderSensitivity | Filters low-confidence decodes. Higher values are stricter. | Maps 0-100 to cost threshold 1.0-0.1. |
| 🔒P (Lock Pitch) | toggle_button | | | *none* | Locks the CW decoder pitch to the current tuned frequency. | |
| 🔒S (Lock Speed) | toggle_button | | | *none* | Locks the CW decoder speed to the current WPM. | |
| Lo (pitch min) | slider | 500 | 300-1200 Hz | *none* | Minimum pitch the CW decoder searches. Automatically clamped to ≤ Hi. | |
| Hi (pitch max) | slider | 700 | 300-1200 Hz | *none* | Maximum pitch the CW decoder searches. Automatically clamped to ≥ Lo. | |
| A- (font size down) | push_button | | | *none* | Decreases the decoded-text font size by 1 pixel. | Persisted between sessions. New in v26.7.4. |
| A+ (font size up) | push_button | | | *none* | Increases the decoded-text font size by 1 pixel. | Persisted between sessions. New in v26.7.4. |
| CPY ALL | push_button | | | *none* | Copies all decoded text to the clipboard. | |
| CPY VIS | push_button | | | *none* | Copies only the text currently visible in the scroll area. | |
| CLR | push_button | | | *none* | Clears the CW decode buffer. | |
| ✕ (close CW) | push_button | | | *none* | Hides the CW decode panel entirely. | |
| CW decode text | text_field | | | *none* | Read-only rolling display of decoded CW text. Colored by confidence: green (<0.15), yellow (<0.35), orange (<0.60), red (≥0.60). | Font size adjustable via A+/A- controls. |
| 3D FFT view | toggle_button | Disabled | | *none* | Toggles the 3D FFT spectrum view. Shows signal history as a forward-scrolling 3D surface with elevation shadows, smooth-scroll boundaries, and resynchronized floor after bandwidth zoom. Slice flags cast cached elevation shadows. | New in v26.7.x (#4413-#4477). Part of SpectrumWidget. |

## CW Decode Panel Controls

The CW decode panel appears at the bottom of the panadapter when CW mode is active. It contains:

- **Drag resize grip**: A thin 4-pixel strip along the top edge of the panel. Drag up or down to resize the panel height and reveal more decoded text history. The panel height is persisted between sessions (range: 60-600 pixels).
- **Stats bar**: Shows detected CW pitch (Hz) and speed (WPM).
- **Sensitivity slider**: Adjusts decoder sensitivity (0-100).
- **Pitch lock/speed lock toggles**: Lock the current pitch or speed values.
- **Pitch range sliders**: Set minimum and maximum pitch search range (300-1200 Hz).
- **Font size controls**: A- and A+ buttons adjust the decoded text font size (8-32 pixels). Changes are persisted and restored on next launch.
- **Copy buttons**: CPY ALL copies all decoded text; CPY VIS copies only visible text.
- **CLR button**: Clears the decode buffer.
- **Close button (✕)**: Closes the CW decode panel.

## Waterfall Freeze Behavior

The waterfall automatically freezes when the radio enters TRANSMITTING state based on the radio's interlock system. It unfreezes when the TRANSMITTING state clears. This behavior tracks the radio's actual hardware interlock state rather than a local software edge, eliminating the 10-23 second TX trail artifact that could appear after unkeying in earlier versions.

- In a multiFLEX session, any connected client transmitting triggers the waterfall freeze on your panadapter.
- On radio reconnect, the desired panadapter FPS and waterfall line duration are automatically reasserted to prevent dropping to the radio's 10 Hz default.

## Secondary Panadapter Initialization

Secondary panadapters (Slices B-H) now have their dBm range primed on reconnect to the radio. This ensures the noise-floor auto-adjust starts from the correct baseline rather than the default [-50, +50] range that could cause a flat spectrum display after reconnection.

## Canvas Mode (v26.8.4)

When hosted on the workspace canvas, the panadapter's title strip streams a live-move gesture that mirrors the container title bar's canvas mode. This is a real gesture the canvas session follows, not a QDrag ghost.

- The title strip is accessible by the automation bridge via its accessible name `panTitleBar`.
- A 6 px drag threshold separates a click (which activates the panadapter) from a drag.
- Everything past the threshold is consumed by the canvas gesture so the floating-drag machinery never sees it.
- A canvas item can always pop out (even as the only pan), since the single-pan button hiding is a stack-mode economy, not a rule about floating. When the item is off-canvas, the stack's `setMultiPanMode()` re-applies its economy.
- Canvas drag signals (`canvasDragBegan`, `canvasDragMoved`, `canvasDragEnded`) are emitted with global positions only while the applet is on-canvas and not floating.

## Indicators

| Label | Possible States | Meaning |
|-------|----------------|---------|
| CW stats | `<hz> Hz <wpm> WPM` | Detected pitch and speed from the ggmorse decoder |
| CW hint | (requires PC Audio) | Reminder that the CW decoder needs PC audio routing to work |

## Behavior Details

### Pop-out/Dock
When docked, clicking ⬈ pops the panadapter into a floating window. When floating, clicking ↩ docks it back. The pop-out button is hidden in single-pan mode. Floating windows are frameless and can be dragged by the title strip and resized by the bottom-right size grip. On macOS, each float/dock cycle resets GPU resources to keep the spectrum live. Saved floating-window state is not restored when subsequent panadapters are added, preventing blank floating windows from spawning.

### Sizing and Layout
- Slider bars use a `GuardedSlider` to prevent signal loops during programmatic changes.
- The CW decode panel height is settable between 60 and 600 pixels.
- The decode text font size ranges from 8 to 32 pixels, adjustable in 1-pixel increments.