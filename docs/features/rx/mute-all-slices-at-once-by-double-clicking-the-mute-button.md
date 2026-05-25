# Mute all slices at once by double-clicking the mute button

Mute or unmute every slice you own in one action, without muting each slice individually.

## Before you start

- You must have more than one active slice (tabs A through H are visible in the RX Controls applet).
- The mute button is the speaker icon (🔊 / 🔇) in the RX Controls applet.

## Steps

1. In the RX Controls applet, double-click the mute button (🔊 when unmuted, 🔇 when muted).
2. All slices you own are muted or unmuted together, matching the new state of the button.

## What each control does

| Control | Label | Default | Behavior | Setting key |
|---------|-------|---------|----------|-------------|
| Mute button | 🔊 / 🔇 | 🔊 (unmuted) | Single-click mutes/unmutes the current slice. Double-click mutes/unmutes all owned slices via the **muteAllToggled** signal. | None (mute state is radio-authoritative per policy #2489) |

## Tips

- The single-click action is deferred by the platform's double-click discrimination interval (~400 ms) so a double-click cancels the single-click timer and triggers the all-slice action instead.
- Mute state is not saved or restored on reconnect — the radio is the source of truth for audio mute.

## Related

- [RX Controls overview](overview.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Understand why mute state is not restored on reconnect (radio-authoritative policy #2489)](../../getting-started/setup/understand-why-mute-state-is-not-restored-on-reconnect-radio-authoritative-policy-2489.md)
