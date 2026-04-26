# Turn on the squelch and set its threshold

Squelch silences the slice audio when the received signal falls below a set level. This is useful on FM, AM, or any mode where you want the speaker quiet between transmissions.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- The RX Controls applet must be visible. If it is not, click the RX tray button on the right sidebar to show it.

## Steps

1. In the RX Controls applet, select the slice you want to adjust by clicking its tab (A through H) if more than one slice is active.
2. Move the squelch level slider to set the threshold. The default is 20, and the valid range is 0–100. A higher value means the signal must be stronger to open the squelch.
3. Click SQL to enable the squelch. The button highlights when squelch is active.
4. Adjust the squelch level slider until the audio opens reliably on signals you want to hear and closes between them.
5. To disable squelch, click SQL again.

## What each control does

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| SQL | Off | On / Off | Enables squelch at the current slider level. Audio is muted when the signal is below the threshold. |
| Squelch level | 20 | 0–100 | Sets the squelch threshold. Takes effect only when SQL is on. Higher values require a stronger signal to open the squelch. |

## Tips

- Set the squelch level slider before clicking SQL so the audio does not cut in and out while you are adjusting.
- If you cannot find a level that opens reliably on weak signals but stays closed on noise, try lowering the value toward 0 in small increments.
- The squelch level slider has no effect when SQL is off.

## Troubleshooting

- **Audio stays muted after clicking SQL** — The squelch level is set too high for the incoming signal. Lower the squelch level slider until the audio opens.
- **Squelch never closes on noise** — The squelch level is too low. Increase the slider value until the audio mutes between transmissions.

## Related

- [RX Controls overview](overview.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md)
