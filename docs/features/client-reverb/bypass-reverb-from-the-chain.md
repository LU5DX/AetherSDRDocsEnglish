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

## Tips

- Bypassing via the CHAIN widget is non-destructive. Your Size, Decay, Damp, Pre, and Mix values are not reset when the stage is disabled.
- To inspect or adjust knob values while reverb is bypassed, double-click the VERB stage to open the floating "Aetherial FreeVerb — TX" editor. Changes made there take effect the next time the stage is enabled.

## Related

- [Aetherial FreeVerb overview](overview.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
