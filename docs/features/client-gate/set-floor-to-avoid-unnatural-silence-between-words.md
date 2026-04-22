# Set Floor to avoid unnatural silence between words

The Floor knob limits how deeply the gate can attenuate your audio. Without a floor limit, the gate can cut signal to near silence between words, which sounds unnatural. Setting Floor to a moderate value — such as the default −15.0 dB — leaves a small residual level during quiet gaps so the cut is less jarring.

## Before you start

- The GATE applet must be visible in the applet panel. It is hidden until the Gate stage is enabled via the CHAIN widget or the floating Gate editor. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) for how to enable it.
- A radio connection is not required to adjust Floor; changes take effect immediately and persist across restarts.

## Steps

1. Locate the GATE sub-container in the applet panel.
2. Find the rightmost knob in the five-knob row, labelled **Floor**.
3. Turn the **Floor** knob clockwise to raise the floor (less maximum attenuation) or counter-clockwise to lower it (more maximum attenuation).
4. Speak normally and watch the gain-reduction bar. The amber fill should not reach beyond the −15 dB tick during normal pauses between words. If it does, raise Floor toward 0.0 dB until the fill stays within a comfortable range.
5. Transmit a short test recording and listen back. If gaps between words sound abruptly silent, raise Floor. If background noise bleeds through noticeably during pauses, lower Floor.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| Floor | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` |
| Gain-reduction bar | — | 0 to 40 dB GR | — |

**Floor** sets the maximum attenuation the gate is allowed to apply. A value of −15.0 dB means the gate can reduce the signal by at most 15 dB, leaving audio at −15 dB relative to its open level rather than cutting to full silence. A value of −80.0 dB gives the gate effectively unlimited cut depth.

The **Gain-reduction bar** is a horizontal amber strip, right-filled, running from 0 to 40 dB. The tick mark at −15 dB corresponds to the default Floor value and serves as a visual reference for how deep the gate is cutting.

## Tips

- The −15 dB tick on the gain-reduction bar is a built-in reference for the default Floor. If the amber fill consistently exceeds that tick during normal speech pauses, your Floor is set lower than the default and may produce a noticeably abrupt cut.
- Floor interacts with Ratio. A high Ratio (hard gate) combined with a very low Floor (e.g. −80.0 dB) produces an aggressive on/off effect. If you want a softer sound, raise Floor toward −10.0 dB or lower Ratio rather than adjusting both independently.
- The Floor knob in the GATE applet tile and the same knob in the floating Gate editor are synchronized in real time. Adjusting one immediately updates the other.

## Related

- [Noise Gate / Expander overview](overview.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
