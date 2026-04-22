# Subscribe to rotator / antenna switch topics

Use the MQTT applet to subscribe to topics published by your rotator controller or antenna switch. Incoming values appear in the message log and, if you prefix a topic with `*`, as an overlay on the panadapter.

## Before you start

- The MQTT applet must be visible. If you do not see it, click the MQTT tray button on the right sidebar to show it.
- Your station MQTT broker must be running and reachable from the machine running AetherSDR.
- If you have not yet configured broker credentials, complete [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md) first.

## Steps

1. Open the MQTT applet by clicking the MQTT tray button on the right sidebar.
2. In the **Host** field, confirm the broker hostname or IP address. Default: `localhost`.
3. In the **Port** field, confirm the broker port. Default: `1883`.
4. If your broker requires authentication, enter values in the **User** and **Pass** fields.
5. In the **Topics** field, enter a comma-separated list of the topics you want to subscribe to. To also show a topic's value as a panadapter overlay, prefix it with `*`. Example:
   ```
   *rotator/pos, *ant/selected, station/log
   ```
6. If your broker uses TLS, check **TLS**. The port switches automatically to `8883`. If you need a custom CA certificate, enter the file path in **CA cert**; leave it blank to use the system CA bundle.
7. Click **Enable** to connect. The button label changes to **On** and the status label reads **Connected** in green. All settings are saved at this point.

## What each control does

| Control | Default | Valid range / notes | Setting key |
|---|---|---|---|
| **Host** | `localhost` | Broker hostname or IP | `MqttHost` |
| **Port** | `1883` | 1–65535; auto-switches to `8883` when TLS is enabled | `MqttPort` |
| **User** | _(empty)_ | Optional broker username | `MqttUser` |
| **Pass** | _(empty)_ | Optional broker password; masked | `MqttPass` |
| **Topics** | _(empty)_ | Comma-separated topic list; prefix with `*` to overlay on panadapter | `MqttTopics` |
| **TLS** | Off | Shows/hides **CA cert** row; auto-flips port between `1883` and `8883` | `MqttTls` |
| **CA cert** | _(empty)_ | Path to CA certificate file; blank uses system CA bundle; visible only when TLS is checked | `MqttCaFile` |
| **Enable** | Off | Connects (On) or disconnects (Off); saves all settings on connect | — |
| **Message log** | — | Displays up to the last 50 received messages as `topic: value` lines | — |

## Tips

- A topic must be entered without the `*` prefix to be subscribed to; the `*` only controls whether the value appears on the panadapter overlay. The subscription itself is always active once you click **Enable**.
- The message log shows only the last segment of the topic path (after the final `/`) next to the value, so `rotator/pos` appears as `pos: 180`.
- Settings are written to disk only when you click **Enable** to connect. If you edit the fields and close the applet without connecting, your changes are not saved.

## Troubleshooting

- **Status label shows an error message instead of "Connected"** — The broker is unreachable or credentials are incorrect. Verify the **Host**, **Port**, **User**, and **Pass** values, then click **Enable** again.
- **Topics field accepts your entries but no messages appear in the log** — Confirm that the broker is publishing on exactly those topic strings. MQTT topic matching is case-sensitive.
- **TLS checkbox is checked but the CA cert row is not visible** — Toggle **TLS** off and on again to force the row to refresh.
- **Port did not switch to 8883 when I checked TLS** — The auto-switch only applies when the current port value is exactly `1883`. If you entered a custom port, it is preserved.

## Related

- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Overlay an MQTT value on the panadapter (prefix topic with *)](overlay-an-mqtt-value-on-the-panadapter-prefix-topic-with.md)
- [Enable TLS with a custom CA certificate](enable-tls-with-a-custom-ca-certificate.md)
- [Publish a canned message with a button (e.g. rotator preset)](publish-a-canned-message-with-a-button-e-g-rotator-preset.md)
