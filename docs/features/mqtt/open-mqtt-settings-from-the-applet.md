# MQTT Applet

The MQTT applet integrates AetherSDR with a station MQTT broker: publish canned messages with user-editable buttons, monitor incoming messages, and overlay topic values on the panadapter.

## Open MQTT settings from the applet

Open the MQTT Settings dialog from the MQTT applet to configure broker connection, subscriptions, and publish button settings.

### Before you start

- The MQTT applet must be visible. Toggle it with the MQTT tray button on the right sidebar.
- The MQTT feature must be compiled in (requires `HAVE_MQTT` build gate).

### Steps

1. In the MQTT applet header, click **Settings...**.
2. The MQTT Settings dialog opens.

## What each control does

| Control                | Behavior                                                                                                                                                                      | Notes                                                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **Settings...** button | Opens the MQTT Settings dialog (`MqttSettingsDialog`) for broker connection, subscriptions, and publish button configuration.                                                 | New in v26.5.3. Replaces the inline Host/Port/User/Pass/TLS/Topics fields.                                                            |
| **Enable (Off/On)**    | Toggle button that connects or disconnects from the broker using settings from MqttSettings. Emits connectRequested / disconnectRequested and saves connection enabled state. | Password is loaded from system keychain on first enable. If keychain password is not yet loaded, shows "Waiting for keychain" status. |
| **Publish buttons**    | Up to 12 push buttons. Click publishes the configured payload to the configured topic via MqttClient::publish.                                                                | Only active while connected. Configured via MqttSettingsDialog Publish Buttons tab. Setting key: `MqttButtons`.                       |
| **Message log**        | Displays received messages as "topic: value" lines and transmitted messages as "TX topic: value" lines. Also processes antenna alias updates from MQTT.                       | Capped to 50 entries.                                                                                                                 |
| Settings...            | Opens the MQTT Settings dialog (MqttSettingsDialog) for broker connection, subscriptions, and publish button configuration.                                                   | New in v26.5.3. Replaces the inline Host/Port/User/Pass/TLS/Topics fields.                                                            |
### Indicators

| Indicator        | States                                                                 | Meaning                                                          |
|-------------------|------------------------------------------------------------------------|------------------------------------------------------------------|
| **Status label**  | "Disconnected" (grey), "Connected" (green), or an error message (default color) | Connection state with colour: green when connected, grey when disconnected, default on error. |

## Message log details

The message log shows both received and transmitted messages:

- **Received messages** appear as `topic: value` lines. For example: `ant/A: 1`
- **Transmitted messages** appear as `TX topic: value` lines. For example: `TX rotator/preset: QTH`

The topic shown is the last segment of the full topic path. For example, if the full topic is `flexradio/6804/ant/A`, the log displays just `ant/A`.

The log is capped to the most recent 50 entries.

## Related

- [Configure broker connection settings (host, port, credentials, TLS)](../../getting-started/setup/configure-broker-connection-settings-host-port-credentials-tls.md)
- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Enable TLS with a custom CA certificate](enable-tls-with-a-custom-ca-certificate.md)
- [Add or remove custom publish buttons](add-or-remove-custom-publish-buttons.md)
- [Subscribe to MQTT topics and toggle panadapter display](subscribe-to-mqtt-topics-and-toggle-panadapter-display.md)
- [Overlay an MQTT value on the panadapter](overlay-an-mqtt-value-on-the-panadapter.md)
- [Publish a canned message with a button (e.g. rotator preset)](publish-a-canned-message-with-a-button-e-g-rotator-preset.md)