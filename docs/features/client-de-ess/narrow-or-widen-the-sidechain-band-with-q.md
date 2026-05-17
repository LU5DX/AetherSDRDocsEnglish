# Narrow or widen the sidechain band with Q

The Q knob controls how wide or narrow the sidechain bandpass filter is around the sibilance centre frequency. A higher Q focuses attenuation on a tighter slice of the spectrum; a lower Q affects a broader band. Adjust Q after locating the sibilance peak with Freq so the de-esser targets exactly the right content without dulling nearby consonants.

## Before you start

- The Aetherial De-Esser (DESS) stage must be enabled and visible. It appears as a sub-container inside the Aetherial Audio (TXDSP) parent container.
- If the applet is not visible, open the Aetherial Audio Channel Strip, which hosts the de-esser controls directly. The separate "Aetherial De-Esser — TX" floating editor no longer exists.
- To bypass the de-esser, single-click the DESS stage in the CHAIN widget. When bypassed, the entire applet tile dims to approximately 55 % opacity as a visual indicator.
- Set the centre frequency with Freq before fine-tuning Q. See [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md).
- The de-esser is available in two side-specific instances: TX (for transmitted audio) and RX (for received audio). The TX version is labeled "Aetherial De-Esser" and the RX version "Aetherial De-Esser — RX". Both share identical controls and behaviour. The RX instance is reachable through the Aetherial Audio Channel Strip.

## Steps

1. Open the Aetherial De-Esser applet inside the Aetherial Audio Channel Strip. Use **showForTx()** to access the TX instance or **showForRx()** to access the RX instance.
2. Locate the **Q** knob in the four-knob tuning row.
3. Rotate **Q** clockwise to increase the value and narrow the sidechain band, or counter-clockwise to decrease the value and widen it.
4. Watch the sidechain response curve — the bandpass peak broadens or sharpens as Q changes.
5. While transmitting or speaking a sibilant phrase, observe the gain-reduction bar to confirm the de-esser is still triggering at the adjusted bandwidth. See [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md).

## What each control does

| Control                  | Default | Valid range     | Behaviour                                                                                               |
|--------------------------|---------|-----------------|---------------------------------------------------------------------------------------------------------|
| **Q**                    | 2.00    | 0.5 to 5.0      | Linear mapping. Sets the bandwidth of the sibilance band — higher Q = narrower. Label 'X.XX'.           |
| Sidechain response curve | —       | —               | Compact-mode bandpass response. Draws the bandpass filter response with a live ball at the current centre frequency. Axis labels (100, 500, 1k, etc.) are rendered using QStaticText for improved performance. |
| Gain-reduction bar       | —       | 0 to 24 dB GR   | Horizontal soft-red strip, right-filled. Scale maxes at 24 dB; a tick marks the -6 dB typical amount. Refreshed ~30 Hz. |
| Attack                   | 1.0 ms  | 0.1 to 30.0 ms  | Exponential mapping (0.1 * 300^n). Sets how quickly the de-esser responds once sibilance crosses the threshold. Present in both TX and RX Channel Strip instances. The docked ClientDeEssApplet omits this knob. |
| Release                  | 100 ms  | 10.0 to 500.0 ms | Exponential mapping (10 * 50^n). Sets how quickly gain returns after sibilance drops below the threshold. Present in both TX and RX Channel Strip instances. The docked ClientDeEssApplet omits this knob. |

## Value entry via inline text editor

As of v26.5.2.1, all knobs in the Aetherial De-Esser support direct numeric entry through an inline text editor:

1. **Activate the editor**: Click any knob's current value text. The value area gains focus and a subtle dark inset with a cyan border appears, indicating edit mode.
2. **Enter a value**: Type the desired numeric value. The editor accepts locale-aware decimal formats (e.g., "12,5" in comma-decimal locales) and tolerates extra characters such as unit labels (e.g., "2.00" or "2.00 ms").
3. **Commit the value**: Press **Enter** or click anywhere outside the editor. The value is clamped to the knob's valid range and applied immediately.
4. **Cancel**: Press **Escape** to revert to the previous value without committing.

This feature provides precise, one-step adjustment without rotating the knob, especially useful for recalling saved settings or matching a known value.

## Bypass dimming

When the DESS stage is bypassed via a single-click in the CHAIN widget, the entire applet tile renders at reduced opacity (approximately 55 %). This matches the dim behaviour used on the EQ curve and gives a clear at-a-glance indication that the stage is inactive. Click the DESS stage again in the CHAIN widget to re-enable it and restore full opacity.

## Tips

- Start at the default of 2.00 and increase Q only if attenuation is spilling onto vowels or other consonants adjacent to the sibilance band.
- Very high Q values (above 4.0) can make the de-esser miss slightly off-centre sibilants. If GR stops triggering reliably, lower Q slightly or re-sweep Freq.
- The response curve gives immediate visual feedback — use it to judge whether the bell is too broad or too sharp before committing to a setting.
- Settings are saved independently for TX and RX instances via separate setting keys: `ClientDeEssTxQ` for TX and `ClientDeEssRxQ` for RX.
- Use the inline value editor (click the current value) for precise numeric entry when you know the exact Q you need.

## Related

- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
- [Bypass the de-esser from the chain](bypass-the-de-esser-from-the-chain.md)