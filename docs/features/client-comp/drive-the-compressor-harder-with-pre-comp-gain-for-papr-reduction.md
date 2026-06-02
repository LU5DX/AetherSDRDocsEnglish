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

| Control        | Label                                                                                                                                                                                                                                                                   | Default                                                                                                                                                                                                                                                                                                                                                                           |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pre-comp gain  | Drive                                                                                                                                                                                                                                                                   | 0.0 dB                                                                                                                                                                                                                                                                                                                                                                            |
| Phase rotation | Phase                                                                                                                                                                                                                                                                   | 0 stages                                                                                                                                                                                                                                                                                                                                                                          |
| Drive          | Pre-comp gain boost with linked auto-makeup. Pushes more signal across the threshold so the compressor engages harder, and simultaneously adds equal gain at the output so average RMS lifts alongside peaks rather than dropping. Pair with Phase to keep peaks clean. | Displayed in the floating StripCompPanel only (right column). Label shows as '+X.X dB'. Tooltip explains PAPR reduction pairing. Auto-makeup matches the broadcast-Optimod model — Drive pushes more material into the curve AND adds equal gain back, so the user's fixed Makeup stays a clean post-everything trim knob.                                                  |
| Phase          | Number of cascaded all-pass sections (0 = off). Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz). Symmetrizes asymmetric voice peaks before compression to reduce PAPR.                          | Displayed in the floating StripCompPanel only (right column). Label 'Off' when 0, 'N stg' when active. Tooltip: 'Pre-comp phase rotator. All-pass cascade that symmetrizes asymmetric voice peaks before compression. 0 = off, 4 = broadcast default.' Default centres (300/700/1500/2500 Hz with optional 1000/2000 Hz) cover the speech formant range without bunching. |
## Tips

- The applet tile now uses theme-aware colors for the compression curve widget. The background, grid, axis labels, curve, and ball all follow the active color theme. The gain-reduction bar fills with the accent slider color defined by the theme.
- Drive is only available in the floating StripCompPanel editor (right column), not in the compact applet tile. Double-click the COMP tile in the CHAIN widget to open it.
- The label shows a plus sign for positive values (e.g. "+6.0 dB").
- If you increase Drive significantly, you may need to adjust Threshold or Makeup gain to maintain your desired audio level.

## Related

- [Open the full Compressor editor for knee, limiter, Drive, and Phase controls](open-the-full-compressor-editor-for-knee-limiter-drive-and-phase-controls.md)
- [Rotate voice phase symmetry with the Phase rotator (0–6 stages)](rotate-voice-phase-symmetry-with-the-phase-rotator-0-6-stages.md)
- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)