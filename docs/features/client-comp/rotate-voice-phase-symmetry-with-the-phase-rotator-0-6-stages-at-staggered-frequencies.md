# Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview

The Aetherial Compressor (TX) and Aetherial AGC-C (RX) are client-side dynamic-range processors. The applet instantiates one TX-bound copy ("Aetherial Compressor") and one RX-bound copy ("Aetherial AGC-C") with fully independent state.

## Applet view

The applet shows:
- A static transfer curve with a live "ball" riding on the current envelope
- A horizontal gain-reduction meter (20 dB max)
- Five tuning knobs: Thresh, Ratio, Attack, Release, Makeup

## Controls

| Control | Default | Valid range | Behavior |
|---------|---------|-------------|----------|
| Transfer curve | — | — | Compact-mode ClientCompCurveWidget. Draws the input/output transfer curve plus a live ball showing the current envelope level. View-only in the applet; editable in the floating ClientCompEditor. |
| Gain-reduction bar | — | 0 to 20 dB GR | Horizontal amber strip, right-filled. Scale maxes at 20 dB reduction; a tick at -6 dB marks a typical working amount. Refreshed ~30 Hz from `ClientComp::gainReductionDb()` with MeterSmoother ballistics. |
| Thresh | -18.0 dB | -60.0 to 0.0 dB | Linear mapping. Sets the level above which compression starts. Label formatted as "-18.0 dB". Setting key: `ClientCompTxThresholdDb`. |
| Ratio | 3.0 | 1.0 to 20.0 | Logarithmic mapping (1 * 20^n). Sets how hard peaks are held once threshold is crossed. Label formatted as "X.XX:1". Setting key: `ClientCompTxRatio`. |
| Attack | 20.0 ms | 0.1 to 300.0 ms | Exponential mapping (0.1 * 3000^n). Sets how quickly the compressor clamps down after the threshold is crossed. Label formatted "X.X ms" below 10, "X ms" above. Setting key: `ClientCompTxAttackMs`. |
| Release | 200 ms | 5 to 2000 ms | Exponential mapping (5 * 400^n). Sets how quickly gain returns after the input drops back below threshold. Label formatted "X ms". Setting key: `ClientCompTxReleaseMs`. |
| Makeup | 0.0 dB | -12.0 to 24.0 dB | Linear mapping. Adds back gain lost to compression. Label shows explicit "+" sign for positive values. Setting key: `ClientCompTxMakeupDb`. |

## Indicators

| Indicator | States | Meaning |
|-----------|--------|---------|
| Envelope ball | resting at threshold line, moving along curve | Live input level plotted against the static transfer curve. |
| Gain-reduction strip | empty, amber fill, -6 dB tick | Amount of dynamic attenuation currently applied by the compressor. |

## Gain-reduction meter behavior

The gain-reduction meter uses MeterSmoother ballistics for natural visual response. The meter updates at approximately 30 Hz and stops repainting when the signal is settled. This reduces CPU usage while maintaining responsive visual feedback during active compression.

## Related

- [Open the full Compressor editor for knee, limiter, Drive, and Phase controls](open-the-full-compressor-editor-for-knee-limiter-drive-and-phase-controls.md)

---

# Open the full Compressor editor for knee, limiter, Drive, and Phase controls

The floating StripCompPanel extends the applet's controls with additional parameters for fine-tuning the compressor.

## Before you start

- The compressor must be enabled on the TX side (Aetherial Compressor) or RX side (Aetherial AGC-C).

## Steps

1. Open the CHAIN widget on the desired side (TX or RX).
2. Double-click the **COMP** tile in the CHAIN widget.
3. The floating StripCompPanel appears.

## Controls in the floating StripCompPanel

The StripCompPanel adds the following controls to the right column:

| Control | Default | Valid range | Behavior |
|---------|---------|-------------|----------|
| Knee | — | — | Sets the transition smoothness around the threshold. |
| Ceiling | — | — | Sets the maximum output level. |
| Makeup | — | — | Post-compression gain trim. |
| Limiter | Disabled | Enable/Disable | Enables a hard limiter after compression. |
| Drive | 0.0 dB | 0.0 to 18.0 dB | Pre-comp gain boost with linked auto-makeup. Pushes more signal across the threshold so the compressor engages harder, and simultaneously adds equal gain at the output so average RMS lifts alongside peaks rather than dropping. Pair with Phase to keep peaks clean. Label shows as "+X.X dB". Setting key: `ClientCompTxDriveDb`. |
| Phase | 0 stages | 0 to 6 stages | Number of cascaded all-pass sections (0 = off). Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz). Symmetrizes asymmetric voice peaks before compression to reduce PAPR. Label "Off" when 0, "N stg" when active. Setting key: `ClientCompTxPhaseRotatorStages`. |

## Drive and Phase pairing

The Drive and Phase knobs work together for optimal peak-to-average power ratio (PAPR) reduction:

- **Drive** pushes more signal into the compressor while adding equal gain at the output. This lifts average RMS alongside peaks.
- **Phase** symmetrizes asymmetric voice peaks before compression, preventing the compressor from over-reacting to waveform asymmetry.
- Start with 4 stages of phase rotation (broadcast default) and adjust Drive upward while monitoring the gain-reduction meter.

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)

---

# Drive the compressor harder with pre-comp gain for PAPR reduction (auto-makeup linked)

The **Drive** knob (0–18 dB) adds pre-compression gain boost with linked auto-makeup gain. This pushes more signal across the threshold while simultaneously adding equal gain at the output, so average RMS lifts alongside peaks rather than dropping.

## Before you start

- The compressor must be enabled on the TX side (Aetherial Compressor).
- You need the floating StripCompPanel open. Double-click the **COMP** tile in the CHAIN widget on the TX side.

## Steps

1. Open the floating StripCompPanel by double-clicking the **COMP** tile in the CHAIN widget on the TX side.
2. Locate the **Drive** knob in the right column of the StripCompPanel.
3. Turn the **Drive** knob clockwise to increase pre-comp gain (0.0 to 18.0 dB).
4. Observe the gain-reduction meter — higher Drive values will cause the compressor to engage more aggressively.
5. Adjust the **Phase** rotator as needed to keep peaks symmetrical (see related topic).

## How auto-makeup works

The auto-makeup matches the broadcast-Optimod model:

- **Drive** pushes more material into the compression curve.
- Equal gain is added back at the output automatically.
- The fixed **Makeup** knob remains a clean post-everything trim control.

This means you can increase Drive to engage the compressor harder without losing average level.

## Tips

- Start with the **Phase** rotator at 4 stages (broadcast default) before adjusting Drive.
- Increase Drive gradually while monitoring your transmitted audio quality.
- Re-adjust the **Thresh** knob if the compressor engages too aggressively.

## Related

- [Rotate voice phase symmetry with the Phase rotator (0–6 stages at staggered frequencies)](rotate-voice-phase-symmetry-with-the-phase-rotator.md)
- [Open the full Compressor editor for knee, limiter, Drive, and Phase controls](open-the-full-compressor-editor-for-knee-limiter-drive-and-phase-controls.md)

---

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

| Control | Default | Valid range |
|---------|---------|-------------|
| Phase knob | 0 stages | 0–6 stages |

## Frequencies and behavior

Each stage adds 12 dB/oct of phase rotation at staggered frequencies:
- Core centers: 300/700/1500/2500 Hz
- Optional: 1000/2000 Hz

These frequencies cover the speech formant range without bunching. The cascade symmetrizes asymmetric voice peaks before compression to reduce PAPR.

- Label shows "Off" when 0, "N stg" when active.
- Tooltip: "Pre-comp phase rotator (#2887). All-pass cascade that symmetrizes asymmetric voice peaks before compression. 0 = off, 4 = broadcast default."

## Tips

- Start with **4 stages** (the broadcast industry default) and listen while speaking. Increase stages if your voice waveform still shows asymmetric peaks on the transfer curve's envelope ball.
- The Phase rotator works before compression, so changes affect how the compressor responds. Re-adjust Threshold and Drive after changing the number of stages.
- Pair the Phase rotator with the **Drive** knob (0–18 dB with auto-makeup gain) for maximum PAPR reduction. Drive pushes more signal into the compressor, and phase rotation keeps the peaks symmetrical so the compressor doesn't over-react to waveform asymmetry.

## Related

- [Drive the compressor harder with pre-comp gain for PAPR reduction (auto-makeup linked)](drive-the-compressor-harder-with-pre-comp-gain-for-papr-reduction-auto-makeup-linked.md)
- [Open the full Compressor editor for knee, limiter, Drive, and Phase controls](open-the-full-compressor-editor-for-knee-limiter-drive-and-phase-controls.md)
- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)