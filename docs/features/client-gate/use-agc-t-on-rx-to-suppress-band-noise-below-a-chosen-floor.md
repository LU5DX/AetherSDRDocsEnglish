# Use AGC-T on RX to Suppress Band Noise Below a Chosen Floor

The Aetherial AGC-T (RX) applet applies a client-side downward expander to your received audio. Use it to reduce persistent band noise, QRM, or hiss between signals by attenuating audio that falls below a level you set.

## Before you start

- The Aetherial AGC-T (RX) applet is hidden until the Gate stage is enabled on the RX side. Enable it via the CHAIN widget or the floating Gate editor for the RX side first.
- The applet lives inside the Aetherial Audio (TXDSP) parent container in the Applet Panel. Open the Applet Panel if it is not visible: `View > Applet Panel`.

## Steps

1. In the Applet Panel, locate the **Aetherial AGC-T** sub-container under the Aetherial Audio (TXDSP) parent container.
2. Enable the Gate stage for the RX side using the CHAIN widget (single-click the Gate stage) or double-click the Gate stage in the CHAIN widget to open the floating **Aetherial Gate — RX** editor.
3. Watch the **Transfer curve** — the live ball moves with your incoming audio level. Note where the ball sits during band noise versus during a signal.
4. Turn the **Thresh** knob to set the level below which the gate begins attenuating. Set it just above the noise floor and below the weakest signal you want to hear. Default: -40.0 dB; range: -80.0 to 0.0 dB. This value is saved as `ClientGateRxThresholdDb`.
5. Turn the **Ratio** knob to control how aggressively audio below the threshold is cut. At 2.0:1 (default) the gate acts as a soft expander; at 10.0:1 it cuts very hard. Range: 1.0 to 10.0. Saved as `ClientGateRxRatio`.
6. Turn the **Floor** knob to set the maximum attenuation the gate is allowed to apply. The default -15.0 dB leaves a faint residual noise rather than cutting to silence. Range: -80.0 to 0.0 dB. Saved as `ClientGateRxFloorDb`.
7. Turn the **Release** knob to control how quickly the gate closes after a signal drops below the threshold. Default: 100 ms; range: 5 to 2000 ms. Saved as `ClientGateRxReleaseMs`. A longer release sounds more natural; a shorter release closes more tightly between signals.
8. Observe the **Gain-reduction bar** while band noise is present with no signal. The amber strip fills from the right as gain reduction is applied. The tick mark at -15 dB indicates the default Floor position. Adjust Thresh and Floor until the bar stays filled during noise and empties promptly when a signal appears.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Thresh | -40.0 dB | -80.0 to 0.0 dB | `ClientGateRxThresholdDb` | Level below which attenuation begins. Lower values let more signal through before the gate acts. |
| Ratio | 2.0 | 1.0 to 10.0 | `ClientGateRxRatio` | Expansion ratio below threshold. Higher values produce a harder gate-like cut; lower values give a gentler slope. Displayed as X.X:1. |
| Release | 100 ms | 5 to 2000 ms | `ClientGateRxReleaseMs` | How quickly the gate closes after input falls below threshold. Uses exponential mapping. |
| Floor | -15.0 dB | -80.0 to 0.0 dB | `ClientGateRxFloorDb` | Maximum attenuation the gate may apply. Prevents complete silence during noise. |
| Transfer curve | — | — | — | Plots the static expander curve. A live ball shows current input level relative to the threshold. |
| Gain-reduction bar | — | 0 to 40 dB GR | — | Amber strip filling from the right shows current attenuation depth. The tick at -15 dB marks the default Floor. |

> **Note:** The source confirms the applet also has a **Return** knob (default 2.0 dB, range 0.0 to 20.0 dB) and a **Release** knob in the actual built UI. The catalog lists Attack (`ClientGateRxAttackMs`, default 0.5 ms, range 0.1 to 100.0 ms) as a separate persisted value; it is adjustable in the floating **Aetherial Gate — RX** editor if not present in the applet tile.

## Tips

- Start with Thresh at -40.0 dB and raise it slowly until the gain-reduction bar fills solidly during band noise but opens cleanly when a signal appears.
- Set Floor to -15.0 dB initially. Reduce it (more negative) only if the residual noise is still distracting. Avoid very low Floor values, as they can make the audio sound unnatural between signals.
- Changes made in the floating **Aetherial Gate — RX** editor and in the applet tile stay synchronized — the tile polls the engine approximately every 33 ms and updates its knobs to match.
- The AGC-T operates entirely client-side and requires no radio connection to configure.

## Troubleshooting

- **The Aetherial AGC-T applet is not visible in the Applet Panel** — The Gate stage on the RX side has not been enabled. Enable it via the CHAIN widget for the RX side. The applet is hidden until the stage is active.
- **The gain-reduction bar shows no activity even during band noise** — Thresh is set too low. The noise floor is not reaching the threshold. Raise Thresh toward 0 dB until the bar shows amber fill during noise.
- **Signals are being cut along with the noise** — Thresh is set too high. Lower Thresh so that only the noise floor triggers attenuation and desired signals open the gate.
- **The gate sounds abrupt or choppy between signals** — Increase the Release value to allow the gate to close more gradually after each signal.

## Related

- [Aetherial TX Gate / Aetherial AGC-T (RX) overview](overview.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
