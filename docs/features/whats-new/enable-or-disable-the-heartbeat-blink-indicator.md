# Enable or disable the heartbeat blink indicator

The Radio heartbeat indicator in the Title Bar shows the radio discovery status at a glance. You can turn the blinking animation on or off; the preference is saved across sessions.

## Steps

1. Locate the **Radio heartbeat** indicator in the Title Bar at the top of the main window.
2. Right-click the **Radio heartbeat** indicator to toggle blinking on or off.

The setting is saved automatically via `HeartbeatBlinkEnabled`.

## What each control does

| Control | Behavior |
|---|---|
| **Radio heartbeat** | Flashes green when a discovery packet arrives; turns solid amber while connecting; blinks red/grey when radio discovery is lost. Right-click to toggle blink on/off. |

### Heartbeat indicator states

| State | Meaning |
|---|---|
| Grey | No discovery traffic |
| Green flash | Radio discovered (discovery packet received) |
| Amber | Connecting to radio |
| Red blink | Radio lost from network |

## Tips

- Disabling the blink does not affect radio connectivity — it only stops the visual animation.
- If you lose track of the current blink state, right-click the indicator again; the toggle reflects the current setting immediately.

## Related

- [title-bar.md](title-bar.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
