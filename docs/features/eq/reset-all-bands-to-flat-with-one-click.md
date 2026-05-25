# Equalizer (Graphic) Applet

The EQ applet provides an 8-band graphic equalizer applied inside the radio itself via the TCP/IP API. Each vertical slider controls one octave band from 63 Hz to 8 kHz with a range of ±10 dB. The applet has separate RX and TX views so you can shape receive and transmit audio independently.

## Before you start

- AetherSDR must be connected to the radio. The EQ applet requires an active radio connection.
- The EQ applet must be open. If it is not visible, click the EQ tray button in the right sidebar applet panel to show it.

## Steps

1. Click the EQ tray button in the right sidebar to open the Equalizer tile if it is not already visible.
2. Select the path you want to shape: click RX to work on the receive equalizer, or click TX to work on the transmit equalizer. The applet opens on the last-used path; the first time you open it, the TX view is selected.
3. Adjust any band slider (63, 125, 250, 500 Hz or 1k, 2k, 4k, 8k) by dragging the handle up or down. The value label below the slider updates live.
4. When dragging a slider, a popup appears near the slider handle showing the exact dB value with a sign (for example, "+3 dB" or "-5 dB").

## Reset all bands to flat with one click

The reset function sets all eight equalizer bands for the currently-selected path (RX or TX) back to 0 dB in one action. Use it to clear a custom curve and return to a flat response without adjusting each slider individually.

1. Select the path you want to reset: click RX to work on the receive equalizer, or click TX to work on the transmit equalizer.
2. Click the reset arc button (the 3/4-circle arrow icon, immediately to the right of ON). Its tooltip reads "Reset all bands to 0 dB."

All eight band sliders move to 0 dB and their value labels update to 0.

## What each control does

| Control | What it does | Default | Range |
|---|---|---|---|
| ON | Enables or disables the equalizer for the selected path (RX or TX). Shows green when enabled. | unchecked | — |
| RX | Selects the receive path for display and editing. Shows blue when active. | unchecked | — |
| TX | Selects the transmit path for display and editing. Shows blue when active. | checked on first launch; then remembers last selection | — |
| Reset arc button | Resets all 8 bands of the currently-selected path to 0 dB. | — | — |
| Band sliders (63–8k) | Vertically-oriented sliders; each trims one octave band for the selected path. Value label below each slider updates live. When dragging a slider, a popup near the handle shows the exact dB value with a sign (for example, "+3 dB" or "-5 dB"). | 0 dB | −10 to +10 dB |
| +10 / 0 / -10 dB scale | Reference labels to the left and right of the slider column indicating the range of the sliders. | — | — |

## Tips

- The applet remembers which view (RX or TX) you last used across sessions. The first time you open the applet after installation, it defaults to TX.
- The reset acts only on the path currently shown. To reset both paths, select RX, click the reset arc button, then select TX and click it again.
- Resetting bands does not disable the equalizer. ON remains in its current state after a reset.
- The drag popup shows the value with a sign (for example, "+3 dB" for positive values, "0 dB" for zero, "-5 dB" for negative values). This matches the behavior of other sliders in the application.
- After releasing a slider handle, the popup lingers briefly before disappearing so you can read the final value.

## Related

- [Equalizer (Graphic) overview](overview.md)
- [Boost or cut specific octave bands (63 Hz to 8 kHz)](boost-or-cut-specific-octave-bands-63-hz-to-8-khz.md)
- [Switch between shaping RX audio and TX audio](switch-between-shaping-rx-audio-and-tx-audio.md)
- [Compare EQ on vs EQ off quickly with the ON button](compare-eq-on-vs-eq-off-quickly-with-the-on-button.md)