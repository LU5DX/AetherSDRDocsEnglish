# See at a glance whether PC Audio, the noise reducer, and audio output are live (RX status tiles)

The RX chain view includes three non-interactive status tiles — RADIO, DSP, and SPEAK — that show at a glance whether the incoming audio path is fully active. Use them to confirm that PC Audio is running, a noise reducer is engaged, and audio output is unmuted, without opening any settings dialogs.

## Before you start

- The Aetherial Audio Chain applet must be visible. If it is not, click the PUDU tray button in the right sidebar to show it.
- You must be viewing the RX chain. The three status tiles are only visible in RX mode.

## Steps

1. Click the PUDU tray button in the right sidebar to open the Aetherial Audio container if it is not already shown.
2. Click **RX** in the applet header. The RX chain strip replaces the TX strip, and the three status tiles appear at either end of the chain.
3. Read the three tiles:
   - **RADIO** — lit green when PC Audio (the standard SSB stream) is enabled on the radio.
   - **DSP** — shows the short name of the active noise reducer (for example, `NR2`, `NR4`, or `BNR`). Displays `DSP` when no noise reducer is on.
   - **SPEAK** — lit green when AetherSDR's audio output is unmuted.

## What each control does

| Tile | Kind | Visible | Behavior | Persisted setting |
|------|------|---------|----------|-------------------|
| RADIO | Indicator | RX mode only | Greens when PC Audio is enabled | — |
| DSP | Indicator | RX mode only | Label rotates to the active noise reducer's short name (e.g. `NR2`, `NR4`, `BNR`); falls back to `DSP` when none is active | — |
| SPEAK | Indicator | RX mode only | Greens when AetherSDR's audio output is unmuted | — |

None of the three tiles are interactive. They cannot be clicked to change state.

## Tips

- If RADIO is not lit, PC Audio is not enabled on the radio side. Check your slice audio settings.
- If DSP shows `DSP` rather than a named module, no client-side noise reducer is currently active. Open `Settings > AetherDSP Settings...` to configure one.
- If SPEAK is not lit, AetherSDR's audio output is muted. Unmute audio output to restore received audio.
- The `PooDooAudioActiveTab` setting persists which chain was last shown. If AetherSDR reopens on the TX side, click **RX** once to return to the status tiles.

## Related

- [Aetherial Audio Chain overview](overview.md)
- [Switch between editing the TX and RX chains](switch-between-editing-the-tx-and-rx-chains.md)
- [Bypass every RX stage at once](bypass-every-rx-stage-at-once.md)
