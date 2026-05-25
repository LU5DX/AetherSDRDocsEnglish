# Publish a canned message with a button (e.g. rotator preset)

This page shows how to add a publish button to the MQTT applet and use it to send a fixed message to your broker — for example, sending a rotator preset command with a single click.

## Before you start

- The MQTT applet must be visible. If it is not, click the MQTT tray button on the right sidebar to show it.
- You must have a broker connection configured. See [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md).
- The applet must be connected (Enable shows "On" and the status label reads "Connected") before publish buttons will fire.

## Steps

1. Open the MQTT applet by clicking the MQTT tray button on the right sidebar.
2. If you are not already connected, click Settings... to open the MQTT Settings dialog. Configure the broker connection details (Host, Port, User, Password), subscription topics, and publish buttons. Click OK to save.
3. Click Enable to set it to "On". Wait for the status label to read "Connected".
4. Click any publish button to send its configured payload to its configured topic immediately. The button is only active while connected.

## What each control does

| Control         | Kind                                                                                                                                        | Default                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Settings...     | Opens the MQTT Settings dialog (MqttSettingsDialog) for broker connection, subscriptions, and publish button configuration.                 | New in v26.5.3. Replaces the inline Host/Port/User/Pass/TLS/Topics fields.          |
| Publish buttons | Click publishes the configured payload to the configured topic via MqttClient::publish. Buttons are configured in the MQTT Settings dialog. | Only active while connected. Configured via MqttSettingsDialog Publish Buttons tab. |
| Message log     | Displays received messages as "topic: value" lines. Also processes antenna alias updates from MQTT.                                        | Capped to 50 entries.                                                               |
| Enable (Off/On) | Toggle button to connect or disconnect from the broker using settings from MqttSettingsDialog.                                              | Off. Password is loaded from system keychain on first enable.                       |

## Indicators

| Indicator    | States                                    | Meaning                                                                                       |
|--------------|-------------------------------------------|-----------------------------------------------------------------------------------------------|
| Status label | Disconnected, Connected, <error message>  | Connection state with colour: green when connected, grey when disconnected, default on error. |

## Tips

- Password is stored in the system keychain and loaded automatically when you first enable the connection. If the keychain password is not yet loaded, the status shows "Waiting for keychain".
- Broker connection settings (host, port, credentials, TLS, and subscriptions) are configured in the MQTT Settings dialog (Settings > MQTT...) rather than inline in the applet.
- Published button definitions are stored as JSON under `MqttButtons` and persist across restarts.
- Hovering over a button in normal mode shows a tooltip with the configured topic and payload so you can confirm what will be sent before clicking.

## Troubleshooting

- **Clicking a publish button does nothing** — The applet is not connected. Check that Enable reads "On" and the status label reads "Connected". If it shows an error, verify your broker settings and click Enable to reconnect.
- **Button is missing after restart** — Settings are saved when you confirm the MQTT Settings dialog. If AetherSDR was force-closed, the `MqttButtons` key may not have been written. Reconfigure the button.
- **Status shows "Waiting for keychain"** — The system keychain has not yet provided the stored password. This usually resolves automatically after a few seconds. If it persists, check your system keychain configuration.

## Related

- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Add or remove custom publish buttons](add-or-remove-custom-publish-buttons.md)
- [Subscribe to rotator / antenna switch topics](subscribe-to-rotator-antenna-switch-topics.md)
- [MQTT overview](overview.md)