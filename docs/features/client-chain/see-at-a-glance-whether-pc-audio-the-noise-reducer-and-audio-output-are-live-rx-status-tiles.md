# See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)

The RX chain view in the Aetherial Audio Chain applet includes three non-interactive status tiles — RADIO, DSP, and SPEAK — that show the live state of your receive signal path without requiring you to open any dialog.

## Before you start

- The Aetherial Audio Chain applet must be visible. If it is not, click the tray button labelled `PUDU` in the right sidebar to enable it.
- You must be viewing the RX chain. The status tiles are only visible when RX is the active tab.

## Steps

1. Click the `PUDU` tray button in the right sidebar if the Aetherial Audio Chain applet is not already shown.
2. In the applet header, click **RX**. The RX chain strip replaces the TX chain strip, and the three status tiles appear on either side of the processing stages.
3. Read the three tiles from left to right:
   - **RADIO** — greens when PC Audio (the standard SSB stream) is enabled on the radio.
   - **DSP** — mirrors which client-side noise reducer is currently active. The label rotates to the active module's short name (for example, `NR2`, `NR4`, or `BNR`). When no noise reducer is on, the tile label falls back to `DSP`.
   - **SPEAK** — greens when AetherSDR's audio output is unmuted.

No further interaction is needed. The tiles update automatically as conditions change.

## What each control does

| Tile | Kind | Behavior |
|---|---|---|
| **RADIO** | Indicator | Greens when PC Audio is enabled. |
| **DSP** | Indicator | Label rotates to the active noise reducer's short name (`NR2`, `NR4`, `BNR`); shows `DSP` when none is active. Greens when a noise reducer is on. |
| **SPEAK** | Indicator | Greens when AetherSDR's audio output is unmuted. |
| RX chain stage (**EQ** / **AGC-T** / **AGC-C** / **TUBE** / **PUDU**) | Drag handle | Single-click toggles bypass for the RX stage; double-click opens its frameless floating editor in RX mode; drag reorders the RX chain. All five RX stages are fully implemented. Order is independent of the TX chain. Distinct mime type `application/x-aethersdr-rx-chain-stage` prevents stray drops between the two strips. |

None of the three tiles are interactive. Single-click, double-click, and drag have no effect on them.

## How TX BYPASS works in v0.9.7

In v0.9.7, the TX BYPASS state is owned by the audio engine rather than tracked locally in the applet. This means the **BYPASS** button on the TX side stays in sync with the BYPASS control in the Aetherial Audio Channel Strip. Pressing **BYPASS** in either place reflects immediately in the other.

The RX side is unaffected — RX bypass continues to use the snapshot mechanism described in [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md).

## How double-click works on TX chain stages in v0.9.7

Previously, double-clicking a TX chain stage opened a per-stage floating editor directly. From v0.9.7, double-clicking any TX chain stage tile opens the **Aetherial Audio Channel Strip** — the unified TX DSP window. The per-stage editors remain accessible from within the channel strip itself.

Double-clicking an RX chain stage continues to open the per-stage frameless floating editor for that stage, unchanged.

## Tips

- The last-active tab (TX or RX) is restored on next launch via the persisted setting `PooDooAudioActiveTab`. If you want the RX status tiles visible by default, leave the **RX** tab selected when you close AetherSDR.
- The **DSP** tile label changing to a specific name (such as `NR2`) is the quickest way to confirm that a noise reducer is actually engaged, without opening `Settings > AetherDSP Settings...`.
- The gate and compressor stages in the RX chain are labelled **AGC-T** and **AGC-C** respectively. These correspond to the Gate and Comp stages internally.
- Because TX bypass state is now engine-owned, the **BYPASS** button on the TX side will correctly reflect any bypass change made from the Aetherial Audio Channel Strip, even if the chain applet was not the source of that change.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)