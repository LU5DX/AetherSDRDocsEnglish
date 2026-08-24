# Pop a panadapter out into its own window

When you have more than one panadapter open, you can detach any of them into a separate floating window. This is useful for placing the panadapter on a second monitor or resizing it independently from the main AetherSDR layout.

## Before you start

- Connect to a FLEX-8600 radio. The pop-out button is only available when a radio connection is active.
- Open at least one additional panadapter. In single-panadapter mode, the pop-out button is hidden. However, when a panadapter is placed on the workspace canvas, the pop-out button is always available regardless of how many panadapters are open.

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

## Workspace canvas mode

When a panadapter is placed on the workspace canvas (rather than in the standard docked layout), its title bar behaves differently:

- **Drag to move** — Click and drag the title bar to move the panadapter around the canvas. A 6-pixel threshold separates a click from a drag; after that threshold, the gesture is consumed by the canvas and moves the panadapter as a whole.
- **Click to activate** — A simple click on the title bar (without dragging past the 6-pixel threshold) activates the panadapter.
- **Pop-out always available** — The **⬈** (pop-out) button is always visible while a panadapter is on the canvas, even if it is the only panadapter open. This is because the single-panadapter button hiding is a layout economy, not a restriction on floating.
- **Mutually exclusive with floating** — Canvas-drag mode only applies when the panadapter is not floating. Floating windows use the frameless-move mechanism instead.

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

## 3D FFT view

The panadapter includes an optional 3D FFT spectrum view that displays signal history as a forward-scrolling 3D surface. This view includes:

- **Elevation shadows** — Slice flags and signal peaks cast cached elevation shadows onto the surface.
- **Smooth-scroll boundaries** — History scrolls smoothly without boundary jumps.
- **Bandwidth-zoom floor resynchronization** — The floor level resynchronizes after a bandwidth zoom to maintain accurate depth perception.

Toggle the **3D FFT view** to enable or disable this display mode. It is part of the spectrum widget and is disabled by default.

## Waterfall freeze during transmission

When any client in a Multi-Flex session begins transmitting, the waterfall in this panadapter freezes automatically. It resumes updating when transmission ends. This eliminates the 10–23 second TX-trail artifact that previously appeared after unkeying. The freeze is driven by the radio's interlock (TRANSMITTING) state, so it applies regardless of which client initiates the transmission.

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
- When on the workspace canvas, click the title bar to activate a panadapter or drag it to reposition. A 6-pixel threshold separates click from drag.
- The **⬈** pop-out button is always available while a panadapter is on the canvas, even if it is the only one open.

## Troubleshooting

- **The ⬈ button is not visible** — You have only one panadapter open and it is not on the workspace canvas. The pop-out, maximize, and close buttons are all hidden in single-panadapter stack mode. Open an additional panadapter or move the panadapter to the canvas to make them appear.
- **The floating window cannot be moved** — Click and drag the title strip inside the floating window, not the spectrum area. The spectrum area is used for tuning.
- **A panadapter on the canvas cannot be dragged** — Click and drag the title bar, not the spectrum area. A 6-pixel drag threshold must be exceeded before the panadapter starts moving. If the panadapter is floating, the canvas-drag mode is disabled; dock it first.
- **The CW decode text area shows no text** — Verify that PC audio is routed to AetherSDR. The panel displays **(requires PC Audio)** when audio is not available.

## Related

- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Panadapter overview](overview.md)