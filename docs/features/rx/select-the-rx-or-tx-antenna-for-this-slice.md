# Select the RX or TX antenna for this slice

The RX Controls applet lets you choose which antenna port the FLEX-8600 uses for receiving and transmitting on each slice independently. Use this when you have multiple antennas connected and need to route a specific slice to a specific port.

## Before you start

- AetherSDR must be connected to the radio. The antenna controls are unavailable without a live connection.
- The antenna list is populated from the radio's own port configuration. Confirm your antennas are connected and recognized by the radio before changing these settings.

## Steps

1. Open the RX Controls applet. If it is not visible, click the **RX** tray button on the right sidebar.
2. If you have more than one slice, click the slice tab (A through H) for the slice you want to change.
3. **To change the RX antenna:** Click the blue antenna label near the top of the applet (shows the current RX antenna, e.g. **ANT1**). A menu appears listing all available antenna ports. Click the port you want. A checkmark shows the current selection.
4. **To change the TX antenna:** Click the red antenna label next to the RX antenna label (also shows the current TX antenna, e.g. **ANT1**). A menu appears listing TX-capable antenna ports. Click the port you want.

## What each control does

| Control                           | Default | Valid values                               |
|-----------------------------------|---------|--------------------------------------------|
| **ANT1** (RX antenna, blue label) | ANT1    | Antenna ports from the radio's ant_list    |
| **ANT1** (TX antenna, red label)  | ANT1    | TX-capable ports from the radio's ant_list |

## Tips

- The RX antenna label is shown in blue; the TX antenna label is shown in red. This is the only visual distinction between the two controls, as they appear side by side in the header row.
- Antenna ports whose names begin with `RX` are filtered out of the TX antenna menu. They will still appear in the RX antenna menu.
- Each slice has its own independent RX and TX antenna assignment. Changing the antenna on slice A does not affect slice B.
- From v0.9.3, the slice tab buttons and the slice badge use per-slice colors managed by SliceColorManager. These colors persist across sessions and are also reflected in VFO widgets and meter strips. The colors are not configurable from the antenna controls page; they apply applet-wide.

## NT mode behavior

NT is a digital mode added in v0.9.3. Its behavior within the RX Controls applet matches other digital modes (DIGU/DIGL) in the following ways:

- **Filter presets** — NT uses the same filter preset widths as DIGU and DIGL (100–2000 Hz).
- **Filter width display** — The filter width indicator derives its value from the high edge of the passband, the same calculation used for USB, DIGU, and FDV modes.
- **Squelch** — The **SQL** button and squelch level slider are disabled in NT mode. If squelch was active when you switched into NT mode, AetherSDR turns squelch off automatically and restores it when you switch back. This matches the behavior for DIGU and DIGL; CW mode is handled differently because the radio manages its squelch state directly.

## Troubleshooting

- **An expected antenna port does not appear in the menu** — The list comes directly from the radio's ant_list. Verify the port is configured and recognized in the radio's own settings. AetherSDR cannot add ports that the radio has not reported.
- **The TX antenna menu is missing a port that appears in the RX antenna menu** — Ports whose names begin with `RX` are intentionally excluded from the TX antenna menu because the radio treats them as receive-only.
- **Both labels are greyed out or unresponsive** — AetherSDR is not connected to the radio. Reconnect via `Settings > Connect to Radio...`.
- **SQL button is greyed out after switching to NT mode** — NT is a digital mode. AetherSDR disables squelch in all digital modes (DIGU, DIGL, NT) because audio is routed via DAX and squelch has no meaningful effect. Switch to a non-digital mode to re-enable squelch.

## Related

- [RX Controls overview](overview.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)