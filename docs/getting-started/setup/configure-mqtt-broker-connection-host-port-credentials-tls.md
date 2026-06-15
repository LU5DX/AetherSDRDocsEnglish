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

## Subscriptions tab

The **Subscriptions** tab replaces the comma-separated Topics text field from earlier versions. It contains:

- **Topic table**: Each row has an editable Topic text field and a Display checkbox. When checked, the topic’s messages appear on the panadapter overlay. Use the **Add** and **Remove** buttons below the table to manage rows.
- **Internal AetherSDR Topics**: A read-only group box listing topics that AetherSDR subscribes to automatically when the MQTT connection is active. Each topic has a checkbox to enable or disable it. Topics with non-gateable behavior (antenna alias topics) are always active and appear grayed out. The available internal subscribe topics are:

  | Topic | Description | User-disableable |
  |-------|-------------|------------------|
  | `aethersdr/antenna/alias/+` | Antenna name (per-port) | No |
  | `aethersdr/antenna/alias/bulk` | Antenna names (bulk) | No |
  | `aethersdr/cw/transmit` | CW keyer input | Yes (off by default) |
  | `aethersdr/ax25/tx` | AX.25 transmit | Yes (off by default) |

  Uncheck the checkbox next to a gateable topic to prevent AetherSDR from subscribing to it.

## Publish Buttons tab

The **Publish Buttons** tab lets you define up to 12 publish buttons. Each row in the table has three editable text fields: **Label**, **Topic**, and **Payload**. Use the **Add** and **Remove** buttons below the table to manage rows. The Add button is disabled when 12 rows are reached.

The tab also includes an **Internal AetherSDR Topics** group box showing topics that AetherSDR publishes automatically when the MQTT connection is active. Each topic has a checkbox to enable or disable it. The available internal publish topics are:

| Topic | Description | Default enabled |
|-------|-------------|-----------------|
| `aethersdr/cw/decode` | CW decoded text | Yes |
| `aethersdr/radio/state` | Radio VFO / mode / TX state | Yes |
| `aethersdr/ax25/rx` | AX.25 received frames | Yes |

Uncheck the checkbox next to a topic to prevent AetherSDR from publishing to it.

## Tips

- If your broker does not require a password, leave the **Password** field empty.
- When **Use TLS** is checked, AetherSDR automatically flips the port to 8883. If your broker uses a different TLS port, adjust **Port** manually after checking TLS.
- The password is stored in the system keychain when available; otherwise it falls back to plaintext storage in AppSettings.
- Relay scripts that forward `aethersdr/cw/decode` into `aethersdr/cw/transmit` should filter on the topic namespace (`aethersdr/...`) to avoid re-publishing AetherSDR's own output back to it and creating a feedback loop.

## Related

- [Configure CA certificate for TLS MQTT](../../features/mqtt-settings/configure-ca-certificate-for-tls-mqtt.md)
- [Subscribe to MQTT topics and toggle panadapter display](../../features/mqtt/subscribe-to-mqtt-topics-and-toggle-panadapter-display.md)
- [Add or remove publish buttons](../../features/mqtt-settings/add-or-remove-publish-buttons.md)