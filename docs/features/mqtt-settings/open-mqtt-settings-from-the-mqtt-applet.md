# Configure MQTT Publish Buttons

## Steps

1. In the MQTT Settings dialog, click the **Publish Buttons** tab.

   The Publish Buttons tab shows a table with columns **Label**, **Topic**, and **Payload**, plus an **Internal AetherSDR Topics** read-only group box.

2. To add a button:
   - Click **Add** to insert a new blank row.
   - The Add button is disabled when 12 rows exist (maximum).
   - Enter a **Label** (button text), **Topic** (MQTT topic to publish to), and **Payload** (message to send).

3. To remove a button:
   - Click in the row you want to remove.
   - Click **Remove**.

4. Click **Apply** to save your button definitions without closing the dialog, or click **OK** to save and close.

## What the Internal AetherSDR Topics section shows

The **Internal AetherSDR Topics** group box lists topics that AetherSDR publishes automatically whenever MQTT is connected:

- `aethersdr/cw/decode`

These topics are not user-configurable and cannot be removed. They appear automatically on the broker when the corresponding feature is active.

## Maximum number of publish buttons

You can define up to **12 publish buttons**. The Add button is disabled when 12 rows exist.

## Related

- [MQTT Settings overview](overview.md)
- [Configure MQTT broker connection (host, port, credentials, TLS)](../../getting-started/setup/configure-mqtt-broker-connection-host-port-credentials-tls.md)
- [Subscribe to MQTT topics and toggle panadapter display](../mqtt/subscribe-to-mqtt-topics-and-toggle-panadapter-display.md)
- [Configure CA certificate for TLS MQTT](configure-ca-certificate-for-tls-mqtt.md)