# Pop a panadapter out into its own window

When you have more than one panadapter open, you can detach any of them into a separate floating window. This is useful for placing the panadapter on a second monitor or resizing it independently from the main AetherSDR layout.

## Before you start

- Connect to a FLEX-8600 radio. The pop-out button is only available when a radio connection is active.
- Open at least one additional panadapter. In single-panadapter mode, the pop-out button is hidden.

## Steps

1. Locate the title bar at the top of the panadapter you want to detach. It shows the slice label (for example, **Slice A**) and a row of small buttons on the right.
2. Click the **⬈** button in that title bar.

   The panadapter detaches into a floating, frameless window.

3. To move the floating window, click and drag the title strip at the top of the floating window.
4. To resize the floating window, drag the size grip in its bottom-right corner.
5. To dock the window back into the main layout, click the **↩** button in the floating window's title bar.

## What each control does

| Control | Description | Default | Notes |
|---|---|---|---|
| **⬈** (pop-out) | Detaches the panadapter into a floating window. | — | Hidden in single-panadapter mode. |
| **↩** (dock) | Returns the floating panadapter to the main layout. | — | Appears in place of ⬈ while the window is floating. |
| **□** (maximize) | Expands this panadapter to fill the main area. | — | Hidden in single-panadapter mode. |
| **×** (close) | Closes this panadapter. | — | Hidden in single-panadapter mode. |
| Slice title | Indicator showing which slice is bound to this panadapter (Slice A through Slice H). | Slice A | Read-only. |

## CW decode panel

When the CW decode panel is open, it appears below the spectrum and waterfall. The panel decodes Morse code from PC audio routed to AetherSDR.

> **Note:** CW decoding requires PC audio routing to be active. If no audio is routed, the panel shows the hint **(requires PC Audio)**.

### CW decode panel controls

| Control | Description | Default | Notes |
|---|---|---|---|
| **CW stats label** | Shows the detected pitch and speed, for example `750 Hz  20 WPM`. | — | Read-only; updated continuously by the decoder. |
| **Sens** slider | Filters low-confidence decodes. Higher values are stricter. | 30 | Maps the 0–100 range to a cost threshold of 1.0–0.1. Saved as `CwDecoderSensitivity`. |
| **🔒P** (Lock Pitch) | Locks the decoder pitch to the current tuned frequency. | Off | Toggle. |
| **🔒S** (Lock Speed) | Locks the decoder speed to the current WPM reading. | Off | Toggle. |
| **Lo** slider | Minimum pitch the decoder searches. Clamped to be no greater than **Hi**. | 500 Hz | Range: 300–1200 Hz. |
| **Hi** slider | Maximum pitch the decoder searches. Clamped to be no less than **Lo**. | 700 Hz | Range: 300–1200 Hz. |
| **CPY ALL** | Copies the full decoded text to the clipboard. | — | — |
| **CPY VIS** | Copies only the text currently visible in the scroll area. | — | — |
| **CLR** | Clears the CW decode buffer. | — | — |
| **✕** (close CW) | Hides the CW decode panel. | — | — |
| **CW decode text** | Read-only rolling display of decoded CW, coloured by decode confidence. | — | Green: cost < 0.15; Yellow: cost < 0.35; Orange: cost < 0.60; Red: cost ≥ 0.60. |

### CW decode text context menu

Right-clicking inside the **CW decode text** area opens a context menu. The menu contains the standard text editing actions (Select All, Copy, and so on) followed by a separator and a **Clear** item. Clicking **Clear** in the context menu has the same effect as clicking the **CLR** button — it empties the decode buffer immediately.

## Tips

- The floating window is frameless. Use the in-app title strip to drag it and the bottom-right size grip to resize it. There is no operating-system window border.
- The ⬈ and ↩ button labels change to reflect the current state: ⬈ when docked, ↩ when floating.
- Use **Lo** and **Hi** together to bracket the pitch range for the signal you are copying. Narrowing the range reduces false decodes when multiple CW signals are present.
- To clear decoded text quickly, right-click the decode text area and select **Clear** rather than reaching for the **CLR** button.

## Troubleshooting

- **The ⬈ button is not visible** — You have only one panadapter open. The pop-out, maximize, and close buttons are all hidden in single-panadapter mode. Open an additional panadapter to make them appear.
- **The floating window cannot be moved** — Click and drag the title strip inside the floating window, not the spectrum area. The spectrum area is used for tuning.
- **The CW decode text area shows no text** — Verify that PC audio is routed to AetherSDR. The panel displays **(requires PC Audio)** when audio is not available.

## Related

- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Panadapter overview](overview.md)