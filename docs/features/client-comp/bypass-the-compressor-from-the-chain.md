# Bypass the Compressor from the Chain

The CHAIN widget controls whether the compressor stage is active or bypassed. Use it to take the compressor out of the TX signal path without changing any of its settings.

## Before you start

- AetherSDR must be open with the PooDoo Audio (TXDSP) parent container visible.
- The COMPRESSOR sub-container tile is only shown when the compressor stage is enabled (bypass off). While bypassed, the tile hides automatically.

## Steps

1. Locate the CHAIN widget inside the PooDoo Audio (TXDSP) parent container.
2. Single-click the Comp stage in the CHAIN widget to toggle the compressor bypass on or off.

When bypass is off, `ClientCompTxEnabled` is set to true and the COMPRESSOR sub-container tile becomes visible. When bypass is on, `ClientCompTxEnabled` is set to false and the tile hides.

## Tips

- Your threshold, ratio, attack, release, and makeup settings are preserved when you bypass. Re-enabling restores the compressor exactly as you left it.
- To open the full editor for knee and limiter controls, double-click the Comp stage in the CHAIN widget rather than single-clicking it.

## Related

- [Compressor overview](overview.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)
- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
