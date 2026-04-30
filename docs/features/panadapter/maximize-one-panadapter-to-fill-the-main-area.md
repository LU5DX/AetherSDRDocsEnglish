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

## Related

- [Panadapter overview](overview.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)