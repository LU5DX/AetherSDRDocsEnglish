# Rotate voice phase symmetry with the Phase rotator (0–6 stages)

The Phase rotator cascades all-pass filter stages before compression to symmetrize voice waveform peaks, reducing the peak-to-average power ratio (PAPR). This lets you drive the compressor harder while keeping peaks clean, maximizing average transmit power without distortion. The control is available in the floating StripCompPanel editor.

## Before you start

- The floating StripCompPanel must be open. Double-click the **COMP** tile in the **CHAIN** widget on the TX side to open `Aetherial Compressor — TX`.

## Steps

1. Open the floating StripCompPanel by double-clicking the **COMP** tile in the CHAIN widget on the TX side.
2. Locate the **Phase** knob in the right column of the editor.
3. Turn the **Phase** knob to the desired number of stages:
   - **0 stages** (displayed as `Off`) — phase rotation disabled.
   - **1–6 stages** — cascaded all-pass sections. 4 stages is the broadcast default.
4. Adjust the **Drive** knob (0.0–18.0 dB) to push more signal into the compressor, using the Phase rotator to keep peak levels under control.

## What each control does

| Control        | Default                                                                                                                                                                                                                                                                 | Valid range                                                                                                                                                                                                                                                                                                                                                                       |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Phase** knob | 0 stages                                                                                                                                                                                                                                                                | 0–6 stages                                                                                                                                                                                                                                                                                                                                                                        |
| **Drive** knob | 0.0 dB                                                                                                                                                                                                                                                                  | 0.0–18.0 dB                                                                                                                                                                                                                                                                                                                                                                       |
| Drive          | Pre-comp gain boost with linked auto-makeup. Pushes more signal across the threshold so the compressor engages harder, and simultaneously adds equal gain at the output so average RMS lifts alongside peaks rather than dropping. Pair with Phase to keep peaks clean. | Displayed in the floating StripCompPanel only (right column). Label shows as '+X.X dB'. Tooltip explains #2887 PAPR reduction pairing. Auto-makeup matches the broadcast-Optimod model — Drive pushes more material into the curve AND adds equal gain back, so the user's fixed Makeup stays a clean post-everything trim knob.                                                  |
| Phase          | Number of cascaded all-pass sections (0 = off). Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz). Symmetrizes asymmetric voice peaks before compression to reduce PAPR.                          | Displayed in the floating StripCompPanel only (right column). Label 'Off' when 0, 'N stg' when active. Tooltip: 'Pre-comp phase rotator (#2887). All-pass cascade that symmetrizes asymmetric voice peaks before compression. 0 = off, 4 = broadcast default.' Default centres (300/700/1500/2500 Hz with optional 1000/2000 Hz) cover the speech formant range without bunching. |
## Tips

- A Phase setting of 4 stages is the broadcast default and works well for most voice audio.
- Pair the Phase rotator with the **Drive** knob: increase Drive to raise average power, then increase Phase stages to clean up the resulting peaks.
- The Phase rotator only affects TX audio and has no effect on RX audio.

## Related

- [Drive the compressor harder with pre-comp gain for PAPR reduction](drive-the-compressor-harder-with-pre-comp-gain-for-papr-reduction.md)
- [Open the full Compressor editor for knee, limiter, Drive, and Phase controls](open-the-full-compressor-editor-for-knee-limiter-drive-and-phase-controls.md)
- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)