# Set DAX RX gain per channel

Each DAX RX channel (1–4) has an independent gain control in the DAX Audio applet. Adjusting these lets you match the audio level delivered to digital mode software or other applications receiving DAX audio.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The DAX Audio applet must be open. If it is not visible, click the **DAX** tray button on the right sidebar to show it.
- DAX must be enabled. If the **Enable** button shows **Disabled**, click **Enable** in the DAX Audio applet before adjusting gain.
- **Windows users:** AetherSDR does not include a built-in DAX driver on Windows. The DAX Audio applet displays a note: "No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX." DAX works on Windows using FlexRadio's own SmartSDR DAX drivers. All controls in the applet are inert on Windows. For configuration guidance, see Help → Configuring Data Modes.

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet.
2. Locate the row for the channel you want to adjust: **DAX 1:**, **DAX 2:**, **DAX 3:**, or **DAX 4:**.
3. Drag the combined meter/slider for that channel left or right to decrease or increase the RX gain.
4. Release the drag. The new value is saved immediately.

Repeat for any other channels that need adjustment.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| DAX Enable | off (Disabled) | — | `AutoStartDAX` |
| DAX 1 gain+meter | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| DAX 2 gain+meter | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| DAX 3 gain+meter | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| DAX 4 gain+meter | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| TX gain+meter | 0.5 | 0.0–1.0 | `DaxTxGain` |

**DAX Enable:** A toggle button labeled **Disabled** or **Enabled** that serves as the master switch for all DAX RX and TX streams. Click to toggle. When enabled, the button text changes to **Enabled**; when disabled, it shows **Disabled**. The setting is persisted as `AutoStartDAX`.

Each RX gain+meter is a combined level meter and gain slider. The background bar shows the smoothed post-fader signal level in real time. The vertical thumb line marks the current gain position. Dragging the thumb emits the new gain and persists it immediately.

Each slider has an accessibility name set to "DAX RX 1 gain", "DAX RX 2 gain", "DAX RX 3 gain", or "DAX RX 4 gain" respectively for screen reader support.

The slice assignment indicator to the left of each slider (showing either **—** or **Slice A**–**Slice H**) is read-only and reflects which slice is currently routed to that DAX channel.

## Tips

- The level meter fill reflects post-fader output level — that is, the incoming audio multiplied by the current gain. Moving the slider gives immediate visual feedback on the effective output.
- Gain values are stored as two-decimal-place floats (for example, `0.75`). They are restored from `DaxRxGain1`–`DaxRxGain4` each time AetherSDR starts.
- If a channel shows **—** in the slice assignment indicator, no slice is routed to it and the meter will show no activity regardless of the gain setting.
- On Linux, the DAX audio bridge uses a native PipeWire stream source path, reducing RX latency from approximately 400 ms to approximately 200 ms compared to the previous PulseAudio client.

## Troubleshooting

- **The meter shows no activity even though gain is set above 0.0** — Check the slice assignment indicator for that row. If it shows **—**, no slice is assigned to that DAX channel. Assign a slice to the channel in your radio configuration, then verify the **Enable** button shows **Enabled**.
- **Gain resets to 0.5 after restart** — The setting was not saved. Confirm the drag completed before closing AetherSDR. The save occurs on release of the slider.
- **DAX Enable button does nothing on Windows** — This is expected. AetherSDR includes no built-in DAX driver on Windows. Use FlexRadio's SmartSDR DAX drivers instead.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)