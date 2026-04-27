# Aetherial TX Gate / Aetherial AGC-T (RX) Overview

AetherSDR includes a client-side downward expander and noise gate that runs independently on both the transmit and receive audio paths. Use it to suppress background noise between words on TX, or to reduce band noise below a chosen floor on RX.

## Before you start

- The Gate stage must be enabled via the CHAIN widget or the floating editor on the matching side before the applet becomes visible.
- AetherSDR does not need to be connected to a radio for gate controls to be adjusted, but audio must be running for the live indicators to be meaningful.

## How it works

AetherSDR instantiates two fully independent copies of the gate applet:

- **Aetherial TX Gate** — acts on outgoing transmit audio. Located in the Aetherial Audio (TXDSP) parent container.
- **Aetherial AGC-T** — acts on incoming receive audio. Located in the same parent container as a separate sub-container.

Both copies share identical controls and indicators. Settings for each side are stored independently. Changes made in the docked applet tile and changes made in the floating editor stay in sync; the applet polls the engine approximately every 33 ms and updates knob positions and the gain-reduction bar to reflect whatever side is active.

### Signal flow

The gate is a **downward expander**. When the input level falls below the Thresh point, the gate attenuates the signal. The amount of attenuation depends on Ratio, and the deepest cut allowed is set by Floor. Attack controls how quickly the gate opens when the signal rises above Thresh; Release controls how quickly it closes again when the signal falls back below it.

Setting Ratio to a low value (near 1.0:1) produces a gentle soft-expander effect that gradually reduces level. Setting Ratio to a high value (near 10.0:1) produces a hard gate that cuts aggressively.

### Opening the applet

Double-click the GATE stage in the CHAIN widget on the TX or RX side to open the matching frameless editor, titled **Aetherial Gate — TX** or **Aetherial Gate — RX**. The docked sub-container titlebars for **Aetherial TX Gate** and **Aetherial AGC-T** can be right-clicked to float, pop out, or hide the tile.

## What each control does

The controls listed below appear identically in both the TX and RX applets. The setting keys shown apply to the TX side; the RX side uses the equivalent `ClientGateRx*` keys.

| Control | Kind | Default | Valid range | TX setting key | Behavior |
|---|---|---|---|---|---|
| Transfer curve | Indicator | — | — | — | Plots the static expander transfer curve. A live ball marks the current input level and shows whether the gate is open or closed. |
| Gain-reduction bar | Meter | — | 0 to 40 dB GR | — | Horizontal amber strip, right-filled. Scale maxes at 40 dB. A tick at −15 dB marks the default soft-expander floor. |
| Thresh | Knob | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` | Level below which the gate starts attenuating. |
| Ratio | Knob | 2.0:1 | 1.0 to 10.0 | `ClientGateTxRatio` | Higher values give a harder gate cut; lower values act as a soft downward expander. |
| Return | Knob | 2.0 dB | 0.0 to 20.0 dB | — | Hysteresis above Thresh at which the gate reopens. |
| Release | Knob | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` | How quickly the gate closes after input falls below threshold. |
| Floor | Knob | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` | Maximum attenuation the gate is allowed to apply. |

The enable/bypass state for each side is persisted under `ClientGateTxEnabled` (TX) and `ClientGateRxEnabled` (RX).

## Tips

- Watch the gain-reduction bar while not speaking (TX) or during a band-noise-only moment (RX). If the bar is not filling, Thresh is set below the noise floor and the gate is not triggering. See [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md).
- The −15 dB tick on the gain-reduction bar marks the Floor default. If the bar fills fully past that tick, Floor is set deeper than −15 dB or Ratio is high enough to push reduction beyond it.
- Changes to any knob take effect immediately and are saved automatically. No Apply button is needed.

## Troubleshooting

- **Applet is not visible** — The Gate stage has not been enabled on that side. Enable it via the CHAIN widget or the floating editor for the TX or RX side.
- **Gate is not attenuating noise between words** — Thresh may be set too low, below the room noise floor. Raise Thresh until the gain-reduction bar shows movement during silence. See [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md).
- **Gate cuts into the start of speech** — Attack is too slow relative to your speech onset, or Thresh is too high. Lower Thresh slightly or reduce Attack. See [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).
- **Unnatural silence between words** — Floor is set too deep. Raise Floor toward 0 dB so some residual audio passes through during closed periods. See [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md).
- **Knob positions in the tile do not match the floating editor** — The tile syncs every ~33 ms. If they appear mismatched immediately after opening the editor, wait one update cycle or move a knob to force a sync.

## Related

- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Use AGC-T on RX to suppress band noise below a chosen floor](use-agc-t-on-rx-to-suppress-band-noise-below-a-chosen-floor.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
