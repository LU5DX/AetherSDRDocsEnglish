# Drive the compressor harder with pre-comp gain for PAPR reduction

Pre-comp gain (Drive) pushes more signal into the compressor so it engages harder, raising average power without increasing peak power. Pair it with the Phase Rotator to keep peaks clean and reduce the peak-to-average-power ratio (PAPR) of your transmitted signal.

## Before you start

- Open the full Compressor editor: double-click the COMP tile in the CHAIN widget on the TX side. The floating editor is titled "Aetherial Compressor — TX".
- The compressor must be enabled (bypassed off) for Drive to take effect.

## Steps

1. In the floating Compressor editor, locate the **Drive** knob in the right column.
2. Click and drag upward on the Drive knob to add gain. The default is 0.0 dB; the valid range is 0.0 to 18.0 dB.
3. While speaking into your microphone, watch the gain-reduction bar in the TX applet tile. As you increase Drive, the amber fill should show more reduction as the compressor works harder.
4. Adjust the **Phase** knob (0–6 stages) to rotate voice phase symmetry. Start with 4 stages (the broadcast default) and listen for cleaner peaks.
5. Observe the live "ball" on the transfer curve — it should move further into the compression region as Drive is increased.

## What each control does

| Control | Label | Default | Range | Setting key | Behavior |
|---------|-------|---------|-------|-------------|----------|
| Pre-comp gain | Drive | 0.0 dB | 0.0 to 18.0 dB | `ClientCompTxDriveDb` | Boosts the audio level before the compressor. Higher values push more signal above threshold, increasing average power. |
| Phase rotation | Phase | 0 stages | 0 to 6 stages | `ClientCompTxPhaseRotatorStages` | Number of cascaded all-pass sections. Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz). Symmetrizes asymmetric voice peaks to reduce PAPR. 0 = off; 4 = broadcast default. |

## Tips

- Drive is only available in the floating StripCompPanel editor (right column), not in the compact applet tile. Double-click the COMP tile in the CHAIN widget to open it.
- The label shows a plus sign for positive values (e.g. "+6.0 dB").
- If you increase Drive significantly, you may need to adjust Threshold or Makeup gain to maintain your desired audio level.

## Related

- [Open the full Compressor editor for knee, limiter, Drive, and Phase controls](open-the-full-compressor-editor-for-knee-limiter-drive-and-phase-controls.md)
- [Rotate voice phase symmetry with the Phase rotator (0–6 stages)](rotate-voice-phase-symmetry-with-the-phase-rotator-0-6-stages.md)
- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
