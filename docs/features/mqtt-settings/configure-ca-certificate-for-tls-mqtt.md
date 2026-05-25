# Configure CA certificate for TLS MQTT

Provide a custom CA certificate file when connecting to an MQTT broker that uses a self-signed or private Certificate Authority. When no CA certificate file is specified, AetherSDR uses the system CA bundle.

## Before you start

- You have a CA certificate file in PEM format on your local filesystem.
- The MQTT Settings dialog is open (`Settings > MQTT...`).

## Steps

1. In the **Broker** tab, check **Use TLS**.
2. In the **CA cert** field, enter the full filesystem path to your CA certificate file, or click **Browse...** to select it.
3. Click **Apply** to save without closing, or **Ok** to save and close.

## What each control does

| Control | Description | Default | Setting key |
|---|---|---|---|
| **Use TLS** | Checkbox that enables TLS encryption. Checking it auto-switches the port from 1883 to 8883 (and vice versa when unchecked). | unchecked | `MqttTls` |
| **CA cert** | Text field for the CA certificate file path. Visible only when **Use TLS** is checked. Leave blank to use the system CA bundle. The **Browse...** button opens a file selection dialog. | blank | `MqttCaFile` |

## Troubleshooting

- **Connection fails with "certificate verify failed"** — The CA certificate file path is incorrect or the certificate does not match the broker. Verify the file path and that the certificate is the CA that signed the broker's certificate.

## Related

- [Configure MQTT broker connection (host, port, credentials, TLS)](../../getting-started/setup/configure-mqtt-broker-connection-host-port-credentials-tls.md)
- [MQTT Settings overview](overview.md)
