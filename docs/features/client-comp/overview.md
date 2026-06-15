# Aetherial Compressor (TX) / Aetherial AGC-C (RX) Overview

AetherSDR includes a client-side dynamic-range compressor that runs in two independent instances: **Aetherial Compressor** on the TX path and **Aetherial AGC-C** on the RX path. Use the TX instance to tame voice peaks before transmitting; use the RX instance to even out received audio levels.

## Before you start

- Both instances live inside the **Aetherial Audio (TXDSP)** parent container in the applet panel. Each tile stays hidden until its stage is enabled — bypass it off via the CHAIN widget or the floating editor on the matching side.
- No radio connection is required to configure the compressor. Settings are saved locally.

## How it works

Each instance processes audio independently. The compressor monitors the input signal level. When the level exceeds the threshold, it attenuates the output by the compression ratio you choose. Attack and Release control how fast it reacts. Makeup adds back gain lost to compression. An optional limiter (configured in the full editor) puts a hard ceiling on output.

The applet tile for each instance shows:

- A **transfer curve** — a static input/output plot with a live envelope ball that rides along the curve in real time, showing the current operating point. The curve uses theme-aware colors for background, grid, labels, identity line, curve line, and ball glow/core.
- A **gain-reduction bar** — a horizontal amber strip that fills from the right. The scale runs 0 to 20 dB of gain reduction. A tick marks the −6 dB point as a typical working reference. The strip refreshes at approximately 30 Hz with smoothed ballistics. The fill color is set by theme and styled at the `applet/comp` scope.

When a compressor stage is bypassed, its entire applet tile dims to approximately 55 % opacity. The tile returns to full opacity when the stage is re-enabled. This visual state matches the dim behavior used by the EQ curve applet.

To open the full editor for either instance — which adds knee, limiter, Drive, and Phase controls not available in the applet — double-click the COMP stage in the CHAIN widget on the TX or RX side. The editor opens titled **Aetherial Compressor — TX** or **Aetherial Compressor — RX** accordingly.

## What each control does

The five knobs appear in a row at the bottom of each applet tile. Both the TX (Aetherial Compressor) and RX (Aetherial AGC-C) instances share the same knob layout with independent state.

Each knob supports inline value editing: click the displayed value text to open an edit field. Type a new value and press Enter or click elsewhere to commit the change. Press Escape to cancel. While the edit field is focused, mouse wheel events continue to adjust the knob as usual.

| Knob    | Default   | Valid range      | Setting key |
|---------|-----------|------------------|-------------|
| Thresh  | −18.0 dB  | −60.0 to 0.0 dB  | `ClientCompTxThresholdDb` |
| Ratio   | 3.0       | 1.0 to 20.0      | `ClientCompTxRatio` |
| Attack  | 20.0 ms   | 0.1 to 300.0 ms  | `ClientCompTxAttackMs` |
| Release | 200 ms    | 5 to 2000 ms     | `ClientCompTxReleaseMs` |
| Makeup  | 0.0 dB    | −12.0 to 24.0 dB | `ClientCompTxMakeupDb` |

### Control behavior details

- **Thresh**: Linear mapping. Sets the level above which compression starts. Label formatted as `-18.0 dB`.
- **Ratio**: Logarithmic mapping (1 * 20^n). Sets how hard peaks are held once threshold is crossed. Label formatted as `X.XX:1`.
- **Attack**: Exponential mapping (0.1 * 3000^n). Sets how quickly the compressor clamps down after the threshold is crossed. Label formatted as `X.X ms` below 10 ms, `X ms` above.
- **Release**: Exponential mapping (5 * 400^n). Sets how quickly gain returns after the input drops back below threshold. Label formatted as `X ms`.
- **Makeup**: Linear mapping. Adds back gain lost to compression. Label shows explicit `+` sign for positive values.

### Compression curve indicators

- **Transfer curve**: Compact-mode ClientCompCurveWidget. Draws the input/output transfer curve plus a live ball showing the current envelope level. View-only in the applet; editable in the floating ClientCompEditor.
- **Gain-reduction bar**: Horizontal amber strip, right-filled. Scale maxes at 20 dB reduction; a tick at -6 dB marks a typical working amount. Refreshed ~30 Hz from `ClientComp::gainReductionDb()` with MeterSmoother ballistics. The smoothing algorithm uses a stateful tick system — the bar repaints only when the smoothed value actually changes, reducing CPU usage while maintaining smooth visual feedback.

## Additional controls in the floating editor

The floating StripCompPanel (open by double-clicking the COMP tile in the CHAIN widget) adds these controls:

| Control | Default | Valid range | Setting key | Behavior |
|---------|---------|-------------|-------------|----------|
| Knee    | Adjustable in editor | Adjustable in editor | `ClientCompTxKneeDb` / `ClientCompRxKneeDb` | Soft-knee width in dB. |
| Ceiling | Adjustable in editor | Adjustable in editor | `ClientCompTxLimCeilingDb` / `ClientCompRxLimCeilingDb` | Hard ceiling applied by the limiter. |
| Makeup  | 0.0 dB  | −12.0 to 24.0 dB | `ClientCompTxMakeupDb` / `ClientCompRxMakeupDb` | Duplicate control in editor for convenience. |
| Drive   | 0.0 dB  | 0.0 to 18.0 dB | `ClientCompTxDriveDb` / `ClientCompRxDriveDb` | Pre-comp gain boost with linked auto-makeup. Pushes more signal across the threshold so the compressor engages harder, and simultaneously adds equal gain at the output so average RMS lifts alongside peaks rather than dropping. Label shows as `+X.X dB`. Tooltip explains #2887 PAPR reduction pairing. |
| Phase   | 0 stages | 0 to 6 stages | `ClientCompTxPhaseRotatorStages` / `ClientCompRxPhaseRotatorStages` | Number of cascaded all-pass sections (0 = off). Each stage adds 12 dB/oct of phase rotation at staggered frequencies (300/700/1500/2500 Hz, plus optional 1000/2000 Hz). Symmetrizes asymmetric voice peaks before compression to reduce PAPR. Label `Off` when 0, `N stg` when active. Tooltip: `Pre-comp phase rotator (#2887). All-pass cascade that symmetrizes asymmetric voice peaks before compression. 0 = off, 4 = broadcast default.` |
| Limiter enable | Off | Off / On | `ClientCompTxLimEnabled` / `ClientCompRxLimEnabled` | Toggle button for output limiter. |

## Indicator states

| Indicator | States | Meaning |
|-----------|--------|---------|
| Envelope ball | resting at threshold line<br>moving along curve | Live input level plotted against the static transfer curve. |
| Gain-reduction strip | empty<br>amber fill<br>−6 dB tick | Amount of dynamic attenuation currently applied by the compressor. |

## Tips

- The envelope ball on the transfer curve gives continuous visual feedback. If the ball sits well above the knee at rest, the threshold is set too low — raise Thresh until the ball only crosses the knee on peaks.
- The −6 dB tick on the gain-reduction bar is a useful reference point. Consistent amber fill up to or slightly past that tick indicates active, moderate compression. Fill reaching the right edge of the bar means the compressor is working at or beyond 20 dB reduction.
- When a stage is bypassed, the tile dims visibly. If the tile appears dim and controls are unresponsive, check that the COMP stage is not bypassed in the CHAIN widget.
- The TX and RX instances are fully independent. Changes to Aetherial Compressor (TX) do not affect Aetherial AGC-C (RX) and vice versa.
- Knee, limiter, Drive, and Phase controls are not available in the applet tile. Open the full editor to access them.
- To change a knob value by typing directly, click the displayed value text. The edit field appears with a dark background and cyan border. Type the new value and press Enter or click elsewhere to apply it. Press Escape to cancel without changing the value.
- The Drive knob includes automatic makeup gain: as you increase Drive, the compressor engages harder while output gain is simultaneously raised so the average RMS level stays up. This matches the broadcast-Optimod model — Drive pushes more material into the curve AND adds equal gain back, so your fixed Makeup knob remains a clean post-everything trim.
- The gain-reduction meter uses an efficient smoothing algorithm that only repaints when the smoothed value changes, reducing CPU usage while maintaining smooth visual feedback.

## Related

- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Set compression ratio for voice (TX) or for received audio (RX AGC-C)](set-compression-ratio-for-voice-tx-or-for-received-audio-rx-agc-c.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)