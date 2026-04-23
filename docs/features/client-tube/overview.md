# Tube Saturator overview

The Tube Saturator is a TX-side processor that shapes your transmitted signal through a bias-swept tube model, adding harmonic richness before the signal reaches the radio. Use it to add warmth or edge to SSB and other voice modes without changing anything on the Flex radio itself.

## Before you start

- The Tube Saturator operates on the transmit audio path. It has no effect on received signals.
- The TUBE stage must be enabled via the CHAIN widget or the floating editor before the applet becomes visible in the PooDoo Audio (TXDSP) container.

## How it works

The Tube Saturator inserts a nonlinear transfer function — a tube model — into the TX audio chain. Drive pushes the signal deeper into the nonlinear region of the curve. Bias shifts the operating point on that curve, changing the ratio of even to odd harmonics. Tone applies a post-saturation tilt to brighten or darken the result. Output trims the level after saturation so you can compensate for any gain change. Mix blends the saturated signal back against the dry signal, allowing parallel saturation.

The transfer curve display shows the current shape of the tube model in real time. A live input ball rides along the curve at the actual input level, showing which part of the curve your signal is exciting at any moment. When Drive is low and the curve is nearly straight, little saturation occurs. As Drive increases, the curve bends and the ball enters the nonlinear region.

Changes made in the floating editor (opened by double-clicking the Tube stage in the CHAIN widget) are reflected on the applet knobs within approximately 33 ms, and vice versa.

To open the applet: enable the Tube stage in the CHAIN widget. The TUBE sub-container appears inside the PooDoo Audio (TXDSP) parent container. Double-click the Tube stage in the CHAIN widget to open the floating editor. Right-click the TUBE sub-container titlebar to float, pop out, or hide it.

## What each control does

| Control | What it does | Default | Valid range | Setting key |
|---|---|---|---|---|
| Transfer curve | Draws the active tube transfer curve. The live input ball moves along the curve at the current input level. Read-only indicator. | — | — | — |
| Drive | Pushes more signal into the tube stage, increasing saturation. | 0.0 dB | 0.0 to 24.0 dB | `ClientTubeTxDriveDb` |
| Tone | Tilts the frequency balance of the saturated signal. Negative values darken; positive values brighten. | 0.00 | -1.0 to 1.0 | `ClientTubeTxTone` |
| Bias | Shifts the operating point on the transfer curve, changing the harmonic mix between even and odd orders. | 0 % | 0 % to 100 % | `ClientTubeTxBiasAmount` |
| Output | Post-tube make-up or trim gain. Use this to compensate for level changes introduced by saturation. | 0.0 dB | -24.0 to 12.0 dB | `ClientTubeTxOutputGainDb` |
| Mix | Blends the dry (unprocessed) and saturated signals. 100 % passes the fully saturated signal; 0 % passes the dry signal unchanged. | 100 % | 0 % to 100 % | `ClientTubeTxDryWet` |

The enabled/disabled state of the Tube stage is persisted as `ClientTubeTxEnabled`. Bypass is controlled from the CHAIN widget, not from within the applet itself.

## Tips

- Start with Drive at a low value and watch the transfer curve. The ball indicates which portion of the curve your signal is using — aim to keep peaks in the gently bent region rather than hard against the limits.
- After increasing Drive, use Output to bring the level back to where it was so downstream processing and your TX audio level remain consistent.
- Setting Mix below 100 % lets you blend in only a portion of the saturation, which can be useful when you want subtle harmonic enhancement without a large tonal change.

## Related

- [Dial Drive until the curve starts to bend](dial-drive-until-the-curve-starts-to-bend.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from the chain](bypass-the-tube-from-the-chain.md)
