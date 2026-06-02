# See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)

The RX chain view in the Aetherial Audio Chain applet includes three interactive and non-interactive status tiles — RADIO, ADSP, and SPEAK — that show the live state of your receive signal path without requiring you to open any dialog.

## Before you start

- The Aetherial Audio Chain applet must be visible. If it is not, click the tray button labelled `PUDU` in the right sidebar to enable it.
- You must be viewing the RX chain. The status tiles are only visible when RX is the active tab.

## Steps

1. Click the `PUDU` tray button in the right sidebar if the Aetherial Audio Chain applet is not already shown.
2. In the applet header, click **RX**. The RX chain strip replaces the TX chain strip, and the three status tiles appear on either side of the processing stages.
3. Read the three tiles from left to right:
   - **RADIO** — greens when PC Audio (the standard SSB stream) is enabled on the radio.
   - **ADSP** — mirrors which client-side noise reducer is currently active. The label rotates to the active module's short name (for example, `NR2`, `NR4`, or `BNR`). When no noise reducer is on, the tile label falls back to `ADSP`. Single-click bypasses the entire NR cluster with an in-memory snapshot; single-click again restores the prior NR state. Double-click opens the AetherDSP Settings dialog.
   - **SPEAK** — greens when AetherSDR's audio output is unmuted.

The RADIO and SPEAK tiles update automatically as conditions change.

## What each control does

| Tile                                                                            | Kind                      | Behavior                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RADIO**                                                                       | Indicator                 | Greens when PC Audio is enabled. Not interactive.                                                                                                                                                                                                                                                                                                                                       |
| **ADSP**                                                                        | Toggle button / indicator | Label rotates to the active noise reducer's short name (`NR2`, `NR4`, `BNR`); shows `ADSP` when none is active. Single-click bypasses the entire NR cluster; single-click again restores the prior NR state. Double-click opens AetherDSP Settings. Greens when a noise reducer is on.                                                                                                  |
| **SPEAK**                                                                       | Indicator                 | Greens when AetherSDR's audio output is unmuted. Not interactive.                                                                                                                                                                                                                                                                                                                       |
| RX chain stage (**EQ** / **AGC-G** / **AGC-C** / **DESS** / **TUBE** / **EVO**) | Drag handle               | Single-click toggles bypass for the RX stage; double-click opens its frameless floating editor in RX mode; drag reorders the RX chain. All six RX stages (EQ, AGC-G/Gate, AGC-C/Comp, DESS/DeEss, TUBE, EVO/Pudu) are fully implemented. Order is independent of the TX chain. Distinct mime type `application/x-aethersdr-rx-chain-stage` prevents stray drops between the two strips. |

The RADIO and SPEAK tiles are not interactive. Single-click, double-click, and drag have no effect on them.

## How TX and RX BYPASS work

The BYPASS state for both TX and RX is owned by the audio engine rather than tracked locally in the applet. This means the **BYPASS** button on either side stays in sync with the matching BYPASS control in the Aetherial Audio Channel Strip (TX) or the RX strip's internal controls. Pressing **BYPASS** in any location reflects immediately in the other.

When switching between TX and RX tabs, the **BYPASS** button visual updates to show the current engine-owned state for the newly active side. No separate snapshot management is needed for either chain.

The BYPASS button disables every stage in the selected chain, including RN2. Its scope is global (per audio engine), not per-profile — the button stays pressed across Channel Strip profile switches.

## How double-click works on TX chain stages

Double-clicking any TX chain stage tile opens the **Aetherial Audio Channel Strip** — the unified TX DSP window. The per-stage editors remain accessible from within the channel strip itself.

Double-clicking an RX chain stage opens the per-stage frameless floating editor for that stage.

## How click discrimination works

When you single-click a chain stage, AetherSDR waits for the duration set in **Interaction Settings** (accessible from `View > Interaction Settings`) before deciding whether it was a single-click or the first click of a double-click. This prevents accidental bypass toggles when you intend to double-click to open an editor.

- If you double-click a stage, the editor opens immediately and no bypass toggle occurs.
- If you single-click a stage and then stop, the bypass toggles after the interaction interval elapses.
- The default interval matches your operating system's double-click time, but you can adjust it in Interaction Settings to better suit your clicking speed.

## Tips

- The last-active tab (TX or RX) is restored on next launch via the persisted setting `PooDooAudioActiveTab`. If you want the RX status tiles visible by default, leave the **RX** tab selected when you close AetherSDR.
- The **ADSP** tile label changing to a specific name (such as `NR2`) is the quickest way to confirm that a noise reducer is actually engaged, without opening `Settings > AetherDSP Settings...`.
- The gate and compressor stages in the RX chain are labelled **AGC-G** and **AGC-C** respectively. These correspond to the Gate and Comp stages internally.
- Because bypass state is now engine-owned for both sides, the **BYPASS** button will correctly reflect any bypass change made from other sources, even if the chain applet was not the source of that change.
- The RX chain includes a fully implemented DESS (De-Esser) stage between AGC-C and TUBE.
- If you find that single-clicks sometimes trigger bypass when you meant to double-click, adjust the click discrimination interval in `View > Interaction Settings` to a longer value.
- The BYPASS button disables all stages including RN2. It remains engaged across Channel Strip profile switches, as its state is global per audio engine.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)