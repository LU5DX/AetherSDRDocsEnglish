```markdown
# Understand why mute state is not restored on reconnect (radio-authoritative policy #2489)

When you mute a slice using the mute button in the RX Controls applet, the mute state is not saved or restored after a radio disconnection and reconnection. This is by design: AetherSDR treats the radio as the authoritative source for audio mute state.

## Steps

1. Click the mute button (🔊 / 🔇) in the RX Controls applet to mute or unmute the slice.
2. Disconnect and reconnect to the radio — the mute button returns to its default unmuted (🔊) state.

## What each control does

| Control     | Label | Default     |
|-------------|-------|-------------|
| Mute toggle | 🔊 / 🔇 | 🔊 (unmuted) |
## Behavior details

- Single-click the mute button toggles mute for this slice. The icon (🔊 or 🔇) updates only when the radio acknowledges the state change via `SliceModel::audioMuteChanged`.
- Double-click the mute button toggles mute for all owned slices simultaneously.
- The single-click action is deferred by the platform double-click interval (approximately 400 ms). This delay allows a double-click to override the single-click and toggle all slices instead.
- No suppress flag is needed for the trailing `clicked()` signal of a double-click sequence. The `eventFilter` returns `true` on `MouseButtonDblClick`, so `QAbstractButton::mouseDoubleClickEvent` is never called. The button never enters pressed-state on the second press, and the second release does not emit `clicked()`.

## Tips

- The mute button only controls audio for the currently selected slice. Each slice has its own mute toggle.
- If you regularly need the audio to start muted after a reconnect, manually mute the slice after connecting, or use the radio's hardware mute if available.

## Related

- [RX Controls overview](../../features/rx/overview.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
```