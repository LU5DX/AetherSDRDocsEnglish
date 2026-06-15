# Choose gate vs soft-expander behaviour via ratio

The Ratio knob controls how aggressively the gate attenuates audio below the threshold. Setting a low ratio produces a soft downward expander that gently reduces quiet audio; setting a high ratio produces a hard gate that cuts it sharply. Choosing the right ratio lets you match the gate's character to your noise situation and operating style.

## Before you start

- The gate stage must be enabled on the side you want to adjust (TX or RX). If the applet is not visible, enable the gate via the CHAIN widget or double-click the GATE stage to open the floating editor.
- Open the **Aetherial TX Gate** sub-container (TX) or the **Aetherial AGC-G** sub-container (RX) inside the Aetherial Audio (TXDSP) parent container in the Applet Panel.
- When a gate stage is bypassed, the entire applet tile dims to approximately 55 % opacity. This visual cue matches the dim effect used on the EQ curve and confirms that the stage is not processing audio. Re-enable the stage to restore full opacity and active processing.

## Steps

1. Locate the **Ratio** knob in the five-knob row at the bottom of the applet.
2. To set soft-expander behaviour, turn **Ratio** toward a low value (for example, 2.0:1). Audio below the threshold is reduced gradually.
3. To set hard-gate behaviour, turn **Ratio** toward a high value (for example, 8.0:1 or higher). Audio below the threshold is cut sharply.
4. Watch the gain-reduction bar while audio passes through. A soft-expander setting produces a shallower, more gradual amber fill; a hard-gate setting produces a deep, abrupt fill when the gate closes.
5. If the hard-gate cut is too severe between words, adjust **Floor** to limit the maximum attenuation. See [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md).

## What each control does

| Control                | Default   | Valid range     |
|------------------------|-----------|-----------------|
| **Thresh**             | -40.0 dB  | -80.0 to 0.0 dB |
| **Ratio**              | 2.0       | 1.0 to 10.0     |
| **Return**             | 2.0 dB    | 0.0 to 20.0 dB  |
| **Release**            | 100 ms    | 5 to 2000 ms    |
| **Floor**              | -15.0 dB  | -80.0 to 0.0 dB |
| **Gain-reduction bar** | —         | 0 to 40 dB GR   |
| Transfer curve         | —         | —               |

## Knob inline editing

Each knob in the applet supports inline value editing. Click on a knob's displayed value to open an editable text field overlaid on the knob. Type a new value and press Enter or click elsewhere to commit the change. The editor accepts locale-aware decimal formats (for example, "12,5" in comma-decimal locales) and strips non-numeric characters, so you can enter values with units (for example, "−6 dB" or "12.5 ms"). If you enter an invalid value, the knob silently reverts to its previous setting. Press Escape to cancel editing without committing a change.

## Tips

- A ratio of 2.0:1 (the default) is a conservative starting point suitable for most TX use. Raise it only if low-level noise is still audible when you are not speaking.
- At ratios above approximately 8.0:1 the gate behaves almost like an on/off switch. Pair this with a carefully set **Thresh** to avoid clipping the leading edge of words.
- Use the **Return** knob to eliminate gate chatter. If the gate flickers open and closed rapidly when you pause speaking, increase **Return** so the gate stays open until the input level drops well clear of the threshold. The cyan band on the transfer curve widens as you increase **Return**, showing the sticky zone directly.
- The transfer curve updates in real time as you move **Ratio** or **Return**. Use the live input ball to confirm the curve shape and hysteresis band match your intent before transmitting.
- Changes to any knob take effect immediately and are saved automatically. No Apply or Save button is required.
- The gain-reduction bar and transfer curve repaint at a smooth, consistent rate thanks to an animation timer. When the audio level is changing, the display updates continuously. When the level settles, the timer stops to save resources but still performs a final redraw to show the settled state. This ensures you always see the current meter reading without unnecessary CPU usage.

## Troubleshooting

- **Ratio knob has no effect on the sound** — Confirm the gate stage is enabled. A bypassed gate passes audio unmodified regardless of knob settings; the applet tile will appear dimmed to approximately 55 % opacity when bypassed. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).
- **Hard-gate ratio cuts too deep and creates unnatural silences** — Lower **Floor** toward 0 dB to reduce the maximum attenuation, or reduce **Ratio** toward the soft-expander range.
- **Soft-expander ratio does not suppress noise enough** — Raise **Ratio** or lower **Thresh** so attenuation begins at a higher input level.
- **Gate chatters or flickers at the threshold** — Increase **Return** so the gate stays open until the signal drops further below the threshold. Watch the cyan hysteresis band on the transfer curve widen as you do so.
- **Display meter or curve appears to stutter** — The animation system uses a precise internal timer that automatically stops when the audio level settles. A brief pause before the final redraw is normal and indicates the timer has stopped correctly. If you see continuous flickering, check that no other application is interfering with the audio pipeline.

## Related

- [Aetherial TX Gate / Aetherial AGC-G (RX) overview](overview.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Tune release for natural gate close](tune-release-for-natural-gate-close.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)