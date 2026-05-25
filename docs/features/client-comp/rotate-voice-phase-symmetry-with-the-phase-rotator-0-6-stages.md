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

| Control | Default | Valid range | Setting key | Behavior |
|---------|---------|-------------|-------------|----------|
| **Phase** knob | 0 stages | 0–6 stages | `ClientCompTxPhaseRotatorStages` | Number of cascaded all-pass sections (0 = off). Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz). Displayed as `Off` when 0, `N stg` when active. |
| **Drive** knob | 0.0 dB | 0.0–18.0 dB | `ClientCompTxDriveDb` | Pre-comp gain boost. Pushes more signal across the threshold so the compressor engages harder, raising average power. Displayed as `+X.X dB`. |

## Tips

- A Phase setting of 4 stages is the broadcast default and works well for most voice audio.
- Pair the Phase rotator with the **Drive** knob: increase Drive to raise average power, then increase Phase stages to clean up the resulting peaks.
- The Phase rotator only affects TX audio and has no effect on RX audio.

## Related

- [Drive the compressor harder with pre-comp gain for PAPR reduction](drive-the-compressor-harder-with-pre-comp-gain-for-papr-reduction.md)
- [Open the full Compressor editor for knee, limiter, Drive, and Phase controls](open-the-full-compressor-editor-for-knee-limiter-drive-and-phase-controls.md)
- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
