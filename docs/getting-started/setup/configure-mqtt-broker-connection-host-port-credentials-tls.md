# Configure MQTT broker connection (host, port, credentials, TLS)

This page explains how to enter the connection details for your MQTT broker so that AetherSDR can publish radio state and subscribe to topics.

## Before you start

- You need the hostname or IP address of your MQTT broker.
- You need the broker’s TCP port (default 1883, or 8883 with TLS).
- If the broker requires authentication, have the username and password ready.
- If using TLS with a custom CA certificate, have the certificate file path available.

## Steps

1. Open **Settings > MQTT...**. The MQTT Settings dialog opens to the Broker tab.
2. In **Host**, type the broker hostname or IP address (default `localhost`).
3. In **Port**, set the TCP port (default 1883, valid range 1–65535).
4. Optionally, enter a **User** and **Password** for broker authentication.
5. If the broker requires TLS, check **Use TLS**. The Port value automatically switches from 1883 to 8883 (and back when unchecked).
6. If you use a custom CA certificate, enter its path in **CA cert** or click **Browse...** to select the file. Leave blank to use the system CA bundle.
7. Click **Apply** to save the connection settings without closing the dialog, or click **OK** to save and close.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---------|---------|-------------|-------------|----------|
| Host | `localhost` | any hostname/IP | `MqttHost` (migrated to `MqttSettings`) | Broker hostname or IP address |
| Port | `1883` | 1–65535 | `MqttPort` (migrated to `MqttSettings`) | Broker TCP port; auto-flips to 8883 when TLS is enabled |
| User | (empty) | any text | `MqttUser` (migrated to `MqttSettings`) | Broker username (optional) |
| Password | (empty) | any text | stored in system keychain (qt6keychain) or plaintext fallback | Broker password (optional, masked) |
| Use TLS | unchecked | – | `MqttTls` (migrated to `MqttSettings`) | Enables TLS encryption; shows/hides the CA cert row |
| CA cert | (empty) | file path or blank | `MqttCaFile` (migrated to `MqttSettings`) | Path to a custom CA certificate file; blank = system CA bundle |

## Tips

- If your broker does not require a password, leave the **Password** field empty.
- When **Use TLS** is checked, AetherSDR automatically flips the port to 8883. If your broker uses a different TLS port, adjust **Port** manually after checking TLS.
- The password is stored in the system keychain when available; otherwise it falls back to plaintext storage in AppSettings.

## Related

- [Configure CA certificate for TLS MQTT](../../features/mqtt-settings/configure-ca-certificate-for-tls-mqtt.md)
- [Subscribe to MQTT topics and toggle panadapter display](../../features/mqtt/subscribe-to-mqtt-topics-and-toggle-panadapter-display.md)
- [Add or remove publish buttons](../../features/mqtt-settings/add-or-remove-publish-buttons.md)
