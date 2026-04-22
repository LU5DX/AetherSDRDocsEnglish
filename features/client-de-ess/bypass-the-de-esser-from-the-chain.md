# Bypass the de-esser from the chain

Use this page to disable the de-esser stage so it passes audio through without any sibilance reduction. Bypass is useful when comparing processed and unprocessed TX audio, or when you want to skip de-essing for a specific session without changing your tuned settings.

## Before you start

- The De-Esser stage must already exist in the PooDoo Audio (TXDSP) chain. If you have not added it, see [De-Esser overview](overview.md).
- The DESS sub-container or the CHAIN widget must be visible in the applet panel.

## Steps

1. Locate the **DeEss** stage in the CHAIN widget inside the PooDoo Audio (TXDSP) container.
2. Single-click the **DeEss** stage to toggle bypass on or off.

When the stage is bypassed, `ClientDeEssTxEnabled` is set to `false`. The four tuning knobs, the sidechain response curve, and the gain-reduction bar remain visible but the de-esser applies no attenuation to the TX audio. Your `Freq`, `Q`, `Thresh`, and `Amount` settings are preserved and take effect immediately when you re-enable the stage.

## Tips

- Single-click toggles bypass; double-click opens the floating De-Ess editor. Avoid double-clicking if you only want to bypass.
- The gain-reduction bar in the DESS sub-container will show no movement while the stage is bypassed, which confirms bypass is active.
- Bypassing from the CHAIN widget does not reset any of the four knob values. Re-enabling restores full de-essing using your last saved settings.

## Troubleshooting

- **Single-clicking the DeEss stage does nothing** — Confirm you are clicking the CHAIN widget stage tile, not the DESS sub-container titlebar. Right-clicking the titlebar gives float/pop-out/hide options, not bypass.
- **Gain-reduction bar still shows activity after bypass** — The meter polls at approximately 30 Hz and may show a brief residual reading. If it continues, verify that `ClientDeEssTxEnabled` was actually toggled by re-opening the floating editor via double-click and checking the enable state.

## Related

- [De-Esser overview](overview.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
- [Watch live GR while reading a sibilant phrase](watch-live-gr-while-reading-a-sibilant-phrase.md)
