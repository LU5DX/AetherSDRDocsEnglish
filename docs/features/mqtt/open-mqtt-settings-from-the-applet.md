# Open MQTT settings from the applet

Open the MQTT Settings dialog from the MQTT applet to configure broker connection, subscriptions, and publish button settings.

## Before you start

- The MQTT applet must be visible. Toggle it with the MQTT tray button on the right sidebar.
- The MQTT feature must be compiled in (requires `HAVE_MQTT` build gate).

## Steps

1. In the MQTT applet header, click **Settings...**.
2. The MQTT Settings dialog opens.

## What each control does

| Control | Behavior |
|---|---|
| **Settings...** button | Opens the MQTT Settings dialog (`MqttSettingsDialog`) for broker connection, subscriptions, and publish button configuration. |

## Related

- [Configure broker connection settings (host, port, credentials, TLS)](../../getting-started/setup/configure-broker-connection-settings-host-port-credentials-tls.md)
- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Enable TLS with a custom CA certificate](enable-tls-with-a-custom-ca-certificate.md)
- [Add or remove custom publish buttons](add-or-remove-custom-publish-buttons.md)
- [Subscribe to MQTT topics and toggle panadapter display](subscribe-to-mqtt-topics-and-toggle-panadapter-display.md)
- [Overlay an MQTT value on the panadapter](overlay-an-mqtt-value-on-the-panadapter.md)
- [Publish a canned message with a button (e.g. rotator preset)](publish-a-canned-message-with-a-button-e-g-rotator-preset.md)
