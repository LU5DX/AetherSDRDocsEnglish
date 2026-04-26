# Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)

Use the Drive knob to push more signal into the tube stage until the transfer curve visibly bends, adding harmonic richness to your TX audio or shaping the tone of received audio.

## Before you start

- The Tube stage must be enabled on the side you want to adjust (TX or RX). If it is not yet active, enable it via the CHAIN widget first. See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- Open the applet: the TX tube applet appears in the "Aetherial Mic-PreAmp" sub-container inside the Aetherial Audio (TXDSP) parent container; the RX tube applet appears in the "Aetherial Dynamic Tube" sub-container. Double-click the TUBE stage in the CHAIN widget to open the matching floating editor ("Aetherial Tube — TX" or "Aetherial Tube — RX") if you prefer a larger view.

## Steps

1. Locate the **Drive** knob in the five-knob row (Drive, Tone, Bias, Output, Mix).
2. Watch the **Transfer curve** display above the knob row. At the default of 0.0 dB the curve is nearly straight.
3. Turn **Drive** clockwise. The knob label updates as `X.X dB`. Increase Drive until you see the transfer curve begin to bend at its top and bottom — this is where saturation starts.
4. Observe the **Live input ball** (the dot riding the transfer curve). As Drive increases, the ball travels further into the bent region of the curve during loud signal peaks, showing you how heavily the tube is being driven.
5. Stop increasing Drive when the amount of curve bend suits the effect you want. Moderate bend (roughly 6–12 dB of Drive) produces subtle warmth; higher Drive produces more obvious saturation.
6. If the driven signal is louder or quieter than the bypass signal, turn the **Output** knob to compensate. See [Compensate level changes with Output](compensate-level-changes-with-output.md).
7. Your setting is saved automatically. The knob value is persisted as `ClientTubeTxDriveDb` (TX) or `ClientTubeRxDriveDb` (RX).

## What each control does

| Control | Default | Valid range | Persisted key (TX / RX) | Behavior |
|---|---|---|---|---|
| Drive | 0.0 dB | 0.0 to 24.0 dB | `ClientTubeTxDriveDb` / `ClientTubeRxDriveDb` | Pushes more signal into the tube stage; higher values bend the transfer curve further. |
| Transfer curve | — | — | — | Displays the tube transfer curve. Bends visibly as Drive, Bias, or model changes. |
| Live input ball | — | — | — | Dot that moves along the transfer curve at the current input level, showing the active saturation regime. |

## Tips

- Start with Drive at 0.0 dB and increase slowly. The first noticeable bend in the transfer curve is typically the most musical-sounding operating point.
- The applet knobs and the floating editor knobs stay in sync. Changes made in one view are reflected in the other within approximately 33 ms.
- If you want only a touch of saturation rather than full processing, set **Mix** below 100 % to blend the dry signal back in. See [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md).
- After setting Drive, use **Tone** to brighten or darken the result without changing the saturation amount. See [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md).
- Use **Bias** to shift the operating point on the curve and change the harmonic character of the saturation. See [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md).

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
