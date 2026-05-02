Looking at the diff, I need to identify user-visible changes:

1. **New SWR sweep controls in the ANT panel**: "Start Sweep" button, "Clear Sweep" button, and a PWR slider (1–10 W) are added to the ANT overlay panel. These are user-facing controls that need documentation.

2. **NRL (DSP row 4) behavior change**: NRL is now visible on 6000-series radios too (not just 8000-series). This is a user-visible behavior change.

The SWR sweep controls already have a section in the docs, but the specific ANT panel controls (Start Sweep, Clear Sweep, PWR slider) are not listed anywhere. I need to add them to the controls table. The NRL change affects DSP row visibility — the current doc doesn't have a DSP rows table, so no change needed there unless it's documented elsewhere. Looking at the current doc, there's no DSP controls table, so that change doesn't warrant a doc update.

The main change is adding the three new ANT panel SWR sweep controls to the documentation.

---

# Panadapter overview

The panadapter displays a real-time FFT spectrum and waterfall for a radio slice, letting you visualise band activity and tune by clicking or dragging. Each panadapter can also show an optional CW decode panel that reads Morse off-air directly in the application.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The panadapter requires an active radio connection.
- For CW decoding, PC audio routing to AetherSDR must be configured. The panel displays a "(requires PC Audio)" reminder when this is not in place.

## How it works

AetherSDR opens with one panadapter visible in the centre of the main window. It is always present; you cannot close the last panadapter. In multi-slice mode, additional panadapters appear, each in its own titled container. Every panadapter is bound to one slice (Slice A through Slice H), shown in the title bar.

**Spectrum and waterfall.** The upper portion of the panadapter shows the FFT spectrum trace; below it is the waterfall. Click anywhere on the spectrum or waterfall to activate that panadapter. Drag to pan across the band. Scroll to zoom. The `View > Single-Click to Tune` and `View > Pan Follows VFO` menu items affect how clicking and scrolling interact with the VFO.

**Title bar.** The 16-pixel title bar across the top of each panadapter carries the slice label, a drag grip, and (in multi-slice mode) the pop-out, maximize, and close buttons. In single-pan mode those three buttons are hidden.

**CW decode panel.** An optional panel can appear beneath the waterfall. It runs an off-air Morse decoder and displays decoded text in a rolling read-only field, colour-coded by decoder confidence. The panel is hidden by default and is enabled from the CW mode controls. See [Turn on the CW decoder to read Morse off-air](turn-on-the-cw-decoder-to-read-morse-off-air.md).

**SWR sweep.** A built-in SWR sweep function steps the transmitter across a range of frequencies and plots the measured SWR. The sweep temporarily takes control of the slice frequency and tune power, then restores all settings when it finishes or is aborted. When a TGXL amplifier is connected, the sweep automatically places it in bypass mode for the duration of the sweep and restores it afterwards.

## What each control does

### Title bar

| Control | Kind | Behavior | Notes |
|---|---|---|---|
| Slice title | Indicator | Shows the slice bound to this panadapter. Values: Slice A – Slice H. | — |
| ⬈ / ↩ (pop-out/dock) | Button | Pops the panadapter into a floating window, or docks it back. | Hidden in single-pan mode. The floating window is frameless; drag via the in-app title strip, resize via the bottom-right size grip. |
| □ (maximize) | Button | Maximizes this panadapter to fill the main layout area. | Hidden in single-pan mode. |
| × (close) | Button | Closes this panadapter. | Hidden in single-pan mode. |

### Spectrum / waterfall

| Control | Kind | Behavior |
|---|---|---|
| Spectrum / waterfall | Display and drag area | Click to activate the panadapter. Drag to pan. Scroll to zoom. |

### ANT panel — SWR sweep controls

These controls appear in the ANT overlay panel. Use them to run or clear a low-power SWR sweep across the current TX band.

| Control | Kind | Default | Valid range | Behavior |
|---|---|---|---|---|
| Start Sweep | Button | — | — | Starts a SWR sweep across the current TX band using the selected power level. The sweep result is plotted as an overlay on the panadapter spectrum. |
| Clear Sweep | Button | — | — | Clears the SWR sweep trace from the panadapter. |
| PWR | Slider | 1 W | 1 – 10 W | Sets the carrier power used during the SWR sweep. Use the lowest level that produces a reliable reading. |

### CW decode panel

| Control | Kind | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|---|
| CW stats label | Indicator | — | `<hz> Hz  <wpm> WPM` | — | Shows the pitch and speed currently detected by the decoder. |
| Sens | Slider | 30 | 0 – 100 | `CwDecoderSensitivity` | Filters low-confidence decodes. Higher values are stricter. Internally maps the 0 – 100 range to a cost threshold of 1.0 – 0.1. |
| 🔒P (Lock Pitch) | Toggle button | Off | On / Off | — | Locks the decoder pitch to the currently tuned frequency. |
| 🔒S (Lock Speed) | Toggle button | Off | On / Off | — | Locks the decoder speed to the current WPM reading. |
| Lo (pitch min) | Slider | 500 Hz | 300 – 1200 Hz | — | Sets the minimum pitch the decoder searches. Clamped to be no greater than Hi. |
| Hi (pitch max) | Slider | 700 Hz | 300 – 1200 Hz | — | Sets the maximum pitch the decoder searches. Clamped to be no less than Lo. |
| CPY ALL | Button | — | — | — | Copies the full decoded text buffer to the clipboard. |
| CPY VIS | Button | — | — | — | Copies only the text currently visible in the scroll area to the clipboard. |
| CLR | Button | — | — | — | Clears the CW decode buffer. |
| × (close CW) | Button | — | — | — | Hides the CW decode panel. |
| CW decode text | Read-only text field | — | — | — | Rolling display of decoded Morse, coloured by confidence: green (highest confidence) through yellow and orange to red (lowest). Right-click the text area to open a context menu; the menu includes standard text actions and a **Clear** item that clears the decode buffer. |

## SWR sweep

The SWR sweep steps the transmitter across a user-defined frequency range and plots the measured SWR as an overlay on the panadapter. Use it to locate the resonant point of an antenna or check tuner performance across a band segment.

**How the sweep runs.** When you start a sweep, AetherSDR records the current slice frequency, panadapter centre and bandwidth, and tune power. If a TGXL amplifier is active on the slice, the sweep waits for TGXL to enter bypass mode before transmitting. The sweep then steps through each frequency, waits a configurable settle time, samples SWR, and advances. On completion — or if you abort — all original settings are restored. If TGXL bypass restoration times out, the sweep finishes but logs a warning.

**SWR source.** The sweep reads SWR from either the radio's internal meter or, when a TGXL is present and available, from the TGXL meter. The source used is shown in the overlay label.

**Sweep phases.** The sweep moves through the following internal phases in order:

| Phase | What is happening |
|---|---|
| Idle | No sweep active. |
| WaitingForTgxlBypass | Sent bypass request to TGXL; waiting for confirmation. |
| TgxlBypassSettle | TGXL confirmed bypass; waiting the settle interval before RF starts. |
| Sweeping | Stepping through frequencies and collecting SWR samples. |
| StoppingTune | Sweep complete; stopping the tune transmit. |
| RestoringTgxl | Returning TGXL to its original operate/bypass state. |

**Inputs are locked during a sweep.** Frequency controls, tune power, and TGXL operate/bypass controls are disabled while a sweep is running. They are re-enabled automatically when the sweep finishes or is aborted.

**Overlay.** During and after the sweep, a SWR curve is drawn over the panadapter spectrum. A marker indicates the frequency currently being measured while the sweep is in progress. The overlay is cleared automatically if you start a new sweep, or you can clear it manually.

## Tips

- The Lo and Hi pitch sliders constrain the frequency range the decoder searches. Narrowing this range around the expected CW tone reduces false decodes on a busy band.
- Decoded text colour reflects decoder confidence. Green text is the most reliable; red text should be treated with caution. Adjust Sens upward to suppress red and orange characters if noise is producing junk output.
- `CwDecoderSensitivity` is persisted across sessions. You do not need to re-tune it each time you open the application.
- You can clear the decode buffer from the keyboard-free right-click context menu on the decoded text area as an alternative to clicking CLR.
- Run the SWR sweep at the lowest power level sufficient to get a reliable reading. The PWR slider in the ANT panel accepts 1 – 10 W; 1 W is the default.
- If a TGXL is in use, do not abort the sweep immediately after it starts. Allow the bypass phase to complete so the amplifier is not inadvertently left in an inconsistent state.

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
<!-- docmesh:llm version=v0.9.4 date=2026-05-01 -->