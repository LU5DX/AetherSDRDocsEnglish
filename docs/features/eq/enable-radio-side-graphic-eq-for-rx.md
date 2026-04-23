# Enable radio-side graphic EQ for RX

Open the Equalizer applet and turn on the RX equalizer path so the Flex radio applies an 8-band graphic EQ to received audio inside the radio itself.

## Before you start

- AetherSDR must be connected to a Flex radio. The EQ applet requires an active radio connection.
- If the applet panel is not visible, enable it via `View > Applet Panel`.

## Steps

1. Click the EQ tray button in the right sidebar to open the Equalizer tile.
2. Click RX. The button highlights blue and the sliders switch to the receive path.
3. Click ON. The button highlights green. The RX equalizer is now active on the radio.
4. Adjust the band sliders (63, 125, 250, 500, 1k, 2k, 4k, 8k) as needed. Each slider trims its band from −10 to +10 dB. The value label below each slider updates live.

## What each control does

| Control | Kind | Default | Range | Behavior |
|---|---|---|---|---|
| ON | Toggle button | Off (unchecked) | On / Off | Enables or disables the equalizer for the currently selected path. Green highlight when enabled. |
| RX | Toggle button | Off (unchecked) | — | Selects the receive path for display and editing. Blue highlight when active. Mutually exclusive with TX. |
| TX | Toggle button | On (checked) | — | Selects the transmit path. The applet opens on the TX view by default. |
| Reset arc | Push button | — | — | Resets all 8 bands of the currently selected path to 0 dB. Tooltip: "Reset all bands to 0 dB". |
| 63 | Vertical slider | 0 dB | −10 to +10 dB | Trims the 63 Hz band for the selected path. |
| 125 | Vertical slider | 0 dB | −10 to +10 dB | Trims the 125 Hz band for the selected path. |
| 250 | Vertical slider | 0 dB | −10 to +10 dB | Trims the 250 Hz band for the selected path. |
| 500 | Vertical slider | 0 dB | −10 to +10 dB | Trims the 500 Hz band for the selected path. |
| 1k | Vertical slider | 0 dB | −10 to +10 dB | Trims the 1 kHz band for the selected path. |
| 2k | Vertical slider | 0 dB | −10 to +10 dB | Trims the 2 kHz band for the selected path. |
| 4k | Vertical slider | 0 dB | −10 to +10 dB | Trims the 4 kHz band for the selected path. |
| 8k | Vertical slider | 0 dB | −10 to +10 dB | Trims the 8 kHz band for the selected path. |

## Tips

- The applet always opens showing the TX path. Click RX before adjusting sliders to make sure you are editing receive bands, not transmit bands.
- To quickly compare equalized and flat receive audio, click ON repeatedly while listening. The radio applies or removes the EQ immediately.
- To start fresh, click the Reset arc button. All RX bands return to 0 dB in one click.

## Troubleshooting

- **ON button does not respond** — Confirm AetherSDR is connected to the radio. The EQ applet requires an active radio connection to send changes.
- **Slider changes affect TX instead of RX** — TX is the default view. Click RX first to switch the applet to the receive path before editing bands.

## Related

- [Equalizer (Graphic) overview](overview.md)
- [Enable radio-side graphic EQ for TX](enable-radio-side-graphic-eq-for-tx.md)
- [Boost or cut specific octave bands (63 Hz to 8 kHz)](boost-or-cut-specific-octave-bands-63-hz-to-8-khz.md)
- [Reset all bands to flat with one click](reset-all-bands-to-flat-with-one-click.md)
- [Switch between shaping RX audio and TX audio](switch-between-shaping-rx-audio-and-tx-audio.md)
- [Compare EQ on vs EQ off quickly with the ON button](compare-eq-on-vs-eq-off-quickly-with-the-on-button.md)
