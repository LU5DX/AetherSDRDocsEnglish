# Configure MQTT Publish Buttons

## Steps

1. In the MQTT Settings dialog, click the **Publish Buttons** tab.

   The Publish Buttons tab shows a table with columns **Label**, **Topic**, and **Payload**.

2. To add a button:
   - Click **Add** to insert a new blank row.
   - The Add button is disabled when 12 rows exist (maximum).
   - Enter a **Label** (button text), **Topic** (MQTT topic to publish to), and **Payload** (message to send).

3. To remove a button:
   - Click in the row you want to remove.
   - Click **Remove**.

4. Click **Apply** to save your button definitions without closing the dialog, or click **OK** to save and close.

## Subscriptions tab

The **Subscriptions** tab contains a table where you can add and manage MQTT topic subscriptions:

- **Topic** (editable text field): The MQTT topic to subscribe to.
- **Display** (checkbox): When checked, enables the panadapter overlay display for that topic.

Use the **Add** and **Remove** buttons below the table to manage subscriptions. The **Internal AetherSDR Topics** group box shows topics that are subscribed automatically when MQTT connects and cannot be removed.

## What the Internal AetherSDR Topics section shows

The **Internal AetherSDR Topics** group box appears on both the **Subscriptions** tab and the **Publish Buttons** tab.

### On the Publish Buttons tab

The **Internal AetherSDR Topics** group box lists topics that AetherSDR publishes automatically whenever MQTT is connected. Each topic has a checkbox that allows you to enable or disable it individually. Topics marked as gateable (not grayed out) can be toggled; non-gateable topics are always active and shown grayed out.

The publish topics are:

| Topic | Description | Default | Gateable |
|-------|-------------|---------|----------|
| `aethersdr/cw/decode` | CW decoded text | On | Yes |
| `aethersdr/radio/state` | Radio VFO / mode / TX state | Off | Yes |
| `aethersdr/ax25/rx` | AX.25 received frames | On | Yes |

### On the Subscriptions tab

The subscribe topics shown in the **Internal AetherSDR Topics** group box on the **Subscriptions** tab are:

| Topic | Description | Default | Gateable |
|-------|-------------|---------|----------|
| `aethersdr/antenna/alias/+` | Antenna name (per-port) | On | No |
| `aethersdr/antenna/alias` | Antenna names (bulk) | On | No |
| `aethersdr/cw/transmit` | CW keyer input | Off | Yes |
| `aethersdr/ax25/tx` | AX.25 transmit | Off | Yes |

When you enable or disable a gateable internal topic, the setting is stored and takes effect the next time MQTT connects or reconnects.

## Maximum number of publish buttons

You can define up to **12 publish buttons**. The Add button is disabled when 12 rows exist.

## Password storage

The MQTT password is stored in your system keychain. If your system does not support keychain storage, the password is kept in memory only for the current session and must be re-entered the next time you launch AetherSDR. A legacy plaintext password (from an earlier version) is migrated to the keychain the first time it is used, then removed from the settings store.

## Related

- [MQTT Settings overview](overview.md)
- [Configure MQTT broker connection (host, port, credentials, TLS)](../../getting-started/setup/configure-mqtt-broker-connection-host-port-credentials-tls.md)
- [Subscribe to MQTT topics and toggle panadapter display](../mqtt/subscribe-to-mqtt-topics-and-toggle-panadapter-display.md)
- [Configure CA certificate for TLS MQTT](configure-ca-certificate-for-tls-mqtt.md)