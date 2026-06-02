# MQTT Settings overview

The MQTT Settings dialog is the central configuration interface for all MQTT functionality in AetherSDR. It lets you connect to an MQTT broker, subscribe to topics (with optional panadapter overlay display), and define up to 12 publish buttons. This page describes the dialog as a whole and points to step-by-step instructions for individual tasks.

## How it works

The MQTT Settings dialog replaces the earlier in-applet settings panel. It is organized into three tabs:

- **Broker** — MQTT broker host, port, username, password, TLS, and CA certificate.
- **Subscriptions** — A table of topics your radio subscribes to. Each row has an editable Topic and a Display checkbox that shows topic data on the panadapter overlay. Below the table is a read-only group box listing the internal AetherSDR topics that are subscribed automatically and cannot be removed.
- **Publish Buttons** — A table defining up to 12 buttons. Each row has Label, Topic, and Payload (all editable). These buttons appear in the MQTT applet in the Applet Panel tray. Below the table is a read-only group box listing internal AetherSDR topics that are published automatically and cannot be modified.

The dialog also includes Ok, Apply, and Cancel buttons. Apply saves all settings (connection, topics, buttons, and password) without closing the dialog.

## What each control does

### Broker tab

| Control | Label | Default | Range | Behavior | Setting key |
|---------|-------|---------|-------|----------|-------------|
| Text field | Host | `localhost` | — | Broker hostname or IP address. | `MqttHost` |
| Spin box | Port | `1883` | 1–65535 | Broker TCP port. Auto-switches to 8883 when TLS is toggled and vice versa. | `MqttPort` |
| Text field | User | *(empty)* | — | Broker username (optional). | `MqttUser` |
| Text field (masked) | Password | *(empty)* | — | Broker password (optional). Stored in the system keychain when available; falls back to plaintext `MqttPass` AppSettings key otherwise. | — |
| Check box | Use TLS | unchecked | — | Enable TLS encryption. Auto-flips the port between 1883 and 8883. Shows/hides the CA cert row. | `MqttTls` |
| Text field + Browse button | CA cert | *(empty)* | — | Path to a CA certificate file. Blank means use the system CA bundle. Row visible only when Use TLS is checked. | `MqttCaFile` |

### Subscriptions tab

| Control | Label | Behavior |
|---------|-------|----------|
| Table columns | Topic, Display | Topic is an editable text field. Display is a checkbox; when checked, the topic's payload is drawn on the panadapter overlay. |
| Push button | Add | Inserts a new empty row. |
| Push button | Remove | Removes all selected rows. |

The **Internal AetherSDR Topics** group box lists topics that are subscribed automatically whenever MQTT connects. These topics are not user-removable.

### Publish Buttons tab

| Control | Label | Behavior |
|---------|-------|----------|
| Table columns | Label, Topic, Payload | All three columns are editable text. Label is the button text shown in the MQTT applet. |
| Push button | Add | Inserts a new empty row. Disabled when the table already has 12 rows. |
| Push button | Remove | Removes all selected rows. |

The **Internal AetherSDR Topics** group box lists topics that are published automatically whenever MQTT is connected. These topics are not user-configurable. Currently the following topics are published:

- `aethersdr/cw/decode`

This group box is part of the Publish Buttons tab and shows the topics in a read-only text area that allows text selection by mouse.

## Tips

- Click Apply to save your settings without closing the dialog. This is useful if you want to test the connection immediately.
- The Password field stores credentials in the system keychain when `HAVE_KEYCHAIN` is set. Legacy plaintext passwords in the `MqttPass` AppSettings key are migrated on first save.

## Related

- [Configure MQTT broker connection (host, port, credentials, TLS)](../../getting-started/setup/configure-mqtt-broker-connection-host-port-credentials-tls.md)
- [Subscribe to MQTT topics and toggle panadapter display](../mqtt/subscribe-to-mqtt-topics-and-toggle-panadapter-display.md)
- [Add or remove publish buttons](add-or-remove-publish-buttons.md)
- [Configure CA certificate for TLS MQTT](configure-ca-certificate-for-tls-mqtt.md)
- [Open MQTT settings from the MQTT applet](open-mqtt-settings-from-the-mqtt-applet.md)