# Adjust AF gain and pan from the VFO panel

Use the Audio tab in the VFO panel to set the audio output level and stereo pan position for any receive slice independently of other slices.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The VFO panel for the target slice must be open. If it is collapsed to a frequency-only strip, click anywhere on the collapsed strip to expand it.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel opens anchored to the marker.
2. Click the **Audio** tab inside the VFO panel.
3. To set the audio output level, drag the **AF Gain slider** left or right. The default is 100; the valid range is 0–100.
4. To set the stereo position, drag the **Pan slider** left or right. The default is 50 (centre); the valid range is 0–100. A value below 50 moves audio toward the left channel; above 50 toward the right.

## What each control does

| Control | Default | Range |
|---|---|---|
| AF Gain slider (Audio tab) | 100 | 0–100 |
| Pan slider (Audio tab) | 50 | 0–100 |
| Mute button (Audio tab) | off | — |
| Squelch button + slider (Audio tab) | off | 0–100 |
| AGC combo (Audio tab) | FAST | FAST \| MED \| SLOW \| OFF |
| ADSP button (DSP tab) | Opens the AetherDSP Settings dialog (client-side NR2 / NR4 / DFNR / RN2 / BNR / MNR). Same entry point as the Settings menu (v0.9.8). | Styled like a radio-side DSP toggle but non-checkable. Click raises and focuses the modeless AetherDSP Settings dialog. |
| AetherVoice button (DSP tab) | Toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite (v0.9.8). | Spans 2 columns in the 4-column DSP grid. Matches the existing menu / chain entry points for the strip. |

## Tips

- Double-clicking either slider resets it to its default value: 100 for AF Gain, 50 for Pan.
- AF gain is per-slice. Adjusting one slice does not affect any other slice.
- To silence a slice without moving the AF Gain slider, use the **Mute button** on the Audio tab instead. Muting does not change the stored gain value.

## Filter width label changes in v0.9.8

The filter width label now uses `RxApplet::formatFilterWidth` as its single source of truth. This fixes a 0.1 kHz offset that previously affected SSB and digital mode readouts (#2197, v0.9.8). The label now stays in sync with the filter readout in the RX applet.

## Squelch behavior for RTTY mode (v26.5.1)

The squelch button and slider are now disabled in RTTY mode, in addition to digital and CW modes. This prevents squelch from gating weak FSK signals when the audio feeds external decoders via DAX (#2504).

## DSP tab changes in v0.9.7

The DSP tab in the VFO panel now shows only radio-supplied noise reduction algorithms. The client-side algorithms that were previously accessible as buttons in this tab — NR2, RN2, NR4, MNR, BNR, and DFNR — have been moved out of the VFO panel. To enable those algorithms, use the spectrum overlay menu or the AetherDSP applet.

The buttons remaining in the DSP tab are:

| Button | Algorithm |
|---|---|
| NR | Noise reduction |
| NB | Noise blanker |
| ANF | Automatic notch filter |
| APF | Audio peaking filter (CW mode only) |
| NRL | Noise reduction level |
| NRS | Spectral subtraction |
| RNN | RNN noise reduction |
| NRF | Spectral noise filter |
| ANFL | LMS notch filter |
| ANFT | FFT notch filter |

### ADSP button (v0.9.8)

The DSP tab now includes an **ADSP button** that opens the AetherDSP Settings dialog. This button provides the same entry point as the Settings menu. It is styled like a radio-side DSP toggle but is non-checkable. Click it to raise and focus the modeless AetherDSP Settings dialog.

### AetherVoice button (v0.9.8)

The DSP tab also includes an **AetherVoice button** that toggles the Aetherial Audio Channel Strip — the unified TX/RX DSP suite. This button spans 2 columns in the 4-column DSP grid and matches existing menu and chain entry points for the strip.

### DSP level slider

A shared level slider now appears below the DSP button grid. The slider retargets automatically to whichever leveled DSP algorithm was most recently enabled. The label to the left of the slider shows the name of the currently targeted algorithm, and the numeric value is shown to the right.

Important change in v0.9.8: The DSP level slider now properly appears on startup for any DSP that was enabled in the radio's saved profile. Previously the slider was missing until manually toggling the algorithm (#startup-slider). This affects NB, NR, ANF, NRL, NRS, NRF, and ANFL.

The slider row remains laid out at all times. When no leveled algorithm is active — or when only RNN, ANFT, or APF is on — the slider row fades out and does not respond to clicks.

| Control | Range | Behavior |
|---|---|---|
| DSP level slider | 0–100 | Sets the level for the most recently enabled leveled DSP algorithm. Retargets automatically when you switch algorithms. Hidden (faded) when no leveled algorithm is active. |

## Related

- [Mute audio for a slice from the VFO panel](mute-audio-for-a-slice-from-the-vfo-panel.md)
- [Enable squelch from the VFO panel](enable-squelch-from-the-vfo-panel.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- [VFO Panel overview](overview.md)