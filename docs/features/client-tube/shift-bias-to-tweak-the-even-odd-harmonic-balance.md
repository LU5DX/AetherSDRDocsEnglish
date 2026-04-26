# Shift Bias to tweak the even / odd harmonic balance

The Bias knob shifts the tube model's operating point on the transfer curve, changing the ratio of even to odd harmonics in the saturated signal. Use it to add asymmetric warmth or push toward a more complex, harmonically rich tone.

## Before you start

- The Tube Saturator stage must be enabled and visible. If the TUBE sub-container is hidden, enable the stage via the CHAIN widget or double-click the Tube stage in the CHAIN widget to open the floating Tube editor.
- Drive should already be set high enough that the transfer curve shows visible bending. Without some drive, Bias has little audible effect.

## Steps

1. Open the TUBE sub-container inside the PooDoo Audio (TXDSP) parent container in the applet panel.
2. Locate the transfer curve display at the top of the applet. The live input ball rides the curve at the current input level.
3. Turn the **Bias** knob. Start from the default of 0 % and increase toward 100 % while watching the curve bend asymmetrically.
4. Transmit a steady signal — for example, speak into the microphone on SSB or key a tone — and listen for the change in harmonic character as Bias increases.
5. Stop at the value where the even/odd harmonic balance suits your taste. The transfer curve and the live input ball update in real time to reflect the new operating point.

## What each control does

| Control | Default | Range | Persisted key | Behavior |
|---|---|---|---|---|
| Bias | 0 % | 0 % to 100 % | `ClientTubeTxBiasAmount` | Shifts the operating point on the transfer curve. Higher values increase asymmetric saturation, altering the even/odd harmonic mix. |
| Drive | 0.0 dB | 0.0 to 24.0 dB | `ClientTubeTxDriveDb` | Pushes more signal into the tube stage. More drive makes Bias changes more pronounced. |
| Transfer curve | — | — | — | Draws the current tube transfer curve. Updates immediately as Bias changes. The live input ball shows the current saturation regime. |

## Tips

- Bias works in conjunction with Drive. At 0.0 dB Drive the curve is nearly linear and Bias has minimal audible effect. Increase Drive first until the curve bends, then dial in Bias.
- The transfer curve's asymmetry becomes visible as Bias increases above 0 %. Use it as a visual reference alongside the audio result.
- If the Bias change shifts your overall output level noticeably, use the **Output** knob (`ClientTubeTxOutputGainDb`, default 0.0 dB, range −24.0 to 12.0 dB) to compensate.
- Changes made to Bias in the floating Tube editor are reflected on the applet knob within approximately 33 ms, and vice versa.

## Troubleshooting

- **Bias knob has no audible effect** — Drive is likely at or near 0.0 dB. Increase Drive until the transfer curve shows clear bending, then adjust Bias.
- **Bias change disappears after restarting AetherSDR** — The value is persisted to `ClientTubeTxBiasAmount`. If the setting is not being saved, confirm the Tube stage is fully enabled before closing the application.

## Related

- [Tube Saturator overview](overview.md)
- [Dial Drive until the curve starts to bend](dial-drive-until-the-curve-starts-to-bend.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from the chain](bypass-the-tube-from-the-chain.md)
