# Close an extra panadapter

When you have multiple panadapters open in a multi-slice layout, you can close any extra one to reclaim screen space. This page explains how to close a panadapter you no longer need.

## Before you start

- Your radio must be connected. The × (close) button is only available when AetherSDR is connected to a FLEX-8600.
- You must have more than one panadapter open. The × (close) button is hidden in single-pan mode.

## Steps

1. Locate the title bar of the panadapter you want to close. It sits at the top of the panadapter and shows a label such as "Slice A" or "Slice B".
2. Click the × button at the right end of that title bar.

The panadapter closes immediately. The remaining panadapters expand to fill the available space.

## Tips

- If you cannot see the × button, you are in single-pan mode — only one panadapter is open, and closing it is not permitted.
- If the panadapter has been popped out into a floating window, the × button is still in the floating window's title bar at the top right. Click it there.

## Troubleshooting

- **The × button is not visible** — The radio is either disconnected or only one panadapter is open. AetherSDR hides the × button in both cases. Connect to the radio and add a second panadapter before trying again.

## CW decode panel

The CW decode panel appears below the panadapter spectrum and waterfall when CW decoding is active. It shows decoded Morse code text, detection statistics, and controls for tuning the decoder.

### CW panel resizing (v26.7.4)

In v26.7.4 the CW decode panel can be resized vertically by dragging the thin resize grip at the top edge of the panel. Drag downward to increase the panel height and reveal more decoded text history, or drag upward to decrease it. The panel height persists between sessions via the `CwDecodeSettings::panelHeight()` setting, clamped between 60 and 600 pixels.

### CW decode text font size (v26.7.4)

In v26.7.4 the decoded text font size can be adjusted using the **A+** and **A-** buttons in the CW panel toolbar. Each click increases or decreases the font size by 1 pixel, clamped between 8 and 32 pixels. The font size persists between sessions via the `CwDecodeSettings::fontPx()` setting.

### CW decode text context menu

Right-clicking anywhere inside the CW decode text area opens a context menu. In addition to the standard text editing commands (Select All, Copy, and so on), the menu includes a **Clear** item. Choosing **Clear** erases the entire CW decode buffer immediately. This is equivalent to clicking the **CLR** button in the CW panel toolbar.

### CW decode TX/RX coloring

In the CW decode panel, received text and transmitted (self-sent) text are rendered in different colors so you can distinguish your own sending from incoming CW. The colors are:

- **Green**: Confidence cost < 0.15 (high confidence)
- **Yellow**: Confidence cost < 0.35
- **Orange**: Confidence cost < 0.60
- **Red**: Confidence cost >= 0.60 (low confidence)
- **Cyan** (`#5fc8ff`): Text decoded from your own transmitted keying

When switching between transmit and receive, a space is automatically inserted to prevent the colored text runs from merging together.

### CW decoder controls

The CW decoder toolbar includes the following controls:

| Control | Type | Description |
|---------|------|-------------|
| CW stats label | Indicator | Shows detected CW pitch and speed as `<hz> Hz  <wpm> WPM` |
| Sens | Slider (0-100) | Filters low-confidence decodes; higher values mean stricter filtering. Maps to a cost threshold from 1.0 (0) to 0.1 (100). Setting key: `CwDecoderSensitivity` |
| 🔒P (Lock Pitch) | Toggle button | Locks the CW decoder pitch to the current tuned frequency |
| 🔒S (Lock Speed) | Toggle button | Locks the CW decoder speed to the current WPM |
| Pitch range slider | Range slider (300-1200 Hz) | Double-handle slider to set the minimum and maximum pitch for the CW decoder search. Default: 500-700 Hz |
| WPM range slider | Range slider (5-60 WPM) | Double-handle slider to set the minimum and maximum speed for the CW decoder search. Default: 15-40 WPM |
| A- (font size down) | Button | Decreases the decoded-text font size by 1 pixel (v26.7.4) |
| A+ (font size up) | Button | Increases the decoded-text font size by 1 pixel (v26.7.4) |
| CPY ALL | Button | Copies the full decoded text to the clipboard |
| CPY VIS | Button | Copies only the text currently visible in the scroll area |
| CLR | Button | Clears the CW decode buffer |
| ✕ (close CW) | Button | Hides the CW decode panel |

### CW hint indicator

When PC audio routing is required but not configured, a hint label appears in the CW panel reminding you that "(requires PC Audio)".

## RTTY decode panel (v26.6.3)

Starting in v26.6.3, AetherSDR includes an RTTY decode panel that appears below the panadapter when the active slice mode is set to RTTY or DIGL. The panel functions similarly to the CW decode panel but for RTTY decoding.

The RTTY panel includes a dropdown to select the RTTY decoder algorithm and controls for adjusting the decoder parameters. The panel is hidden by default and only appears when the slice mode is set appropriately.

## Slice title with Multi-Flex

In Multi-Flex sessions, the slice title shown in the panadapter title bar uses the radio-provided index letter so the title matches the slice badge. This ensures consistency when multiple clients are connected to the same radio.

## Waterfall freeze behavior

The waterfall automatically freezes when any client in a Multi-Flex session begins transmitting. The freeze state is driven by the radio's interlock TRANSMITTING state rather than the local MOX edge, eliminating the 10-23 second TX-trail artifact that could appear after unkeying.

On radio reconnect, the desired panadapter FPS and waterfall line duration are reasserted to prevent silently dropping to the radio's 10 Hz default. Additionally, secondary panadapters (Slices B–H) have their dBm range primed on reconnect so the noise-floor auto-adjust starts from the correct baseline rather than the default [-50, +50] range that caused flat spectrum on reconnect.

## Panadapter theming (v26.6.1)

In v26.6.1, the panadapter and its CW decode panel now use theme-aware styling instead of hardcoded colors. The title bar gradient, drag grip dots, slice title, stats labels, and CW panel background all reference theme color tokens. This means the panadapter automatically adapts to light and dark themes without requiring manual color overrides. The theme system replaces the previous fixed-color stylesheets with token-based values such as `{{color.background.1}}`, `{{color.text.secondary}}`, and `{{color.accent}}`.

## 3D FFT spectrum view (v26.7.x)

Starting in v26.7.x, the panadapter includes an optional 3D FFT spectrum view. When enabled, signal history is displayed as a forward-scrolling 3D surface with elevation shadows and smooth-scroll boundaries. Slice flags cast cached elevation shadows on the surface. The floor resynchronizes automatically after a bandwidth zoom.

Use the **3D FFT view** toggle button to enable or disable this view. The button is part of the SpectrumWidget and defaults to disabled.

## Canvas hosting (v26.8.4)

In v26.8.4, a panadapter on the workspace canvas behaves as a live-move item. When the panadapter is hosted on the canvas (rather than in the older stack layout), dragging its title strip streams the move gesture directly to the canvas — the same mechanism used by other canvas items — instead of the old floating-window drag. A 6-pixel threshold separates a click (which activates the panadapter) from a drag.

When a panadapter is on the canvas, the pop-out button (⬈) is always visible, even if it is the only panadapter present. This is intentional: the single-pan button hiding applies only to the stacked layout, not to canvas items, which can always be popped out.

## Related

- [Panadapter overview](overview.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)