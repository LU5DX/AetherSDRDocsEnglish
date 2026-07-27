# Set threshold just below the loudest 'S' peaks

This page explains how to set the Thresh knob so the de-esser acts only on genuine sibilance and leaves quieter speech untouched. A well-placed threshold is the difference between transparent de-essing and audible pumping.

## Before you start

- The Aetherial De-Esser must be enabled via the CHAIN widget. See [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md).
- The Aetherial De-Esser applet must be visible in the applet panel (sub-container "Aetherial De-Esser" inside the Aetherial Audio (TXDSP) parent container).
- You need a way to transmit or monitor your own TX audio so that genuine speech reaches the de-esser's sidechain.

## Steps

1. Open the de-esser controls: open the Aetherial Audio Channel Strip, or work directly on the Thresh knob in the docked applet.
2. Start speaking into your microphone, repeating a sibilant phrase — something with repeated 'S' and 'T' sounds works well.
3. Watch the Gain-reduction bar. If it shows a soft-red fill during normal vowels and consonants (not just on 'S' peaks), the threshold is too low. If it never moves during loud 'S' sounds, the threshold is too high.
4. Turn the Thresh knob clockwise to raise the threshold (toward 0.0 dB) until the Gain-reduction bar stays empty during normal speech.
5. Then turn Thresh slowly counter-clockwise (toward −60.0 dB) until the Gain-reduction bar just starts to fill on your loudest 'S' peaks and no more.
6. Verify: speak normally through a full sentence. The Gain-reduction bar should be empty most of the time and fill briefly only on hard sibilants.

## What each control does

| Control            | Default              | Valid range                              |
|--------------------|----------------------|------------------------------------------|
| Thresh             | −30.0 dB             | −60.0 to 0.0 dB                          |
| Gain-reduction bar | —                    | 0 to 24 dB GR                            |
| Freq               | 6000 Hz              | 1000 to 12000 Hz                         |
| Q                  | 2.00                 | 0.5 to 5.0                               |
| Amount             | −6.0 dB              | −24.0 to 0.0 dB                          |
| Attack             | 1.0 ms               | 0.1 to 30.0 ms                           |
| Release            | 100 ms               | 10.0 to 500.0 ms                         |
| Slope              | 24 dB/oct (2 stages) | 12 / 24 / 36 / 48 dB/oct (1 to 4 stages) |

**Thresh** — the level above which the de-esser begins attenuating the sibilance band. Raising this value (toward 0.0 dB) makes the de-esser act only on the very loudest sibilance. Lowering it (toward −60.0 dB) causes the de-esser to trigger on progressively quieter signals.

**Gain-reduction bar** — a horizontal soft-red strip that fills from the right to show current attenuation. The scale runs from 0 to 24 dB. A tick marks the −6 dB position, which is the default Amount value. The bar refreshes approximately 30 times per second. The bar's colour is drawn from the theme's `color.accent.danger` value.

**Freq** — sets the centre frequency of the sibilance band (1000 to 12000 Hz, logarithmic mapping). Default 6000 Hz. Labels show "6.0 kHz" above 1 kHz and "N Hz" below. Press Enter or click away after typing a value to commit it. Setting key: `ClientDeEssTxFrequencyHz`.

**Q** — sets the bandwidth of the sibilance band (0.5 to 5.0, linear mapping). Higher Q = narrower band. Default 2.00. Label format "X.XX". Press Enter or click away after typing a value to commit it. Setting key: `ClientDeEssTxQ`.

**Amount** — maximum attenuation applied at peak sibilance (−24.0 to 0.0 dB, linear mapping). Values are negative (or zero) because they represent reduction. Default −6.0 dB. Press Enter or click away after typing a value to commit it. Setting key: `ClientDeEssTxAmountDb`.

**Attack** — how quickly the de-esser responds once sibilance crosses the threshold (0.1 to 30.0 ms, exponential mapping). Present in the Channel Strip StripDeEssPanel for both RX and TX. The docked ClientDeEssApplet omits this knob. Setting key: `ClientDeEssTxAttackMs`.

**Release** — how quickly gain returns after sibilance drops below the threshold (10.0 to 500.0 ms, exponential mapping). Present in the Channel Strip StripDeEssPanel for both RX and TX. The docked ClientDeEssApplet omits this knob. Setting key: `ClientDeEssTxReleaseMs`.

**Slope** — sets the sidechain bandpass cascade count. Each stage adds 12 dB/oct of rolloff outside the sibilant band. Higher slope = narrower effective notch, less mid-band collateral on Ess-heavy phrases. Click the button to cycle through 12 → 24 → 36 → 48 dB/oct (1 to 4 stages). Present in the Channel Strip StripDeEssPanel (left column, bottom). Persisted as `ClientDeEssTxSlopeStages` for TX and `ClientDeEssRxSlopeStages` for RX.

## Sidechain response curve

The Sidechain response curve indicator draws the bandpass filter response with a live ball at the current centre frequency. The frequency axis is labelled with major gridlines at 100, 500, 1k, 2k, 3k, 4k, 5k, 6k, 7k, 8k, 9k, 10k, 11k, and 12k Hz. These labels are drawn as high-performance static text objects cached after the first paint. The labels appear only when the curve widget is not in compact mode.

The curve and grid colours are drawn from the theme: `color.background.0`, `color.background.1`, `color.text.label`, `color.accent.danger`, and `color.accent.dim`. The curve colour uses a soft red ("sibilant band").

The Centre-frequency ball rests on the curve peak, marking the currently-tuned sibilance centre frequency. The ball uses `color.accent.dim` for glow and `color.text.primary` for the core.

The curve updates automatically when Slope stages are changed to reflect the steeper or shallower rolloff.

As of v26.7.4, the curve widget no longer uses a separate edit-style for its appearance — the edit-style constant has been removed, and the widget always refreshes its display regardless of whether the animated gain-reduction value has fully settled. This ensures that the sidechain response curve redraws continuously for smooth visual tracking during parameter changes.

## Inline value editing

Each tuning knob (Freq, Q, Thresh, Amount, Attack, Release) supports direct value entry. Click the displayed value text to activate an inline editor overlay. The editor appears as a cyan-bordered text field against a dark background.

- **Enter** — commits the typed value and closes the editor.
- **Click elsewhere (focus loss)** — commits the typed value and closes the editor.
- **Escape** — discards the typed value and reverts to the previous value.

The inline editor accepts locale-aware number formats (for example "12,5" in comma-decimal locales). It also tolerates extra text such as unit suffixes ("6 kHz", "−30 dB") by stripping non-numeric characters before parsing. If parsing fails, the editor silently reverts to the last valid displayed value.

The editor is hidden by default in the docked ClientDeEssApplet, and visible by default in the Channel Strip StripDeEssPanel. When hidden, knob values display as painted text only.

This feature is provided by `ClientCompKnob`, which is also used by the Compressor and other audio processing widgets in the Aetherial Audio Channel Strip. See Inline edit knob values.

## Bypass dimming

When the DESS stage is bypassed via the CHAIN widget, the entire de-esser applet tile renders at reduced opacity (approximately 55 % of full brightness). This matches the dim effect applied to the EQ curve when that stage is bypassed. Full opacity is restored as soon as the stage is re-enabled.

## Theme-aware knob colours

As of v26.6.1, the de-esser's knobs read their colours from the theme system's `color.knob.*` namespace:

| Theme key | Component | Description |
|-----------|-----------|-------------|
| `color.knob.background` | Ring background | The unlit portion of the knob arc |
| `color.knob.foreground` | Ring arc | The lit portion of the knob arc |
| `color.knob.handle` | Pointer | The knob indicator line |
| `color.text.secondary` | Label | The knob component label |
| `color.text.primary` | Value | The current numeric value |

The applet container `applet/deess` carries per-applet colour overrides. If a theme defines an `applet/deess` section, its colours take precedence over the global `color.knob.*` values.

## Smoothed gain-reduction meter (v26.6.3)

As of v26.6.3, the gain-reduction meter uses an improved animation timer that stops updating the display once the smoothed value has fully settled. Previously the timer continued running even when no further visual change was needed. The meter now stops and restarts efficiently, reducing CPU overhead during periods of stable gain reduction.

The smooth animation uses a 30 Hz refresh rate with a precise timer for consistent visual tracking of sibilance peaks.

As of v26.7.4, the curve widget always redraws regardless of whether the animation has settled, ensuring continuous visual updates.

## Tips

- The threshold interacts with Amount (`ClientDeEssTxAmountDb`). Set the threshold first, then dial Amount to taste. See [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md).
- If you are unsure where your sibilance peaks are in frequency, locate them first before finalising the threshold. See [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md).
- Watching the Gain-reduction bar in real time while speaking is the most reliable way to judge threshold placement. See [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md).
- Use higher Slope values (36 or 48 dB/oct) when you have dense sibilant passages to minimise collateral attenuation of the mid speech band. A Slope of 24 dB/oct is a good starting point for most voices.

## Troubleshooting

- **Gain-reduction bar fills continuously, even on vowels** — Thresh is set too low. Raise it (clockwise) until the bar is empty during non-sibilant speech.
- **Gain-reduction bar never moves, even on hard 'S' sounds** — Thresh is set too high, or the sibilance band (Freq, Q) is not centred on the problem frequencies. Raise the band level by lowering Thresh, or revisit Freq. See [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md).
- **De-esser appears to do nothing at all** — confirm the DESS stage is enabled in the CHAIN widget. See [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md).
- **Applet tile appears dimmed** — the DESS stage is currently bypassed in the CHAIN widget. Single-click the stage in the CHAIN widget to re-enable it and restore full brightness.

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)
- Opening the RX de-esser panel
- Inline edit knob values