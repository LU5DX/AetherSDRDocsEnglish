# Panadapter overview

The panadapter displays a real-time FFT spectrum and waterfall for a radio slice, letting you visualise band activity and tune by clicking or dragging. Each panadapter can also show an optional CW decode panel that reads Morse off-air directly in the application, and an optional RTTY decode panel for RTTY/DIGL modes.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The panadapter requires an active radio connection.
- For CW decoding, PC audio routing to AetherSDR must be configured. The panel displays a "(requires PC Audio)" reminder when this is not in place.

## How it works

AetherSDR opens with one panadapter visible in the centre of the main window. It is always present; you cannot close the last panadapter. In multi-slice mode, additional panadapters appear, each in its own titled container. Every panadapter is bound to one slice (Slice A through Slice H), shown in the title bar. In Multi-Flex sessions, the title uses the radio-provided index letter so it matches the slice badge.

**Spectrum and waterfall.** The upper portion of the panadapter shows the FFT spectrum trace; below it is the waterfall. Click anywhere on the spectrum or waterfall to activate that panadapter. Drag to pan across the band. Scroll to zoom. The `View > Single-Click to Tune` and `View > Pan Follows VFO` menu items affect how clicking and scrolling interact with the VFO.

**Title bar.** The 16-pixel title bar across the top of each panadapter carries the slice label, a drag grip, and (in multi-slice mode) the pop-out, maximize, and close buttons. In single-pan mode those three buttons are hidden. The title bar uses theme-aware colour tokens for the gradient background and text labels.

**Waterfall freeze behaviour.** When any connected client begins transmitting, the waterfall freezes automatically. It unfreezes when transmission stops, eliminating the 10–23 second TX-trail artifact that previously appeared after unkeying.

**Reconnection behaviour.** On radio reconnect, the panadapter FPS and waterfall line duration are reasserted to prevent silently dropping to the radio's 10 Hz default.

**CW decode panel.** An optional panel can appear beneath the waterfall. It runs an off-air Morse decoder and displays decoded text in a rolling read-only field, colour-coded by decoder confidence. The panel is hidden by default and is enabled from the CW mode controls. See [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).

**RTTY decode panel.** An optional panel can appear beneath the waterfall when the slice mode is RTTY or DIGL. It displays decoded RTTY text in a rolling read-only field. The panel is hidden by default and is enabled from the RTTY/DIGL mode controls.

## What each control does

### Title bar

| Control | Kind | Behavior | Notes |
|---|---|---|---|
| Slice title | Indicator | Shows the slice bound to this panadapter. Values: Slice A – Slice H. In Multi-Flex sessions, uses the radio-provided index letter. | — |
| ⬈ / ↩ (pop-out/dock) | Button | Pops the panadapter into a floating window, or docks it back. | Hidden in single-pan mode. The floating window is frameless; drag via the in-app title strip, resize via the bottom-right size grip. On macOS, GPU resources are reset each float/dock cycle to keep the spectrum live. |
| □ (maximize) | Button | Maximizes this panadapter to fill the main layout area. | Hidden in single-pan mode. |
| × (close) | Button | Closes this panadapter. | Hidden in single-pan mode. |

### Spectrum / waterfall

| Control | Kind | Behavior |
|---|---|---|
| Spectrum / waterfall | Display and drag area | Click to activate the panadapter. Drag to pan. Scroll to zoom. |

### CW decode panel

| Control | Kind | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|---|
| CW stats label | Indicator | — | `<hz> Hz  <wpm> WPM` | — | Shows the pitch and speed currently detected by the decoder. |
| Sens | Slider | 30 | 0 – 100 | `CwDecoderSensitivity` | Filters low-confidence decodes. Higher values are stricter. Internally maps the 0 – 100 range to a cost threshold of 1.0 – 0.1. Uses themed slider styling via `applyPrimarySliderStyle`. |
| 🔒P (Lock Pitch) | Toggle button | Off | On / Off | — | Locks the decoder pitch to the currently tuned frequency. |
| 🔒S (Lock Speed) | Toggle button | Off | On / Off | — | Locks the decoder speed to the current WPM reading. |
| Pitch (range slider) | Range slider | 500 – 700 Hz | 300 – 1200 Hz | — | Sets the minimum and maximum pitch the decoder searches. Uses a dual-handle slider; Lo and Hi are adjusted together. |
| WPM (range slider) | Range slider | 15 – 40 WPM | 5 – 60 WPM | — | Sets the minimum and maximum speed (WPM) the decoder searches. Uses a dual-handle slider. |
| CPY ALL | Button | — | — | — | Copies the full decoded text buffer to the clipboard. |
| CPY VIS | Button | — | — | — | Copies only the text currently visible in the scroll area to the clipboard. |
| CLR | Button | — | — | — | Clears the CW decode buffer. |
| × (close CW) | Button | — | — | — | Hides the CW decode panel. |
| CW decode text | Read-only text field | — | — | — | Rolling display of decoded Morse, colour-coded by confidence: green (<0.15 cost), yellow (<0.35), orange (<0.60), red (>=0.60). Right-click the text area to open a context menu; the menu includes standard text actions and a **Clear** item that clears the decode buffer. |

### TX-side CW decode

When your own transmitted signal is routed back through PC audio to AetherSDR, the decoder can also display your transmitted Morse. Your transmitted text appears in a distinct cyan colour (#5fc8ff) to differentiate it from received signals. A separator space is automatically inserted between receive and transmit text, and between transmit and receive text, to prevent the colour runs from visually merging.

| Behaviour | Detail |
|---|---|
| TX text colour | Cyan (#5fc8ff) |
| Separator insertion | Automatic space added on TX→RX and RX→TX transitions |
| Confidence filter | Same `Sens` slider threshold applies to both receive and transmit paths |

### RTTY decode panel

| Control | Kind | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|---|
| CPY ALL | Button | — | — | — | Copies the full decoded RTTY text buffer to the clipboard. |
| CPY VIS | Button | — | — | — | Copies only the RTTY text currently visible in the scroll area to the clipboard. |
| CLR | Button | — | — | — | Clears the RTTY decode buffer. |
| × (close RTTY) | Button | — | — | — | Hides the RTTY decode panel. |
| RTTY decode text | Read-only text field | — | — | — | Rolling display of decoded RTTY characters. Right-click the text area to open a context menu; the menu includes standard text actions and a **Clear** item that clears the decode buffer. |

## Theme integration

All visual elements of the panadapter now use theme-aware colour tokens instead of hardcoded hex values:

- **Container:** The panadapter widget is registered with the theme system as `applet/panadapter`.
- **Title bar gradient:** Uses `{{color.text.disabled}}`, `{{color.background.1}}` tokens.
- **Drag grip dots:** Uses `{{color.text.label}}` token.
- **Slice title:** Uses `{{color.text.secondary}}` token.
- **CW panel background:** Uses `{{color.background.0}}` and `{{color.background.1}}` tokens.
- **CW title:** Uses `{{color.accent}}` token.
- **CW hint:** Uses `{{color.meter.bar.fill}}` token.
- **CW stats label:** Uses `{{color.text.label}}` token.
- **Sensitivity slider:** Styled via `applyPrimarySliderStyle()`.

This ensures the panadapter appearance adapts to the selected theme without manual colour overrides.

## Tips

- The Pitch range slider constrains the frequency range the decoder searches. Narrowing this range around the expected CW tone reduces false decodes on a busy band.
- The WPM range slider constrains the speed range the decoder searches. Narrowing this range around the expected sending speed reduces false decodes.
- Decoded text colour reflects decoder confidence. Green text is the most reliable; red text should be treated with caution. Adjust Sens upward to suppress red and orange characters if noise is producing junk output.
- `CwDecoderSensitivity` is persisted across sessions. You do not need to re-tune it each time you open the application.
- You can clear the decode buffer from the keyboard-free right-click context menu on the decoded text area as an alternative to clicking CLR.
- When viewing both transmitted and received CW in the same panel, the cyan TX text helps you identify your own keying. No textual "[TX]" prefix is added — colour alone distinguishes the source.
- The RTTY decode panel automatically appears when the slice mode is set to RTTY or DIGL.

## Related

- [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md)
- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)