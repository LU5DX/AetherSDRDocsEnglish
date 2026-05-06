# Enable squelch from the VFO panel

Squelch mutes audio for a slice when the received signal falls below a set threshold. Use this to silence background noise on FM, AM, or digital modes when no signal is present.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The VFO panel for the target slice must be open. If it is not, click the VFO marker flag on the spectrum display for that slice.
- If the VFO panel is collapsed to the frequency-only strip, click it once to expand it.

## Steps

1. Open the VFO panel by clicking the VFO marker flag on the spectrum display for the slice you want to configure.
2. Click the **Audio** tab inside the VFO panel.
3. Click the **Squelch button** to enable squelch. The button activates and squelch is applied to the slice immediately.
4. Drag the adjacent squelch slider left or right to set the threshold. The valid range is 0–100.

To disable squelch, click the **Squelch button** again.

## What each control does

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| Squelch button | Off | On / Off | Enables or disables squelch for this slice. |
| Squelch slider | — | 0–100 | Sets the squelch threshold. Higher values require a stronger signal to open the squelch. |

Neither the button state nor the slider position is persisted as an AetherSDR AppSettings key — both reflect live radio state.

## Tips

- Set the slider just above the noise floor to prevent the audio from cutting in and out on weak signals.
- The squelch threshold interacts with the AGC setting. If you change the AGC mode using the **AGC combo**, you may need to readjust the squelch slider.

## DSP tab changes in v0.9.7

The **DSP tab** of the VFO panel was reorganised in v0.9.7. The following buttons were removed from the VFO panel DSP grid:

| Removed button | Reason |
|---|---|
| NR2 | Moved to the spectrum overlay menu and the AetherDSP applet. |
| RN2 | Moved to the spectrum overlay menu and the AetherDSP applet. |
| BNR | Moved to the spectrum overlay menu and the AetherDSP applet. |
| NR4 | Moved to the spectrum overlay menu and the AetherDSP applet. |
| MNR | Moved to the spectrum overlay menu and the AetherDSP applet. |
| DFNR | Moved to the spectrum overlay menu and the AetherDSP applet. |

To toggle NR2, RN2, BNR, NR4, MNR, or DFNR, right-click the spectrum display to open the spectrum overlay menu, or open the AetherDSP applet.

The buttons that remain in the VFO panel DSP tab are:

| Button | Behavior |
|---|---|
| NR | Enables radio-side noise reduction. |
| NB | Enables the noise blanker. |
| ANF | Enables the automatic notch filter. |
| APF | Enables the audio peak filter (visible in CW mode only). |
| NRL | Enables LMS noise reduction. |
| NRS | Enables spectral subtraction. |
| RNN | Enables RNN noise reduction. |
| NRF | Enables the spectral noise filter. |
| ANFL | Enables the LMS notch filter. |
| ANFT | Enables the FFT notch filter. |

### DSP level slider

A shared **DSP level slider** row appears below the DSP button grid. The slider targets whichever leveled DSP button was most recently turned on. The label to the left of the slider shows the active target (for example, **NR** or **NB**). The numeric value is shown to the right.

The slider row is always present in the layout. When no leveled DSP is active — or when only RNN, ANFT, or APF is on — the row fades out and does not respond to interaction. It becomes fully visible again as soon as a compatible DSP button is enabled.

Leveled DSP targets supported by the slider:

| Target | Controlled by |
|---|---|
| NR | `setNrLevel` |
| NB | `setNbLevel` |
| ANF | `setAnfLevel` |
| NRL | `setNrlLevel` |
| NRS | `setNrsLevel` |
| NRF | `setNrfLevel` |
| ANFL | `setAnflLevel` |

The slider range is 0–100. The level value is not persisted as an AetherSDR AppSettings key — it reflects live radio state.

## Related

- [Adjust AF gain and pan from the VFO panel](adjust-af-gain-and-pan-from-the-vfo-panel.md)
- [Mute audio for a slice from the VFO panel](mute-audio-for-a-slice-from-the-vfo-panel.md)
- [VFO Panel overview](overview.md)