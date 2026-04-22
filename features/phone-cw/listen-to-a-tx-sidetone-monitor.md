# Listen to a TX sidetone monitor

The Phone/CW applet lets you hear your transmitted audio through your computer speakers or headphones while you transmit. This is useful for verifying audio quality and levels without a second receiver.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet is unavailable without an active radio connection.
- The active slice must be in a phone mode (SSB, AM, FM). In CW mode, the applet switches to the CW panel, which has a separate sidetone control — see [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md).
- Confirm the P/CW applet is visible in the Applet Panel on the right sidebar. If it is not visible, click the **P/CW** tray button to show it.

## Steps

1. In the Phone/CW applet, locate the **MON** toggle button.
2. Click **MON** to enable the TX sidetone monitor. The button lights green when active.
3. Adjust the **Monitor volume** slider to set the listening level. The range is 0–100.
4. Transmit normally. You will hear the transmitted audio at the volume set by the **Monitor volume** slider.
5. To disable monitoring, click **MON** again. The button returns to its inactive state.

## What each control does

| Control | Type | Behavior | Default | Range | Setting key |
|---|---|---|---|---|---|
| **MON** | Toggle button | Enables or disables the TX sidetone monitor. | — | On / Off | — |
| **Monitor volume** | Slider | Sets the sideband monitor playback volume. | — | 0–100 | — |

## Tips

- The **Monitor volume** slider is independent of the radio's main audio output level. You can adjust it without affecting receive audio.
- If you are using the **PC** mic source, the mic gain value is stored client-side as `PcMicGain` (default 50, range 0–100). The radio does not report this value back, so the slider position in the applet is the authoritative value.

## Troubleshooting

- **MON is active but no audio is heard during transmit** — Confirm that the **Monitor volume** slider is not set to 0. Also check that your system audio output device is correctly configured.
- **MON button is not visible** — The applet may be displaying the CW panel rather than the Phone panel. MON is a Phone-mode control. Switch the active slice to a phone mode (SSB, AM, or FM) to restore the Phone panel.

## Related

- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
