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

| Control              | Kind                                 | Default | Description |
|----------------------|--------------------------------------|---------|-------------|
| Slice title          | Indicator                            | Slice A | Shows which slice is bound to this panadapter. |
| ⬈ / ↩ (pop-out/dock) | Push button                          | —       | Pops the panadapter out into a floating window or docks it back; emits popOutClicked or dockClicked. Hidden in single-pan mode. Floating window is frameless (v0.9.0, #1922) — drag via the in-app title strip, resize via the bottom-right size grip; see 00-navigation.json for the shared frameless chrome. On macOS, every float/dock cycle now calls resetGpuResources() and re-binds the QRhi/Metal surface to the new window so the spectrum stays live (v0.9.5.1, #2280). Saved floating-window state is no longer restored when subsequent panadapters are added, preventing a blank floating window from spawning. rebuildDockedSplitter() reclaims any empty splitter slots when a pan docks back. |
| □ (maximize)         | Push button                          | —       | Maximizes this panadapter in a multi-pan layout; emits maximizeRequested. Hidden in single-pan mode. |
| × (close)            | Push button                          | —       | Closes this panadapter; emits closeRequested. Hidden in single-pan mode. |
| Spectrum / waterfall | Drag area                            | —       | Click activates the panadapter; drag to tune, scroll to zoom (SpectrumWidget). |
| CW stats label       | Indicator                            | —       | Shows detected CW pitch and speed in the format `<hz> Hz  <wpm> WPM`. |
| Sens                 | Slider                               | 30      | Filters low-confidence decodes; higher = stricter. Maps 0-100 to cost threshold 1.0-0.1. Setting key: `CwDecoderSensitivity`. |
| 🔒P (Lock Pitch)      | Toggle button                        | —       | Locks the CW decoder pitch to the current tuned frequency. |
| 🔒S (Lock Speed)      | Toggle button                        | —       | Locks the CW decoder speed to the current WPM. |
| Pitch range          | Dual-handle slider                   | Lo: 500 Hz, Hi: 700 Hz | Sets the decoder pitch search range (Lo to Hi). Range: 300-1200 Hz. Label shows "Pitch". |
| WPM range            | Dual-handle slider                   | Lo: 15 WPM, Hi: 40 WPM | Sets the decoder speed search range. Range: 5-60 WPM. Label shows "WPM". |
| CPY ALL              | Push button                          | —       | Copies the full decoded text to the clipboard. |
| CPY VIS              | Push button                          | —       | Copies only the text currently visible in the scroll area. |
| CLR                  | Push button                          | —       | Clears the CW decode buffer. |
| ✕ (close CW)         | Push button                          | —       | Hides the CW decode panel; emits cwPanelCloseRequested. |
| CW decode text       | Read-only text field                 | —       | Rolling display of decoded CW coloured by confidence. Colours: <0.15 green, <0.35 yellow, <0.60 orange, >=0.60 red. |
| Start Sweep          | Push button                          | —       | Runs a low-power tune sweep across the current TX band and plots SWR on the panadapter. |
| Clear Sweep          | Push button                          | —       | Removes the displayed SWR sweep trace from the panadapter. |
| PWR (sweep power)    | Slider                               | 1 W     | Sets the carrier power used during the sweep. Range: 1 W to 10 W. The current value is shown as a read-only label to the right of the slider. |

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

The **Pitch range** dual-handle slider sets the decoder pitch search range. The lower handle sets the minimum pitch (Lo), the upper handle sets the maximum pitch (Hi). The range is 300-1200 Hz.

The **WPM range** dual-handle slider sets the decoder speed search range. The lower handle sets the minimum speed, the upper handle sets the maximum speed. The range is 5-60 WPM. Defaults: 15-40 WPM.

Click **CPY ALL** to copy the entire decoded text buffer to the clipboard. Click **CPY VIS** to copy only the text currently visible in the scroll area. Click **CLR** to clear the decode buffer. Click **✕ (close CW)** to hide the panel.

### TX-side decoded text

When the radio is transmitting, the decoder also decodes the keying from your transmitter and appends it to the CW decode text area in cyan (#5fc8ff). This allows you to see both incoming and outgoing CW in the same panel, colour-coded so you can distinguish your own sending from received signals. A space is inserted between receive and transmit runs to keep them visually separate.

The same confidence filter (Sens slider) applies to TX-side text as to RX-side text.

### Right-click menu on the CW decode text area

Right-clicking inside the CW decode text area opens a context menu. In addition to the standard text actions (Select All, Copy, and so on), the menu includes a **Clear** item. Selecting **Clear** has the same effect as clicking the **CLR** button — it clears the decode buffer.

## Waterfall freeze on transmit

When the radio begins transmitting (based on the radio's interlock TRANSMITTING state, not the local MOX edge), the waterfall display freezes automatically. This prevents a 10–23 second TX-trail artifact that previously appeared after unkeying. Any client transmitting to the radio triggers the freeze. The waterfall unfreezes when transmission ends.

On radio reconnect, the desired panadapter FPS and waterfall line duration are reasserted to prevent silently dropping to the radio's 10 Hz default (#2465).

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

## Theme support (v0.9.7)

The panadapper's title bar and CW panel now use theme-aware styling instead of hard-coded colors. The title bar background uses a gradient with `{{color.text.disabled}}` and `{{color.background.1}}` theme variables. The CW panel background uses `{{color.background.0}}` with a top border in `{{color.background.1}}`. The CW title text uses `{{color.accent}}`, the hint text uses `{{color.meter.bar.fill}}`, and labels use `{{color.text.label}}`. The slider uses the primary slider style via `applyPrimarySliderStyle()`.

## Tips

- Drag on the Spectrum / waterfall area to tune the slice frequency. Scroll to zoom the span.
- To give one panadapter more screen space without closing others, click □ (maximize) in its title bar. See [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md).
- To move a panadapter to a separate window, click ⬈ (pop-out). See [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md).

## Related

- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Close an extra panadapter](close-an-extra-panadapter.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)