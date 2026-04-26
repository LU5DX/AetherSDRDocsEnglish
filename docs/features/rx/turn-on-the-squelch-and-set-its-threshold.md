# Turn on the squelch and set its threshold

Use the squelch to mute the slice audio when no signal is present. This is most useful on FM and noisy bands where you want silence between transmissions.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- Select the slice you want to apply squelch to using the slice tabs (A–H) at the top of the RX Controls applet.

## Steps

1. Click the **RX** tray button on the right sidebar to open the RX Controls applet, if it is not already visible.
2. If you have more than one slice, click the appropriate slice tab (A–H) to bind the applet to the correct slice.
3. Move the **Squelch level** slider to the threshold you want. The default is 20; the valid range is 0–100. A higher value requires a stronger signal to open the squelch.
4. Click **SQL** to enable the squelch. The button activates and the squelch takes effect at the level set in step 3.

To disable the squelch, click **SQL** again.

## What each control does

| Control | Kind | Default | Range | Behavior |
|---|---|---|---|---|
| **SQL** | Toggle button | Off | On / Off | Enables squelch at the current slider level. Audio is muted until a signal exceeds the threshold. |
| **Squelch level** | Slider | 20 | 0–100 | Sets the squelch threshold. Takes effect only when **SQL** is on. Higher values require a stronger signal to open the squelch. |

## Tips

- Set the **Squelch level** slider before clicking **SQL** so the squelch opens at the right threshold immediately on activation.
- If the squelch never opens, lower the **Squelch level** slider. If it never closes, raise it.
- Squelch level has no effect when **SQL** is off.

## Troubleshooting

- **Audio is always muted after enabling SQL** — The **Squelch level** slider is set too high. Lower the slider until the squelch opens on your target signal, then click **SQL** again.
- **Squelch never closes between transmissions** — The **Squelch level** slider is set too low. Raise the slider until weak noise no longer opens it.

## Related

- [RX Controls overview](overview.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
