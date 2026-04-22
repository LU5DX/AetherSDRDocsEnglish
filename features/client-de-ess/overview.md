# De-Esser Overview

The De-Esser reduces harsh sibilance ("S" and "T" sounds) on your TX audio by ducking a narrow frequency band whenever its level exceeds a set threshold. Use it to take the edge off a bright microphone or a room with pronounced high-frequency reflections without coloring the rest of your voice.

## Before you start

- The De-Esser operates on the TX audio path only. It has no effect on received audio.
- The De-Ess stage must be enabled in the CHAIN widget before the applet appears. See [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md) for how to enable and disable it.
- No radio connection is required to view or adjust the De-Esser controls.

## How it works

The De-Esser uses a sidechain architecture. A bandpass filter isolates the frequency range you define with Freq and Q. When the level in that band rises above the Thresh level, the De-Esser attenuates that band by up to the Amount you set. Audio outside the sidechain band is unaffected.

The applet lives in the DESS sub-container inside the PooDoo Audio (TXDSP) parent container. It is hidden until the De-Ess stage is enabled via the CHAIN widget or the floating editor. To open the floating editor, double-click the DeEss stage in the CHAIN widget. To float, pop out, or hide the docked applet, right-click the DESS sub-container titlebar.

The applet displays two visual indicators and four tuning knobs:

- **Sidechain response curve** — draws the bandpass filter shape. A live ball marks the current centre frequency on the curve peak.
- **Gain-reduction bar** — a horizontal soft-red strip that fills from the right to show current attenuation. The scale runs from 0 to 24 dB; a tick marks the −6 dB point. The bar refreshes approximately 30 times per second.

## What each control does

| Control | Default | Valid range | Persisted setting | Description |
|---|---|---|---|---|
| Freq | 6000 Hz | 1000 – 12000 Hz | `ClientDeEssTxFrequencyHz` | Centre frequency of the sibilance band. Uses logarithmic scaling. Displays as "X.X kHz" at or above 1000 Hz. |
| Q | 2.00 | 0.5 – 5.0 | `ClientDeEssTxQ` | Bandwidth of the sibilance band. Higher values produce a narrower band. |
| Thresh | −30.0 dB | −60.0 to 0.0 dB | `ClientDeEssTxThresholdDb` | Level above which attenuation begins. Set this just below your loudest sibilant peaks. |
| Amount | −6.0 dB | −24.0 to 0.0 dB | `ClientDeEssTxAmountDb` | Maximum attenuation applied at peak sibilance. Values are zero or negative because they represent reduction. |

The enabled/disabled state of the De-Ess stage is persisted as `ClientDeEssTxEnabled` and is controlled from the CHAIN widget, not from the applet itself.

## Tips

- Start with Freq at the default 6.0 kHz and sweep it while speaking sibilant phrases. Watch the gain-reduction bar — peak activity indicates you have found the sibilance centre frequency.
- A Q of 2.00 is a reasonable starting point. Narrow the band (increase Q toward 5.0) if the de-esser affects consonants other than sibilants. Widen it (decrease Q toward 0.5) if sibilance still escapes.
- Set Thresh so the gain-reduction bar barely moves on normal speech and reacts clearly on hard "S" sounds. Too low a threshold causes constant gain reduction that dulls the voice.
- Keep Amount at −6.0 dB or shallower for transparent results. Deeper values can produce an audible "lisp" effect if over-applied.

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)
