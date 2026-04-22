# Switch between shaping RX audio and TX audio

The Equalizer applet maintains separate band settings for the receive and transmit paths. Use the RX and TX selector buttons to choose which path the sliders and ON button act on.

## Before you start

- AetherSDR must be connected to the radio. The EQ applet requires an active radio connection.
- Open the Equalizer tile by clicking the EQ tray button in the right sidebar applet panel.

## Steps

1. Click the EQ tray button in the right sidebar to open the Equalizer tile if it is not already visible.
2. To edit the receive path, click RX. The sliders and ON button now reflect and control the RX equalizer bands.
3. To edit the transmit path, click TX. The sliders and ON button now reflect and control the TX equalizer bands.

## What each control does

| Control | Kind | Default | Behavior |
|---|---|---|---|
| RX | Toggle button | Unchecked | Selects the receive equalizer path for display and editing. Blue highlight when active. |
| TX | Toggle button | Checked | Selects the transmit equalizer path for display and editing. Blue highlight when active. The applet opens on this view. |
| ON | Toggle button | Unchecked | Enables or disables the equalizer for whichever path (RX or TX) is currently selected. Green highlight when enabled. |
| 63, 125, 250, 500, 1k, 2k, 4k, 8k | Sliders | 0 dB each | Trim the corresponding frequency band for the selected path. Range: −10 to +10 dB. The value label below each slider updates live. |
| Reset arc (revert icon) | Push button | — | Resets all 8 bands of the currently selected path to 0 dB. |

## Tips

- RX and TX are mutually exclusive. Clicking one automatically deselects the other. You cannot edit both paths at the same time.
- The ON button, all sliders, and the reset button always operate on whichever path is currently selected. Switch to RX before resetting or adjusting if you intend to change the receive path.
- When you switch from TX to RX (or back), the sliders immediately update to show the stored values for the newly selected path. Your changes to the previous path are not lost.

## Related

- [Equalizer (Graphic) overview](overview.md)
- [Enable radio-side graphic EQ for RX](enable-radio-side-graphic-eq-for-rx.md)
- [Enable radio-side graphic EQ for TX](enable-radio-side-graphic-eq-for-tx.md)
- [Boost or cut specific octave bands (63 Hz to 8 kHz)](boost-or-cut-specific-octave-bands-63-hz-to-8-khz.md)
- [Reset all bands to flat with one click](reset-all-bands-to-flat-with-one-click.md)
