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

| Control          | Description                                                                          | Default |
|------------------|--------------------------------------------------------------------------------------|---------|
| **⬈** (pop-out)  | Detaches the panadapter into a floating window.                                      | —       |
| **↩** (dock)     | Returns the floating panadapter to the main layout.                                  | —       |
| **□** (maximize) | Expands this panadapter to fill the main area.                                       | —       |
| **×** (close)    | Closes this panadapter.                                                              | —       |
| Slice title      | Indicator showing which slice is bound to this panadapter (Slice A through Slice H). | Slice A |

> **Note for Multi-Flex sessions:** When using multiple clients, the slice title matches the radio-provided index letter so the title corresponds to the slice badge.

## CW decode panel

When the CW decode panel is open, it appears below the spectrum and waterfall. The panel decodes Morse code from PC audio routed to AetherSDR. Both received (RX) and transmitted (TX) CW are decoded and displayed in the same panel, with different colors to distinguish them.

> **Note:** CW decoding requires PC audio routing to be active. If no audio is routed, the panel shows the hint **(requires PC Audio)**.

### CW decode panel controls

| Control | Description | Default | Notes |
|---|---|---|---|
| **CW stats label** | Shows the detected pitch and speed, for example `750 Hz  20 WPM`. | — | Read-only; updated continuously by the decoder. |
| **Sens** slider | Filters low-confidence decodes. Higher values are stricter. | 30 | Maps the 0–100 range to a cost threshold of 1.0–0.1. Saved as `CwDecoderSensitivity`. |
| **🔒P** (Lock Pitch) | Locks the decoder pitch to the current tuned frequency. | Off | Toggle. |
| **🔒S** (Lock Speed) | Locks the decoder speed to the current WPM reading. | Off | Toggle. |
| **Pitch** range slider | Sets the minimum and maximum pitch the decoder searches. | 500–700 Hz | Range: 300–1200 Hz. Double-handle slider replaces the separate **Lo** and **Hi** sliders. |
| **WPM** range slider | Sets the minimum and maximum speed the decoder searches. | 15–40 WPM | Range: 5–60 WPM. |
| **CPY ALL** | Copies the full decoded text to the clipboard. | — | — |
| **CPY VIS** | Copies only the text currently visible in the scroll area. | — | — |
| **A-** | Decreases the decoded-text font size by 1 pixel. | — | Persisted across sessions via `CwDecodeSettings::fontPx`. Range: 8–32 px. |
| **A+** | Increases the decoded-text font size by 1 pixel. | — | Persisted across sessions via `CwDecodeSettings::fontPx`. Range: 8–32 px. |
| **CLR** | Clears the CW decode buffer. | — | — |
| **✕** (close CW) | Hides the CW decode panel. | — | — |
| **CW decode text** | Read-only rolling display of decoded CW, coloured by decode confidence. | — | Green: cost < 0.15; Yellow: cost < 0.35; Orange: cost < 0.60; Red: cost ≥ 0.60. TX-originated text appears in cyan (#5fc8ff). |
| **Drag grip** (thin strip at top of CW panel) | Drag up or down to resize the CW decode panel height. | — | Vertical size cursor. Panel height persisted via `CwDecodeSettings::panelHeight`. Range: 60–600 px. |

### CW decode text behaviour

The CW decode panel now displays both received (RX) and transmitted (TX) Morse decoding in a single rolling text area:

- **RX text** — Coloured by confidence as described above (green, yellow, orange, red).
- **TX text** — Rendered in cyan (#5fc8ff) so you can distinguish your own sending from incoming CW.
- **Boundary handling** — When switching between TX and RX, a space is inserted automatically so the colored runs do not visually merge.
- **Source tracking** — The decoder tracks whether the last decoded text came from TX or RX to apply the correct separator logic.

### CW decode text context menu

Right-clicking inside the **CW decode text** area opens a context menu. The menu contains the standard text editing actions (Select All, Copy, and so on) followed by a separator and a **Clear** item. Clicking **Clear** in the context menu has the same effect as clicking the **CLR** button — it empties the decode buffer immediately.

### CW decode panel font size

The decoded-text font size defaults to 13 pixels. Use the **A-** and **A+** buttons to decrease or increase the font size by 1 pixel per click. The size is clamped to the range 8–32 pixels and is persisted across sessions via the `CwDecodeSettings` configuration.

### CW decode panel height

Drag the thin horizontal grip at the top of the CW decode panel up or down to resize the panel height. The height is clamped to the range 60–600 pixels and is persisted across sessions via the `CwDecodeSettings` configuration. A taller panel reveals more decoded-text history.

## Waterfall freeze during transmission

When any client in a Multi-Flex session begins transmitting, the waterfall in this panadapter freezes automatically. It resumes updating when transmission ends. This eliminates the 10–23 second TX-trail artifact that previously appeared after unkeying.

On radio reconnection, the panadapter reasserts the desired frame rate and waterfall line duration to prevent silently dropping to the radio's default 10 Hz.

Secondary panadapters (Slices B–H) have their dBm range primed on reconnection so the noise-floor auto-adjust starts from the correct baseline rather than the default [-50, +50] range that caused a flat spectrum on reconnect.

## RTTY decode panel

When the active slice mode is RTTY or DIGL, an RTTY decode panel appears below the spectrum and waterfall. This panel decodes RTTY signals from the PC audio routed to AetherSDR. The panel has a fixed height of 90 pixels and is hidden when the slice mode is not RTTY or DIGL.

> **Note:** RTTY decoding requires PC audio routing to be active.

## Theme support

The panadapter title bar, CW decode panel, RTTY decode panel, and all associated controls now use theme-aware color tokens (subject to change in future releases). The visual appearance adapts to the active theme without requiring manual style overrides.

## Tips

- The floating window is frameless. Use the in-app title strip to drag it and the bottom-right size grip to resize it. There is no operating-system window border.
- The ⬈ and ↩ button labels change to reflect the current state: ⬈ when docked, ↩ when floating.
- Use the **Pitch** range slider to bracket the pitch range for the signal you are copying. Narrowing the range reduces false decodes when multiple CW signals are present.
- Use the **WPM** range slider to bracket the speed range for the signal you are copying. Narrowing the range reduces false decodes when multiple CW signals are present.
- To clear decoded text quickly, right-click the decode text area and select **Clear** rather than reaching for the **CLR** button.
- TX-side decoded text appears in cyan to help you distinguish your own sending from incoming CW, without needing a textual prefix.
- Use the **A-** and **A+** buttons to adjust the decoded-text font size for better readability.
- Drag the thin grip at the top of the CW decode panel to reveal more decoded-text history.

## Troubleshooting

- **The ⬈ button is not visible** — You have only one panadapter open. The pop-out, maximize, and close buttons are all hidden in single-panadapter mode. Open an additional panadapter to make them appear.
- **The floating window cannot be moved** — Click and drag the title strip inside the floating window, not the spectrum area. The spectrum area is used for tuning.
- **The CW decode text area shows no text** — Verify that PC audio is routed to AetherSDR. The panel displays **(requires PC Audio)** when audio is not available.

## Related

- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Panadapter overview](overview.md)