# Overlay an MQTT value on the panadapter

Display the latest value of a subscribed MQTT topic directly on the panadapter, so you can monitor station telemetry (e.g. antenna temperature, rotor position, weather data) while operating.

## Before you start

- Connect to a station MQTT broker and subscribe to the topic whose value you want to overlay. See [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md).
- The topic subscription must have **Display on panadapter** enabled in the MQTT Settings dialog (`Settings > MQTT...`). See [Subscribe to MQTT topics and toggle panadapter display](subscribe-to-mqtt-topics-and-toggle-panadapter-display.md).

## Steps

1. Open the MQTT applet by clicking the **MQTT** tray button on the right sidebar.
2. Click the **Off/On** toggle button to connect to the broker. The button reads "On" and the status label turns green when connected.
3. Ensure the subscribed topic appears in the message log. A line like `antennaTemp: 28.4` confirms data is arriving.
4. The panadapter overlay updates automatically as messages arrive. Only topics with **Display on panadapter** checked in their subscription configuration are overlaid.

## What each control does

| Control | Behavior | Setting key |
|---------|----------|-------------|
| **Off/On** toggle | Connects or disconnects from the broker. Saves connection state. | — |
| **Settings...** button | Opens the MQTT Settings dialog for broker configuration, subscriptions, and publish buttons. | — |
| Message log | Shows the last 50 received messages as `topic: value`. Enables the panadapter overlay for display-enabled topics. | — |
| Publish buttons | Up to 12 buttons configured in MQTT Settings. Each publishes its configured payload to its configured topic. | `MqttButtons` |

## Tips

- Only the **last value** of each display-enabled topic is overlaid. The overlay shows the short topic name (last segment) and the value.
- To clear the overlay, disconnect the MQTT client (toggle **Off/On** to "Off").

## Troubleshooting

- **Nothing appears on the panadapter** — Verify the topic subscription has **Display on panadapter** enabled in `Settings > MQTT... > Subscriptions`. Check that the message log shows the topic receiving values.
- **"Waiting for keychain"** status — The MQTT password is stored in your system keychain. If it hasn't been loaded, the connection is deferred. Enter the password in the keychain prompt, or configure the broker connection without a password.

## Related

- [Subscribe to MQTT topics and toggle panadapter display](subscribe-to-mqtt-topics-and-toggle-panadapter-display.md)
- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
