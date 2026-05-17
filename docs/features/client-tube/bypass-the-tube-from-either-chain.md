# Bypass the tube from either chain

Use this procedure to enable or disable the tube saturator on the TX chain, the RX chain, or both, without changing any of the tuning knobs. Bypassing lets you compare the processed and unprocessed signal instantly and leaves all settings intact.

## Before you start

- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel. The "Aetherial Mic-PreAmp" (TX) and "Aetherial Dynamic Tube" (RX) sub-containers appear inside it.
- The TUBE stage must be present in the relevant CHAIN widget. Bypass is controlled by a single click on the TUBE stage in the CHAIN widget for the matching side.

## Steps

1. Locate the CHAIN widget for the side you want to change — TX or RX.
2. Single-click the **TUBE** stage in that CHAIN widget to toggle bypass on or off.
   - When the tube is active, the stage appears lit.
   - When bypassed, the stage appears unlit and the signal passes through unprocessed.
3. Repeat on the other side's CHAIN widget if you also want to bypass that chain.

The bypass state is persisted immediately. TX state is saved to `ClientTubeTxEnabled`; RX state is saved to `ClientTubeRxEnabled`.

## What each control does

| Control | What it does | Default | Persisted key |
|---|---|---|---|
| TUBE stage (TX) — single click | Toggles the TX tube saturator in or out of the signal chain | — | `ClientTubeTxEnabled` |
| TUBE stage (RX) — single click | Toggles the RX tube saturator in or out of the signal chain | — | `ClientTubeRxEnabled` |

## Tips

- Double-clicking the TUBE stage in the CHAIN widget opens the floating editor ("Aetherial Tube — TX" or "Aetherial Tube — RX") instead of toggling bypass. Use a single click for bypass only.
- All knob values (Drive, Tone, Bias, Output, Dry/Wet, Envelope, Attack, Release) are unaffected by bypass. You can re-enable the tube at any time and the previous settings are restored.
- When the tube stage is bypassed, the entire docked applet tile dims to approximately 55 % opacity. This matches the dim effect used by the EQ curve tile and gives a clear at-a-glance indication that processing is inactive. The tile returns to full opacity as soon as bypass is turned off.
- The transfer curve and live input ball in the applet tile continue to reflect the current knob positions even while bypassed.
- The floating editor includes an **Output level meter** (labelled **OUT**) on the far right. It shows post-saturation peak level with fast-attack/slow-release ballistics and is colour-coded: green (−60 to −12 dB), lime (−12 to −6 dB), amber (−6 to −3 dB), and red (above −3 dB). The meter is not visible in the docked applet tile.
- Each knob supports inline value editing. Click a knob's value label in the floating editor to open a QLineEdit overlay. Type a value and press Enter or click elsewhere to commit. The value is clamped to the knob's valid range. Press Escape to cancel without changing the value.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Parallel-blend saturation with Dry/Wet](parallel-blend-saturation-with-mix.md)