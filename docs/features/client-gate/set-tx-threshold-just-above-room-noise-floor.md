# Set TX threshold just above room noise floor

Setting Thresh correctly tells the TX gate where your room's background noise ends and your voice begins. A threshold just above the noise floor keeps mic hiss and ambient sound silent between transmissions while letting your voice through cleanly.

## Before you start

- The TX gate stage must be enabled in the CHAIN widget on the TX side. If it is not enabled, the applet is hidden and knob changes have no effect. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).
- Open the "Aetherial TX Gate" sub-container inside the Aetherial Audio (TXDSP) parent container, or double-click the GATE stage in the CHAIN widget to open the floating "Aetherial Gate — TX" editor.
- When the gate stage is bypassed, the entire applet tile renders at reduced opacity (approximately 55% of full brightness). This is a visual indicator only — knob positions are preserved and take effect as soon as the stage is re-enabled.

## Steps

1. Put on your headphones and set the room to its normal ambient conditions — fan running, computer noise present, whatever is typical when you operate.
2. Do not speak. Watch the live input ball on the Transfer curve. The ball shows where your room noise sits on the input axis.
3. Watch the Gain-reduction bar. If the bar shows no amber fill while you are silent, Thresh is already below your noise floor and the gate is not closing — raise Thresh.
4. Turn the Thresh knob slowly clockwise until the amber Gain-reduction bar begins to fill consistently while you are silent. This is the noise floor.
5. Back Thresh off by 2–3 dB so the gate closes firmly on noise without clipping the leading edge of your voice. The input ball should sit clearly below the threshold line when you are silent.
6. Speak at normal volume. Confirm the Gain-reduction bar drops to zero (no fill) immediately when you start talking, indicating the gate has opened.
7. Return to silence. Confirm the amber fill returns promptly. If the gate is slow to close, reduce Release. See [Tune release for natural close](tune-attack-release-for-natural-open-close.md).

## What each control does

| Control                | Default   | Valid range       | Behavior                                                                                                                                                                                                                                                              |
|------------------------|-----------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Thresh                 | −40.0 dB  | −80.0 to 0.0 dB   | Linear mapping. Level below which the gate starts attenuating.                                                                                                                                                                                                        |
| Ratio                  | 2.0       | 1.0 to 10.0       | Linear mapping. Higher ratios give a harder, more gate-like cut; lower ratios act as a soft downward expander. Label 'X.X:1'.                                                                                                                                         |
| Return                 | 2.0 dB    | 0.0 to 20.0 dB    | Linear mapping (n * 20). Sets the hysteresis deadband: the gate opens above Thresh and doesn't close again until the input drops below Thresh − Return, preventing rapid chatter near the threshold. Label 'X.XX dB'. The curve widget draws a soft-cyan vertical band between (Thresh − Return) and Thresh to make the sticky zone visible. |
| Release                | 100 ms    | 5 to 2000 ms      | Exponential mapping (5 * 400^n). Sets how quickly the gate closes after input falls below Thresh − Return. Label 'X.X ms' below 100, 'X ms' above.                                                                                                                    |
| Floor                  | −15.0 dB  | −80.0 to 0.0 dB   | Linear mapping. Maximum attenuation the gate is allowed to apply.                                                                                                                                                                                                     |
| Flip (Expander / Gate) | Unchecked | Editor-only       | Unchecked = downward-expander (gentle, ratio-based). Checked = Gate (hard cut). Snaps ratio and floor to preset pairs when toggled; other knobs stay put. Label updates live between 'Expander' and 'Gate'. Colour: unchecked = green (Expander), checked = amber (Gate). Tooltip: 'Flip between downward Expander (gentle) and Gate (hard) modes. Snaps ratio + floor to preset pairs; other knobs stay where you left them.' |
| Peek (lookahead)       | Off       | Editor-only       | Sets a pre-read delay so the gate can open fractionally before a transient arrives, avoiding clipped attack edges. 'Off' disables the delay line entirely. Higher values increase latency on the TX path. 1 and 1.5 ms match Ableton's preset options; 3 and 5 ms added for very fast transients. |
| Attack                 | 0.3 ms    | Editor-only       | Exponential mapping (0.1 * 1000^n). Sets how quickly the gate opens after input rises above Thresh. Label 'X.XX ms' below 10 ms, 'X.X ms' above.                                                                                                                     |
| Hold                   | 0 ms      | Editor-only       | Linear mapping (n * 500). After the input drops below Thresh − Return the gate stays open for this long before it begins closing, preventing flutter on rhythmic material. Label 'X.X ms'.                                                                           |

The Transfer curve plots the static input/output relationship and shows a live input ball at the current signal level. When Return is greater than zero, a soft-cyan vertical band appears on the curve between (Thresh − Return) and Thresh, marking the range where the gate's open/closed state is sticky. The Gain-reduction bar is an amber horizontal strip, right-filled, scaled 0 to 40 dB; a tick marks the −15 dB default Floor position. In v26.5.1, axis labels are rendered using cached static text for improved performance, reducing CPU overhead during live animation. This change is transparent to users — the visual appearance remains identical.

### Inline value editor (v26.5.2.1)

In v26.5.2.1, all knob controls in the applet gained an inline value editor. Click the value text below any knob to open a small text-entry field that overlays the displayed value. Enter a numeric value (with or without unit text) and press Enter to commit; the knob snaps to the typed value, clamped to its valid range. Clicking elsewhere on the interface also commits the edit. Press Escape to cancel and revert to the previous value. The editor recognises commas as decimal separators in locales that use them. This allows precise entry without dragging a knob.

### Theming (v26.6.1)

In v26.6.1, the applet and all its child controls — the Transfer curve widget and every knob — became fully themeable. Knob colours (ring background, ring foreground/arc, handle/pointer, label text, and value text) now read from theme keys in the `color.knob.*` namespace. The Transfer curve widget reads its background, grid, axis labels, identity line, curve, and ball colours from `color.background.*`, `color.text.*`, and `color.accent.*` theme keys. The curve colour is read from `color.accent.warning`, which renders as amber by default. When a custom theme is applied, all gate-related colours update immediately without requiring a restart. The visual default appearance is unchanged.

### Animation performance (v26.7.4)

In v26.7.4, the Transfer curve widget and Gain-reduction bar now repaint on every animation tick rather than only when the smoothed value changes or settles. This ensures smoother visual tracking of the live input ball and gain-reduction meter during rapid signal changes, at the cost of slightly higher CPU usage. The visual appearance and responsiveness are improved for fast transients.

## Tips

- Set Thresh during your worst-case noise condition (loudest fan, most background activity). A threshold calibrated to a quiet room will let noise through when conditions change.
- If the gate chops the start of words, lower Thresh by 1–2 dB so the gate triggers earlier.
- Increase Return if the gate chatters or flutters when your voice level hovers near the threshold. The wider the deadband, the more stable the open/close behaviour.
- The Gain-reduction bar and the input ball update live at approximately 30 Hz, so short noise bursts will be visible even if brief.
- Changes to any knob are saved immediately and survive a restart. You do not need to confirm or apply separately.
- To enter a precise knob value, click the value text below the knob and type the number, then press Enter. The knob moves to the entered value instantly.

## Troubleshooting

- **The applet is not visible** — The GATE stage is not enabled. Single-click the GATE stage in the CHAIN widget to enable it, or double-click to open the floating editor and enable it there.
- **The applet tile appears dimmed** — The gate stage is bypassed. The tile renders at reduced opacity when the stage is disabled. Re-enable the GATE stage in the CHAIN widget to restore full brightness and resume processing.
- **The Gain-reduction bar never fills while silent** — Thresh is set below the noise floor. Raise Thresh until consistent amber fill appears during silence.
- **The gate chops the beginning of words** — Thresh is too close to your voice level. Lower Thresh slightly.
- **The gate chatters or flutters near the threshold** — Increase Return to widen the hysteresis deadband. The cyan band on the Transfer curve grows as you raise Return, showing the sticky zone.
- **The gate does not close between words** — Thresh is too low for the current noise floor. Raise Thresh until the bar fills reliably during pauses.

## Related

- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)