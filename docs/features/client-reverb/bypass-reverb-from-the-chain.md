# Bypass reverb from the chain

Disabling the reverb stage removes the Aetherial FreeVerb processing from the TX audio chain without changing any of the knob values. Use this when you want a dry transmission but intend to re-enable reverb later with the same settings intact.

## Before you start

- The Aetherial Audio (TXDSP) container must be visible in the applet panel.
- The VERB stage must already appear in the CHAIN widget. If the reverb stage has never been enabled, it will not yet be present in the chain.

## Steps

1. Locate the CHAIN widget inside the Aetherial Audio (TXDSP) container in the applet panel.
2. Single-click the VERB stage in the CHAIN widget to toggle it off.

The VERB stage indicator changes to show it is inactive. The "Aetherial FreeVerb" sub-container hides, and the TX audio path passes through without reverb processing. All five knob values (`ClientReverbTxSize`, `ClientReverbTxDecayS`, `ClientReverbTxDamping`, `ClientReverbTxPreDelayMs`, `ClientReverbTxMix`) are preserved.

To re-enable reverb, single-click the VERB stage again. The sub-container reappears and processing resumes with the previously saved settings.

## Live reverb visualisation

Starting in v0.9.7, the Aetherial FreeVerb applet includes a compact live visualisation panel (90 px tall) that updates in real time as you adjust the knobs. It is displayed directly inside the "Aetherial FreeVerb — TX" editor above the knob row and requires no configuration.

The visualisation shows three overlaid elements against a dark background:

| Element | Colour | What it represents |
|---|---|---|
| Dry sine packet | Cyan | The unprocessed signal. Fades toward the right as Mix increases. |
| First-order reflections | Yellow | Early reflections. Spacing and count respond to Size; amplitude decay responds to Damp. |
| Reverberant tail | Magenta | The full reverb tail. Length follows Decay; high-frequency roll-off follows Damp; onset position follows Pre. |

All five knobs feed the visualisation directly. Changes to Size, Decay, Damp, Pre, or Mix are reflected immediately — you do not need to transmit to see the effect.

## Tips

- Bypassing via the CHAIN widget is non-destructive. Your Size, Decay, Damp, Pre, and Mix values are not reset when the stage is disabled.
- To inspect or adjust knob values while reverb is bypassed, double-click the VERB stage to open the floating "Aetherial FreeVerb — TX" editor. Changes made there take effect the next time the stage is enabled.
- Use the live visualisation to set Decay and Mix before going on air. A short Decay (0.3–1.2 s) with a low Mix (10–15 %) keeps voice intelligible.

## Related

- [Aetherial FreeVerb overview](overview.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)