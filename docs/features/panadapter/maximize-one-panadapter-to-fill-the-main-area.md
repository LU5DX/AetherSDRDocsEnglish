# Maximize one panadapter to fill the main area

When you have more than one panadapter open, you can expand a single one to fill the entire main area, pushing the others aside temporarily.

## Before you start

- You must be connected to a FLEX-8600 radio.
- At least two panadapters must be open. In single-pan mode the maximize button is hidden.

## Steps

1. Locate the title bar of the panadapter you want to expand. It contains the slice name (for example, "Slice A"), followed by the ⬈, □, and × buttons on the right.
2. Click □ in that panadapter's title bar.

The selected panadapter expands to fill the main area.

## Tips

- To restore the multi-pan layout, click □ again on the maximized panadapter.

## Related

- [Panadapter overview](overview.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)


# CW decode panel

The CW decode panel appears beneath the spectrum and waterfall when enabled. It displays decoded Morse text and provides controls for tuning the decoder.

## CW decode text area context menu

Right-clicking anywhere in the decoded text area opens a context menu. In addition to the standard text actions (Select All, Copy, and so on), the menu contains a **Clear** entry. Click **Clear** to erase the entire CW decode buffer without leaving the text area. This is equivalent to clicking the **CLR** button in the panel toolbar.

## Controls reference

| Control | Type | Default | Description |
|---|---|---|---|
| CW stats label | Indicator | — | Shows the detected CW pitch and speed in the format `<hz> Hz  <wpm> WPM`. |
| Sens | Slider | 30 (range 0–100) | Filters low-confidence decodes. Higher values are stricter. Maps 0–100 to a cost threshold of 1.0–0.1. Setting key: `CwDecoderSensitivity`. |
| 🔒P (Lock Pitch) | Toggle button | — | Locks the CW decoder pitch to the current tuned frequency. |
| 🔒S (Lock Speed) | Toggle button | — | Locks the CW decoder speed to the current WPM. |
| Lo (pitch min) | Slider | 500 Hz (range 300–1200 Hz) | Sets the minimum pitch the CW decoder searches. Clamped to be no greater than the Hi value. |
| Hi (pitch max) | Slider | 700 Hz (range 300–1200 Hz) | Sets the maximum pitch the CW decoder searches. Clamped to be no less than the Lo value. |
| CPY ALL | Button | — | Copies the full decoded text to the clipboard. |
| CPY VIS | Button | — | Copies only the text currently visible in the scroll area to the clipboard. |
| CLR | Button | — | Clears the CW decode buffer. |
| ✕ (close CW) | Button | — | Hides the CW decode panel. |
| CW decode text | Read-only text field | — | Rolling display of decoded CW coloured by confidence: green (cost < 0.15), yellow (< 0.35), orange (< 0.60), red (≥ 0.60). Right-click for the context menu. |

## Notes

- The CW decode panel requires PC audio routing to function. If audio is not configured the panel shows the reminder `(requires PC Audio)`.

## Related

- [Panadapter overview](overview.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)