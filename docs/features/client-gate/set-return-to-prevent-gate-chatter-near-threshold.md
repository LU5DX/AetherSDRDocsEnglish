# Set Return to prevent gate chatter near threshold

When audio levels hover near the threshold, the gate can open and close rapidly, producing an audible stuttering effect called chatter. The Return knob adds a hysteresis deadband so the gate does not close again until the signal drops a set amount below the threshold where it opened.

## Before you start

- The gate must be enabled on the TX or RX side. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) to confirm the gate stage is active.
- Set Thresh first so you have a stable reference point. See [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md).

## Steps

1. Open the **Aetherial TX Gate** sub-container (TX side) or the **Aetherial AGC-G** sub-container (RX side) inside the Aetherial Audio (TXDSP) parent container. Alternatively, double-click the GATE stage in the CHAIN widget to open the floating editor titled **Aetherial Gate — TX** or **Aetherial Gate — RX**.
2. Locate the **Return** knob.
3. Turn **Return** upward from its default of 2.00 dB until the chatter stops. Start with small increases — 3 to 5 dB is often sufficient for voice.
4. Watch the transfer curve. A soft-cyan vertical band appears between (Thresh − Return) and Thresh, showing the hysteresis deadband. Widen or narrow it by adjusting **Return** until the band covers the range where your signal fluctuates.
5. Speak or pass audio at a level that previously caused chatter. Confirm the gate opens cleanly and does not re-close until your level drops below the bottom edge of the cyan band.

## What each control does

| Control | Default | Valid range | Persisted key (TX / RX) |
|---|---|---|---|
| **Return** | 2.00 dB | 0.0 to 20.0 dB | `ClientGateTxReturnDb` / `ClientGateRxReturnDb` |
| **Thresh** | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` / `ClientGateRxThresholdDb` |

**Return** sets the width of the hysteresis deadband in decibels. The gate opens when input rises above Thresh and does not close again until input falls below Thresh − Return. Setting Return to 0.0 dB removes the deadband entirely; the gate opens and closes at the same level, which maximises chatter risk near threshold.

The transfer curve draws a soft-cyan vertical band between (Thresh − Return) and Thresh whenever Return is greater than 0.0 dB. This band is the gate's sticky zone — signals inside it leave the gate in whatever state it is already in.

## Bypassed appearance

When the gate stage is bypassed, the entire applet tile dims to reduced opacity. This matches the dim effect used on the equaliser curve and provides an at-a-glance reminder that the gate is not processing audio. Re-enable the gate stage to restore full opacity and resume processing. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).

## Tips

- If you raise Return so high that the gate stays open through long pauses in speech, reduce it in small steps (0.5 dB at a time) until pauses close the gate naturally.
- Use the gain-reduction bar (amber strip, 0 to 40 dB scale) to confirm the gate is closing during true silence. If the bar never fills during a pause, Return may be too wide relative to your actual noise floor.
- Changes to Return take effect immediately and are saved automatically. No restart is required.

## Troubleshooting

- **Chatter persists after increasing Return** — Thresh may be set too close to a noisy signal that fluctuates widely. Lower Thresh slightly so the gate opens only on clear speech, then re-tune Return.
- **Gate stays open permanently** — Return is set wider than the gap between your signal level and the noise floor. Reduce Return until the gate closes reliably during silence.
- **Cyan band is not visible on the transfer curve** — Return is set to 0.0 dB. Any value above 0.0 dB will render the band.
- **Applet tile appears dimmed** — The gate stage is bypassed. Enable the gate stage to restore full opacity and active processing.

## Related

- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Tune release for natural gate close](tune-release-for-natural-gate-close.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)