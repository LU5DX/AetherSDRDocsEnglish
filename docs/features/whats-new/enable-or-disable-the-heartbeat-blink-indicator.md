# Enable or disable the heartbeat blink indicator

The **Radio heartbeat** indicator in the title bar flashes green, amber, or red to reflect radio connection status. Right-click it to turn the blink animation on or off; your preference is saved across sessions.

## Steps

1. Locate the **Radio heartbeat** indicator in the title bar at the top of the main window.
2. Right-click the indicator to toggle blinking on or off.

The setting is saved immediately. When blink is disabled, the indicator still changes colour to reflect connection state but does not animate.

## What each control does

| Control | Behavior |
|---|---|
| **Radio heartbeat** | Flashes green when a discovery packet arrives; turns solid amber while connecting; blinks red/grey when radio discovery is lost. Right-click to toggle blink on or off. Persisted via `HeartbeatBlinkEnabled`. |

### Heartbeat states

| State | Meaning |
|---|---|
| Grey (idle) | No discovery traffic detected. |
| Green flash | Radio discovered; discovery packet received. |
| Amber | Connecting to radio. |
| Red blink | Radio lost from network. |

## Tips

- Disabling blink can reduce visual distraction during long operating sessions while still letting you see the connection state from the indicator colour alone.
- If you lose track of whether blink is currently enabled, right-click the indicator — the toggle acts immediately and you will see the difference within one heartbeat cycle.

## Related

- [title-bar.md](title-bar.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
