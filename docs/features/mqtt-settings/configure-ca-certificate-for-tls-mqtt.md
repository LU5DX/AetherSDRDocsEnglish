# Configure MQTT Settings

The MQTT Settings dialog centralizes all MQTT configuration: broker connection, topic subscriptions, and publish buttons. It replaces the in-applet settings panel from earlier versions.

## Before you start

- The MQTT Settings dialog is open (`Settings > MQTT...`).

## Broker tab

Configure the broker connection parameters.

1. In the **Host** field, enter the broker hostname or IP address (default `localhost`).
2. In the **Port** field, enter the broker TCP port (default `1883`, range 1–65535). The port auto-switches between 1883 and 8883 when you toggle TLS.
3. Optionally, enter a **User** name for broker authentication.
4. Optionally, enter a **Password** (masked). The password is stored in the system keychain. If no keychain is available, the password is kept in memory only for the current session and must be re-entered on the next launch. It is never written to the settings store in plaintext.
5. Check **Use TLS** to enable TLS encryption. This auto-switches the port between 1883 and 8883.
6. If TLS is enabled, optionally specify a **CA cert** file path. Leave blank to use the system CA bundle. Click **Browse...** to select a file.
7. Click **Apply** to save settings without closing, or **Ok** to save and close.

### Broker controls

| Control | Description | Default | Setting key |
|---|---|---|---|
| **Host** | Broker hostname or IP address. | `localhost` | `MqttHost` |
| **Port** | Broker TCP port (1–65535). Auto-switches between 1883 and 8883 when TLS is toggled. | `1883` | `MqttPort` |
| **User** | Broker username (optional). | blank | `MqttUser` |
| **Password** | Broker password (optional, masked). Stored in system keychain with one-shot migration from legacy plaintext settings. Falls back to session-only memory storage when keychain is unavailable. | blank | — |
| **Use TLS** | Checkbox enabling TLS encryption. Auto-switches the port between 1883 and 8883. Shows/hides the CA cert row. | unchecked | `MqttTls` |
| **CA cert** | Path to a CA certificate file. Blank means use the system CA bundle. Visible only when TLS is checked. | blank | `MqttCaFile` |

## Subscriptions tab

Manage subscribed topics.

1. In the **Subscriptions** tab, the table lists subscribed topics. Each row has:
   - **Topic**: editable subscription topic string.
   - **Display**: checkbox controlling whether the topic appears on the panadapter overlay.
2. Click **Add** to add a new row, or **Remove** to delete the selected row.
3. The **Internal AetherSDR Topics** group box lists topics subscribed automatically when MQTT connects. These topics cannot be removed:

| Topic | Description | Gateable | Default enabled |
|---|---|---|---|
| `aethersdr/antenna/alias/+` | Antenna name (per-port) | No (always on) | On |
| `aethersdr/antenna/alias` | Antenna names (bulk) | No (always on) | On |
| `aethersdr/cw/transmit` | CW keyer input | Yes | On |
| `aethersdr/ax25/tx` | AX.25 transmit | Yes | On |

Note: The `defaultEnabled` column shows the initial state when per-topic gating was introduced in v26.6.3. For topics listed as always on (`Gateable = No`), the checkbox is grayed out and cannot be changed.

## Publish Buttons tab

Manage up to 12 publish buttons.

1. In the **Publish Buttons** tab, the table lists button definitions. Each row has:
   - **Label**: button display text.
   - **Topic**: MQTT topic to publish to.
   - **Payload**: payload text to publish.
2. Click **Add** to add a new row, or **Remove** to delete the selected row. The **Add** button is disabled when 12 rows are present.
3. Button definitions are shared with the MQTT applet.

## Troubleshooting

- **Connection fails with "certificate verify failed"** — The CA certificate file path is incorrect or the certificate does not match the broker. Verify the file path and that the certificate is the CA that signed the broker's certificate.
- **Password is lost between launches** — This occurs when the system keychain is unavailable. The password is held in memory for the current session only and must be re-entered on the next launch.
- **Publish or subscribe topic not working** — Check the **Subscriptions** tab to ensure the desired topic is present, and verify the **Display** checkbox if you expect overlay output.

## Related

- [Configure MQTT broker connection (host, port, credentials, TLS)](../../getting-started/setup/configure-mqtt-broker-connection-host-port-credentials-tls.md)
- [MQTT Settings overview](overview.md)