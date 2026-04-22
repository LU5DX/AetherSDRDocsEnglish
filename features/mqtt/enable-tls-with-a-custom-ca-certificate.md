# Enable TLS with a custom CA certificate

This page explains how to turn on TLS encryption for the MQTT connection and, optionally, supply a custom CA certificate when your broker uses a private or self-signed certificate authority.

## Before you start

- The MQTT applet must be available. If the MQTT tray button is not visible on the right sidebar, your build of AetherSDR may not include MQTT support.
- Your broker must be configured for TLS, typically listening on port 8883.
- If your broker uses a private CA, have the CA certificate file path ready (PEM format).

## Steps

1. Click the MQTT tray button on the right sidebar to open the MQTT applet.
2. If the connection is currently active (Enable shows "On"), click Enable to toggle it to "Off". Settings cannot be changed while connected.
3. Check the TLS checkbox. The Port field automatically changes from `1883` to `8883`, and the CA cert row appears below TLS.
4. Confirm the Port field shows the correct port for your broker. The default after enabling TLS is `8883`; edit it if your broker uses a different port.
5. In the CA cert field, enter the full path to your CA certificate file. Leave the field blank to use the system CA bundle instead.
6. Verify the Host, Port, User, Pass, and Topics fields are correct.
7. Click Enable. The button changes to "On" and all settings — including `MqttTls` and `MqttCaFile` — are saved. The status label changes to "Connected" in green when the broker accepts the connection.

## What each control does

| Label | Kind | Default | Notes | Setting key |
|---|---|---|---|---|
| TLS | Checkbox | Off (unchecked) | Enables TLS encryption. Shows the CA cert row and auto-switches Port between `1883` and `8883`. | `MqttTls` |
| CA cert | Text field | *(blank)* | Path to a CA certificate file. Visible only when TLS is checked. Blank means the system CA bundle is used. | `MqttCaFile` |
| Port | Text field | `1883` (no TLS) / `8883` (TLS) | Valid range: 1–65535. Automatically updated when TLS is toggled, but can be edited manually. | `MqttPort` |
| Enable | Toggle button | Off | Connects or disconnects. Saves all settings — including TLS and CA cert — when toggled to "On". | *(not persisted independently)* |

## Tips

- If you uncheck TLS after having set it to port `8883`, the Port field automatically reverts to `1883`. Check the port value before clicking Enable if your broker uses a non-standard port.
- The CA cert row is hidden when TLS is unchecked. If you cannot see the CA cert field, confirm the TLS checkbox is checked.
- Settings are saved only when Enable is clicked to the "On" position. Editing fields and then closing the applet without clicking Enable does not persist changes.
- The status label shows "Disconnected" in grey, "Connected" in green, or an error message if the connection fails — for example, if the CA certificate path is wrong or the certificate does not validate the broker.

## Troubleshooting

- **Status label shows an error after clicking Enable with TLS on** — The broker certificate could not be verified. Confirm the CA cert path is correct and the file is readable. If your broker uses a public CA, try leaving CA cert blank to fall back to the system CA bundle.
- **CA cert field is not visible** — The TLS checkbox is not checked. Check the TLS checkbox; the CA cert row appears immediately.
- **Port reverted to 1883 after unchecking TLS** — This is expected behavior. Re-enter your broker's port manually if it is non-standard.
- **Enable toggles back to "Off" immediately** — The broker is unreachable or rejected the connection. Check the Host, Port, and TLS settings, and confirm the broker is running and accessible from this machine.

## Related

- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Subscribe to rotator / antenna switch topics](subscribe-to-rotator-antenna-switch-topics.md)
- [MQTT overview](overview.md)
