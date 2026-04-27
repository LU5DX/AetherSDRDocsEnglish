# Turn on the squelch and set its threshold

Use the squelch controls in the RX Controls applet to silence the audio output when no signal is present. This is most useful on FM and noisy HF frequencies where you want audio only when a signal opens the squelch.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- Identify which slice you want to apply squelch to.

## Steps

1. Open the RX Controls applet by clicking the **RX** tray button on the right sidebar if it is not already visible.
2. If you have multiple slices, click the appropriate slice tab (**A** through **H**) at the top of the applet to select the target slice.
3. Set the squelch threshold by dragging the **Squelch level** slider to the desired level. A higher value requires a stronger signal to open the squelch.
4. Click **SQL** to enable the squelch. The button activates and the squelch takes effect at the level set in step 3.

To disable the squelch, click **SQL** again to deactivate it.

## What each control does

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| **SQL** | Off | On / Off | Enables squelch at the current slider level. Has no effect when not checked. |
| **Squelch level** | 20 | 0–100 | Sets the squelch threshold. Higher values require a stronger signal to open the squelch. Takes effect only when **SQL** is on. |

## Tips

- Adjust the **Squelch level** slider before clicking **SQL** so you can hear where the threshold sits relative to background noise.
- If the squelch never opens on a signal you can hear, lower the **Squelch level** value.
- If the squelch never closes between signals, raise the **Squelch level** value.

## Troubleshooting

- **Audio is silent even with SQL off** — Check whether the slice is muted. The mute toggle (🔊 / 🔇) is separate from squelch. Click the mute button to unmute if needed. Also verify the **AF gain** slider is not at 0.
- **Squelch level set but has no effect** — The **Squelch level** slider only controls the threshold; the squelch circuit is inactive until **SQL** is enabled. Confirm **SQL** is checked.

## Related

- [RX Controls overview](overview.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md)
