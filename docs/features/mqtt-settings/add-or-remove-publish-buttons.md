# Add or remove publish buttons

Configure up to 12 publish buttons that send MQTT messages with a single click. Each button has a label, topic, and payload that you define in the Publish Buttons tab of the MQTT Settings dialog.

## Before you start

- MQTT must be compiled into your build of AetherSDR (the dialog is guarded by the `HAVE_MQTT` build gate).
- An MQTT broker connection must be configured. See Configure MQTT broker connection.

## Steps

1. Open the MQTT Settings dialog: **Settings > MQTT...**.
2. Click the **Publish Buttons** tab.
3. To add a button, click **Add**. A new row appears in the table with empty Label, Topic, and Payload cells.
4. Double-click each cell and type the values you want.
5. To remove one or more buttons, select their rows (click the row number on the left, or Ctrl-click multiple rows) and click **Remove**.
6. Click **Apply** to save without closing, or **Ok** to save and close.

## What each control does

| Control | Behavior | Limit |
|---|---|---|
| **Add** | Inserts a new row in the button table. Disabled when 12 rows are present. | 12 buttons maximum |
| **Remove** | Removes the selected rows from the button table. | — |
| **Label** (table cell) | Text displayed on the publish button in the MQTT applet. | Editable text |
| **Topic** (table cell) | MQTT topic string sent when the button is clicked. | Editable text |
| **Payload** (table cell) | MQTT payload string sent when the button is clicked. | Editable text |

All button definitions are saved to `MqttSettings` (nested JSON key `buttons`) when you click Apply or Ok.

## Tips

- Rows with empty Label, Topic, *and* Payload are omitted on save — you can leave unfinished rows.
- Button definitions are shared between the MQTT Settings dialog and the MQTT applet panel.

## Related

- Configure MQTT broker connection (host, port, credentials, TLS)
