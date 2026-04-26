# Aetherial De-Esser overview

The Aetherial De-Esser is a TX-only client-side processor that reduces harsh sibilance ("S" and "T" sounds) in your transmitted audio. It works by monitoring a narrow frequency band and ducking it when the signal level in that band exceeds a set threshold.

## Before you start

- The De-Esser is a TX-only stage. It has no effect on received audio.
- The applet is hidden until the De-Ess stage is enabled. Enable it via the CHAIN widget inside the Aetherial Audio (TXDSP) parent container, or from the floating editor.
- No radio connection is required to configure the de-esser.

## How it works

The de-esser uses a sidechain design. A bandpass filter isolates the sibilance band defined by **Freq** and **Q**. When the level in that band exceeds the **Thresh** value, the de-esser attenuates the band by up to the **Amount** value. The rest of your audio passes through unaffected.

The applet displays two live indicators while you transmit:

- **Sidechain response curve** — shows the bandpass filter shape with a ball marker at the current centre frequency. As you adjust **Freq** and **Q**, the curve and ball update immediately.
- **Gain-reduction bar** — a horizontal soft-red strip that fills from the right to show how much attenuation is being applied at any moment. The scale runs from 0 to 24 dB; a tick marks the −6 dB point. The meter refreshes approximately 30 times per second.

To open the full floating editor, double-click the DESS stage in the CHAIN widget. The editor window is titled "Aetherial De-Esser — TX". To bypass the de-esser without changing any settings, use the single-click gesture on the DESS stage in the CHAIN widget.

## What each control does

| Control | Default | Valid range | Persisted setting | Description |
|---|---|---|---|---|
| **Freq** | 6000 Hz | 1000 – 12000 Hz | `ClientDeEssTxFrequencyHz` | Centre frequency of the sibilance band. Uses logarithmic scaling. Displays as "X.X kHz" at or above 1000 Hz. |
| **Q** | 2.00 | 0.5 – 5.0 | `ClientDeEssTxQ` | Bandwidth of the sibilance band. Higher values produce a narrower band. Uses linear scaling. |
| **Thresh** | −30.0 dB | −60.0 to 0.0 dB | `ClientDeEssTxThresholdDb` | Level above which the de-esser begins attenuating the band. Set this just below your loudest sibilant peaks. |
| **Amount** | −6.0 dB | −24.0 to 0.0 dB | `ClientDeEssTxAmountDb` | Maximum attenuation applied when sibilance is at its peak. Negative values represent reduction; 0 dB means no attenuation. |
| **Sidechain response curve** | — | — | — | Live display of the bandpass filter shape. The ball marks the current centre frequency. |
| **Gain-reduction bar** | — | 0 – 24 dB GR | — | Live meter showing current attenuation. Soft-red fill; tick at −6 dB. |

Enabled state is persisted as `ClientDeEssTxEnabled`.

## Tips

- Start with **Freq** at the default 6.0 kHz and sweep it slowly while speaking sibilant words. Watch the gain-reduction bar — maximum deflection indicates you have found the peak sibilance frequency.
- A **Q** of 2.00 is a reasonable starting point. Increase it to isolate a narrow problem band; decrease it if the sibilance is spread across a wider range.
- Set **Thresh** so the gain-reduction bar only moves on genuine "S" and "T" sounds, not on normal vowels or consonants.
- The −6 dB tick on the gain-reduction bar marks the default **Amount** value. Keeping reduction near that tick usually produces transparent results. Larger amounts are available but can make the effect audible as pumping or lisping.

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)
