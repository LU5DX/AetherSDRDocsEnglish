# Connect to a station MQTT broker

This page explains how to open the MQTT applet and connect AetherSDR to a station MQTT broker so you can subscribe to topics, view incoming messages, and publish canned payloads.

## Before you start

- Your MQTT broker is running and reachable from the machine running AetherSDR.
- You know the broker's hostname or IP address, port, and credentials (if any).
- AetherSDR was built with MQTT support (`HAVE_MQTT`). If the MQTT tray button is absent, your build does not include this feature.

## Steps

1. If the applet panel is not visible, click `View > Applet Panel` to show it.
2. Click the **MQTT** tray button on the right sidebar. The MQTT applet opens.
3. In the **Host** field, enter the broker hostname or IP address. Default is `localhost`.
4. In the **Port** field, enter the broker TCP port. Default is `1883`. Valid range: 1–65535.
5. If the broker requires authentication, enter your credentials in the **User** and **Pass** fields. Both are optional and may be left blank.
6. In the **Topics** field, enter a comma-separated list of topics to subscribe to. Leave blank if you only need to publish. To also overlay a topic's value on the panadapter, prefix it with `*`. Example:
   ```
   *rotator/pos, *ant/selected, station/log
   ```
7. If the broker requires TLS, check the **TLS** checkbox. The port field switches automatically from `1883` to `8883`. If you need a custom CA certificate, enter the file path in the **CA cert** field that appears. Leave **CA cert** blank to use the system CA bundle.
8. Click **Enable** (currently showing "Off") to connect. The button label changes to "On" and all settings are saved.
9. Watch the status label to the right of the button. It reads "Connected" in green when the broker accepts the connection.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Host** | Broker hostname or IP address | `localhost` | Any valid hostname or IP | `MqttHost` |
| **Port** | Broker TCP port | `1883` | 1–65535 | `MqttPort` |
| **User** | Broker username (optional) | _(blank)_ | — | `MqttUser` |
| **Pass** | Broker password (optional, masked) | _(blank)_ | — | `MqttPass` |
| **Topics** | Comma-separated subscription list; prefix with `*` to overlay on panadapter | _(blank)_ | — | `MqttTopics` |
| **TLS** | Enable TLS encryption; auto-switches port between `1883` and `8883`; shows/hides **CA cert** row | Off | On / Off | `MqttTls` |
| **CA cert** | Path to CA certificate file; blank uses the system CA bundle. Visible only when TLS is checked. | _(blank)_ | — | `MqttCaFile` |
| **Enable** | Connects (On) or disconnects (Off); saves all settings on connect | Off | Off / On | — |
| **Message log** | Displays received messages as `topic: value` lines | — | Last 50 entries | — |

## Tips

- Settings are saved to persistent storage only when you click **Enable** to connect, not when you type them. If you edit the fields and close the applet without connecting, your changes are lost.
- The **CA cert** field and its label are hidden when **TLS** is unchecked. Check **TLS** first to make the row appear.
- The **Message log** keeps the last 50 message blocks. Older entries are dropped automatically.
- Publish buttons are only active while connected. See [Add or remove custom publish buttons](../../features/mqtt/add-or-remove-custom-publish-buttons.md) to configure them.

## Troubleshooting

- **Status label shows an error message instead of "Connected"** — The broker refused the connection or is unreachable. Verify the **Host**, **Port**, and credentials. If TLS is enabled, confirm the broker is listening on port `8883` and the CA certificate path is correct.
- **MQTT tray button is absent** — AetherSDR was built without MQTT support. You need a build compiled with the `HAVE_MQTT` flag.
- **Port did not switch when I checked TLS** — The auto-switch only triggers if the current port value is exactly `1883` (switching to `8883`) or `8883` (switching to `1883`). If you had entered a custom port, it is left unchanged.
- **Topics field accepts input but no messages appear** — Confirm the broker is publishing to the exact topic strings entered. MQTT topic matching is case-sensitive.

## Related

- [MQTT overview](../../features/mqtt/overview.md)
- [Subscribe to rotator / antenna switch topics](../../features/mqtt/subscribe-to-rotator-antenna-switch-topics.md)
- [Overlay an MQTT value on the panadapter (prefix topic with *)](../../features/mqtt/overlay-an-mqtt-value-on-the-panadapter-prefix-topic-with.md)
- [Publish a canned message with a button (e.g. rotator preset)](../../features/mqtt/publish-a-canned-message-with-a-button-e-g-rotator-preset.md)
- [Add or remove custom publish buttons](../../features/mqtt/add-or-remove-custom-publish-buttons.md)
- [Enable TLS with a custom CA certificate](../../features/mqtt/enable-tls-with-a-custom-ca-certificate.md)
