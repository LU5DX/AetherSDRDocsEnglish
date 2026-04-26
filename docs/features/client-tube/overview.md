# Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) Overview

AetherSDR includes a client-side dynamic tube saturator that runs independently on both the transmit and receive audio paths. Use it to add harmonic richness to your transmitted signal (Aetherial Mic-PreAmp) or to shape the tone of received audio (Aetherial Dynamic Tube) — without touching any radio-side DSP.

## Before you start

- The tube stage must be enabled via the CHAIN widget on the matching TX or RX side before the applet becomes visible.
- No radio connection is required to configure the tube parameters.

## How it works

AetherSDR instantiates two fully independent copies of the tube saturator: one bound to the TX path (titled **Aetherial Mic-PreAmp**) and one bound to the RX path (titled **Aetherial Dynamic Tube**). Each copy has its own set of controls and persisted settings. Changes made in the docked applet and changes made in the floating editor stay in sync automatically.

**Opening the applet.** The TX and RX sub-containers appear inside the Aetherial Audio (TXDSP) parent container in the applet panel. They remain hidden until the Tube stage is enabled via the CHAIN widget. Double-clicking the TUBE stage in the CHAIN widget opens the matching frameless editor, titled **Aetherial Tube — TX** or **Aetherial Tube — RX**. Right-clicking the sub-container titlebar lets you float, pop out, or hide it.

**The transfer curve.** The applet displays a compact transfer curve that bends in real time as you adjust Drive, Bias, and the tube model. A live input ball rides along the curve at the current signal level, showing which saturation regime the signal is operating in.

**Signal flow.** The signal passes through Drive (input gain into the tube model), then the tube transfer function shaped by Bias, then Tone filtering, then Output (post-tube trim), with Mix blending the wet result back against the dry signal.

**Settings sync.** The five knobs in the docked applet and their counterparts in the floating editor poll each other at approximately 30 Hz. Adjusting a knob in either location updates the other.

## What each control does

The following controls and defaults apply to both the TX and RX instances. Settings keys are shown for the TX instance; the RX instance uses the corresponding `ClientTubeRx*` keys.

| Control | Default | Valid range | Persisted key (TX) | Behavior |
|---|---|---|---|---|
| Transfer curve | — | — | — | Displays the current tube transfer curve. The live input ball moves along the curve at the current input level. Read-only indicator. |
| Drive | 0.0 dB | 0.0 – 24.0 dB | `ClientTubeTxDriveDb` | Pushes more signal into the tube stage. Higher values cause more saturation and curve bending. |
| Tone | 0.00 | -1.0 – 1.0 | `ClientTubeTxTone` | Shapes the spectral character of the saturated signal. Negative values darken; positive values brighten. |
| Bias | 0 % | 0 – 100 % | `ClientTubeTxBiasAmount` | Shifts the operating point on the transfer curve, changing the balance of even and odd harmonics. |
| Output | 0.0 dB | -24.0 – 12.0 dB | `ClientTubeTxOutputGainDb` | Post-tube make-up or trim gain. Use it to compensate for level changes introduced by Drive. |
| Mix | 100 % | 0 – 100 % | `ClientTubeTxDryWet` | Blends the saturated (wet) signal against the unprocessed (dry) signal. 100 % is fully saturated; 0 % is fully dry. |

RX-path equivalents use `ClientTubeRxEnabled`, `ClientTubeRxDriveDb`, `ClientTubeRxTone`, `ClientTubeRxBiasAmount`, `ClientTubeRxOutputGainDb`, and `ClientTubeRxDryWet`.

## Tips

- Start with Drive at 0.0 dB and increase slowly while watching the transfer curve bend. The point where the curve noticeably deviates from a straight line is the onset of saturation.
- Use Mix below 100 % to blend in saturation subtly without fully replacing the dry signal. This is especially useful on RX to preserve clarity while adding warmth.
- Bias shifts which harmonics dominate. Small amounts (10–20 %) introduce asymmetry and even-order harmonics characteristic of single-ended tube stages.
- After raising Drive, lower Output to keep the processed level matched to the unprocessed level.
- The TX and RX instances are completely independent. Settings changed on one side do not affect the other.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
