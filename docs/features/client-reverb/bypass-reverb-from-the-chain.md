# Bypass reverb from the chain

This page explains how to disable the TX reverb stage so it no longer processes your transmitted audio. Use this when you want to remove reverb entirely without changing any of the knob settings.

## Before you start

- The REVERB sub-container is visible inside the PooDoo Audio (TXDSP) parent container only when the Reverb stage has been enabled via the CHAIN widget or the floating Reverb editor.
- If the REVERB sub-container is not visible, the stage is already bypassed.

## Steps

1. Locate the CHAIN widget inside the PooDoo Audio (TXDSP) parent container in the applet panel.
2. Click the Reverb stage in the CHAIN widget once to disable it.

The REVERB sub-container will hide and the reverb tail will no longer be applied to the transmitted signal. The persisted setting `ClientReverbTxEnabled` is set to disabled. All knob values (Size, Decay, Damp, Pre, Mix) are retained.

## Tips

- To re-enable reverb without reconfiguring it, click the Reverb stage in the CHAIN widget again. Your previous knob values are restored.
- Double-clicking the Reverb stage in the CHAIN widget opens the floating Reverb editor instead of toggling the bypass.

## Related

- [Reverb overview](overview.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
