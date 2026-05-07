# Tune Attack and Release for natural-sounding de-essing response

This page helps you adjust the Attack and Release knobs on the RX-side or TX-side De-Ess editor so the de-esser responds to sibilance quickly without sounding choppy or unnatural.

## Before you start

- The De-Ess stage must be enabled in the CHAIN widget (click DESS once to enable; double-click to open the editor).
- For TX: the docked **Aetherial De-Esser** applet shows the four everyday knobs (Freq, Q, Thresh, Amount). **Attack** and **Release** are only available in the frameless editor window opened by double-clicking DESS in the CHAIN widget (or by opening the Aetherial Audio Channel Strip).
- For RX: open the Aetherial Audio Channel Strip and double-click DESS in the RX chain to open the RX De-Ess editor, which includes Attack and Release.
- The Attack and Release knobs are only present in the **StripDeEssPanel** (inside the Channel Strip), not in the docked ClientDeEssApplet.

## Steps

1. Open the De-Ess editor that includes Attack and Release:
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

5. Test with a sibilant phrase while watching the **Gain-reduction bar** (the soft-red strip at the bottom of the De-Ess curve widget):
   - Aim for smooth, brief reductions on each 'S' peak (the bar should fill and empty cleanly with each syllable).
   - If the bar "hangs" after sibilance stops, increase **Release** (longer sustain).
   - If the bar reacts sluggishly to the first 'S' of a word, decrease **Attack** (faster response).

6. Listen on-air or record a short sample and adjust iteratively until the de-essing sounds transparent.

## What each control does

| Control | Kind | Default | Valid range | Mapping | Setting key |
|---|---|---|---|---|---|
| Attack | knob | 1.0 ms | 0.1–30.0 ms | Exponential (`0.1 * 300^n`) | `ClientDeEssTxAttackMs` or `ClientDeEssRxAttackMs` |
| Release | knob | 100 ms | 10.0–500.0 ms | Exponential (`10 * 50^n`) | `ClientDeEssTxReleaseMs` or `ClientDeEssRxReleaseMs` |

These two controls exist only in the frameless strip editors (StripDeEssPanel). The docked ClientDeEssApplet omits them.

## Tips

- For typical SSB voices, **Attack 0.5–2 ms** and **Release 80–150 ms** works well. Very fast speech (e.g. contesting) may need shorter values at both ends.
- The **-6 dB tick** on the gain-reduction bar marks the default Amount level — it's a useful reference for how much the de-esser is actually reducing.
- Attack and Release settings are stored per path (TX and RX) and persist across sessions.

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
