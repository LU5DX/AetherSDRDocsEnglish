# MQTT Settings overview

The MQTT Settings dialog is the central configuration interface for all MQTT functionality in AetherSDR. It lets you connect to an MQTT broker, subscribe to topics (with optional panadapter overlay display), define up to 12 publish buttons, and enable or disable individual internal AetherSDR topics. This page describes the dialog as a whole and points to step-by-step instructions for individual tasks.

## How it works

The MQTT Settings dialog replaces the earlier in-applet settings panel. It is organized into three tabs:

- **Broker** — MQTT broker host, port, username, password, TLS, and CA certificate.
- **Subscriptions** — A table of topics your radio subscribes to. Each row has an editable Topic and a Display checkbox that shows topic data on the panadapter overlay. Below the table is a group box listing internal AetherSDR subscription topics. Each internal topic has an Enable checkbox; topics labeled as always active are grayed out and cannot be disabled.
- **Publish Buttons** — A table defining up to 12 buttons. Each row has Label, Topic, and Payload (all editable). These buttons appear in the MQTT applet in the Applet Panel tray. Below the table is a group box listing internal AetherSDR publish topics with Enable checkboxes.

The dialog also includes Ok, Apply, and Cancel buttons. Apply saves all settings (connection, topics, button definitions, password, and internal topic enable states) without closing the dialog.

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

The **Internal AetherSDR Topics** group box lists topics that are subscribed automatically when MQTT connects. Each topic has an Enable checkbox. Topics labeled as always active are shown grayed out and cannot be disabled. The following internal subscription topics are available:

| Topic | Description | Default | User-disableable |
|-------|-------------|---------|------------------|
| `aethersdr/antenna_alias/+/name` | Antenna name (per-port) | On | No (always active) |
| `aethersdr/antenna_alias/bulk` | Antenna names (bulk) | On | No (always active) |
| `aethersdr/cw/transmit` | CW keyer input | On | Yes |
| `aethersdr/ax25/tx` | AX.25 transmit | On | Yes |

### Publish Buttons tab

| Control | Label | Behavior |
|---------|-------|----------|
| Table columns | Label, Topic, Payload | All three columns are editable text. Label is the button text shown in the MQTT applet. |
| Push button | Add | Inserts a new empty row. Disabled when the table already has 12 rows. |
| Push button | Remove | Removes all selected rows. |

The **Internal AetherSDR Topics** group box lists topics that are published automatically when MQTT is connected. Each topic has an Enable checkbox. The following internal publish topics are available:

| Topic | Description | Default | User-disableable |
|-------|-------------|---------|------------------|
| `aethersdr/cw/decode` | CW decoded text | On | Yes |
| `aethersdr/radio/state` | Radio VFO / mode / TX state | Off | Yes |
| `aethersdr/ax25/rx` | AX.25 received frames | Off | Yes |

## Tips

- Click Apply to save your settings without closing the dialog. This is useful if you want to test the connection immediately.
- The Password field stores credentials in the system keychain when `HAVE_KEYCHAIN` is set. Legacy plaintext passwords in the `MqttPass` AppSettings key are migrated on first save.
- Disable internal topics you do not need to reduce MQTT traffic. Topics labeled "always active" cannot be disabled because they are required for antenna alias functionality.
- If you use relay scripts that forward `aethersdr/cw/decode` into `aethersdr/cw/transmit`, filter on the topic namespace (`aethersdr/...`) to avoid re-publishing AetherSDR's own output back to it and creating a feedback loop.

## Related

- [Configure MQTT broker connection (host, port, credentials, TLS)](../../getting-started/setup/configure-mqtt-broker-connection-host-port-credentials-tls.md)
- [Subscribe to MQTT topics and toggle panadapter display](../mqtt/subscribe-to-mqtt-topics-and-toggle-panadapter-display.md)
- [Add or remove publish buttons](add-or-remove-publish-buttons.md)
- Enable or disable internal MQTT topics
- [Configure CA certificate for TLS MQTT](configure-ca-certificate-for-tls-mqtt.md)
- [Open MQTT settings from the MQTT applet](open-mqtt-settings-from-the-mqtt-applet.md)