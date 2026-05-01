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

| Control              | Kind                                                                                                 | Default                                                                                                                                                                                                                                                                                                                                         |
|----------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Slice title          | Indicator                                                                                            | Slice A                                                                                                                                                                                                                                                                                                                                         |
| Spectrum / waterfall | Click / drag area                                                                                    | —                                                                                                                                                                                                                                                                                                                                               |
| ⬈ / ↩ (pop-out/dock) | Pops the panadapter out into a floating window or docks it back; emits popOutClicked or dockClicked. | Hidden in single-pan mode. Floating window is frameless (v0.9.0, #1922) — drag via the in-app title strip, resize via the bottom-right size grip; see 00-navigation.json for the shared frameless chrome. v0.9.3: floating window inherits dark theme on creation (#2096); geometry is saved before close to fix restore-position race (#2154). |
| □ (maximize)         | Push button                                                                                          | —                                                                                                                                                                                                                                                                                                                                               |
| × (close)            | Push button                                                                                          | —                                                                                                                                                                                                                                                                                                                                               |
| Sens                 | Slider                                                                                               | 30                                                                                                                                                                                                                                                                                                                                              |
| 🔒P (Lock Pitch)      | Toggle button                                                                                        | —                                                                                                                                                                                                                                                                                                                                               |
| 🔒S (Lock Speed)      | Toggle button                                                                                        | —                                                                                                                                                                                                                                                                                                                                               |
| Lo (pitch min)       | Slider                                                                                               | 500 Hz                                                                                                                                                                                                                                                                                                                                          |
| Hi (pitch max)       | Slider                                                                                               | 700 Hz                                                                                                                                                                                                                                                                                                                                          |
| CPY ALL              | Push button                                                                                          | —                                                                                                                                                                                                                                                                                                                                               |
| CPY VIS              | Push button                                                                                          | —                                                                                                                                                                                                                                                                                                                                               |
| CLR                  | Push button                                                                                          | —                                                                                                                                                                                                                                                                                                                                               |
| ✕ (close CW)         | Push button                                                                                          | —                                                                                                                                                                                                                                                                                                                                               |
| CW decode text       | Read-only text field                                                                                 | —                                                                                                                                                                                                                                                                                                                                               |
| Start Sweep          | Push button                                                                                          | —                                                                                                                                                                                                                                                                                                                                               |
| Clear Sweep          | Push button                                                                                          | —                                                                                                                                                                                                                                                                                                                                               |
| PWR (sweep power)    | Slider                                                                                               | 1 W                                                                                                                                                                                                                                                                                                                                             |

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

## ANT panel SWR sweep controls

The ANT panel includes controls for running a low-power SWR sweep across the current TX band and displaying the result on the panadapter.

- **Start Sweep** — runs a low-power tune sweep across the current TX band and plots SWR on the panadapter. The sweep uses the slice associated with the current panel and the power level set by the PWR slider. When a TGXL antenna tuner is in use, the sweep automatically bypasses the tuner before sweeping and restores the original tuner state when it finishes or is aborted.
- **Clear Sweep** — removes the displayed SWR sweep trace from the panadapter.
- **PWR slider** — sets the carrier power used during the sweep. Range is 1 W to 10 W. The current value is shown as a read-only label to the right of the slider. The slider can also be set programmatically via `setSwrSweepPowerWatts`; the label updates automatically.

### SWR sweep phases

The sweep progresses through the following internal phases. These are not directly visible in the UI but determine what the radio is doing at each point during the sweep:

| Phase | Description |
|---|---|
| Idle | No sweep in progress. |
| WaitingForTgxlBypass | Waiting for the TGXL tuner to confirm bypass mode before RF starts. |
| TgxlBypassSettle | Allowing a settle period after the TGXL bypass is confirmed. |
| Sweeping | Stepping through sweep frequencies and collecting SWR samples. |
| StoppingTune | Waiting for the radio to stop the tune carrier after the sweep completes or is aborted. |
| RestoringTgxl | Restoring the TGXL tuner to its original operate/bypass state. |

SWR readings can be sourced from the radio's own forward/reflected power meters or from the TGXL tuner's meter, depending on which is available for the connected antenna port.

## DSP row visibility (extended DSP, #2177)

The NRL noise-reduction row (DSP row 4) is available on both 6000-series and 8000-series firmware and is always visible regardless of whether extended DSP is enabled. The NRS (row 5), RNN (row 6), and NRF (row 8) rows remain hidden unless the connected radio reports extended DSP support.

## Tips

- Drag on the Spectrum / waterfall area to tune the slice frequency. Scroll to zoom the span.
- To give one panadapter more screen space without closing others, click □ (maximize) in its title bar. See [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md).
- To move a panadapter to a separate window, click ⬈ (pop-out). See [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md).

## Related

- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
<!-- docmesh:llm version=v0.9.4 date=2026-05-01 -->