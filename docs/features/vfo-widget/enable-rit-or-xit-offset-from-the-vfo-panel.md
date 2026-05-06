# Enable RIT or XIT offset from the VFO panel

RIT (Receiver Incremental Tuning) and XIT (Transmitter Incremental Tuning) let you shift the receive or transmit frequency by a small offset without moving the main VFO. This is useful for working split-frequency contacts or compensating for a station that is slightly off your dial frequency.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires a live radio connection.
- The VFO panel for the target slice must be open and expanded. If it is collapsed to the frequency-only strip, click anywhere on it to expand it.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel appears anchored to the marker.
2. Click the **X/RIT** tab inside the VFO panel.
3. To enable receiver offset, click the **RIT** button. The button activates and the label shows the current RIT offset.
4. To enable transmitter offset, click the **XIT** button. The button activates and the label shows the current XIT offset.
5. With RIT or XIT active, place the mouse pointer over the corresponding button and scroll the mouse wheel to adjust the offset. Each scroll step changes the offset by 10 Hz.
6. To disable RIT or XIT, click the active button again.

## What each control does

| Control | Kind | Default | Valid range | Persisted setting |
|---|---|---|---|---|
| RIT button + label | Toggle button | off | — | — |
| XIT button + label | Toggle button | off | — | — |

**RIT / XIT buttons + labels** — Enable receiver (RIT) or transmitter (XIT) incremental tuning for this slice. When active, the label next to each button shows the current offset value. Scroll the mouse wheel over the button to adjust the offset in 10 Hz steps. Neither setting is persisted; state reflects live radio state.

## Tips

- RIT and XIT offsets are independent. You can enable both at the same time to offset receive and transmit independently.
- Scroll-wheel adjustment is 10 Hz per step. For larger offsets, scroll multiple notches.

## Changes in v0.9.7

### DSP tab — radio-side buttons only

The **DSP tab** in the VFO panel now shows only buttons for DSP functions that the radio itself provides. The following buttons have been removed from the VFO panel DSP tab:

- **NR2** (spectral noise reduction)
- **RN2** (RNNoise noise suppression)
- **BNR** (GPU neural denoising)
- **NR4** (spectral bleach noise reduction)
- **MNR** (macOS MMSE-Wiener noise reduction)
- **DFNR** (DeepFilterNet3 neural noise reduction)

These client-side DSP modules are now accessible from the spectrum overlay menu and the AetherDSP applet. Use those locations to enable or adjust them.

The buttons that remain on the DSP tab are: **NR**, **NB**, **ANF**, **APF**, **NRL**, **NRS**, **RNN**, **NRF**, **ANFL**, and **ANFT**. The grid layout is four columns across three rows. The **APF** button is visible only when the slice is in a CW mode.

### DSP tab — DSP level slider

A shared level slider row has been added at the bottom of the DSP tab. The slider adjusts the processing depth of whichever supported DSP function was most recently enabled. The label to the left of the slider shows the name of the current target (for example, **NR** or **NB**). The numeric value is shown to the right.

The slider targets the following functions: NR, NB, ANF, NRL, NRS, NRF, and ANFL. It does not target RNN, ANFT, or APF. When none of those functions is active, the slider row is still present in the layout but its contents are visually faded out to indicate that no target is selected. Clicking or dragging the slider while it is faded has no effect.

| Control | Kind | Default | Valid range | Persisted setting |
|---|---|---|---|---|
| DSP level slider (DSP tab) | Slider | — | 0–100 | — |

**DSP level slider** — Sets the processing depth for the most recently activated supported DSP function on this slice. The label to the left identifies the current target. The row fades when no eligible DSP function is active. Not persisted; reflects live radio state.

## Related

- [VFO Panel overview](overview.md)
- [Change mode from the VFO panel](change-mode-from-the-vfo-panel.md)
- [Tune the radio by typing a frequency into the VFO panel](tune-the-radio-by-typing-a-frequency-into-the-vfo-panel.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)