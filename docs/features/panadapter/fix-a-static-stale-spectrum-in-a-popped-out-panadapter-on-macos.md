# Panadapter Applet

## Overview

The Panadapter applet provides a container for a single panadapter display (FFT spectrum + waterfall) with a title bar and an optional CW decode panel underneath for off-air Morse decoding.

## Title Bar Controls

The title bar contains the following controls (visible only in multi-pan mode):

| Control | Type | Behavior |
|---------|------|----------|
| Slice title | Indicator | Shows which slice is bound to this panadapter (Slice A..Slice H). Uses rich text formatting for the slice letter. |
| ⬈ / ↩ (pop-out/dock) | Push button | Pops the panadapter out into a floating window or docks it back. In v0.9.5.1+, GPU resources are reset on each float/dock cycle for macOS compatibility. Floating window is frameless — drag via the title strip. |
| □ (maximize) | Push button | Maximizes this panadapter in a multi-pan layout. |
| × (close) | Push button | Closes this panadapter. |

## Spectrum and Waterfall

The main spectrum/waterfall area provides:
- Click to activate the panadapter
- Drag to tune
- Scroll to zoom

**TX-freeze behavior (v0.9.7+):** The waterfall freeze/unfreeze is driven by the radio's interlock TRANSMITTING state rather than the local MOX edge, eliminating the 10–23 second TX-trail artifact after unkeying. In Multi-Flex setups, any client transmitting triggers the freeze.

**Reconnect behavior:** On radio reconnect, the desired panadapter FPS and waterfall line duration are automatically reasserted to prevent dropping to the radio's default 10 Hz (#2465).

**Secondary panadapter dBm range:** On reconnect, secondary panadapters (Slices B–H) have their dBm range primed so the noise-floor auto-adjust starts from the correct baseline rather than the default [-50, +50] range that caused flat spectrum (#3034).

## CW Decode Panel

The CW decode panel provides off-air Morse decoding with the following controls:

### Decoder Controls

| Control | Type | Default | Range | Behavior |
|---------|------|---------|-------|----------|
| Sens | Slider | 30 | 0-100 | Filters low-confidence decodes; higher = stricter. Maps 0-100 to cost threshold 1.0-0.1. |
| 🔒P (Lock Pitch) | Toggle button | — | — | Locks the CW decoder pitch to the current tuned frequency. |
| 🔒S (Lock Speed) | Toggle button | — | — | Locks the CW decoder speed to the current WPM. |
| Pitch range | Dual-handle slider | Lo: 500, Hi: 700 | 300-1200 Hz | Minimum and maximum pitch the CW decoder searches. Values are clamped so Lo ≤ Hi. |
| WPM range | Dual-handle slider | Lo: 15, Hi: 40 | 5-60 WPM | Minimum and maximum speed the CW decoder searches. Values are clamped so Lo ≤ Hi. |

### Display Controls

| Control | Type | Behavior |
|---------|------|----------|
| CW stats label | Indicator | Shows detected CW pitch and speed (e.g., "700 Hz 25 WPM"). |
| A- (Font down) | Push button | Decreases the decoded-text font size. Settings are persisted across sessions. |
| A+ (Font up) | Push button | Increases the decoded-text font size. Settings are persisted across sessions. |
| CPY ALL | Push button | Copies the full decoded text to the clipboard. |
| CPY VIS | Push button | Copies only the text currently visible in the scroll area. |
| CLR | Push button | Clears the CW decode buffer. |
| ✕ (close CW) | Push button | Hides the CW decode panel. |

### CW Decode Panel Resizing

A thin drag grip appears along the top edge of the CW decode panel. To resize the panel:

1. Hover over the drag grip (cursor changes to a vertical resize arrow).
2. Click and drag up or down to adjust the panel height.
3. The height is persisted and restored on restart.

The drag grip allows adjusting the panel height without reparenting the GPU spectrum widget.

### Decoded Text Display

The read-only rolling display shows decoded CW with color coding by confidence:
- **Green:** < 0.15 confidence cost
- **Yellow:** < 0.35 confidence cost
- **Orange:** < 0.60 confidence cost
- **Red:** ≥ 0.60 confidence cost

The font size can be adjusted using the A- and A+ buttons, with the setting persisted across sessions.

**TX decode support (v0.9.7+):** When both incoming and outgoing CW are decoded through the same panel, transmitted text appears in cyan (#5fc8ff) to distinguish it from received text. A separator space is automatically inserted between TX and RX runs to prevent visual merging (#2417).

### Decoder Requirements

- Requires PC audio routing to the radio for off-air decoding.
- When PC audio is not configured, a "(requires PC Audio)" hint is shown.

### Theme Support (v26.6.1+)

Starting with v26.6.1, the panadapter applet theme colors are sourced from the theme system. The title bar background gradient uses `{{color.text.disabled}}`, `{{color.background.1}}`, and `#1a2a38` stop colors. The drag grip uses `{{color.text.label}}`. The slice title uses `{{color.text.secondary}}`. The CW panel background uses `{{color.background.0}}` with a border using `{{color.background.1}}`. The CW title uses `{{color.accent}}`. The CW hint uses `{{color.meter.bar.fill}}`. The CW stats label uses `{{color.text.label}}`. The Sens label uses `{{color.text.label}}`. The sensitivity slider uses `applyPrimarySliderStyle()` for themed appearance. The CW resize grip uses `{{color.background.2}}`.

## Floating Window Behavior (macOS)

**Metal GPU surface issue (v0.9.5.1+):** On macOS, popping a panadapter out into a floating window can leave the spectrum frozen. AetherSDR automatically resolves this by resetting GPU resources and re-binding the Metal rendering surface during each float/dock cycle.

### Steps to restore spectrum after freeze

1. In the panadapter title bar, click ↩ to dock the floating panadapter back into the main window.
2. Click ⬈ to pop it out again.

After step 2 the spectrum should be live.

### Tips

- If the spectrum is still static after one dock/pop cycle, repeat the cycle once more.
- Quitting and relaunching AetherSDR also clears the condition.

### Troubleshooting

- **The ⬈ pop-out button is not visible** — You are in single-pan mode. Add a second panadapter to enable multi-pan mode.
- **Spectrum is still frozen after dock/undock** — Confirm you are on v0.9.5.1 or later.

## Multi-Flex Session Support (v0.9.7+)

In Multi-Flex sessions, the slice title uses the radio-provided index letter to match the slice badge. The optional per-client letter overrides the standard A-H assignment to ensure the title matches the actual slice being displayed (#2606).

## RTTY Decode Panel (v26.6.3+)

The RTTY decode panel appears automatically when the slice mode is set to RTTY or DIGL. It provides off-air RTTY decoding with the following controls:

### Decoder Controls

| Control | Type | Default | Range | Behavior |
|---------|------|---------|-------|----------|
| BAUD | Combo box | 45.45 | 45.45, 50, 75, 100, 110, 150, 200, 300 | Selects the RTTY baud rate. |
| SHIFT | Combo box | 170 | 170, 200, 425, 850 | Selects the RTTY frequency shift. |
| CPY ALL | Push button | — | — | Copies the full decoded text to the clipboard. |
| CPY VIS | Push button | — | — | Copies only the text currently visible in the scroll area. |
| CLR | Push button | — | — | Clears the RTTY decode buffer. |
| ✕ (close RTTY) | Push button | — | — | Hides the RTTY decode panel. |

### Decoded Text Display

The read-only rolling display shows decoded RTTY characters.

### Decoder Requirements

- Requires PC audio routing to the radio for off-air decoding.
- The panel only appears when the slice mode is RTTY or DIGL.
- Baud rate and shift settings are saved per-slice and persist across sessions.

## Related

- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Panadapter overview](overview.md)