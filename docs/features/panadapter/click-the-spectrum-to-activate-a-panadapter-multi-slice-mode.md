# Click the spectrum to activate a panadapter (multi-slice mode)

In a multi-panadapter layout, only one panadapter is active at a time. Clicking the spectrum area of an inactive panadapter brings it into focus so that your controls, slices, and tuning apply to it.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- At least two panadapters must be open. In single-panadapter mode, the title bar buttons (⬈, □, ×) are hidden and there is nothing to switch between.

## Steps

1. Locate the panadapter you want to activate. Its title bar shows the slice it is bound to (for example, "Slice B").
2. Click anywhere on the Spectrum / waterfall area of that panadapter.
3. The panadapter is now active. Tuning, scroll-to-zoom, and all slice controls apply to it.

## What each control does

| Control | Kind | Default | Range | Persisted key |
|---|---|---|---|---|
| Slice title | Indicator | Slice A | Slice A – Slice H | — |
| Spectrum / waterfall | Click / drag area | — | — | — |
| ⬈ / ↩ (pop-out/dock) | Push button | — | — | — |
| □ (maximize) | Push button | — | — | — |
| × (close) | Push button | — | — | — |
| Sens | Slider | 30 | 0 – 100 | `CwDecoderSensitivity` |
| 🔒P (Lock Pitch) | Toggle button | — | — | — |
| 🔒S (Lock Speed) | Toggle button | — | — | — |
| Lo (pitch min) | Slider | 500 Hz | 300 – 1200 Hz | — |
| Hi (pitch max) | Slider | 700 Hz | 300 – 1200 Hz | — |
| CPY ALL | Push button | — | — | — |
| CPY VIS | Push button | — | — | — |
| CLR | Push button | — | — | — |
| ✕ (close CW) | Push button | — | — | — |
| CW decode text | Read-only text field | — | — | — |

The ⬈ / ↩, □, and × buttons are hidden in single-panadapter mode. They appear only when more than one panadapter is open.

## CW decode panel

The CW decode panel appears beneath the spectrum when enabled. It requires PC audio routing to function — a "(requires PC Audio)" reminder is shown when audio is not yet routed.

Decoded text is coloured by confidence level:

| Colour | Cost threshold |
|---|---|
| Green | below 0.15 |
| Yellow | 0.15 – below 0.35 |
| Orange | 0.35 – below 0.60 |
| Red | 0.60 and above |

The **Sens** slider maps the 0 – 100 range to a cost threshold of 1.0 – 0.1. Higher values filter out lower-confidence decodes.

The **Lo** and **Hi** sliders set the pitch search range. Lo is clamped to be no greater than Hi, and Hi is clamped to be no less than Lo.

Click **CPY ALL** to copy the entire decoded text buffer to the clipboard. Click **CPY VIS** to copy only the text currently visible in the scroll area. Click **CLR** to clear the decode buffer. Click **✕ (close CW)** to hide the panel.

### Right-click menu on the CW decode text area

Right-clicking inside the CW decode text area opens a context menu. In addition to the standard text actions (Select All, Copy, and so on), the menu includes a **Clear** item. Selecting **Clear** has the same effect as clicking the **CLR** button — it clears the decode buffer.

## Tips

- Drag on the Spectrum / waterfall area to tune the slice frequency. Scroll to zoom the span.
- To give one panadapter more screen space without closing others, click □ (maximize) in its title bar. See [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md).
- To move a panadapter to a separate window, click ⬈ (pop-out). See [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md).

## Related

- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)