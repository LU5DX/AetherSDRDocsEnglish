# Tune Release for Natural Gate Close

The Release knob controls how quickly the gate closes after audio drops below the threshold. Setting it correctly prevents the gate from cutting off word endings too abruptly or leaving the gate open so long that background noise bleeds through between words.

## Before you start

- The gate stage must be enabled on the TX or RX side. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if the gate is currently bypassed. When the gate stage is bypassed, the entire applet tile dims to approximately 55% opacity — this is normal and indicates the DSP stage is inactive.
- Open the Aetherial TX Gate or Aetherial AGC-G (RX) applet so the knobs are visible. The applet appears inside the Aetherial Audio (TXDSP) parent container once the gate stage is active.

## Steps

1. Locate the **Release** knob in the five-knob row at the bottom of the applet. It is the fourth knob from the left, between **Return** and **Floor**.
2. Turn **Release** clockwise to increase the release time (slower close) or counter-clockwise to decrease it (faster close). The knob label updates live, showing the current value in milliseconds — formatted as `X.X ms` below 100 ms and `X ms` at 100 ms and above.
3. Speak or pass audio through the gate while watching the gain-reduction bar. After audio drops below the threshold, observe how quickly the amber strip rises to full attenuation. Adjust **Release** until the gate closes smoothly without clipping word endings.
4. If the gate closes so slowly that noise is audible between words, reduce **Release**. If word endings are cut off, increase **Release**.

## What each control does

| Control | Default | Valid range | Persisted key (TX / RX) |
|---|---|---|---|
| **Release** | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` / `ClientGateRxReleaseMs` |

The knob uses an exponential mapping (5 × 400^n), so small movements at the low end of the range produce finer timing adjustments, while the upper range covers long, gradual fade-outs. Release begins only after the input has fallen below Thresh − Return; the **Return** value therefore affects when the release phase starts.

## Transfer curve display

The transfer curve widget plots the expander's static transfer curve with a live ball at the current input level. A soft-cyan hysteresis-band overlay appears between (Thresh − Return) and Thresh, making the sticky zone visible. The widget uses compact-mode rendering when the applet is in its smaller state, with axis labels drawn using cached static text for improved performance. Colors in the curve widget now respect the selected theme: the curve color uses the accent warning color, and grid, background, and label colors follow the theme's color palette.

## Gain-reduction bar

A horizontal amber strip, filled from the right, shows the depth of attenuation applied. The scale maxes at 40 dB gain reduction, with a tick at -15 dB marking the default Floor setting.

## Inline value editing

Each knob in the five-knob row supports direct numeric entry. Click the value text below a knob to activate an inline editor. Type a number and press Enter or click elsewhere to commit the value. The value is clamped to the knob's valid range. Press Escape to cancel editing and revert to the previous value. The editor appears as a subtle dark inset with a cyan border when focused, and matches the painted label appearance when unfocused. Knob colors for the ring arc, background, handle, label, and value text now follow the theme's designated color namespace (`color.knob.*`), with the label text using color.text.secondary and value text using color.text.primary.

## Tips

- 100 ms (the default) suits most voice TX work. Increase toward 200–400 ms if consonants at the end of words are being clipped. Decrease toward 20–50 ms if background noise is audible in the gaps between words.
- Release interacts with **Return**: a larger Return deadband delays the start of the release phase. If the gate seems to hang open, check **Return** before shortening **Release** further.
- The gain-reduction bar updates approximately every 33 ms. Watch it in real time while adjusting **Release** to confirm the close speed before transmitting.
- Changes take effect immediately and are saved automatically. No radio connection is required to adjust this setting.
- If the applet tile appears dimmed, the gate stage is bypassed and no processing is occurring. Re-enable the stage before making adjustments. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).
- For precise adjustments, click the value text below the Release knob to enter a specific millisecond value directly. This is useful when you need to match a known timing from another processor or save a specific setting for later recall.
- The applet and its curve widget now use the active theme's colors. Knob ring arcs, backgrounds, and handles draw from the theme's knob color namespace. The curve widget uses theme colors for its background, grid, axis labels, identity line, and the amber accent warning color for the curve — all of which update when the theme changes.

## Related

- [Set Return to prevent gate chatter near threshold](set-return-to-prevent-gate-chatter-near-threshold.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Customize theme colors for knobs and curves](customize-theme-colors-for-knobs-and-curves.md) (if applicable for your theme setup)