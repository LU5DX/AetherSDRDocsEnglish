# Dial in a subtle Mix — 10-15 % is typical for voice

The Mix knob controls the dry/wet balance of the Aetherial FreeVerb reverb on your transmitted audio. Keeping Mix in the 10–15 % range adds a light sense of space without making your voice sound processed or distant.

## Before you start

- The Reverb stage must be enabled in the CHAIN widget. The "Aetherial FreeVerb" sub-container is hidden until the stage is active.
- You can adjust Mix from either the compact applet row inside the Aetherial Audio (TXDSP) container or from the floating "Aetherial FreeVerb — TX" editor.

## Steps

1. Open the floating editor by double-clicking the VERB stage in the CHAIN widget. The editor titled "Aetherial FreeVerb — TX" appears.
2. Locate the Mix knob — the rightmost of the five knobs in the editor row.
3. Turn Mix to your target value. The knob label updates in real time, displayed as a percentage (for example, `15 %`).
4. For voice, set Mix between 10 % and 15 %. Lower values blend in less reverb tail; higher values make the effect more prominent.
5. Close the editor or leave it open. The value is saved immediately.

## What each control does

| Label | Default | Valid range | Persisted key | Behavior |
|-------|---------|-------------|---------------|----------|
| Mix | 15 % | 0–100 % (0.0 to 1.0) | `ClientReverbTxMix` | Linear dry/wet balance. Higher values increase the proportion of reverb tail in the transmitted signal. |
| Size | 50 % | 0–100 % (0.0 to 1.0) | `ClientReverbTxSize` | Models the room size. |
| Decay | 1.20 s | 0.3 to 5.0 s | `ClientReverbTxDecayS` | Sets the reverb tail length (exponential mapping). |
| Damp | 50 % | 0–100 % (0.0 to 1.0) | `ClientReverbTxDamping` | Higher values damp high frequencies faster in the tail. |
| Pre | 20 ms | 0 to 100 ms | `ClientReverbTxPreDelayMs` | Pre-delay between the dry signal and the first reflections. |

## Tips

- The default Mix value is 15 %, which is already within the typical voice range. If you reset the knob to default, it returns to 15 %.
- Both the compact applet knob and the floating editor knob stay in sync. Changes made in one are reflected in the other within approximately 33 ms.
- Mix at 0 % passes only dry signal; the reverb stage is still active but inaudible. To remove it from the processing chain entirely, see [Bypass reverb from the chain](bypass-reverb-from-the-chain.md).

## Related

- [Aetherial FreeVerb overview](overview.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Reduce the high-end sparkle of the tail with Damp](reduce-the-high-end-sparkle-of-the-tail-with-damp.md)
- [Offset reflections from the dry signal with Pre](offset-reflections-from-the-dry-signal-with-pre.md)
