# Overlay an MQTT value on the panadapter

Display the latest value of a subscribed MQTT topic directly on the panadapter, so you can monitor station telemetry (e.g. antenna temperature, rotor position, weather data) while operating.

## Before you start

- Connect to a station MQTT broker and subscribe to the topic whose value you want to overlay. See [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md).
- The topic subscription must have **Display on panadapter** enabled in the MQTT Settings dialog (`Settings > MQTT...`). See [Subscribe to MQTT topics and toggle panadapter display](subscribe-to-mqtt-topics-and-toggle-panadapter-display.md).

## Steps

1. Open the MQTT applet by clicking the **MQTT** tray button on the right sidebar.
2. Click the **Enable (Off/On)** toggle button to connect to the broker. The button reads "On" and the status label turns green when connected.
3. Ensure the subscribed topic appears in the message log. A line like `antennaTemp: 28.4` confirms data is arriving.
4. The panadapter overlay updates automatically as messages arrive. Only topics with **Display on panadapter** checked in their subscription configuration are overlaid.

## What each control does

| Control                    | Behavior                                                                                                                                                                                                                                                                                         | Setting key                                                                         |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| **Enable (Off/On)** toggle | Connects or disconnects from the broker using settings from MqttSettings. Emits connectRequested / disconnectRequested and saves connection enabled state. Password is loaded from system keychain on first enable. If keychain password is not yet loaded, shows 'Waiting for keychain' status. | —                                                                                   |
| **Settings...** button     | Opens the MQTT Settings dialog (MqttSettingsDialog) for broker connection, subscriptions, and publish button configuration. New in v26.5.3. Replaces the inline Host/Port/User/Pass/TLS/Topics fields.                                                                                           | —                                                                                   |
| Publish buttons            | Click publishes the configured payload to the configured topic via MqttClient::publish. Buttons are configured in the MQTT Settings dialog.                                                                                                                                                      | Only active while connected. Configured via MqttSettingsDialog Publish Buttons tab. |
| Message log                | Displays received messages as 'topic: value' lines. Also processes antenna alias updates from MQTT.                                                                                                                                                                                              | Capped to 50 entries.                                                               |

## Status indicator

| Indicator     | States                                        | Meaning                                                                 |
|---------------|-----------------------------------------------|-------------------------------------------------------------------------|
| Status label  | Disconnected, Connected, `<error message>`    | Connection state with colour: green when connected, grey when disconnected, default on error. |

## Tips

- Only the **last value** of each display-enabled topic is overlaid. The overlay shows the short topic name (last segment) and the value.
- To clear the overlay, disconnect the MQTT client (toggle **Enable (Off/On)** to "Off").
- Transmitted messages appear in the message log with a `TX` prefix, showing the short topic name and first 80 characters of the payload. This helps confirm that publish buttons are working correctly.
- Message log is capped at 50 entries. Older entries are removed automatically when the limit is reached.

## Troubleshooting

- **Nothing appears on the panadapter** — Verify the topic subscription has **Display on panadapter** enabled in `Settings > MQTT... > Subscriptions`. Check that the message log shows the topic receiving values.
- **"Waiting for keychain"** status — The MQTT password is stored in your system keychain. If it hasn't been loaded, the connection is deferred. Enter the password in the keychain prompt, or configure the broker connection without a password.

## Related

- [Subscribe to MQTT topics and toggle panadapter display](subscribe-to-mqtt-topics-and-toggle-panadapter-display.md)
- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)