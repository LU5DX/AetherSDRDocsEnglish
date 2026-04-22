# Overlay an MQTT value on the panadapter (prefix topic with *)

When a subscribed topic is prefixed with `*` in the Topics field, AetherSDR overlays the most recent value from that topic directly on the panadapter display. This lets you monitor live data such as rotator position or antenna selection without switching away from the RF view.

## Before you start

- The MQTT applet must be visible. If it is not, click the MQTT tray button on the right sidebar to show it.
- You need a reachable MQTT broker publishing the topic you want to display. See [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md) if the broker is not yet configured.
- If the applet is currently connected (Enable shows "On"), click Enable to disconnect before editing the topic list.

## Steps

1. Open the MQTT applet by clicking the MQTT tray button on the right sidebar.
2. In the Topics field, enter each topic you want to subscribe to as a comma-separated list. Prefix any topic with `*` to also overlay its value on the panadapter. For example:

    ```
    *rotator/pos, *ant/selected, station/log
    ```

    Topics without `*` are logged in the message log only. Topics prefixed with `*` are both logged and overlaid on the panadapter.

3. Verify the Host, Port, User, and Pass fields are correct for your broker.
4. Click Enable.
5. The button label changes to "On" and the status label shows "Connected" in green. Incoming values for `*`-prefixed topics appear on the panadapter. All received messages appear in the message log as `topic: value` lines.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| Host | `localhost` | Any hostname or IP | `MqttHost` | Broker hostname or IP address. Saved when Enable is clicked. |
| Port | `1883` | 1–65535 | `MqttPort` | Broker TCP port. Auto-switches between 1883 and 8883 when TLS is toggled. |
| User | _(empty)_ | Any string | `MqttUser` | Broker username. Optional. |
| Pass | _(empty)_ | Any string | `MqttPass` | Broker password. Displayed masked. Optional. |
| Topics | _(empty)_ | Comma-separated list | `MqttTopics` | Topics to subscribe to. Prefix with `*` to overlay the value on the panadapter. |
| TLS | Off | On / Off | `MqttTls` | Enables TLS encryption. Shows the CA cert row and auto-flips the port between 1883 and 8883. |
| CA cert | _(empty)_ | File path | `MqttCaFile` | Path to a CA certificate file. Blank uses the system CA bundle. Visible only when TLS is checked. |
| Enable | Off | Off / On | _(none)_ | Connects or disconnects the broker. Saves all settings on connect. |
| Message log | — | Last 50 entries | _(none)_ | Displays received messages as `topic: value` lines. |

## Tips

- Only the final segment of the topic path is shown in the panadapter overlay. For example, `rotator/pos` displays as `pos: <value>`. Use topic names whose last segment is self-explanatory if you subscribe to multiple topics at once.
- The overlay updates each time a new message arrives on the topic. There is no averaging or smoothing; the raw payload value (up to 80 characters) is displayed.
- Removing the `*` prefix from a topic and clicking Enable again stops the overlay for that topic without unsubscribing from it entirely. The value continues to appear in the message log.
- All settings are saved to persistent storage only when Enable is clicked to connect. Editing the fields and leaving the applet without clicking Enable discards the changes.

## Troubleshooting

- **Status shows "Connected" but no overlay appears on the panadapter** — Confirm the topic string in Topics exactly matches what the broker is publishing, including capitalisation and path separators. MQTT topic matching is case-sensitive.
- **Status shows an error message instead of "Connected"** — The broker rejected the connection. Check Host, Port, User, and Pass. If TLS is enabled, verify the CA cert path or leave it blank to use the system CA bundle.
- **Overlay disappears after a disconnect** — When the connection drops, AetherSDR clears the panadapter overlay. Reconnect by clicking Enable to restore it.

## Related

- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Subscribe to rotator / antenna switch topics](subscribe-to-rotator-antenna-switch-topics.md)
- [Enable TLS with a custom CA certificate](enable-tls-with-a-custom-ca-certificate.md)
- [MQTT overview](overview.md)
