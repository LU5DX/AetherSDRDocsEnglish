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

## Publish Buttons tab

| Control | Description | Default | Setting key |
|---|---|---|---|
| **Internal AetherSDR Topics** | Read-only group box that lists topics published automatically when MQTT is connected. Each topic can be toggled on or off via a checkbox. Topics with a grayed-out checkbox are always active and cannot be disabled. | See table below | — |

### Internal publish topics

| Topic | Description | Gateable | Default enabled |
|---|---|---|---|
| `aethersdr/cw/decode` | CW decoded text | Yes | On |
| `aethersdr/radio/state` | Radio VFO / mode / TX state | Yes | Off |
| `aethersdr/ax25/rx` | AX.25 received frames | Yes | Off |

## Subscriptions tab

| Control | Description | Default | Setting key |
|---|---|---|---|
| **Internal AetherSDR Topics** | Read-only group box that lists topics subscribed automatically when MQTT connects. Each topic can be toggled on or off via a checkbox. Topics with a grayed-out checkbox are always active and cannot be disabled. | See table below | `mqtt_internal_<sanitized_topic>` |

### Internal subscribe topics

| Topic | Description | Gateable | Default enabled |
|---|---|---|---|
| `aethersdr/antenna/alias/+` | Antenna name (per-port) | No (always on) | On |
| `aethersdr/antenna/alias` | Antenna names (bulk) | No (always on) | On |
| `aethersdr/cw/transmit` | CW keyer input | Yes | On |
| `aethersdr/ax25/tx` | AX.25 transmit | Yes | On |

Note: The `defaultEnabled` column shows the initial state when per-topic gating was introduced in v26.6.3. For topics listed as always on (`Gateable = No`), the checkbox is grayed out and cannot be changed.

## Troubleshooting

- **Connection fails with "certificate verify failed"** — The CA certificate file path is incorrect or the certificate does not match the broker. Verify the file path and that the certificate is the CA that signed the broker's certificate.
- **Publish or subscribe topic not working** — Check the **Internal AetherSDR Topics** section to ensure the desired topic is enabled (checkbox checked). Topics can be individually disabled to reduce network traffic.

## Related

- [Configure MQTT broker connection (host, port, credentials, TLS)](../../getting-started/setup/configure-mqtt-broker-connection-host-port-credentials-tls.md)
- [MQTT Settings overview](overview.md)