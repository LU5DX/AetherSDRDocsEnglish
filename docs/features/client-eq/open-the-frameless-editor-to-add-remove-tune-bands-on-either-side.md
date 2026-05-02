The diff touches only `AppletPanel.cpp` and `AppletPanel.h` — it adds a `ShackSwitchApplet` and a new "SS" button to the applet panel. This is entirely unrelated to the `ClientEqApplet` documentation page. No user-visible behavior of the Parametric EQ is changed.

# Open the Frameless Editor to Add / Remove / Tune Bands on Either Side

The frameless editor is where you do all active EQ work: adding and removing bands, dragging them to new frequencies and gains, adjusting Q, switching filter types, and selecting a filter family. The applet tiles are view-only; this floating window is the editing surface.

## Before you start

- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel.
- The TX or RX EQ stage you want to edit must exist in the CHAIN widget. If the stage is not yet in the chain, add it there first.

## Steps

1. Locate the CHAIN widget for the side you want to edit (TX or RX).
2. Double-click the EQ stage in the CHAIN widget for that side.
   - Double-clicking the TX EQ stage opens the editor titled **Aetherial Parametric EQ — TX**.
   - Double-clicking the RX EQ stage opens the editor titled **Aetherial Parametric EQ — RX**.
3. The frameless editor window appears at its default size (900 × 520 px). Its title bar shows which side is active.
4. To **add a band**, use the icon row along the top of the canvas area. Click the relevant band-type icon to insert a band at a default position.
5. To **remove a band**, select it in the canvas or parameter row and use the remove control in the icon row.
6. To **tune a band**, drag it directly on the canvas:
   - For peak and shelf bands: drag to adjust frequency and gain simultaneously.
   - For HP/LP bands: drag to adjust frequency and Q.
   - Hold **Shift** while dragging to adjust Q alone.
   - Click a band's icon to cycle through filter types.
7. To change the **filter family** applied to HP/LP cascade math, open the drop-down in the top strip and select one of: **Butterworth**, **Chebyshev**, **Bessel**, or **Elliptic**.
8. To freeze the analyzer's peak trace while tuning, click **Peak Hold** in the editor header strip. The button turns amber when active. Click it again to resume normal decay (~10 dB/sec).
9. To discard all edits and return to defaults, click **Reset**. This restores the default 10-band count and parameters and sets the filter family back to Butterworth. The reset saves immediately.
10. To close the editor, use the close button in the editor's frameless title bar. The applet tiles continue showing the summed curve for their respective sides.

## What each control does

| Control                    | What it does                                                                                                                                                                                                                                                                                                                     | Default                                                                                                                                                                                                                                                                                                                 |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Canvas (drag — peak/shelf) | Adjusts frequency and gain for the selected band                                                                                                                                                                                                                                                                                 | Per-band defaults                                                                                                                                                                                                                                                                                                       |
| Canvas (drag — HP/LP)      | Adjusts frequency and Q for the selected band                                                                                                                                                                                                                                                                                    | Per-band defaults                                                                                                                                                                                                                                                                                                       |
| Canvas (Shift + drag)      | Adjusts Q only for the selected band                                                                                                                                                                                                                                                                                             | —                                                                                                                                                                                                                                                                                                                       |
| Band icon (click)          | Cycles the selected band through available filter types                                                                                                                                                                                                                                                                          | —                                                                                                                                                                                                                                                                                                                       |
| Filter family drop-down    | Sets the math topology for HP/LP cascades: Butterworth (maximally flat passband), Chebyshev (steeper transition, 1 dB passband ripple), Bessel (linear phase, gentler rolloff), Elliptic (steepest transition, ripple in both bands). Persisted per path as `ClientEqTxFilterFamily` / `ClientEqRxFilterFamily`.                  | Butterworth                                                                                                                                                                                                                                                                                                             |
| Peak Hold                  | Freezes the analyzer's per-bin peak-hold trace at its highest observed level. Located in the editor header strip. Turns amber when checked. Toggle off to resume normal decay (~10 dB/sec). Applies only to the floating editor — not the docked applet tile.                                                                     | Off (unchecked)                                                                                                                                                                                                                                                                                                         |
| Reset                      | Restores all bands to their default values, resets band count to the default 10 bands, sets filter family to Butterworth, and saves immediately. Tooltip: "Reset all bands to default values". Located in the editor header strip.                                                                                               | —                                                                                                                                                                                                                                                                                                                       |
| Output Fader               | Vertical combined fader + level meter on the right edge of the floating editor. Drag to set post-EQ master gain; scroll wheel adjusts in 0.5 dB steps; double-click resets to 0 dB. The level bar behind the handle shows the smoothed post-EQ peak in real time with the same green-amber-red gradient as the Tube level meter. Persisted separately per path as `ClientEqTxMasterGain` / `ClientEqRxMasterGain`. Range: −36 to +12 dB. Located in the floating editor only — not in the docked applet tile. | 0 dB                                                                                                                                                                                                                                                                                                                    |

## Tips

- The editor is a single shared window reused for both sides. Opening it on the TX side while it is already showing the RX side flips its title and content to TX. You cannot have TX and RX editors open simultaneously.
- Changes save immediately through the audio engine. Closing the editor does not discard unsaved work.
- Bypass is not controlled from inside the editor. To enable or bypass an EQ stage, use the CHAIN widget's single-click gesture on that stage.
- The peak-hold trace in the docked applet tile decays continuously at ~10 dB/sec. The **Peak Hold** button in the floating editor freezes the trace only within the editor view.

## Troubleshooting

- **Double-clicking the EQ stage does nothing** — the stage may not be fully initialized if no radio connection is active. Connect to a FLEX-8600 and try again.
- **Peak Hold button stays lit after you stop using it** — click **Peak Hold** again to uncheck it and resume normal analyzer decay.

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)
<!-- docmesh:llm version=V0.9.4 date=2026-05-01 -->
