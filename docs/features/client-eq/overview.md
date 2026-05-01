# Aetherial Parametric EQ (TX / RX) overview

The Aetherial Parametric EQ provides client-side parametric equalization for both your transmit and receive audio paths. Use it to shape your TX microphone audio or to tailor the sound of received audio before it reaches your speakers or headphones, without touching any radio-side processing.

## Before you start

- AetherSDR must be running. A radio connection is not required to configure the EQ, but a connection is needed for the live FFT analyzer overlay to show real audio.
- The EQ applet tiles are hidden until the matching EQ stage is enabled via the CHAIN widget or the floating editor. If you do not see "Aetherial TX EQ" or "Aetherial RX EQ" in the Aetherial Audio (TXDSP) parent container, enable the EQ stage first.

## How it works

AetherSDR instantiates two separate EQ tiles inside the Aetherial Audio (TXDSP) parent container:

- **Aetherial TX EQ** — processes audio on the transmit path only.
- **Aetherial RX EQ** — processes audio on the receive path only.

Each tile is fixed to its path. There is no in-tile RX/TX selector. The tile shows a compact view of the summed EQ response curve and a live FFT analyzer overlay for that path. A peak-hold trace is drawn on top of the live analyzer, showing the per-frequency maximum level seen since the last reset; the trace decays at approximately 10 dB/sec during normal operation. Editing — adding, removing, and tuning bands — happens in a separate floating window called the **Aetherial Parametric EQ** editor, which opens from the CHAIN widget. The editor's title bar reads either "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX" depending on which side you opened it from. One shared editor instance is reused for both sides; the title flips when you switch sides.

### Applet tile

Each tile contains one control area:

| Element | Description |
|---|---|
| Analyzer / curve area | A minimum 80 px tall view showing the summed EQ response curve for all enabled bands on that path, with a live FFT analyzer overlay and a peak-hold trace. This area is view-only in the applet tile. |

The **summed EQ response** displays the cumulative frequency response of all enabled bands. When no bands are boosted or cut, the curve is flat; it dims to grey when the EQ stage is bypassed. The **live analyzer overlay** shows the real-time FFT of audio passing through that path as a cyan gradient fill; it is idle when no audio is active and running when audio is present. The **peak-hold trace** is a soft off-white line that tracks the per-frequency maximum energy observed, helping you identify resonances and harsh peaks while tuning. The trace decays at approximately 10 dB/sec between updates. It can be frozen from the floating editor using the Peak Hold button.

### Floating editor

Double-clicking the EQ stage in the CHAIN widget opens the floating editor for that side. The editor provides:

| Control | Description |
|---|---|
| Analyzer / curve area (canvas) | Interactive canvas where you drag band handles to set frequency and gain. Drag peak/shelf handles to adjust frequency and gain. Drag HP/LP handles to adjust frequency and Q. Hold Shift while dragging to adjust Q on any band type. Click a band icon to cycle through filter types. The peak-hold trace is visible here as well and reflects the frozen/decaying state set by the Peak Hold button. |
| Peak Hold | Checkable button in the editor header strip. When checked, the analyzer's per-bin peak-hold trace stops decaying — every frequency's highest observed level is held until you toggle the button off. The button shows an amber background when checked. Toggle off to resume normal decay at approximately 10 dB/sec. |
| Filter family | Combo box in the editor header strip. Selects the filter family applied to HP/LP cascade math. Options: Butterworth (maximally flat passband), Chebyshev (steeper transition, 1 dB passband ripple), Bessel (linear phase, gentler rolloff), Elliptic (steepest transition, ripple in both bands). Default: Butterworth. Shelves and peaks use their native second-order topology regardless of this setting. Persisted separately per path: `ClientEqTxFilterFamily` / `ClientEqRxFilterFamily`. |
| Reset | Push button in the editor header strip. Drops every band back to default values, restores the default 10-band count, and resets the filter family to Butterworth. Saves immediately. Tooltip: "Reset all bands to default values". |
| Output Fader | Vertical combined fader + level meter on the right edge of the floating editor. Drag to set post-EQ master gain; scroll wheel adjusts in 0.5 dB steps; double-click resets to 0 dB. Range: -36 to +12 dB. The level bar behind the handle shows the smoothed post-EQ peak in real time with the same green-amber-red gradient as the Tube level meter. Located in the floating editor only — not in the docked applet tile. |

Bypass is handled from the CHAIN widget, not from inside the editor. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md).

### Persisted settings

| Setting key | What it stores | Notes |
|---|---|---|
| `ClientEqRxEnabled` | Whether the RX EQ stage is enabled. | |
| `ClientEqTxEnabled` | Whether the TX EQ stage is enabled. | |
| `ClientEqRxBands` | Band parameters for the RX EQ. | |
| `ClientEqTxBands` | Band parameters for the TX EQ. | |
| `ClientEqTxFilterFamily` | Filter family selection for the TX EQ. | Persisted per path alongside `ClientEqRxFilterFamily`. |
| `ClientEqRxFilterFamily` | Filter family selection for the RX EQ. | Persisted per path alongside `ClientEqTxFilterFamily`. |
| `ClientEqTxMasterGain` | Post-EQ output master gain for the TX EQ (-36 to +12 dB). | Tooltip on the Output Fader: "Output gain (dB). Drag to set, wheel for fine step, double-click to reset to 0 dB." Default: 0 dB. |
| `ClientEqRxMasterGain` | Post-EQ output master gain for the RX EQ (-36 to +12 dB). | Tooltip on the Output Fader: "Output gain (dB). Drag to set, wheel for fine step, double-click to reset to 0 dB." Default: 0 dB. |

## Tips

- The applet tiles are hidden by default. If you want a persistent visual reference of your EQ curve while operating, enable the EQ stage via the CHAIN widget so the tile becomes visible in the Aetherial Audio (TXDSP) container.
- The floating editor is shared between TX and RX. Opening it from the TX chain tile and then opening it from the RX chain tile switches the editor to the RX side; your TX settings are not affected.
- Use Peak Hold to freeze the analyzer trace while you tune a band. Resonances that only appear briefly become easy to spot because the trace does not decay while the button is checked. Toggle Peak Hold off when you are done to resume normal decay.
- Click Reset to return the EQ to a known state before building a new preset from scratch. The reset saves immediately and survives a restart.
- Right-click the "Aetherial TX EQ" or "Aetherial RX EQ" sub-container titlebar to float, pop out, or hide the tile.

## Related

- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)
<!-- docmesh:llm version=v0.9.4 date=2026-05-01 -->
