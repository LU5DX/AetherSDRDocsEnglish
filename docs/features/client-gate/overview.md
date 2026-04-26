# Aetherial TX Gate / Aetherial AGC-T (RX) Overview

AetherSDR includes a client-side downward expander and noise gate that runs independently on both the transmit and receive audio paths. Use it to suppress background noise between words on TX, or to reduce band noise below a chosen floor on RX.

## Before you start

- The Gate stage must be enabled via the CHAIN widget or the floating editor on the matching side before the applet becomes visible.
- A radio connection is not required to configure gate settings.

## How it works

AetherSDR instantiates two fully independent copies of the gate processor:

- **Aetherial TX Gate** — operates on the transmit audio path. It attenuates audio that falls below the set threshold, reducing room noise and breath sounds between transmissions.
- **Aetherial AGC-T** — operates on the receive audio path. It attenuates received audio below the threshold, reducing continuous band noise between signals.

Both copies appear as sub-containers inside the Aetherial Audio (TXDSP) parent container. They share the same set of controls and indicators but store their parameters independently.

### Signal flow

The gate is a downward expander. When the input level drops below Thresh, the gate begins attenuating the signal. The amount of attenuation depends on Ratio and is bounded by Floor — the gate never cuts deeper than the Floor value, which prevents an unnatural dead silence. Attack and Release control how quickly the gate opens and closes in response to level changes.

At high Ratio values (approaching 10:1) the gate behaves as a hard cut; at low Ratio values (near 1:1) it acts as a gentle downward expander. Most users set Ratio between 2:1 and 4:1 for natural-sounding results.

### Visual feedback

Each applet tile provides two live indicators:

- **Transfer curve** — a static plot of the expander's input-to-output transfer function with a live ball showing the current input level. The ball position indicates whether the gate is currently open (ball above threshold line) or closed (ball below threshold line).
- **Gain-reduction bar** — a horizontal amber strip that fills from the right. The scale runs from 0 to 40 dB of gain reduction. A tick mark at −15 dB indicates the default Floor value. An empty bar means no attenuation is being applied.

The knobs on the applet tile and the floating editor (opened by double-clicking the GATE stage in the CHAIN widget) are kept in sync automatically.

## What each control does

| Control | Default | Valid range | Persisted setting (TX / RX) | Description |
|---|---|---|---|---|
| Thresh | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` / `ClientGateRxThresholdDb` | Level below which the gate starts attenuating. Set just above the noise floor you want to suppress. |
| Ratio | 2.0 | 1.0 to 10.0 | `ClientGateTxRatio` / `ClientGateRxRatio` | Expansion ratio, displayed as X.X:1. Higher values give a harder, more gate-like cut; lower values give a soft downward expansion. |
| Attack | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` / `ClientGateRxAttackMs` | How quickly the gate opens when input rises above Thresh. Shorter values open faster. |
| Release | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` / `ClientGateRxReleaseMs` | How quickly the gate closes after input falls below Thresh. Longer values give a more natural tail. |
| Floor | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` / `ClientGateRxFloorDb` | Maximum attenuation the gate is allowed to apply. Prevents the gate from producing total silence. |

The enabled/disabled state of each side is persisted separately: `ClientGateTxEnabled` (TX) and `ClientGateRxEnabled` (RX).

## Tips

- Watch the gain-reduction bar while not speaking on TX. If the bar shows no movement at all, Thresh may be set below the noise floor and the gate is not activating. If it never empties while you are speaking, Thresh is too high.
- Changes made on the applet tile knobs and the floating editor are reflected in both views within one meter tick (approximately 33 ms).
- Right-click the "Aetherial TX Gate" or "Aetherial AGC-T" sub-container titlebar to float, pop out, or hide the tile without disabling the gate processor.

## Related

- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Use AGC-T on RX to suppress band noise below a chosen floor](use-agc-t-on-rx-to-suppress-band-noise-below-a-chosen-floor.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
