# Tune Attack, Release, and Slope for natural-sounding de-essing response

This page helps you adjust the Attack, Release, and Slope controls on the RX-side or TX-side De-Ess editor so the de-esser responds to sibilance quickly without sounding choppy or unnatural.

## Before you start

- The De-Ess stage must be enabled in the CHAIN widget (click DESS once to enable; double-click to open the editor).
- For TX: the docked **Aetherial De-Esser** applet shows the four everyday knobs (Freq, Q, Thresh, Amount). **Attack**, **Release**, and **Slope** are only available in the frameless editor window opened by double-clicking DESS in the CHAIN widget (or by opening the Aetherial Audio Channel Strip).
- For RX: open the Aetherial Audio Channel Strip and double-click DESS in the RX chain to open the RX De-Ess editor, which includes Attack, Release, and Slope.
- The Attack, Release, and Slope controls are only present in the **StripDeEssPanel** (inside the Channel Strip), not in the docked ClientDeEssApplet.

## Inline value editing

All knobs in the De-Ess editor now support inline numeric entry for precise adjustment:

1. Click the value text displayed below any knob to enter edit mode. The value area shows a subtle dark inset with a cyan border to indicate edit mode.
2. Type a numeric value. Locale-aware parsing is supported (e.g., "12,5" works in comma-decimal locales). Optional units or descriptive text (e.g., "12.5 ms" or "−6 dB") are stripped and parsed correctly.
3. Press **Enter** or click elsewhere to commit the value. The value is clamped to the knob's valid range.
4. Press **Escape** while editing to cancel and revert to the previous value.

## Steps

1. Open the De-Ess editor that includes Attack, Release, and Slope:
   - **TX:** Double-click the DESS stage in the CHAIN widget to open the frameless editor titled **Aetherial De-Esser — TX**.
   - **RX:** Open the **Aetherial Audio Channel Strip** and double-click **DESS** in the RX chain to open the RX De-Ess editor.

2. Train the de-esser on sibilant speech:
   - Sweep the **Freq** knob to locate your peak sibilance (see [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)).
   - Set **Thresh** just below the loudest 'S' peaks (see [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)).
   - Adjust **Amount** for transparent reduction (see [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)).

3. Adjust **Attack**:
   - Default: **1.0 ms**
   - Range: **0.1 to 30.0 ms** (exponential mapping)
   - Turn **clockwise** to slow the attack (longer reaction time; may let some sibilance through before ducking).
   - Turn **counter-clockwise** to speed the attack (faster reaction; catches sibilance quickly but can sound clicky if too fast).

4. Adjust **Release**:
   - Default: **100 ms**
   - Range: **10.0 to 500.0 ms** (exponential mapping)
   - Turn **clockwise** to lengthen release (gain returns slowly after sibilance stops; may sound "pumped" on fast speech).
   - Turn **counter-clockwise** to shorten release (gain snaps back quickly; can sound choppy on sustained 'S' sounds).

5. Adjust **Slope**:
   - Click the **Slope** button at the bottom of the left knob column to cycle through available slopes.
   - Default: **24 dB/oct** (2 cascaded bandpass biquads)
   - Available settings: **12, 24, 36, 48 dB/oct** (1 to 4 stages)
   - Higher slope = narrower effective notch around the sibilant frequency = less mid-band collateral on Ess-heavy phrases.
   - The button text updates to show the current setting (e.g., "24 dB/oct").

6. Test with a sibilant phrase while watching the **Gain-reduction bar** (the soft-red strip at the bottom of the De-Ess curve widget):
   - Aim for smooth, brief reductions on each 'S' peak (the bar should fill and empty cleanly with each syllable).
   - If the bar "hangs" after sibilance stops, increase **Release** (longer sustain).
   - If the bar reacts sluggishly to the first 'S' of a word, decrease **Attack** (faster response).
   - If you hear collateral attenuation of mid speech bands on Ess-heavy phrases, try a higher **Slope** setting.

7. Listen on-air or record a short sample and adjust iteratively until the de-essing sounds transparent.

## What each control does

| Control | Kind        | Default   | Range              | Mapping       | Setting key (TX)              | Setting key (RX)              |
|---------|-------------|-----------|--------------------|---------------|-------------------------------|-------------------------------|
| Attack  | knob        | 1.0 ms    | 0.1 to 30.0 ms     | Exponential   | `ClientDeEssTxAttackMs`       | `ClientDeEssRxAttackMs`       |
| Release | knob        | 100 ms    | 10.0 to 500.0 ms   | Exponential   | `ClientDeEssTxReleaseMs`      | `ClientDeEssRxReleaseMs`      |
| Slope   | push button | 24 dB/oct | 12/24/36/48 dB/oct | Cascaded biquad stages | `ClientDeEssTxSlopeStages`    | `ClientDeEssRxSlopeStages`    |

These controls exist only in the frameless strip editors (StripDeEssPanel). The docked ClientDeEssApplet omits them.

## Tips

- For typical SSB voices, **Attack 0.5–2 ms** and **Release 80–150 ms** works well. Very fast speech (e.g. contesting) may need shorter values at both ends.
- Start with **Slope** at 24 dB/oct (the default). Increase to 36 or 48 dB/oct only if you hear unwanted attenuation of nearby speech frequencies.
- The **-6 dB tick** on the gain-reduction bar marks the default Amount level — it's a useful reference for how much the de-esser is actually reducing.
- The sidechain response curve now shows frequency axis labels at 100, 500, 1k, 2k, 4k, 8k, and 16k Hz using cached static text for improved performance. The axis labels are only displayed when the curve widget is in its full (non-compact) mode. When in compact mode (as in the docked applet), only the grid lines are drawn without frequency labels.
- Attack, Release, and Slope settings are stored per path (TX and RX) and persist across sessions.
- To enter precise values, click any knob's value text to activate the inline editor. Type the desired number (with or without units) and press Enter to commit.

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)