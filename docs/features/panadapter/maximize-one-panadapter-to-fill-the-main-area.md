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

## TX-side decoded text

When both the radio's transmitted keying and received audio are routed to the same CW decode panel, your own sending appears in cyan (`#5fc8ff`) while incoming CW appears in the standard confidence-based colors. A single space separates Tx and Rx runs of text so they do not visually merge. No leading space is added when the panel is empty or when the first decoded text is from the transmitter.

## Controls reference

| Control         | Type                 | Default                    |
|-----------------|----------------------|----------------------------|
| CW stats label  | Indicator            | —                          |
| Sens            | Slider               | 30 (range 0–100)           |
| 🔒P (Lock Pitch) | Toggle button        | —                          |
| 🔒S (Lock Speed) | Toggle button        | —                          |
| Lo (pitch min)  | Slider               | 500 Hz (range 300–1200 Hz) |
| Hi (pitch max)  | Slider               | 700 Hz (range 300–1200 Hz) |
| CPY ALL         | Button               | —                          |
| CPY VIS         | Button               | —                          |
| CLR             | Button               | —                          |
| ✕ (close CW)    | Button               | —                          |
| CW decode text  | Read-only text field | —                          |

## Notes

- The CW decode panel requires PC audio routing to function. If audio is not configured the panel shows the reminder `(requires PC Audio)`.
- The Sensitivity slider maps values 0–100 to a cost threshold of 1.0–0.1. Higher values filter out lower-confidence decodes.
- The Lo and Hi pitch sliders clamp so that Lo can never exceed Hi, and Hi can never be less than Lo.
- The Lock Pitch and Lock Speed toggle buttons freeze the decoder to the currently detected pitch or speed, preventing the decoder from tracking changes.
- When the radio is transmitting, waterfall freeze is driven by the radio's interlock TRANSMITTING state across all connected clients (Multi-Flex), eliminating the 10–23 second TX-trail artifact after unkeying.
- On radio reconnect, the desired panadapter FPS and waterfall line duration are reasserted to prevent silently dropping to the radio's 10 Hz default.
- The panadapter title bar and CW panel now use theme-aware colors via `ThemeManager::applyStyleSheet()` instead of hardcoded hex values. The title bar gradient references `{{color.text.disabled}}` and `{{color.background.1}}`, the drag grip uses `{{color.text.label}}`, and the slice title uses `{{color.text.secondary}}`. The CW panel background and border use `{{color.background.0}}` and `{{color.background.1}}` respectively. The Sensitivity slider uses the `applyPrimarySliderStyle()` helper for consistent theming.

## Related

- [Panadapter overview](overview.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)