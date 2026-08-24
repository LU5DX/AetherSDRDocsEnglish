# Enable TLS with a custom CA certificate

This page explains how to turn on TLS encryption for the MQTT connection and, optionally, supply a custom CA certificate when your broker uses a private or self-signed certificate authority.

## Before you start

- The MQTT applet must be available. If the MQTT tray button is not visible on the right sidebar, your build of AetherSDR may not include MQTT support.
- Your broker must be configured for TLS, typically listening on port 8883.
- If your broker uses a private CA, have the CA certificate file path ready (PEM format).

## Steps

1. Click the MQTT tray button on the right sidebar to open the MQTT applet.
2. If the connection is currently active (Enable shows "On"), click Enable to toggle it to "Off". Settings cannot be changed while connected.
3. Click **Settings...** to open the MQTT Settings dialog.
4. In the **MQTT Settings** dialog, configure the TLS settings:
   - Switch to the **Connection** tab.
   - Enable the **Use TLS** checkbox.
   - The Port field automatically changes from `1883` to `8883`.
   - In the **CA certificate** field, enter the full path to your CA certificate file. Leave the field blank to use the system CA bundle instead.
5. Confirm the Host, Port, and other connection fields are correct.
6. Click **OK** to save the connection settings and close the dialog.
7. Click Enable. The button changes to "On" and all settings are saved. The status label changes to "Connected" in green when the broker accepts the connection.

## What each control does

| Label           | Kind                                                                                                                                        | Default                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Enable          | Toggle button. Connects or disconnects from the broker. Password is loaded from system keychain on first enable.                            | Off                                                                                 |
| Settings...     | Push button. Opens the MQTT Settings dialog for broker connection, subscriptions, and publish button configuration.                         | None                                                                                |
| Publish buttons | Click publishes the configured payload to the configured topic via MqttClient::publish. Buttons are configured in the MQTT Settings dialog. | Only active while connected. Configured via MqttSettingsDialog Publish Buttons tab. |
| Message log     | Displays received messages as 'topic: value' lines. Also processes antenna alias updates from MQTT.                                         | Capped to 50 entries.                                                               |
## Indicators

| Label        | States                                    | Meaning                                                                                 |
|--------------|-------------------------------------------|-----------------------------------------------------------------------------------------|
| Status label | "Disconnected", "Connected", <error message> | Connection state with colour: green when connected, grey when disconnected, default on error. |

## Tips

- The password is stored in the system keychain and is loaded automatically when you first enable the connection. On builds without keychain support, the password is stored for the current session only and must be re-entered after restarting AetherSDR.
- If you uncheck TLS after having set it to port `8883`, the Port field automatically reverts to `1883`. Check the port value before clicking Enable if your broker uses a non-standard port.
- The CA certificate field is only available when the Use TLS checkbox is checked.
- Settings are saved when you click **OK** in the MQTT Settings dialog or when Enable is clicked to the "On" position.
- The status label shows "Disconnected" in grey, "Connected" in green, or an error message if the connection fails — for example, if the CA certificate path is wrong or the certificate does not validate the broker.
- The MQTT applet now supports theming. Colors adapt to the selected theme using `ThemeManager`.
- The message log now displays both received messages and published messages. Published messages are prefixed with "TX" followed by the topic and payload (truncated to 80 characters).

## Troubleshooting

- **Status label shows an error after clicking Enable with TLS on** — The broker certificate could not be verified. Confirm the CA cert path is correct and the file is readable. If your broker uses a public CA, try leaving CA cert blank to fall back to the system CA bundle.
- **CA certificate field is not visible** — The Use TLS checkbox is not checked. Check the Use TLS checkbox; the CA certificate field appears immediately.
- **Port reverted to 1883 after unchecking TLS** — This is expected behavior. Re-enter your broker's port manually if it is non-standard.
- **Enable toggles back to "Off" immediately** — The broker is unreachable or rejected the connection. Check the Host, Port, and TLS settings, and confirm the broker is running and accessible from this machine.
- **Status shows 'Waiting for keychain'** — The system keychain is not unlocked or the password has not been saved yet. Re-enter the password in the MQTT Settings dialog and try again. On builds without keychain support, the password is session-only and you must re-enter it after restarting AetherSDR.

## Related

- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Subscribe to rotator / antenna switch topics](subscribe-to-rotator-antenna-switch-topics.md)
- [MQTT overview](overview.md)