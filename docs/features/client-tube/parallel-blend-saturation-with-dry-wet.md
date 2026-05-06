# Parallel-blend saturation with Dry/Wet

Use the Dry/Wet control to blend the saturated tube signal with the original unprocessed signal. Setting Dry/Wet below 100 % lets you dial in subtle harmonic color without fully replacing the clean signal.

## Before you start

- The Tube stage must be enabled for the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- Open the floating editor for the relevant side: double-click the TUBE stage in the CHAIN widget to open "Aetherial Tube — TX" or "Aetherial Tube — RX".

## Steps

1. Open the floating editor by double-clicking the TUBE stage in the CHAIN widget on the TX or RX side.
2. Locate the **Dry/Wet** knob in the left column of the editor (top knob in that column).
3. Turn **Dry/Wet** toward 0 % to blend in more of the unprocessed signal, or toward 100 % for a fully saturated output.
4. Watch the transfer curve and the **OUT** level meter on the right of the editor as you adjust. Reducing Dry/Wet lowers the contribution of the saturated signal; use **Output** to compensate if overall level changes.

Alternatively, adjust **Mix** directly from the docked applet tile without opening the editor. The **Mix** knob on the tile is the same Dry/Wet control.

## What each control does

| Control | Default | Valid range | Persisted setting key |
|---|---|---|---|
| **Dry/Wet** (editor) / **Mix** (docked tile) | 100 % | 0 % to 100 % (stored as 0.0 to 1.0) | `ClientTubeTxDryWet` (TX), `ClientTubeRxDryWet` (RX) |

## Tips

- A Dry/Wet value between 20 % and 50 % is effective for adding warmth on SSB TX without audible distortion artifacts. The dry signal anchors the fundamental while the wet signal contributes harmonics.
- Changes made in the floating editor and on the docked tile stay in sync. A 30 Hz polling timer keeps both views updated automatically.
- If you raise **Drive** for more harmonic density, lowering **Dry/Wet** lets you recover a natural-sounding blend without reducing Drive itself.

## Troubleshooting

- **Adjusting Dry/Wet has no audible effect** — confirm the Tube stage is enabled. If the stage is bypassed in the CHAIN widget, the signal passes through unprocessed regardless of the Dry/Wet setting. When the stage is bypassed, the entire docked applet tile dims to approximately 55 % opacity as a visual reminder that the stage is inactive.
- **Level changes when moving Dry/Wet** — this is expected. Use the **Output** knob (range −24.0 to 12.0 dB, default 0.00 dB) to trim the post-saturation level. See [Compensate level changes with Output](compensate-level-changes-with-output.md).

## Related

- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Monitor output clipping with the level meter in the editor](monitor-output-clipping-with-the-level-meter-in-the-editor.md)