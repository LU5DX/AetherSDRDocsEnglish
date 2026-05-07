# Bypass the entire client NR cluster from the RX chain ADSP tile

Quickly disable all client-side noise reduction engines at once using the ADSP tile in the RX Chain strip, without opening the full AetherDSP Settings dialog.

## Before you start

- Ensure a radio connection is active and you have an RX slice displayed.
- Locate the RX Chain strip showing the processing tiles (ADSP, NB, etc.).

## Steps

1. Find the **ADSP** tile in the RX Chain strip.
2. Double-click the **ADSP** tile. The AetherDSP Settings dialog opens.
3. In the toggle row at the top, click any active (lit) noise reduction toggle (NR2, NR4, MNR, DFNR, RN2, or BNR) to deactivate it.
4. Repeat step 3 for each lit toggle until all toggles are dimmed. No client NR engines are now active.

The ADSP tile in the RX Chain strip updates to reflect the bypassed state.

## Tips

- Bypassing the entire cluster returns the audio to the raw sliced audio stream from the radio, with no client-side processing.
- The six DSP toggles (NR2, NR4, MNR, DFNR, RN2, BNR) also serve as tab selectors. Clicking a toggle both activates that engine and selects its tab — but only one engine can be active at a time (NR2, NR4, and DFNR are mutually exclusive; MNR and BNR may stack in some builds).
- To quickly re-enable a single engine, click its toggle in the row.

## Related

- [AetherDSP Settings overview](overview.md)
- [Open AetherDSP Settings from the VFO DSP grid ADSP button](open-aetherdsp-settings-from-the-vfo-dsp-grid-adsp-button.md)
- [Choosing the right noise reduction: NR2, NR4, DFNR, MNR](../../operating/dsp/noise-reduction-overview.md)
