# Overlay an MQTT value on the panadapter (prefix topic with *)

When a subscribed topic is prefixed with `*` in the Topics field, AetherSDR overlays the most recent value from that topic directly on the panadapter display. This lets you monitor live data such as rotator position or antenna selection without switching away from the RF view.

## Before you start

- The MQTT applet must be visible. If it is not, click the MQTT tray button on the right sidebar to show it.
- You need a reachable MQTT broker publishing the topic you want to display. See [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md) if the broker is not yet configured.
- If the applet is currently connected (Enable shows "On"), click Enable to disconnect before editing settings.

## Steps

1. Open the MQTT applet by clicking the MQTT tray button on the right sidebar.
2. Click **Settings...** to open the MQTT Settings dialog.
3. In the **Subscriptions** tab, enter each topic you want to subscribe to as a comma-separated list. Prefix any topic with `*` to also overlay its value on the panadapter. For example:

    ```
    *rotator/pos, *ant/selected, station/log
    ```

    Topics without `*` are logged in the message log only. Topics prefixed with `*` are both logged and overlaid on the panadapter.

4. In the **Connection** tab, verify the Host, Port, User, and Pass fields are correct for your broker. Configure TLS if required.
5. Click **Save** to close the dialog.
6. Click **Enable** in the applet.
7. The button label changes to "On" and the status label shows "Connected" in green. Incoming values for `*`-prefixed topics appear on the panadapter. All received messages appear in the message log as `topic: value` lines.

## What each control does

| Control       | Default                                                                                                                     | Valid range                                                                |
|---------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Enable        | Off                                                                                                                         | Off / On                                                                   |
| Settings...   | Opens the MQTT Settings dialog (MqttSettingsDialog) for broker connection, subscriptions, and publish button configuration. | New in v26.5.3. Replaces the inline Host/Port/User/Pass/TLS/Topics fields. |
| Publish buttons | Click publishes the configured payload to the configured topic. Configured in the MQTT Settings dialog Publish Buttons tab. | Up to 12 buttons. Only active while connected.                             |
| Message log   | Displays received messages as 'topic: value' lines. Also processes antenna alias updates from MQTT.                         | Capped to 50 entries.                                                      |

## Indicators

| Indicator    | States                                                    | Meaning                                                    |
|--------------|-----------------------------------------------------------|------------------------------------------------------------|
| Status label | Disconnected / Connected / <error message>                | Green when connected, grey when disconnected, default on error. |

## Tips

- Only the final segment of the topic path is shown in the panadapter overlay. For example, `rotator/pos` displays as `pos: <value>`. Use topic names whose last segment is self-explanatory if you subscribe to multiple topics at once.
- The overlay updates each time a new message arrives on the topic. There is no averaging or smoothing; the raw payload value (up to 80 characters) is displayed.
- Removing the `*` prefix from a topic and clicking Enable again stops the overlay for that topic without unsubscribing from it entirely. The value continues to appear in the message log.
- Password is stored in the system keychain. On first enable, if the keychain password is not yet loaded, the status shows "Waiting for keychain".

## Troubleshooting

- **Status shows "Connected" but no overlay appears on the panadapter** — Confirm the topic string in Topics exactly matches what the broker is publishing, including capitalisation and path separators. MQTT topic matching is case-sensitive.
- **Status shows an error message instead of "Connected"** — The broker rejected the connection. Check Host, Port, User, and Pass in the MQTT Settings dialog. If TLS is enabled, verify the CA cert path or leave it blank to use the system CA bundle.
- **Overlay disappears after a disconnect** — When the connection drops, AetherSDR clears the panadapter overlay. Reconnect by clicking Enable to restore it.
- **Status shows "Waiting for keychain"** — The password has not been retrieved from the system keychain yet. Wait a moment or ensure the keychain is unlocked.

## Related

- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Subscribe to rotator / antenna switch topics](subscribe-to-rotator-antenna-switch-topics.md)
- [Enable TLS with a custom CA certificate](enable-tls-with-a-custom-ca-certificate.md)
- [MQTT overview](overview.md)