# Enable Blink Status Indicator

`View > Blink Status Indicator` is a checkable menu item that controls whether the title bar status indicator blinks to signal the radio's heartbeat. Disabling it keeps the indicator static if the blinking is distracting.

## Before you start

- AetherSDR must be running.
- A FLEX-8600 radio does not need to be connected to toggle this setting, but the blinking behavior is only visible when a radio heartbeat is active.

## Steps

1. Click `View` in the menu bar.
2. Click `Blink Status Indicator` to toggle it.
   - A check mark next to the item means blinking is enabled.
   - No check mark means the indicator is static.

## What each control does

| Control | Default | Description |
|---|---|---|
| `Blink Status Indicator` | On (checked) | When enabled, the title bar status indicator blinks in response to the radio heartbeat signal. When disabled, the indicator remains static. |

## Related

- [Enable Frameless Window](enable-frameless-window.md)
- [Enable Minimal Mode](enable-minimal-mode.md)
