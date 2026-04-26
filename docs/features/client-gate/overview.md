# Noise Gate / Expander overview

The Noise Gate / Expander is a TX-side downward expander that attenuates audio falling below a set level. Use it to suppress background noise, fan hum, and room ambience between words without manually operating a hardware gate.

## Before you start

- The GATE applet is hidden until the Gate stage is enabled via the CHAIN widget or the floating Gate editor. Enable the stage there first.
- The applet lives inside the PooDoo Audio (TXDSP) parent container. Make sure the applet panel is visible (`View > Applet Panel`).

## How it works

When your microphone audio drops below the **Thresh** level, the gate begins attenuating the signal. The depth and speed of that attenuation are controlled by **Ratio**, **Attack**, **Release**, and **Floor**.

At a **Ratio** of 2.0:1 (the default) the gate acts as a soft downward expander — audio below the threshold is turned down gradually. At higher ratios (approaching 10.0:1) the cut becomes sharper and the behaviour is closer to a hard gate. The **Floor** knob caps the maximum attenuation so the gate never creates an unnaturally complete silence.

The applet shows two live indicators while you transmit or monitor:

- **Transfer curve** — a static curve plot with a live ball that moves to the current input level, showing whether the gate is open (ball above threshold) or closed (ball below threshold).
- **Gain-reduction bar** — a horizontal amber strip that fills from the right. The scale runs 0 to 40 dB of gain reduction. A tick mark at −15 dB indicates the default **Floor** value.

All five knobs in the applet are wired directly to the audio engine. Changes made here are immediately reflected in the floating Gate editor, and vice versa. Settings are persisted automatically after each adjustment.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| Thresh | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` |
| Ratio | 2.0:1 | 1.0 to 10.0 | `ClientGateTxRatio` |
| Attack | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` |
| Release | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` |
| Floor | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` |

**Thresh** — the level below which the gate starts attenuating. Set this just above your room noise floor so speech opens the gate cleanly.

**Ratio** — controls how hard the cut is. Lower values (near 1.0:1) produce a gentle downward expansion. Higher values (near 10.0:1) produce an abrupt gate-like cutoff.

**Attack** — how quickly the gate opens when input rises above the threshold. Uses an exponential scale (0.1 ms to 100.0 ms). Faster attack values let the leading edge of each word through immediately.

**Release** — how quickly the gate closes after input falls below the threshold. Uses an exponential scale (5 ms to 2000 ms). Longer release values give a more natural tail-off; very short values can produce a choppy sound.

**Floor** — the maximum gain reduction the gate is permitted to apply. At the default of −15.0 dB, background noise is reduced by up to 15 dB rather than silenced entirely. Set lower for a harder cut, higher to be more conservative.

Whether the gate stage is active or bypassed is persisted in `ClientGateTxEnabled`.

## Tips

- Watch the transfer curve ball and the gain-reduction bar while not speaking. If the bar shows significant amber fill at rest, the gate is working. If the ball rarely crosses threshold during speech, **Thresh** may be set too high.
- The floating Gate editor and the GATE applet knobs stay in sync. You do not need to open the editor for routine threshold or floor adjustments.
- Right-click the GATE sub-container titlebar to float, pop-out, or hide the applet if you need more screen space.

## Related

- [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
