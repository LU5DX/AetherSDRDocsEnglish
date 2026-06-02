# Sweep Freq to locate peak sibilance

Use the Freq knob to scan across the sibilance range while transmitting or monitoring audio, watching the gain-reduction bar for the frequency that triggers the most reduction. This identifies the centre of the problem sibilance band before you finalize your Q, Thresh, and Amount settings.

## Before you start

- The Aetherial De-Esser must be enabled via the CHAIN widget in the Aetherial Audio (TXDSP) container. The applet is hidden until the DESS stage is active.
- You need a live audio source — either transmitting or routing audio through the TX DSP chain — so the gain-reduction bar responds in real time.
- Open the de-esser applet. Bypass and enable are controlled by a single-click on the DESS stage in the CHAIN widget. Editing is done via the Aetherial Audio Channel Strip.

## Steps

1. Set Thresh to a value just below your typical sibilance peaks — a starting point of -30.0 dB (the default) works for most voices.
2. Set Amount to a clearly audible value such as -12.0 dB or lower so gain reduction is easy to see on the bar.
3. Speak or play audio containing sustained "S" and "T" sounds continuously into the microphone.
4. Slowly turn the Freq knob from its default of 6.0 kHz upward or downward across the 1000 to 12000 Hz range.
5. Watch the gain-reduction bar. The bar fills furthest to the right — indicating maximum attenuation — when Freq is centred on the dominant sibilance band.
6. Stop at the Freq value that produces the highest gain-reduction reading. That value is your sibilance centre frequency.
7. Return Amount to your intended operating value (default -6.0 dB) once the sweep is complete.

## What each control does

| Control                  | Default   | Valid range        |
|--------------------------|-----------|--------------------|
| Freq                     | 6000 Hz   | 1000 to 12000 Hz   |
| Q                        | 2.00      | 0.5 to 5.0         |
| Thresh                   | -30.0 dB  | -60.0 to 0.0 dB    |
| Amount                   | -6.0 dB   | -24.0 to 0.0 dB    |
| Attack                   | 1.0 ms    | 0.1 to 30.0 ms     |
| Release                  | 100 ms    | 10.0 to 500.0 ms   |
| Sidechain response curve | —         | —                  |
| Gain-reduction bar       | —         | 0 to 24 dB GR      |
| Slope                    | 24 dB/oct | 12/24/36/48 dB/oct |

**Note:** The Attack and Release knobs appear only in the Channel Strip StripDeEssPanel (both RX and TX). The docked ClientDeEssApplet omits these controls.

## Direct value entry

Click any knob's value display to reveal an inline text editor. Type a numeric value (including units or trailing text) and press Enter or click elsewhere to commit. The value is clamped to the knob's valid range. To cancel, press Escape — the knob reverts to its previous value.

- The editor supports locale-aware parsing so "12,5" works in comma-decimal locales.
- Trailing text such as "ms" or "dB" is stripped automatically.
- While the editor is active, mouse-wheel events still adjust the knob normally.

## Sidechain response curve axis labels

The curve widget draws frequency-axis labels using QStaticText for improved rendering performance. Labels are rendered as "100", "500", "1k", "2k", etc. The label text is cached after the first paint and reused on subsequent redraws. The axis labels are hidden when the curve widget is in compact mode.

## Bypass dim

When the DESS stage is bypassed via the CHAIN widget, the entire de-esser applet tile renders at reduced opacity (approximately 55% of full brightness). This matches the dim effect used on the EQ curve and gives a clear at-a-glance indication that the stage is inactive. The tile returns to full brightness as soon as the stage is re-enabled.

## RX and TX instances

The Aetherial De-Esser has separate settings for the TX and RX paths. The docked Applet Panel shows the TX copy labelled "Aetherial De-Esser". The RX copy, labelled "Aetherial De-Esser — RX", is reachable through the Aetherial Audio Channel Strip's StripDeEssPanel.

The StripDeEssPanel in the Channel Strip can be opened for either TX or RX. When opened for TX, the window title reads "Aetherial De-Esser — TX". When opened for RX, the window title reads "Aetherial De-Esser — RX". Each instance independently saves and restores its own knob settings using separate settings keys:
- TX: `ClientDeEssTxFrequencyHz`, `ClientDeEssTxQ`, `ClientDeEssTxThresholdDb`, `ClientDeEssTxAmountDb`, `ClientDeEssTxAttackMs`, `ClientDeEssTxReleaseMs`, `ClientDeEssTxSlopeStages`
- RX: `ClientDeEssRxFrequencyHz`, `ClientDeEssRxQ`, `ClientDeEssRxThresholdDb`, `ClientDeEssRxAmountDb`, `ClientDeEssRxAttackMs`, `ClientDeEssRxReleaseMs`, `ClientDeEssRxSlopeStages`

## Applet container styling

The docked Aetherial De-Esser applet tile uses the `applet/deess` container namespace for theme colour resolution. Knob colours — background ring, foreground arc, pointer, label text, and value text — are drawn from the theme's `color.knob.*` namespace:
- `color.knob.background` — ring background
- `color.knob.foreground` — ring arc
- `color.knob.handle` — pointer
- `color.text.secondary` — knob label
- `color.text.primary` — knob value

The sidechain response curve widget uses the following theme colour keys:
- `color.background.0` — curve background
- `color.background.1` — grid lines and major grid lines
- `color.text.label` — axis labels
- `color.accent.danger` — sibilant band curve (soft red)
- `color.accent.dim` — threshold indicator line
- `color.accent.danger` blended with `color.background.0` — centre-frequency ball glow and core

This allows consistent per-applet colour overrides without modifying widget code.

## Tips

- Keep Q at its default of 2.00 during the initial sweep. A very narrow Q can cause you to sweep past the true peak without triggering the bar. Narrow the band with Q only after you have located the peak.
- If the gain-reduction bar never moves, Thresh is set too high. Lower it until the bar responds to "S" sounds.
- The centre-frequency ball on the sidechain response curve moves as you turn Freq, giving a visual reference even before audio is present.
- Adjust Slope after finding the sibilance centre frequency. Start with 24 dB/oct (the default). If the de-esser affects mid-band speech, try 36 or 48 dB/oct for a narrower notch. If sibilants are still harsh, try 12 dB/oct for a wider notch.

## Slope button operation

In the Channel Strip StripDeEssPanel, a Slope push button is located at the bottom of the left knob column. Click it to cycle through 12, 24, 36, and 48 dB/oct (1 to 4 cascaded bandpass biquad stages). The button label updates to show the current value (e.g., "24 dB/oct").

The Slope setting is persisted per path: `ClientDeEssTxSlopeStages` for TX and `ClientDeEssRxSlopeStages` for RX. Changes take effect immediately and the sidechain response curve redraws to reflect the new slope.

## Troubleshooting

- **Gain-reduction bar does not move during the sweep** — Thresh is above the level of your sibilance peaks. Lower Thresh until the bar begins to respond, then re-sweep.
- **Bar stays near maximum across a wide Freq range** — Amount is set to a very large negative value and Thresh is very low. Raise Thresh slightly so the bar discriminates between frequencies rather than clamping at maximum everywhere.
- **Applet is not visible** — The DESS stage has not been enabled in the CHAIN widget. Enable it there first; the applet remains hidden until the stage is active.
- **Applet tile appears dimmed** — The DESS stage is currently bypassed. Single-click the DESS stage in the CHAIN widget to re-enable it.
- **Inline editor does not appear when clicking a knob** — The knob's inline edit mode may be disabled in your configuration. Verify that the `m_inlineEdit` flag is enabled (it is on by default).

## Related

- [Aetherial De-Esser overview](overview.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)