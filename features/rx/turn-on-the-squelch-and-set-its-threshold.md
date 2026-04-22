# Turn on the squelch and set its threshold

Use the squelch to mute a slice's audio when no signal is present. This is most useful on FM, NFM, or noisy HF bands where you want silence between transmissions.

## Before you start

- AetherSDR must be connected to the radio. Squelch is a per-slice control and requires an active slice.
- Open the RX Controls applet. If it is not visible, click the **RX** tray button on the right sidebar.

## Steps

1. In the RX Controls applet, locate the **SQL** button and the squelch level slider immediately to its right.
2. Set the squelch threshold first: drag the squelch level slider left (lower) or right (higher) until it is at the level you want. The default is 20 (range 0–100). A higher value requires a stronger signal to open the squelch.
3. Click **SQL** to enable the squelch. The button lights up when active.
4. To disable the squelch, click **SQL** again.

## What each control does

| Control | Default | Range | Behavior |
|---|---|---|---|
| **SQL** | Off | On / Off | Enables squelch at the current slider level. Audio is muted until the signal crosses the threshold. |
| Squelch level slider | 20 | 0–100 | Sets the squelch threshold. Has no effect unless **SQL** is on. |

## Tips

- Set the threshold while the band is quiet. Raise the slider until the audio just cuts off, then back off slightly so weak signals still open the squelch.
- The squelch level slider can be adjusted while **SQL** is already on; changes take effect immediately.

## Troubleshooting

- **Audio is silent even with SQL off** — Check the 🔊 / 🔇 mute button. If the slice is muted, audio will be silent regardless of squelch state. Click the mute button to unmute.
- **SQL is on but audio never opens** — The squelch level slider may be set too high. Drag it toward 0 until audio passes through, then raise it gradually to find the correct threshold.

## Related

- [RX Controls overview](overview.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md)
