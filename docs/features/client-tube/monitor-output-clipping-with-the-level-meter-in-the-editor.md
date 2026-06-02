# Monitor output clipping with the level meter in the editor

The floating Tube editor includes a live output level meter that shows the post-saturation peak level. Use it to confirm that Drive and Output settings are not clipping the processed signal before it leaves the tube stage.

## Before you start

- The Tube stage must be enabled on the side you want to monitor (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md) if the stage is not yet active.
- The floating editor must be open. The level meter is not visible in the docked applet tile.

## Steps

1. Double-click the TUBE stage in the CHAIN widget on the TX or RX side to open the floating editor. The TX editor is titled "Aetherial Tube — TX"; the RX editor is titled "Aetherial Tube — RX".
2. Locate the "OUT" meter on the far right of the editor. It displays post-saturation peak level with fast-attack and slow-release ballistics.
3. Pass audio through the stage — transmit or receive signal as appropriate — and observe the meter while adjusting Drive and Output.
4. Keep the meter out of the red zone. The color bands indicate the following levels:

| Color | Range          | Notes                                                                                                         |
|-------|----------------|---------------------------------------------------------------------------------------------------------------|
| Green | −60 to −12 dB  |                                                                                                               |
| Lime  | −12 to −6 dB   |                                                                                                               |
| Amber | −6 to −3 dB    |                                                                                                               |
| Red   | Above −3 dB    |                                                                                                               |

5. If the meter consistently reads red, reduce the Output knob (range −24.0 to 12.0 dB, default 0.00 dB, persisted as `ClientTubeTxOutputDb` or `ClientTubeRxOutputDb`) or reduce the Drive knob (range 0.0 to 24.0 dB, default 0.00 dB, persisted as `ClientTubeTxDriveDb` or `ClientTubeRxDriveDb`) until the meter stays in the amber or lower bands under typical signal conditions.

## Tips

- The meter reflects the signal after the tube stage. Reducing Drive affects harmonic character as well as level; reducing Output trims level only without changing the saturation curve.
- The Dry/Wet knob (persisted as `ClientTubeTxDryWet` or `ClientTubeRxDryWet`) blends the dry signal back in. At values below 100 %, the meter will read lower because the unprocessed signal is mixed with the saturated output, which can mask how hard the tube itself is being driven.
- Changes made in the floating editor are reflected on the docked applet tile knobs within approximately 33 ms via the sync timer, and vice versa.
- When the Tube stage is bypassed, the entire docked applet tile renders at reduced opacity (approximately 55 % of full brightness). This visual dim matches the behavior of the EQ curve tile and gives a clear at-a-glance indication that the stage is inactive. The opacity returns to 100 % as soon as the stage is re-enabled.
- Knob values can be edited directly by clicking on the value text. This opens an inline text editor overlay. Type the desired value and press Enter or click elsewhere to commit. The value is clamped to the valid range for that knob. Press Escape to cancel the edit and revert to the previous value.

## Related

- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Parallel-blend saturation with Dry/Wet](parallel-blend-saturation-with-dry-wet.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)