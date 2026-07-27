# Aetherial De-Esser

The Aetherial De-Esser tames harsh 'S' and 'T' sibilance by ducking a narrow band when it exceeds a sidechain threshold. It uses split-band processing: only the sibilant bandpass output is attenuated, leaving lows and mids untouched. This fixes the broadband-attenuation bug that previously caused approximately 30 W of TX power loss. The panel shows the sidechain bandpass response, a 24 dB gain-reduction meter, six tuning knobs (Freq, Q, Thresh, Amount, Attack, Release), and a user-selectable cascade slope (12/24/36/48 dB/oct).

**Applet instances:**
- **TX instance**: "Aetherial De-Esser" (shown in the docked Applet Panel)
- **RX instance**: "Aetherial De-Esser — RX" (reachable through the Aetherial Audio Channel Strip)

## Before you start

- AetherSDR must be open and the Aetherial Audio (TXDSP or RXDSP) processing chain must be visible.
- The DESS stage must already exist in the CHAIN widget. If the de-esser has never been enabled, the DESS stage may not be present.
- The de-esser is available on both TX and RX audio paths. Each path has its own independent instance of the Aetherial De-Esser.

## Bypass the de-esser from the chain

Remove the Aetherial De-Esser from your TX or RX audio path without changing any of its settings. Bypassing is useful when you want to compare treated and untreated audio, or temporarily disable de-essing for a particular session.

### Steps for TX de-esser bypass

1. Locate the CHAIN widget in the Aetherial Audio (TXDSP) container.
2. Find the **DESS** stage in the chain.
3. Single-click the **DESS** stage to toggle bypass on or off.

### Steps for RX de-esser bypass

1. Locate the CHAIN widget in the Aetherial Audio (RXDSP) container.
2. Find the **DESS** stage in the chain.
3. Single-click the **DESS** stage to toggle bypass on or off.

When bypassed, the entire de-esser tile renders at reduced opacity (55% of normal). Single-clicking again re-enables it and restores the tile to full opacity. The `ClientDeEssTxEnabled` and `ClientDeEssRxEnabled` settings are updated immediately.

## Opening the de-esser settings panel

The de-esser settings panel has two instances:
- **TX instance**: "Aetherial De-Esser — TX" (accessible from the Aetherial Audio Channel Strip's TX path)
- **RX instance**: "Aetherial De-Esser — RX" (accessible from the Aetherial Audio Channel Strip's RX path)

To open the appropriate instance:
1. Open the Aetherial Audio Channel Strip.
2. Click the **DESS** stage to open the de-esser settings panel for that path (TX or RX).
3. The panel title bar shows either "Aetherial De-Esser — TX" or "Aetherial De-Esser — RX" depending on which path you accessed.

## De-esser controls

The Aetherial De-Esser panel contains the following controls:

| Label                    | Kind        | Default              |
|--------------------------|-------------|----------------------|
| Sidechain response curve | indicator   | —                    |
| Gain-reduction bar       | meter       | —                    |
| Freq                     | knob        | 6000 Hz              |
| Q                        | knob        | 2.00                 |
| Thresh                   | knob        | -30.0 dB             |
| Amount                   | knob        | -6.0 dB              |
| Attack                   | knob        | 1.0 ms               |
| Release                  | knob        | 100 ms               |
| Slope                    | push_button | 24 dB/oct (2 stages) |

### Control details

- **Freq** (logarithmic mapping, 1000 to 12000 Hz): Sets the centre frequency of the sibilance band. Labels show "6.0 kHz" above 1 kHz, "N Hz" below.
- **Q** (linear mapping, 0.5 to 5.0): Sets the bandwidth of the sibilance band — higher Q equals narrower bandwidth. Labels show "X.XX".
- **Thresh** (linear mapping, -60.0 to 0.0 dB): Level above which the de-esser starts attenuating the band.
- **Amount** (linear mapping, -24.0 to 0.0 dB): Maximum attenuation applied at peak sibilance. Values are negative (or zero) because they represent reduction.
- **Attack** (exponential mapping, 0.1 to 30.0 ms): Sets how quickly the de-esser responds once sibilance crosses the threshold. Present in the Channel Strip StripDeEssPanel (RX and TX). The docked ClientDeEssApplet omits this knob.
- **Release** (exponential mapping, 10.0 to 500.0 ms): Sets how quickly gain returns after sibilance drops below the threshold. Present in the Channel Strip StripDeEssPanel (RX and TX). The docked ClientDeEssApplet omits this knob.
- **Slope** (cycles through 12/24/36/48 dB/oct): Sets the sidechain bandpass cascade count. Each stage adds 12 dB/oct of rolloff outside the sibilant band. Higher slope equals narrower effective notch, less mid-band collateral on Ess-heavy phrases. Present in the floating StripDeEssPanel (left column, bottom). Label shows "N dB/oct". Present for both TX and RX paths. Persisted as `ClientDeEssTxSlopeStages` / `ClientDeEssRxSlopeStages`.

## Indicators

| Label | States | Meaning |
|---|---|---|
| Centre-frequency ball | resting on curve peak | Marks the currently-tuned sibilance centre frequency on the response curve. |
| Gain-reduction strip | empty, soft-red fill | Current attenuation applied to the sibilance band. The meter is a horizontal soft-red strip, right-filled. Scale maxes at 24 dB; a tick marks the -6 dB typical amount. Refreshed at approximately 30 Hz. |

## Inline value editing on knobs

The de-esser knobs (Freq, Q, Thresh, Amount, Attack, Release) support inline value editing. Instead of dragging the knob, you can type a value directly.

### To edit a knob value using inline editing

1. Click the value text below any de-esser knob. A small text field appears, outlined in cyan when focused.
2. Type the new value. You can include units (e.g., "6 kHz", "-24.0 dB", "100 ms") or just the number (e.g., "6000", "2.0", "0.1").
3. Press **Enter** or click anywhere else on the panel to commit the value.
4. To cancel editing, press **Escape** — the previous value is restored.

The value is automatically clamped to the knob's valid range. Locale-aware parsing is supported (e.g., "12,5" works in comma-decimal locales).

## Theming and knob colors

In v26.6.1, the knob component colors are now sourced from the theme manager's `color.knob.*` namespace:
- `color.knob.background` — the knob ring background
- `color.knob.foreground` — the knob value arc
- `color.knob.handle` — the knob pointer indicator

The de-esser applet container is registered as `applet/deess`, which allows per-applet container overrides (e.g., the de-esser can have an amber knob foreground while other applets use a different color). Label and value text below the knob continue to use `color.text.secondary` and `color.text.primary` respectively.

The sidechain response curve widget also sources its colors from theme keys:
- `color.background.0` — curve background
- `color.background.1` — grid lines
- `color.text.label` — axis labels
- `color.accent.danger` — the sibilant band curve (soft red)
- `color.accent.dim` — threshold indicator line

## Tips

- Bypassing does not reset any knob values. Freq, Q, Thresh, Amount, Attack, Release, and Slope all retain their current settings when you re-enable the stage.
- The TX and RX de-esser instances are independent. Changing settings on one does not affect the other.
- The sidechain response curve and gain-reduction meter reflect the currently active instance (TX or RX) in the panel title bar.
- You can use inline value editing to enter exact values without dragging knobs. This is especially useful for fine-tuning or when you know the precise setting you need.
- The Slope button cycles through 12 → 24 → 36 → 48 dB/oct when clicked. Use a steeper slope for narrower filtering around the sibilant frequency to reduce collateral attenuation on mid-range speech.
- The de-esser container (`applet/deess`) allows theme authors to customize knob colors specifically for the de-esser panel without affecting other comp knobs.
- In v26.7.4, the gain-reduction meter updates on every frame for smoother visual response during fast sibilance transients, at the cost of slightly higher CPU usage during dynamic passages.

## Related

- [Aetherial De-Esser overview](overview.md)
- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)