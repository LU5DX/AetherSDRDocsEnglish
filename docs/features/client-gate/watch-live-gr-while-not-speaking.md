# Watch Live GR While Not Speaking

The gain-reduction bar and transfer curve update in real time, so you can watch exactly how much attenuation the gate is applying — even when you are not transmitting. This lets you verify that the gate is closing cleanly between words and opening fast enough when you speak.

## Before you start

- The Gate stage must be enabled in the CHAIN widget. The GATE sub-container is hidden until the stage is active.
- The GATE sub-container must be visible inside the PooDoo Audio (TXDSP) parent container.

## Steps

1. Open the PooDoo Audio (TXDSP) parent container in the applet panel.
2. Locate the GATE sub-container. If it is not visible, enable the Gate stage via the CHAIN widget.
3. Stay silent — do not speak into the microphone.
4. Watch the **Gain-reduction bar**: the amber strip fills from the right. A full fill indicates the gate is applying close to 40 dB of attenuation. No fill means the gate is open and passing audio.
5. Watch the **Transfer curve**: the live input ball moves left along the curve as your input level drops below the Thresh point.
6. Speak briefly, then go silent again. Confirm the amber fill returns promptly after you stop speaking. If it does not, the Release time may need adjustment — see [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).

## What each control does

| Control | Kind | Default | Valid range | Persisted key |
|---|---|---|---|---|
| Transfer curve | Indicator | — | — | — |
| Gain-reduction bar | Meter | — | 0 to 40 dB GR | — |
| Thresh | Knob | -40.0 dB | -80.0 to 0.0 dB | `ClientGateTxThresholdDb` |
| Ratio | Knob | 2.0 | 1.0 to 10.0 | `ClientGateTxRatio` |
| Attack | Knob | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` |
| Release | Knob | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` |
| Floor | Knob | -15.0 dB | -80.0 to 0.0 dB | `ClientGateTxFloorDb` |

**Gain-reduction bar:** A horizontal amber strip that fills from the right. The scale runs from 0 to 40 dB. A tick mark at the -15 dB position marks the default Floor value. When the gate is open (you are speaking above threshold), the bar is empty.

**Transfer curve:** Plots the expander's static transfer curve. The live input ball shows the current input level and whether the gate is open or closed. Below the Thresh point the ball moves into the attenuated portion of the curve.

## Tips

- The meter timer updates approximately every 33 ms, so the bar reflects near-real-time gain reduction.
- Changes made in the floating Gate editor are reflected live in the GATE sub-container knobs and vice versa — both views stay synchronized without requiring a restart.
- The -15 dB tick on the gain-reduction bar corresponds to the default Floor value (`ClientGateTxFloorDb`). If your bar never fills past that tick at rest, the Floor is doing its job and preventing an unnaturally deep cut.

## Related

- [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
