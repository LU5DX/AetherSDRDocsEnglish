# Reset all bands to flat with one click

The reset function sets all eight equalizer bands for the currently-selected path (RX or TX) back to 0 dB in one action. Use it to clear a custom curve and return to a flat response without adjusting each slider individually.

## Before you start

- AetherSDR must be connected to the radio. The EQ applet requires an active radio connection.
- The EQ applet must be open. If it is not visible, click the EQ tray button in the right sidebar applet panel to show it.

## Steps

1. Click the EQ tray button in the right sidebar to open the Equalizer tile if it is not already visible.
2. Select the path you want to reset: click RX to work on the receive equalizer, or click TX to work on the transmit equalizer. The applet opens on the TX view by default.
3. Click the reset arc button (the 3/4-circle arrow icon, immediately to the right of ON). Its tooltip reads "Reset all bands to 0 dB."

All eight band sliders (63, 125, 250, 500 Hz and 1k, 2k, 4k, 8k) move to 0 dB and their value labels update to 0.

## What each control does

| Control | What it does | Default | Range |
|---|---|---|---|
| RX | Selects the receive path for display and editing. | unchecked | — |
| TX | Selects the transmit path for display and editing. | checked | — |
| Reset arc button | Resets all 8 bands of the currently-selected path to 0 dB. | — | — |
| Band sliders (63–8k) | Individual trim per band; all return to 0 after a reset. | 0 dB | −10 to +10 dB |

## Tips

- The reset acts only on the path currently shown. To reset both paths, select RX, click the reset arc button, then select TX and click it again.
- Resetting bands does not disable the equalizer. ON remains in its current state after a reset.

## Related

- [Equalizer (Graphic) overview](overview.md)
- [Boost or cut specific octave bands (63 Hz to 8 kHz)](boost-or-cut-specific-octave-bands-63-hz-to-8-khz.md)
- [Switch between shaping RX audio and TX audio](switch-between-shaping-rx-audio-and-tx-audio.md)
- [Compare EQ on vs EQ off quickly with the ON button](compare-eq-on-vs-eq-off-quickly-with-the-on-button.md)
