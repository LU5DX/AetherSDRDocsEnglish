# Understand why mute state is not restored on reconnect (radio-authoritative policy #2489)

When you mute a slice using the mute button in the RX Controls applet, the mute state is not saved or restored after a radio disconnection and reconnection. This is by design: AetherSDR treats the radio as the authoritative source for audio mute state.

## Steps

1. Click the mute button (🔊 / 🔇) in the RX Controls applet to mute or unmute the slice.
2. Disconnect and reconnect to the radio — the mute button returns to its default unmuted (🔊) state.

## What each control does

| Control | Label | Default | Behavior |
|---|---|---|---|
| Mute toggle | 🔊 / 🔇 | 🔊 (unmuted) | Mutes the slice audio output. State is NOT saved or restored across reconnects per the Radio-Authoritative Settings Policy (#2489). |

## Tips

- The mute button only controls audio for the currently selected slice. Each slice has its own mute toggle.
- If you regularly need the audio to start muted after a reconnect, manually mute the slice after connecting, or use the radio's hardware mute if available.

## Related

- [RX Controls overview](../../features/rx/overview.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
