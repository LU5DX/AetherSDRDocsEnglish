# Dial Amount for the most transparent de-essing

The Amount knob sets the maximum attenuation the de-esser applies when sibilance peaks above the threshold. Dialing the right value lets you tame harshness without making your audio sound processed or pumped.

## Before you start

- The Aetherial De-Esser (DESS) stage must be enabled in the CHAIN widget. The applet is hidden until the stage is active.
- Open the Aetherial De-Esser applet via the Aetherial Audio Channel Strip. The floating editor (previously accessible by double-clicking the DESS stage) no longer exists; all controls are available directly in the applet.
- Set Freq and Thresh first so the de-esser is already triggering on the right band. See [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md) and [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md).

## Steps

1. Have someone transmit into the microphone — or read a sibilant phrase aloud — so the de-esser is actively triggering.
2. Watch the Gain-reduction bar. It fills right-to-left in soft red to show how much attenuation is being applied. A tick marks the −6 dB point.
3. Turn the Amount knob counterclockwise to increase attenuation (more negative values) until the harshness is gone.
4. Back off clockwise until the Gain-reduction bar only reaches the −6 dB tick on the loudest "S" peaks. Stopping here keeps processing transparent.
5. If the Gain-reduction bar is pegged near 24 dB or the audio sounds hollow, raise Amount toward 0 dB in small steps until naturalness returns.
6. Changes are saved automatically. The setting persists as `ClientDeEssTxAmountDb`.

## What each control does

| Control            | Default     | Valid range     | Behavior                                                                                               |
|--------------------|-------------|-----------------|--------------------------------------------------------------------------------------------------------|
| Amount             | −6.0 dB     | −24.0 to 0.0 dB | Linear mapping. Maximum attenuation applied at peak sibilance. Values are negative (or zero) because they represent reduction. |
| Gain-reduction bar | —           | 0 to 24 dB GR   | Horizontal soft-red strip, right-filled. Scale maxes at 24 dB; a tick marks the −6 dB typical amount. Refreshed ~30 Hz. |
| Attack             | 1.0 ms      | 0.1 to 30.0 ms  | Exponential mapping (0.1 × 300^n). Sets how quickly the de-esser responds once sibilance crosses the threshold. Present in the Channel Strip StripDeEssPanel (RX and TX). The docked ClientDeEssApplet omits this knob. |
| Release            | 100 ms      | 10.0 to 500.0 ms| Exponential mapping (10 × 50^n). Sets how quickly gain returns after sibilance drops below the threshold. Present in the Channel Strip StripDeEssPanel (RX and TX). The docked ClientDeEssApplet omits this knob. |

## Sidechain response curve

The Sidechain response curve indicator shows the bandpass filter response with a live ball at the current centre frequency. In compact mode, the curve widget displays the response without frequency axis labels. The axis labels use `QStaticText` for efficient rendering and display frequencies as "100", "500", "1k", "2k", "3k", "4k", "5k", "6k", "8k", "10k", "12k" when not in compact mode.

## RX and TX instances

The Aetherial De-Esser has separate instances for transmit and receive:

- **TX instance** — Labeled "Aetherial De-Esser" in the docked Applet Panel. Opens from the TX chain in the Aetherial Audio Channel Strip.
- **RX instance** — Labeled "Aetherial De-Esser — RX" in its title bar. Reachable through the RX side of the Aetherial Audio Channel Strip. Uses its own dedicated window titled "Aetherial De-Esser — RX".

Each instance has independent settings, persisted separately. RX settings save under `ClientDeEssRxFrequencyHz`, `ClientDeEssRxQ`, etc.

## Bypass dimming

When the DESS stage is bypassed via a single click in the CHAIN widget, the entire applet renders at reduced opacity (55 %). This matches the dim effect used on the EQ curve and gives a clear visual indication that the stage is inactive. Click the CHAIN widget again to re-enable the stage and restore full opacity.

## Tips

- −6 dB (the default) is a reasonable starting point for most voices. The tick on the Gain-reduction bar marks this level, making it easy to use as a reference during adjustment.
- Aim for the Gain-reduction bar to move noticeably on "S" and "T" sounds but never pin against the 24 dB end. Heavy gain reduction at that extreme is audible as a lisp or dropout.
- Narrowing the sidechain band with Q before finalizing Amount reduces collateral attenuation on nearby speech energy, which helps transparency. See [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md).
- Amount values are always negative or zero — they represent reduction, not boost.

## Troubleshooting

- **Audio sounds hollow or lisping on every "S"** — Amount is set too low (too much attenuation). Raise it toward 0 dB in 2 dB steps while speaking until naturalness returns.
- **Gain-reduction bar never moves** — The de-esser is not triggering. Check that Thresh is set below your actual sibilance level and that the DESS stage is enabled. See [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md).
- **Gain-reduction bar pins at 24 dB constantly** — Thresh is set too low, causing the de-esser to trigger on all speech, not just sibilance. Raise Thresh first, then re-evaluate Amount.
- **Applet appears faded or dim** — The DESS stage is bypassed. Click the stage in the CHAIN widget once to re-enable it.

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)
- [Aetherial De-Esser overview](overview.md)