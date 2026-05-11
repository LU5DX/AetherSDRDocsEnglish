# Use AGC-G on RX to suppress band noise below a chosen floor

The RX-side Aetherial AGC-G (client-side downward expander) attenuates received audio that falls below a threshold you set, letting you silence background band noise or static between signals while keeping wanted audio untouched.

## Before you start

- You must be connected to a FLEX-8600 radio.
- The Aetherial Audio (TXDSP) parent container must be visible in the Applet Panel.
- The RX side Gate stage must be enabled via the CHAIN widget (double-click the GATE stage on the RX side to open its editor, or single-click to toggle bypass).

## Steps

1. In the Applet Panel, locate the **Aetherial AGC-G (RX)** sub-container inside the Aetherial Audio (TXDSP) parent container. If it is hidden, double-click the GATE stage in the CHAIN widget on the RX side to open the floating editor (titled "Aetherial Gate — RX").

2. Adjust **Thresh** (default: -40.0 dB) downward until the band noise you want to suppress sits below the threshold. Watch the live input ball on the transfer-curve display — when the ball is below the threshold line, the gate is closed and attenuation is applied.

3. Set **Floor** (default: -15.0 dB) to the maximum attenuation you want applied to background noise. A typical setting is -15 to -20 dB — enough to silence noise without making gaps between words sound unnaturally silent.

4. Adjust **Ratio** (default: 2.0) to control how aggressively the gate cuts:
   - Lower ratios (1.0–3.0) act as a soft downward expander — background noise fades smoothly.
   - Higher ratios (5.0–10.0) create a harder, more traditional gate feel.

5. Set **Return** (default: 2.0 dB) to prevent rapid opening and closing near the threshold. A cyan hysteresis band appears on the transfer curve between (Thresh − Return) and Thresh — the gate stays open inside this zone until the input drops below it, then must rise above Thresh to reopen.

6. Adjust **Release** (default: 100 ms) to control how quickly the gate closes after the input falls below Thresh − Return. Longer values (500–2000 ms) give a more natural fade; shorter values (5–50 ms) can sound abrupt.

## What each control does

| Control | Default | Range | Setting key | Behavior |
|---------|---------|-------|-------------|----------|
| Thresh | -40.0 dB | -80.0 to 0.0 dB | `ClientGateRxThresholdDb` | Level below which the gate starts attenuating. Linear mapping. |
| Ratio | 2.0 | 1.0 to 10.0 | `ClientGateRxRatio` | Higher ratios give a harder, more gate-like cut; lower ratios act as a soft downward expander. Displayed as "X.X:1". |
| Return | 2.0 dB | 0.0 to 20.0 dB | `ClientGateRxReturnDb` | Hysteresis deadband: gate opens above Thresh and stays open until input drops below Thresh − Return. Displayed as "X.XX dB". The transfer-curve widget draws a soft-cyan vertical band between (Thresh − Return) and Thresh to make the sticky zone visible. |
| Release | 100 ms | 5 to 2000 ms | `ClientGateRxReleaseMs` | How quickly the gate closes after input falls below Thresh − Return. Exponential mapping. Displayed as "X.X ms" below 100 ms, "X ms" above. |
| Floor | -15.0 dB | -80.0 to 0.0 dB | `ClientGateRxFloorDb` | Maximum attenuation the gate is allowed to apply. Linear mapping. |
| Gain-reduction bar | — | 0 to 40 dB GR | — | Amber horizontal strip, right-filled. Scale maxes at 40 dB; a tick at -15 dB marks the default Floor. |
| Transfer curve | — | — | — | Plots the expander's static transfer curve and a live ball at the current input level. In compact mode (when the floating editor is used), axis labels are cached as static text and rendered at 7-pixel font size for improved performance. |

## Tips

- Start with Thresh just above the highest level of background noise you want to suppress. Adjust while listening to a weak signal — the gate should open cleanly when the signal rises above the noise.
- The Gain-reduction bar shows live attenuation depth. When no signal is present, it should show steady GR equal to your Floor setting. If it never reaches Floor, Thresh may be set too low or the band noise is too loud.
- Tuning knobs here and in the floating editor stay in sync — changes in either place update the other live.
- The transfer-curve display caches axis labels for efficient rendering. When switching between compact mode (floating editor) and full-size mode, labels automatically refresh at the appropriate font size.

## Related

- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Set Return to prevent gate chatter near threshold](set-return-to-prevent-gate-chatter-near-threshold.md)
- [Tune release for natural gate close](tune-release-for-natural-gate-close.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)