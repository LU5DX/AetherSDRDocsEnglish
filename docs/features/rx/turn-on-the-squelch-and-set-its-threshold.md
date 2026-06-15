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

| Control           | Default | Valid range |
|-------------------|---------|-------------|
| **SQL**           | Off     | On / Off    |
| **Squelch level** | 20      | 0–100       |
## About the manual squelch level memory

The last manual squelch threshold you set is saved between sessions. When you change modes or restart AetherSDR, the **Squelch level** slider returns to your previous manual setting (value stored in `LastManualSquelchLevel`). This persists separately from the radio's automatic squelch level, which the radio may override when an algorithm-suggested value differs from your preference.

## Tips

- Adjust the **Squelch level** slider before clicking **SQL** so you can hear where the threshold sits relative to background noise.
- If the squelch never opens on a signal you can hear, lower the **Squelch level** value.
- If the squelch never closes between signals, raise the **Squelch level** value.
- The slider defaults to 20 on first launch of a new installation.

## Troubleshooting

- **Audio is silent even with SQL off** — Check whether the slice is muted. The mute toggle (🔊 / 🔇) is separate from squelch. Click the mute button to unmute if needed. Also verify the **AF gain** slider is not at 0.
- **Squelch level set but has no effect** — The **Squelch level** slider only controls the threshold; the squelch circuit is inactive until **SQL** is enabled. Confirm **SQL** is checked.
- **SQL button is greyed out** — Squelch is not available in CW, CWL, DIGU, DIGL, NT, or RTTY modes. In CW/CWL mode the radio manages squelch internally. In digital modes (DIGU, DIGL, NT) and RTTY, audio is routed via DAX and squelch is not meaningful — it would gate weak FSK signals and break decoding. Switch to a mode that supports squelch, or use the **AF gain** slider to control audio level instead.
- **Squelch level resets to a different value than I set** — If you see the slider at a level you did not choose, the radio may have reported an automatic squelch level. The manual threshold from your last adjustment is preserved in AetherSDR's settings and will be restored when you next enable squelch with **SQL**.
- **Slice tabs look wrong after reconnecting** — In v0.9.5.1, slice tab buttons are fully rebuilt whenever the radio reconnects or the number of available slices changes. If the tab row appears incorrect, disconnect and reconnect to the radio; the tabs will reset to match the current hardware slice count.

## Related

- [RX Controls overview](overview.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md)
- [Adjust filter width](adjust-filter-width.md)
- [Adjust AF gain and pan balance](adjust-af-gain-and-pan-balance.md)