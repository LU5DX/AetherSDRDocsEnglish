# Configure MQTT publish buttons

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

## Settings storage

- All button definitions are saved to `MqttSettings` (nested JSON key `buttons`) when you click Apply or Ok.

## Tips

- Rows with empty Label, Topic, *and* Payload are omitted on save — you can leave unfinished rows.
- Button definitions are shared between the MQTT Settings dialog and the MQTT applet panel.

## Related

- Configure MQTT broker connection (host, port, credentials, TLS)
- Configure MQTT subscriptions

---

# Configure MQTT broker connection

Configure the connection between AetherSDR and your MQTT broker, including host, port, credentials, and TLS settings.

## Before you start

- MQTT must be compiled into your build of AetherSDR (the dialog is guarded by the `HAVE_MQTT` build gate).

## Steps

1. Open the MQTT Settings dialog: **Settings > MQTT...**.
2. In the **Broker** tab, configure the connection:
   - **Host**: Enter the hostname or IP address of your MQTT broker. Default is `localhost`.
   - **Port**: Enter the TCP port of your broker. Default is `1883`. Valid range is 1–65535. The port automatically switches between 1883 and 8883 when you toggle TLS.
   - **User**: Enter the broker username if authentication is required (optional).
   - **Password**: Enter the broker password if authentication is required (optional). The field is masked.
   - **Use TLS**: Check to enable TLS encryption. Checking or unchecking this automatically flips the port between 1883 and 8883.
   - **CA cert**: If TLS is enabled, enter the path to a CA certificate file, or click **Browse** to select one. Leave blank to use the system CA bundle. This field is only visible when TLS is checked.
3. Click **Apply** to save without closing, or **Ok** to save and close.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **Host** | Broker hostname or IP address. | Stored in `MqttHost`. |
| **Port** | Broker TCP port. | Stored in `MqttPort`. Auto-switches between 1883 and 8883 when TLS is toggled. |
| **User** | Broker username (optional). | Stored in `MqttUser`. |
| **Password** | Broker password (optional, masked). | Stored in the system keychain when available; falls back to session-only storage otherwise. |
| **Use TLS** | Enables TLS encryption. | Stored in `MqttTls`. Shows/hides the CA cert row. |
| **CA cert** | Path to a CA certificate file. Blank means use the system CA bundle. | Stored in `MqttCaFile`. Row visible only when TLS is checked. |
| **Apply** | Saves all settings (connection, topics, buttons, password) without closing the dialog. | Part of the QDialogButtonBox with Ok and Cancel. |

## Password storage

- When AetherSDR is built with keychain support, the password is stored in the system keychain (for example, Keychain on macOS, kwallet on Linux, or Credential Manager on Windows).
- When AetherSDR is built without keychain support, the password is stored **in memory only** and must be re-entered each time the application launches. It is never written to the settings store.
- If you previously stored the password in plaintext settings (from an older version), AetherSDR migrates it to the new storage method on first launch and removes the old plaintext copy.

## Related

- Configure MQTT subscriptions
- Add or remove publish buttons

---

# Configure MQTT subscriptions

Subscribe to MQTT topics and display their messages on the panadapter overlay. You define the list of subscribed topics in the Subscriptions tab of the MQTT Settings dialog.

## Before you start

- MQTT must be compiled into your build of AetherSDR (the dialog is guarded by the `HAVE_MQTT` build gate).
- An MQTT broker connection must be configured. See Configure MQTT broker connection.

## Steps

1. Open the MQTT Settings dialog: **Settings > MQTT...**.
2. Click the **Subscriptions** tab.
3. To add a subscription, click **Add**. A new row appears in the table.
4. Double-click the **Topic** cell and type the topic string you want to subscribe to.
5. To show messages on the panadapter overlay, check the **Display** checkbox for that row.
6. To remove one or more subscriptions, select their rows and click **Remove**.
7. Click **Apply** to save without closing, or **Ok** to save and close.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **Add** | Inserts a new row in the subscription table. | — |
| **Remove** | Removes the selected rows from the subscription table. | — |
| **Topic** (table cell) | MQTT topic string to subscribe to. | Editable text. |
| **Display** (table cell) | Checkbox; when checked, messages for this topic are shown on the panadapter overlay. | — |

## Internal AetherSDR Topics

The **Internal AetherSDR Topics** group box at the bottom of the Subscriptions tab lists topics that AetherSDR subscribes to automatically whenever MQTT is connected. These subscriptions are read-only and cannot be removed.

AetherSDR automatically subscribes to these internal topics when the MQTT connection is established:

- `aethersdr/cw/decode` — CW decoded text
- `aethersdr/radio/state` — Radio VFO / mode / TX state
- `aethersdr/ax25/rx` — AX.25 received frames

## Settings storage

- All subscription definitions are saved to `MqttSettings` when you click Apply or Ok.

## Related

- Configure MQTT broker connection (host, port, credentials, TLS)
- Add or remove publish buttons