# Noise Gate / Expander overview

The Noise Gate / Expander is a TX-side downward expander that attenuates audio falling below a set level. Use it to silence background noise and room ambience between words without manually keying the mic.

## Before you start

- The GATE applet is hidden until the Gate stage is enabled. Enable it through the CHAIN widget or the floating Gate editor.
- The applet lives inside the PooDoo Audio (TXDSP) parent container as the "GATE" sub-container.

## How it works

When your microphone signal drops below the threshold you set, the gate attenuates the audio by an amount determined by the ratio and floor settings. When your signal rises back above the threshold, the gate opens again at the speed set by attack. When it falls back below, it closes at the speed set by release.

At low ratios (close to 1.0:1) the gate acts as a soft downward expander — audio below the threshold is turned down gradually. At high ratios (approaching 10.0:1) the gate acts more like a hard cut, abruptly silencing anything below the threshold. The floor sets a ceiling on how deeply the gate is allowed to cut, preventing unnatural complete silence between words.

The applet gives you two live indicators while you talk:

- **Transfer curve** — a plot of the expander's static input-to-output curve, with a live ball showing the current input level and whether the gate is open or closed.
- **Gain-reduction bar** — an amber horizontal strip, right-filled, showing how many dB of attenuation the gate is currently applying. The scale runs 0 to 40 dB. A tick mark at 15 dB indicates the default Floor value.

Knob changes made in the applet and in the floating Gate editor stay in sync — turning a knob in either place updates the other.

## What each control does

| Control | Default | Valid range | Persisted setting | Description |
|---|---|---|---|---|
| Thresh | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` | Level below which the gate begins attenuating. Set just above your room noise floor. |
| Ratio | 2.0:1 | 1.0 to 10.0 | `ClientGateTxRatio` | Higher values produce a harder gate-like cut; lower values produce a gentler downward expansion. |
| Attack | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` | How quickly the gate opens when input rises above threshold. Shorter times sound more immediate; longer times ease in. |
| Release | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` | How quickly the gate closes after input falls below threshold. Longer times avoid choppy tails between syllables. |
| Floor | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` | Maximum attenuation the gate can apply. Limits how quiet the audio gets when the gate is closed. |

Enabled state is persisted as `ClientGateTxEnabled`.

## Tips

- Watch the gain-reduction bar while you are not speaking. If it reads near 0 dB, lower the threshold — the gate is not closing.
- If the gate cuts into the start of words, increase Attack slightly.
- If the gate chops off the end of words, increase Release.
- Set Floor to a moderate value such as −15.0 dB rather than −80.0 dB to preserve a small amount of room tone and avoid robotic silences.
- To open the floating Gate editor, double-click the Gate stage in the CHAIN widget. Right-click the "GATE" sub-container titlebar to float, pop out, or hide the applet.

## Related

- [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
