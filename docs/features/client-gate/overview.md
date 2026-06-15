# Aetherial TX Gate / Aetherial AGC-G (RX) Overview

AetherSDR includes a client-side downward expander and noise gate that runs independently on both the transmit and receive audio paths. Use it to suppress background noise between words on TX, or to reduce band noise below a chosen floor on RX.

## Before you start

- The Gate stage must be enabled via the CHAIN widget or the floating editor on the matching side before the applet becomes visible.
- AetherSDR does not need to be connected to a radio for gate controls to be adjusted, but audio must be running for the live indicators to be meaningful.

## How it works

AetherSDR instantiates two fully independent copies of the gate applet:

- **Aetherial TX Gate** — acts on outgoing transmit audio. Located in the Aetherial Audio (TXDSP) parent container.
- **Aetherial AGC-G** — acts on incoming receive audio. Located in the same parent container as a separate sub-container.

Both copies share identical controls and indicators. Settings for each side are stored independently. Changes made in the docked applet tile and changes made in the floating editor stay in sync; the applet polls the engine approximately every 33 ms and updates knob positions and the gain-reduction bar to reflect whatever side is active.

### Signal flow

The gate is a **downward expander**. When the input level falls below the Thresh point, the gate attenuates the signal. The amount of attenuation depends on Ratio, and the deepest cut allowed is set by Floor. Return sets a hysteresis deadband: the gate opens when the signal rises above Thresh and does not close again until the signal drops below Thresh − Return. Release controls how quickly the gate closes once the signal falls below that lower boundary.

Setting Ratio to a low value (near 1.0:1) produces a gentle soft-expander effect that gradually reduces level. Setting Ratio to a high value (near 10.0:1) produces a hard gate that cuts aggressively.

### Bypass dimming

When the gate stage is bypassed, the entire applet tile renders at reduced opacity (approximately 55 % of full brightness). This matches the dim effect used on the EQ curve and gives a clear at-a-glance indication that the stage is not processing audio. The tile returns to full opacity as soon as the stage is re-enabled.

### Opening the applet

Double-click the GATE stage in the CHAIN widget on the TX or RX side to open the matching frameless editor, titled **Aetherial Gate — TX** or **Aetherial Gate — RX**. The docked sub-container titlebars for **Aetherial TX Gate** and **Aetherial AGC-G** can be right-clicked to float, pop out, or hide the tile.

## What each control does

The controls listed below appear identically in both the TX and RX applets. The setting keys shown apply to the TX side; the RX side uses the equivalent `ClientGateRx*` keys.

| Control | Kind | Default | Valid Range | Setting Key | Behavior |
|---|---|---|---|---|---|
| Transfer curve | Indicator | — | — | — | Compact-mode ClientGateCurveWidget. Plots the expander's static transfer curve and a live ball at the current input level. |
| Gain-reduction bar | Meter | — | 0 to 40 dB GR | — | Horizontal amber strip, right-filled. Scale maxes at 40 dB (gates can cut very deep); a tick at -15 dB marks the soft-expander default floor. |
| Thresh | Knob | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` | Linear mapping. Level below which the gate starts attenuating. |
| Ratio | Knob | 2.0:1 | 1.0 to 10.0 | `ClientGateTxRatio` | Linear mapping. Higher ratios give a harder, more gate-like cut; lower ratios act as a soft downward expander. Label shows as 'X.X:1'. |
| Return | Knob | 2.0 dB | 0.0 to 20.0 dB | `ClientGateTxReturnDb` | Linear mapping (n * 20). Sets the hysteresis deadband: the gate opens above Thresh and doesn't close again until the input drops below Thresh − Return, preventing rapid chatter near the threshold. Label shows as 'X.XX dB'. The curve widget draws a soft-cyan vertical band between (Thresh − Return) and Thresh to make the sticky zone visible. |
| Release | Knob | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` | Exponential mapping (5 * 400^n). Sets how quickly the gate closes after input falls below Thresh − Return. Label shows 'X.X ms' below 100, 'X ms' above. |
| Floor | Knob | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` | Linear mapping. Maximum attenuation the gate is allowed to apply. |
| Flip (Expander / Gate) | Toggle | Unchecked (Expander) | — | — | Editor-only control (floating ClientGateEditor). Unchecked = downward-expander (gentle, ratio-based). Checked = Gate (hard cut). Snaps ratio and floor to preset pairs when toggled; other knobs stay put. Label updates live between 'Expander' and 'Gate'. Colour: unchecked = green (Expander), checked = amber (Gate). Tooltip: 'Flip between downward Expander (gentle) and Gate (hard) modes. Snaps ratio + floor to preset pairs; other knobs stay where you left them.' |
| Peek (lookahead) | Dropdown | Off | Off, 1 ms, 1.5 ms, 3 ms, 5 ms | — | Editor-only control. Sets a pre-read delay so the gate can open fractionally before a transient arrives, avoiding clipped attack edges. 'Off' disables the delay line entirely. Higher values increase latency on the TX path. 1 and 1.5 ms match Ableton's preset options; 3 and 5 ms added for very fast transients. |
| Attack | Knob | 0.50 ms | 0.1 to 100 ms | `ClientGateTxAttackMs` | Editor-only control. Exponential mapping (0.1 * 1000^n). Sets how quickly the gate opens after input rises above Thresh. Label shows 'X.XX ms' below 10 ms, 'X.X ms' above. |
| Hold | Knob | 0.0 ms | 0.0 to 500 ms | `ClientGateTxHoldMs` | Editor-only control. Linear mapping (n * 500). After the input drops below Thresh − Return the gate stays open for this long before it begins closing, preventing flutter on rhythmic material. Label shows 'X.X ms'. |

The enable/bypass state for each side is persisted under `ClientGateTxEnabled` (TX) and `ClientGateRxEnabled` (RX).

## Inline value editing

Knobs in the applet tile support direct numeric entry. Click the value text below a knob to activate a inline editor that looks identical to the painted value label. Type a number and press Enter or click elsewhere to commit the value. The value is clamped to the knob's valid range. Press Escape to cancel the edit and revert to the previous value.

The inline editor is available on all knob controls in both the TX and RX applet tiles.

## Visual indicators

| Indicator | States | Meaning |
|---|---|---|
| Input ball | Below threshold / above threshold | Shows whether the gate is currently open or closed. |
| Hysteresis band | Absent (Return = 0) / soft-cyan vertical band | Visualises the Return deadband on the transfer-curve input axis — the gate's sticky zone between (Thresh − Return) and Thresh. |
| Gain-reduction strip | Empty / amber fill / −15 dB tick | Depth of attenuation while the gate is closed. Scale maxes at 40 dB; a tick at −15 dB marks the soft-expander default floor. |
| Applet tile opacity | Full opacity (enabled) / ~55 % opacity (bypassed) | Indicates at a glance whether the gate stage is currently processing audio. |

## Theme-aware knob colours

Knob components now read from the theme colour system rather than using hard-coded colours. The following colour roles control knob appearance:

- **`color.knob.background`** — Background ring colour.
- **`color.knob.foreground`** — Value arc colour.
- **`color.knob.handle`** — Pointer/indicator colour.
- **`color.text.secondary`** — Knob label text colour.
- **`color.text.primary`** — Knob value text colour.

The gate applet container is registered under the `applet/gate` theme path, allowing per-applet theme overrides. This enables the amber knob foreground colour used in the gate's transfer curve and gain-reduction bar to be styled independently from knobs in other applets.

## Animation optimisations (v26.6.3)

The meter-smoothing timer now stops when the gain-reduction value has settled, and only triggers a repaint when necessary. This reduces CPU usage when the gate is not actively attenuating audio. The live input ball and gain-reduction bar continue to update normally during active gating.

## Tips

- Watch the gain-reduction bar while not speaking (TX) or during a band-noise-only moment (RX). If the bar is not filling, Thresh is set below the noise floor and the gate is not triggering. See [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md).
- The −15 dB tick on the gain-reduction bar marks the Floor default. If the bar fills fully past that tick, Floor is set deeper than −15 dB or Ratio is high enough to push reduction beyond it.
- Use the cyan hysteresis band on the transfer curve to judge whether the Return value is wide enough to prevent chatter without making the gate sluggish to close.
- When the tile appears dimmed, the gate stage is bypassed. Re-enable it via the CHAIN widget or the floating editor before expecting any attenuation.
- Changes to any knob take effect immediately and are saved automatically. No Apply button is needed.
- To enter a precise numeric value, click the value text below any knob and type the number directly.

## Troubleshooting

- **Applet is not visible** — The Gate stage has not been enabled on that side. Enable it via the CHAIN widget or the floating editor for the TX or RX side.
- **Applet tile appears dimmed** — The gate stage is bypassed. The tile renders at reduced opacity when bypass is active. Enable the stage via the CHAIN widget or the floating editor to restore full processing and full tile brightness.
- **Gate is not attenuating noise between words** — Thresh may be set too low, below the room noise floor. Raise Thresh until the gain-reduction bar shows movement during silence. See [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md).
- **Gate chatters rapidly near the threshold** — Return is set too low. Increase Return so the gate does not reopen until the signal is clearly above Thresh, widening the deadband shown by the cyan band on the transfer curve.
- **Unnatural silence between words** — Floor is set too deep. Raise Floor toward 0 dB so some residual audio passes through during closed periods. See [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md).
- **Knob positions in the tile do not match the floating editor** — The tile syncs every ~33 ms. If they appear mismatched immediately after opening the editor, wait one update cycle or move a knob to force a sync.
- **Axis label clipping or jitter on the transfer curve** — This issue has been resolved in v26.5.1. The curve now uses cached static text for axis labels, improving rendering performance and preventing label movement during compact mode transitions.

## Related

- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Use AGC-G on RX to suppress band noise below a chosen floor](use-agc-g-on-rx-to-suppress-band-noise-below-a-chosen-floor.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)