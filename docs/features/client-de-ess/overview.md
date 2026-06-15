# Aetherial De-Esser overview

The Aetherial De-Esser is a client-side processor available in both TX and RX instances. It reduces harsh sibilance ("S" and "T" sounds) by monitoring a narrow frequency band and ducking it when the signal level in that band exceeds a set threshold.

## Before you start

- The de-esser is available as a standalone docked applet (TX only, labeled "Aetherial De-Esser") and through the Aetherial Audio Channel Strip (RX and TX).
- The docked applet is hidden until the De-Ess stage is enabled. Enable it via the CHAIN widget inside the Aetherial Audio (TXDSP) parent container.
- To open the RX instance, use the **Aetherial Audio Channel Strip** icon for the receive channel, then click the De-Ess stage. The panel opens with the title "Aetherial De-Esser — RX".
- No radio connection is required to configure the de-esser.

## How it works

The de-esser uses a sidechain design. A bandpass filter isolates the sibilance band defined by **Freq** and **Q**. When the level in that band exceeds the **Thresh** value, the de-esser attenuates the band by up to the **Amount** value. The rest of your audio passes through unaffected.

The panel displays two live indicators while audio is active:

- **Sidechain response curve** — shows the bandpass filter shape with a ball marker at the current centre frequency. As you adjust **Freq** and **Q**, the curve and ball update immediately. Frequency axis labels (100, 500, 1k, 2k, 4k, 8k, 12k) are rendered using cached text for performance.
- **Gain-reduction bar** — a horizontal soft-red strip that fills from the right to show how much attenuation is being applied at any moment. The scale runs from 0 to 24 dB; a tick marks the −6 dB point. The meter refreshes approximately 30 times per second.

When the de-esser stage is bypassed, the entire panel renders at reduced opacity (approximately 55%) to give a clear visual indication that the stage is inactive. To bypass or re-enable the de-esser, use the single-click gesture on the DESS stage in the CHAIN widget.

## TX and RX instances

The de-esser has separate instances for transmit and receive:

| Instance | How to access | Title bar label |
|---|---|---|
| TX (docked applet) | Click the De-Esser icon in the Applet Panel | "Aetherial De-Esser" |
| TX (channel strip) | Open the TX channel strip, click De-Ess stage | "Aetherial De-Esser — TX" |
| RX (channel strip) | Open the RX channel strip, click De-Ess stage | "Aetherial De-Esser — RX" |

Each instance maintains independent settings for Freq, Q, Thresh, Amount, Attack, Release, and Slope. The docked applet omits Attack and Release knobs.

## What each control does

| Control     | Default      | Valid range          | Setting key (TX)         | Behavior |
|-------------|--------------|----------------------|--------------------------|----------|
| **Freq**    | 6000 Hz      | 1000 – 12000 Hz      | `ClientDeEssTxFrequencyHz` | Logarithmic mapping. Sets the centre frequency of the sibilance band. |
| **Q**       | 2.00         | 0.5 – 5.0            | `ClientDeEssTxQ`         | Linear mapping. Sets the bandwidth of the sibilance band — higher Q = narrower. |
| **Thresh**  | −30.0 dB     | −60.0 to 0.0 dB      | `ClientDeEssTxThresholdDb` | Linear mapping. Level above which the de-esser starts attenuating the band. |
| **Amount**  | −6.0 dB      | −24.0 to 0.0 dB      | `ClientDeEssTxAmountDb`  | Linear mapping. Maximum attenuation applied at peak sibilance. Values are negative (or zero) because they represent reduction. |
| **Attack**  | 1.0 ms       | 0.1 to 30.0 ms       | `ClientDeEssTxAttackMs`  | Exponential mapping. Sets how quickly the de-esser responds once sibilance crosses the threshold. Present in the Channel Strip StripDeEssPanel (RX and TX). The docked ClientDeEssApplet omits this knob. |
| **Release** | 100 ms       | 10.0 to 500.0 ms     | `ClientDeEssTxReleaseMs` | Exponential mapping. Sets how quickly gain returns after sibilance drops below the threshold. Present in the Channel Strip StripDeEssPanel (RX and TX). The docked ClientDeEssApplet omits this knob. |
| **Slope**   | 24 dB/oct (2 stages) | 12 / 24 / 36 / 48 dB/oct (1 to 4 stages) | `ClientDeEssTxSlopeStages` | Cycles the sidechain bandpass cascade count. Each stage adds 12 dB/oct of rolloff outside the sibilant band. Higher slope = narrower effective notch, less mid-band collateral on Ess-heavy phrases. Present in the floating StripDeEssPanel (left column, bottom). Label shows 'N dB/oct'. |

### Inline value editing

Each knob supports inline value editing. Click the displayed value text to open a small text entry field. Type a new value and press **Enter** or click outside the field to commit. The value is automatically clamped to the knob's valid range. Press **Escape** to cancel the edit and revert to the previous value. This feature works the same way in the docked applet and the channel strip panels.

## Slope button

The **Slope** button in the Channel Strip panel lets you adjust the sidechain filter steepness:

- Click the button to cycle through 12 → 24 → 36 → 48 dB/oct (1 to 4 cascaded bandpass biquads).
- Each click increases the rolloff by 12 dB/oct outside the sibilant band.
- Higher slope values create a narrower notch around the centre frequency, reducing collateral attenuation of mid-range speech.
- The button label updates to show the current setting (e.g., "24 dB/oct").
- The sidechain response curve updates to reflect the new slope.
- Slope setting persists independently for TX and RX paths.

## Settings persistence

Each instance saves and restores its control values from the settings database:

| Setting key | Purpose |
|---|---|
| `ClientDeEssTxFrequencyHz` | TX centre frequency |
| `ClientDeEssTxQ` | TX bandwidth factor |
| `ClientDeEssTxThresholdDb` | TX sidechain threshold |
| `ClientDeEssTxAmountDb` | TX maximum attenuation |
| `ClientDeEssTxAttackMs` | TX attack time |
| `ClientDeEssTxReleaseMs` | TX release time |
| `ClientDeEssTxSlopeStages` | TX slope stage count |
| `ClientDeEssTxEnabled` | TX enabled state |

RX settings use a parallel key set (`ClientDeEssRx*`). Settings are saved when you adjust any knob or close the panel.

## Theming

The de-esser panel and its knobs use the application theme system. Knob colors (background ring, foreground arc, pointer handle, label text, value text) are drawn from theme color keys:

- `color.knob.background` — knob background ring
- `color.knob.foreground` — knob value arc
- `color.knob.handle` — knob pointer line
- `color.text.secondary` — knob label text
- `color.text.primary` — knob value text

The sidechain response curve also uses theme colors:

- `color.background.0` — curve widget background
- `color.background.1` — grid lines and major grid lines
- `color.text.label` — axis labels
- `color.accent.danger` — sibilant band curve (soft red)
- `color.accent.dim` — threshold/marker lines
- `color.accent.warning` — centre-frequency ball glow
- `color.text.primary` — centre-frequency ball core

The docked applet container is registered with the theme as `applet/deess`, allowing per-applet color overrides when defined by the active theme.

## Tips

- Start with **Freq** at the default 6.0 kHz and sweep it slowly while speaking sibilant words. Watch the gain-reduction bar — maximum deflection indicates you have found the peak sibilance frequency.
- A **Q** of 2.00 is a reasonable starting point. Increase it to isolate a narrow problem band; decrease it if the sibilance is spread across a wider range.
- Set **Thresh** so the gain-reduction bar only moves on genuine "S" and "T" sounds, not on normal vowels or consonants.
- The −6 dB tick on the gain-reduction bar marks the default **Amount** value. Keeping reduction near that tick usually produces transparent results. Larger amounts are available but can make the effect audible as pumping or lisping.
- Use the **Slope** button to fine-tune the filter steepness. Start with 24 dB/oct and increase if you hear too much mid-range attenuation on sibilant-heavy phrases.
- Use different settings for TX and RX — you may need more aggressive de-essing on receive than on transmit, or vice versa.
- When the stage is bypassed, the panel dims noticeably. If the panel appears dim and you are not hearing de-essing, check that the DESS stage is not bypassed in the CHAIN widget.

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)