# Enable radio-side graphic EQ for TX

This page explains how to turn on the graphic equalizer for the transmit path. The equalizer runs inside the FLEX-8600 itself, shaping your transmitted audio across eight fixed bands before it leaves the radio.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The EQ applet requires an active radio connection.
- The applet panel must be visible. If it is not, click `View > Applet Panel` to show it.

## Steps

1. Click the EQ tray button in the right sidebar applet panel. The Equalizer tile opens in the top row of the applet panel.
2. Confirm TX is selected. The TX button is checked by default when the applet opens. If it is not highlighted, click TX.
3. Click ON. The button turns green, indicating the transmit equalizer is now active on the radio.

## What each control does

| Control | Description | Default | Range |
|---|---|---|---|
| ON | Enables or disables the equalizer for the currently-selected path (TX or RX). Green when active. | Off | On / Off |
| TX | Selects the transmit equalizer bands for display and editing. | Checked | — |
| RX | Selects the receive equalizer bands for display and editing. | Unchecked | — |
| Reset arc button | Resets all 8 bands of the current path to 0 dB. Tooltip: "Reset all bands to 0 dB". | — | — |
| 63 | Trims the 63 Hz band. Value label below the slider updates live. | 0 dB | −10 to +10 dB |
| 125 | Trims the 125 Hz band. | 0 dB | −10 to +10 dB |
| 250 | Trims the 250 Hz band. | 0 dB | −10 to +10 dB |
| 500 | Trims the 500 Hz band. | 0 dB | −10 to +10 dB |
| 1k | Trims the 1 kHz band. | 0 dB | −10 to +10 dB |
| 2k | Trims the 2 kHz band. | 0 dB | −10 to +10 dB |
| 4k | Trims the 4 kHz band. | 0 dB | −10 to +10 dB |
| 8k | Trims the 8 kHz band. | 0 dB | −10 to +10 dB |

## Tips

- The TX button is checked by default each time you open the applet, so you do not need to switch paths if you only intend to adjust TX audio.
- Clicking ON a second time disables the equalizer without clearing your band settings. Your slider positions are preserved.
- To start from a flat response before shaping, click the Reset arc button before enabling ON.

## Troubleshooting

- **ON does not stay lit after clicking** — The applet lost its radio connection. Check that AetherSDR is still connected to the radio. Disconnect and reconnect if necessary.
- **Sliders move but transmitted audio sounds unchanged** — Confirm that ON is lit green and that TX is the selected path, not RX.

## Related

- [Equalizer (Graphic) overview](overview.md)
- [Enable radio-side graphic EQ for RX](enable-radio-side-graphic-eq-for-rx.md)
- [Boost or cut specific octave bands (63 Hz to 8 kHz)](boost-or-cut-specific-octave-bands-63-hz-to-8-khz.md)
- [Reset all bands to flat with one click](reset-all-bands-to-flat-with-one-click.md)
- [Switch between shaping RX audio and TX audio](switch-between-shaping-rx-audio-and-tx-audio.md)
- [Compare EQ on vs EQ off quickly with the ON button](compare-eq-on-vs-eq-off-quickly-with-the-on-button.md)
