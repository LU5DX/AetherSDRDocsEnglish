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

## Inline value editing

Each knob in the Aetherial De-Esser applet supports direct numeric entry. Click the knob's value label to open a small text editor overlay. Type a value and press Enter or click elsewhere to commit. The value is clamped to the knob's valid range automatically.

- The editor accepts locale-aware number formats (e.g., "12,5" in comma-decimal locales).
- If you type additional text (e.g., "12.5 ms" or "−6 dB"), the editor strips non-numeric characters and parses the number.
- Press Escape to cancel editing and revert to the previous value.
- Mouse wheel scrolling still works while the editor is focused, forwarded to the knob for adjustment.
- When not focused, the editor appears identical to a painted value label — a subtle dark inset and cyan border appear on focus to indicate edit mode.

## What each control does

| Control                  | Default                                                                                                                                                                                              | Valid range                                                                                                                                                                                |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sidechain response curve | —                                                                                                                                                                                                    | —                                                                                                                                                                                          |
| Gain-reduction bar       | —                                                                                                                                                                                                    | 0 to 24 dB GR                                                                                                                                                                              |
| Freq                     | 6000 Hz                                                                                                                                                                                              | 1000 to 12000 Hz                                                                                                                                                                           |
| Q                        | 2.00                                                                                                                                                                                                 | 0.5 to 5.0                                                                                                                                                                                 |
| Thresh                   | −30.0 dB                                                                                                                                                                                             | −60.0 to 0.0 dB                                                                                                                                                                            |
| Amount                   | −6.0 dB                                                                                                                                                                                              | −24.0 to 0.0 dB                                                                                                                                                                            |
| Attack (channel strip only)   | 1.0 ms                                                                                                                                                                                               | 0.1 to 30.0 ms                                                                                                                                                                             |
| Release (channel strip only)  | 100 ms                                                                                                                                                                                               | 10.0 to 500.0 ms                                                                                                                                                                           |
| Slope                    | 24 dB/oct (2 stages)                                                                                                                                                                                 | 12 / 24 / 36 / 48 dB/oct (1 to 4 stages)                                                                                                                                                  |

## Sidechain response curve

The Sidechain response curve indicator shows the bandpass filter response with a live ball at the current centre frequency. In compact mode, the curve widget displays the response without frequency axis labels. The axis labels use `QStaticText` for efficient rendering and display frequencies as "100", "500", "1k", "2k", "3k", "4k", "5k", "6k", "8k", "10k", "12k" when not in compact mode.

## Slope control

A Slope button appears at the bottom of the left knob column in the Aetherial Audio Channel Strip (both TX and RX panels). It cycles through 12 → 24 → 36 → 48 dB/oct (1 to 4 cascaded bandpass biquads) each time you click it.

- Higher slope = narrower notch around the sibilant frequency = less mid-band collateral on Ess-heavy phrases.
- The button displays the current value as "N dB/oct" (e.g., "24 dB/oct").
- The setting is persisted separately for TX and RX as `ClientDeEssTxSlopeStages` and `ClientDeEssRxSlopeStages`.

To adjust the slope:

1. Click the Slope button repeatedly to cycle through the available values.
2. Observe the sidechain response curve update in real time to see the narrowed notch.
3. Stop when the de-esser targets only the sibilance without affecting nearby speech energy.

**Note:** The docked Aetherial De-Esser applet omits the Attack, Release, and Slope controls. These are only available in the Aetherial Audio Channel Strip panel.

## RX and TX instances

The Aetherial De-Esser has separate instances for transmit and receive:

- **TX instance** — Labeled "Aetherial De-Esser" in the docked Applet Panel. Opens from the TX chain in the Aetherial Audio Channel Strip.
- **RX instance** — Labeled "Aetherial De-Esser — RX" in its title bar. Reachable through the RX side of the Aetherial Audio Channel Strip. Uses its own dedicated window titled "Aetherial De-Esser — RX".

Each instance has independent settings, persisted separately. RX settings save under `ClientDeEssRxFrequencyHz`, `ClientDeEssRxQ`, etc. The Slope button in the RX panel uses `ClientDeEssRxSlopeStages`.

## Bypass dimming

When the DESS stage is bypassed via a single click in the CHAIN widget, the entire applet renders at reduced opacity (55 %). This matches the dim effect used on the EQ curve and gives a clear visual indication that the stage is inactive. Click the CHAIN widget again to re-enable the stage and restore full opacity.

## Tips

- −6 dB (the default) is a reasonable starting point for most voices. The tick on the Gain-reduction bar marks this level, making it easy to use as a reference during adjustment.
- Aim for the Gain-reduction bar to move noticeably on "S" and "T" sounds but never pin against the 24 dB end. Heavy gain reduction at that extreme is audible as a lisp or dropout.
- Narrowing the sidechain band with Q before finalizing Amount reduces collateral attenuation on nearby speech energy, which helps transparency. See [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md).
- Amount values are always negative or zero — they represent reduction, not boost.
- Use inline value editing for precise numeric entry instead of fine-tuning by knob rotation.
- Adjust Slope to tighten the sidechain notch — this preserves mid-band speech while aggressively cutting sibilants.

## Troubleshooting

- **Audio sounds hollow or lisping on every "S"** — Amount is set too low (too much attenuation). Raise it toward 0 dB in 2 dB steps while speaking until naturalness returns.
- **Gain-reduction bar never moves** — The de-esser is not triggering. Check that Thresh is set below your actual sibilance level and that the DESS stage is enabled. See [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md).
- **Gain-reduction bar pins at 24 dB constantly** — Thresh is set too low, causing the de-esser to trigger on all speech, not just sibilance. Raise Thresh first, then re-evaluate Amount.
- **Applet appears faded or dim** — The DESS stage is bypassed. Click the stage in the CHAIN widget once to re-enable it.
- **Inline editor doesn't accept typed value** — Ensure the value is within the knob's valid range. Off-range values are clamped automatically. If the value reverts, check for extra spaces or characters that weren't stripped.
- **Mid-band speech sounds dull or attenuated** — Slope may be set too low. Increase Slope to 36 or 48 dB/oct to narrow the sidechain notch and preserve mid-band energy.

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)
- [Aetherial De-Esser overview](overview.md)