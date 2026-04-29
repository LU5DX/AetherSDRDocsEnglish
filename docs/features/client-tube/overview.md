# Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview

AetherSDR includes a client-side tube saturation stage that runs on your computer, independent of the radio. Two fully separate instances exist: **Aetherial Mic-PreAmp** shapes your transmitted audio before it reaches the radio, and **Aetherial Dynamic Tube** shapes received audio on the way to your speakers or headphones. Both use the same bias-swept tube model and the same controls; their settings are stored independently.

## Before you start

- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel. The Tube sub-containers are hidden until the Tube stage is enabled via the CHAIN widget on the matching side.
- No radio connection is required to configure the tube controls.

## How it works

Each instance runs its signal through a tube transfer curve model. The curve bends according to Drive, Bias, and the selected tube character model (A, B, or C). A live input ball rides the curve in real time, showing which part of the saturation regime is active at the current signal level.

You can open the full editor for either side by double-clicking the TUBE stage in the CHAIN widget. The floating editor is titled **Aetherial Tube — TX** or **Aetherial Tube — RX**. The docked sub-container tile shows a compact set of knobs and the transfer curve without opening the editor. Changes made in the floating editor and in the docked tile stay in sync automatically.

The floating editor also includes an **OUT** level meter on its far right, showing post-saturation peak level. The meter is not visible in the docked tile.

To open the docked tile's context menu, right-click the **Aetherial Mic-PreAmp** or **Aetherial Dynamic Tube** sub-container titlebar. From there you can float, pop out, or hide the tile.

## What each control does

The table below applies to both the TX and RX instances. Where setting keys differ by side, both are shown. Controls marked **Editor only** are available in the floating editor but not in the docked tile.

| Control | Default | Valid range | TX setting key | RX setting key | Description |
|---|---|---|---|---|---|
| Transfer curve | — | — | — | — | Displays the current tube transfer curve. The live input ball moves along the curve at the current input level, showing the active saturation regime. Read-only indicator. Available in both the docked tile and the editor. |
| Drive | 0.00 dB | 0.0 – 24.0 dB | `ClientTubeTxDriveDb` | `ClientTubeRxDriveDb` | Pushes more signal into the tube stage. Higher values produce more saturation and curve bending. Displayed as `X.XX dB`. |
| Tone | 0.00 | −1.0 – 1.0 | `ClientTubeTxTone` | `ClientTubeRxTone` | Adjusts tonal character of the saturated signal. Negative values darken; positive values brighten. Displayed as `X.XX`. |
| A | checked (default) | — | `ClientTubeTxModel` | `ClientTubeRxModel` | Selects tube character Model A. Exclusive with B and C. Lit amber when active. **Editor only.** |
| B | unchecked | — | `ClientTubeTxModel` | `ClientTubeRxModel` | Selects tube character Model B. Exclusive with A and C. Lit amber when active. **Editor only.** |
| C | unchecked | — | `ClientTubeTxModel` | `ClientTubeRxModel` | Selects tube character Model C. Exclusive with A and B. Lit amber when active. **Editor only.** |
| Bias | 0 % | 0.0 – 1.0 (displayed as 0 – 100 %) | `ClientTubeTxBias` | `ClientTubeRxBias` | Shifts the operating point on the transfer curve, changing the mix of even and odd harmonics. Displayed as a percentage. |
| Output | 0.00 dB | −24.0 – 12.0 dB | `ClientTubeTxOutputDb` | `ClientTubeRxOutputDb` | Post-tube make-up or trim gain. Use this to compensate for level changes introduced by saturation. Displayed as `X.XX dB`. |
| Dry/Wet | 100 % | 0.0 – 1.0 (displayed as 0 – 100 %) | `ClientTubeTxDryWet` | `ClientTubeRxDryWet` | Dry/wet blend between the unprocessed and saturated signal. 100 % passes only the saturated signal; 0 % passes only the dry signal. |
| Envelope | 0 % | −1.0 – 1.0 (displayed as signed percentage) | `ClientTubeTxEnvelope` | `ClientTubeRxEnvelope` | Envelope-follower depth. Positive values increase drive on transients so the tube gets hotter on loud peaks; negative values reduce drive dynamically, compressing harmonic output. Has no effect when set to 0 %. **Editor only.** |
| Attack | 5.00 ms | 0.1 – 30.0 ms | `ClientTubeTxAttackMs` | `ClientTubeRxAttackMs` | Sets how quickly the envelope follower responds to rising signal levels. Only active when Envelope ≠ 0 %. Displayed as `X.XX ms` below 10 ms, `X.X ms` above. **Editor only.** |
| Release | 35.00 ms | 10.0 – 500.0 ms | `ClientTubeTxReleaseMs` | `ClientTubeRxReleaseMs` | Sets how quickly the envelope follower recovers after signal levels drop. Only active when Envelope ≠ 0 %. Displayed as `X.XX ms` below 100 ms, `X.X ms` above. **Editor only.** |

## Output level meter (editor only)

The floating editor contains an **OUT** level meter on its far right column. It shows the post-saturation peak level using fast-attack / slow-release ballistics. The color bands are:

| Color | Range |
|---|---|
| Green | −60 to −12 dB |
| Lime | −12 to −6 dB |
| Amber | −6 to −3 dB |
| Red | Above −3 dB |

The meter is not present in the docked applet tile.

Bypass for each instance is controlled from the CHAIN widget, not from within the tube tile itself. See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).

## Tips

- Start with Drive at 0.00 dB and raise it slowly until the transfer curve begins to bend visibly. The live input ball shows whether peaks are reaching the saturated region.
- Use Output to bring the processed level back in line with the dry level after adding Drive, so comparisons are level-matched. Watch the OUT meter in the editor to check post-saturation peak levels.
- Set Dry/Wet below 100 % to blend in parallel with the dry signal, which can add body without the full character of full saturation.
- Bias at 0 % produces a symmetrical curve. Raising it introduces asymmetry, shifting the harmonic content toward even-order harmonics.
- Use Model A, B, or C to change the fundamental character of the tube curve before adjusting Drive and Bias.
- Set Envelope to a positive value to make the saturation track transients — loud peaks drive the tube harder automatically. Use Attack and Release to control how quickly the follower reacts and recovers.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Dry/Wet](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)