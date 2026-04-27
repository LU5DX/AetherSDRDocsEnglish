# Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview

AetherSDR includes a client-side tube saturation stage that runs on your computer, independent of the radio. Two fully separate instances exist: **Aetherial Mic-PreAmp** shapes your transmitted audio before it reaches the radio, and **Aetherial Dynamic Tube** shapes received audio on the way to your speakers or headphones. Both use the same bias-swept tube model and the same five controls; their settings are stored independently.

## Before you start

- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel. The Tube sub-containers are hidden until the Tube stage is enabled via the CHAIN widget on the matching side.
- No radio connection is required to configure the tube controls.

## How it works

Each instance runs its signal through a tube transfer curve model. The curve bends according to Drive, Bias, and the selected model. A live input ball rides the curve in real time, showing which part of the saturation regime is active at the current signal level.

You can open the full editor for either side by double-clicking the TUBE stage in the CHAIN widget. The floating editor is titled **Aetherial Tube — TX** or **Aetherial Tube — RX**. The five knobs are also available directly in the docked sub-container tile without opening the editor. Changes made in the floating editor and in the docked tile stay in sync automatically.

To open the docked tile's context menu, right-click the **Aetherial Mic-PreAmp** or **Aetherial Dynamic Tube** sub-container titlebar. From there you can float, pop out, or hide the tile.

## What each control does

The table below applies to both the TX and RX instances. Where setting keys differ by side, both are shown.

| Control | Default | Valid range | TX setting key | RX setting key | Description |
|---|---|---|---|---|---|
| Transfer curve | — | — | — | — | Displays the current tube transfer curve. The live input ball moves along the curve at the current input level, showing the active saturation regime. Read-only indicator. |
| Drive | 0.0 dB | 0.0 – 24.0 dB | `ClientTubeTxDriveDb` | `ClientTubeRxDriveDb` | Pushes more signal into the tube stage. Higher values produce more saturation and curve bending. Displayed as `X.X dB`. |
| Tone | 0.00 | −1.0 – 1.0 | `ClientTubeTxTone` | `ClientTubeRxTone` | Adjusts tonal character of the saturated signal. Negative values darken; positive values brighten. Displayed as `X.XX`. |
| Bias | 0 % | 0.0 – 1.0 (displayed as 0 – 100 %) | `ClientTubeTxBiasAmount` | `ClientTubeRxBiasAmount` | Shifts the operating point on the transfer curve, changing the mix of even and odd harmonics. Displayed as a percentage. |
| Output | 0.0 dB | −24.0 – 12.0 dB | `ClientTubeTxOutputGainDb` | `ClientTubeRxOutputGainDb` | Post-tube make-up or trim gain. Use this to compensate for level changes introduced by saturation. Displayed as `X.X dB`. |
| Mix | 100 % | 0.0 – 1.0 (displayed as 0 – 100 %) | `ClientTubeTxDryWet` | `ClientTubeRxDryWet` | Dry/wet blend between the unprocessed and saturated signal. 100 % passes only the saturated signal; 0 % passes only the dry signal. |

Bypass for each instance is controlled from the CHAIN widget, not from within the tube tile itself. See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).

## Tips

- Start with Drive at 0.0 dB and raise it slowly until the transfer curve begins to bend visibly. The live input ball shows whether peaks are reaching the saturated region.
- Use Output to bring the processed level back in line with the dry level after adding Drive, so comparisons are level-matched.
- Set Mix below 100 % to blend in parallel with the dry signal, which can add body without the full character of full saturation.
- Bias at 0 % produces a symmetrical curve. Raising it introduces asymmetry, shifting the harmonic content toward even-order harmonics.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
