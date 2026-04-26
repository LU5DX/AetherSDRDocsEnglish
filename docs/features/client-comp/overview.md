# Aetherial Compressor (TX) / Aetherial AGC-C (RX) Overview

AetherSDR includes a client-side dynamic-range compressor that runs in two independent instances: **Aetherial Compressor** on the TX path and **Aetherial AGC-C** on the RX path. Use the TX instance to tame voice peaks before transmitting; use the RX instance to even out received audio levels.

## Before you start

- Both instances live inside the **Aetherial Audio (TXDSP)** parent container in the applet panel. Each tile stays hidden until its stage is enabled — bypass it off via the CHAIN widget or the floating editor on the matching side.
- No radio connection is required to configure the compressor. Settings are saved locally.

## How it works

Each instance processes audio independently. The compressor monitors the input signal level. When the level exceeds the threshold, it attenuates the output by the compression ratio you choose. Attack and Release control how fast it reacts. Makeup adds back gain lost to compression. An optional limiter (configured in the full editor) puts a hard ceiling on output.

The applet tile for each instance shows:

- A **transfer curve** — a static input/output plot with a live envelope ball that rides along the curve in real time, showing the current operating point.
- A **gain-reduction bar** — a horizontal amber strip that fills from the right. The scale runs 0 to 20 dB of gain reduction. A tick marks the −6 dB point as a typical working reference. The strip refreshes at approximately 30 Hz.

To open the full editor for either instance — which adds knee and limiter controls not available in the applet — double-click the COMP stage in the CHAIN widget on the TX or RX side. The editor opens titled **Aetherial Compressor — TX** or **Aetherial Compressor — RX** accordingly.

## What each control does

The five knobs appear in a row at the bottom of each applet tile. Both the TX (Aetherial Compressor) and RX (Aetherial AGC-C) instances share the same knob layout with independent state.

| Knob | Default | Valid range | TX setting key | RX setting key | Behavior |
|---|---|---|---|---|---|
| Thresh | −18.0 dB | −60.0 to 0.0 dB | `ClientCompTxThresholdDb` | `ClientCompRxThresholdDb` | Sets the level above which compression starts. Mapped linearly. Label shows value as `-18.0 dB`. |
| Ratio | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` | `ClientCompRxRatio` | Sets how hard peaks are held once threshold is crossed. Mapped logarithmically. Label shows value as `X.XX:1`. |
| Attack | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` | `ClientCompRxAttackMs` | Sets how quickly the compressor clamps down after threshold is crossed. Mapped exponentially. Label shows `X.X ms` below 10, `X ms` above. |
| Release | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` | `ClientCompRxReleaseMs` | Sets how quickly gain returns after the input drops back below threshold. Mapped exponentially. Label shows `X ms`. |
| Makeup | 0.0 dB | −12.0 to 24.0 dB | `ClientCompTxMakeupDb` | `ClientCompRxMakeupDb` | Adds back gain lost to compression. Label shows an explicit `+` sign for positive values. |

Additional settings managed only through the full editor:

| Setting key (TX) | Setting key (RX) | Description |
|---|---|---|
| `ClientCompTxEnabled` | `ClientCompRxEnabled` | Whether the compressor stage is active (bypass off). |
| `ClientCompTxKneeDb` | `ClientCompRxKneeDb` | Soft-knee width in dB. Adjustable in the floating editor. |
| `ClientCompTxLimEnabled` | `ClientCompRxLimEnabled` | Whether the output limiter is active. |
| `ClientCompTxLimCeilingDb` | `ClientCompRxLimCeilingDb` | Hard ceiling applied by the limiter. |

## Tips

- The envelope ball on the transfer curve gives continuous visual feedback. If the ball sits well above the knee at rest, the threshold is set too low — raise Thresh until the ball only crosses the knee on peaks.
- The −6 dB tick on the gain-reduction bar is a useful reference point. Consistent amber fill up to or slightly past that tick indicates active, moderate compression. Fill reaching the right edge of the bar means the compressor is working at or beyond 20 dB reduction.
- The TX and RX instances are fully independent. Changes to Aetherial Compressor (TX) do not affect Aetherial AGC-C (RX) and vice versa.
- Knee and limiter controls are not available in the applet tile. Open the full editor to access them.

## Related

- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Set compression ratio for voice (TX) or for received audio (RX AGC-C)](set-compression-ratio-for-voice-tx-or-for-received-audio-rx-agc-c.md)
- [Tune attack / release for a natural-sounding squeeze](tune-attack-release-for-a-natural-sounding-squeeze.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
