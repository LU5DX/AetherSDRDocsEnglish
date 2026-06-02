# Rotate voice phase symmetry with the Phase rotator (0–6 stages at staggered frequencies)

The Phase rotator cascades all-pass filter sections to symmetrize asymmetric voice peaks before compression, reducing the peak-to-average power ratio (PAPR). This lets you run more average power without clipping or distorting.

## Before you start

- The compressor must be enabled on the TX side (Aetherial Compressor).
- You need the floating StripCompPanel open. Double-click the **COMP** tile in the CHAIN widget on the TX side.

## Steps

1. Open the floating StripCompPanel by double-clicking the **COMP** tile in the CHAIN widget on the TX side.
2. Locate the **Phase** knob in the right column of the StripCompPanel.
3. Turn the **Phase** knob to the desired number of stages (0–6):
   - **0** — off (no phase rotation).
   - **4** — broadcast default, recommended starting point.
   - **1–6** — number of cascaded all-pass stages at staggered frequencies.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---------|---------|-------------|-------------|----------|
| Phase knob | 0 stages | 0–6 stages | `ClientCompTxPhaseRotatorStages` | Number of cascaded all-pass sections. Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300, 700, 1500, 2500 Hz, plus optional 1000 and 2000 Hz). Label shows "Off" at 0, "N stg" when active. |

## Tips

- Start with **4 stages** (the broadcast industry default) and listen while speaking. Increase stages if your voice waveform still shows asymmetric peaks on the transfer curve's envelope ball.
- The Phase rotator works before compression, so changes affect how the compressor responds. Re-adjust Threshold and Drive after changing the number of stages.
- Pair the Phase rotator with the **Drive** knob (0–18 dB with auto-makeup gain) for maximum PAPR reduction. Drive pushes more signal into the compressor, and phase rotation keeps the peaks symmetrical so the compressor doesn't over-react to waveform asymmetry.

## Related

- [Drive the compressor harder with pre-comp gain for PAPR reduction (auto-makeup linked)](drive-the-compressor-harder-with-pre-comp-gain-for-papr-reduction-auto-makeup-linked.md)
- [Open the full Compressor editor for knee, limiter, Drive, and Phase controls](open-the-full-compressor-editor-for-knee-limiter-drive-and-phase-controls.md)
- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
