# MQTT Applet

The MQTT applet integrates AetherSDR with a station MQTT broker. It allows you to publish canned messages with user-editable buttons, monitor incoming messages, view published messages in the message log, and overlay topic values on the panadapter.

## Overview

The MQTT applet provides four main functions:
- **Publish buttons**: Up to 12 user-defined buttons that send fixed payloads to fixed topics when clicked.
- **Message log**: Displays up to 50 received messages and published messages as "topic: value" lines.
- **Published message log**: Shows sent messages prefixed with "TX" in the message log.
- **Connection control**: Enable/Disable toggle to connect or disconnect from the broker.

## Connection setup

Connection settings (host, port, credentials, TLS, and subscriptions) are configured in the dedicated MQTT Settings dialog.

1. In the MQTT applet, click **Settings...**.
2. In the MQTT Settings dialog, configure the broker connection:
   - **Host**: Broker hostname or IP address.
   - **Port**: Broker port (default 1883 for plain, 8883 for TLS).
   - **User**: Username for authentication (leave blank if not required).
   - **Password**: Password for authentication. Stored in the system keychain.
   - **TLS**: Enable TLS encryption.
   - **CA cert**: Path to CA certificate file (optional; blank uses system CA bundle).
3. Configure subscription topics in the **Subscriptions** tab:
   - Enter comma-separated topics to subscribe to.
   - Prefix with `*` to display on panadapter overlay.
   - Example: `*rotator/pos, *ant/selected, station/log`
4. Configure publish buttons in the **Publish Buttons** tab.
5. Click **OK** to save settings.

## Connect to the broker

1. In the MQTT applet, click **Enable** (toggle button) to connect.
2. The status label shows connection state:
   - **Disconnected** (grey) - not connected.
   - **Connected** (green) - connected and ready.
   - Error message (default colour) - connection failed.

On first enable, the password is loaded from the system keychain. If the keychain password is not yet loaded, the status shows "Waiting for keychain".

To disconnect, click **Enable** again.

## Publish buttons

The MQTT applet supports up to 12 user-defined publish buttons. Each button sends a fixed payload to a fixed topic when clicked.

### Before you start

- The MQTT applet must be visible. If it is not, click the MQTT tray button on the right sidebar to show it.
- You do not need to be connected to the broker to edit buttons. However, buttons only publish when the applet is connected (status shows "Connected").
- Button definitions are stored in `MqttButtons` and persist between sessions.

### Add a button

1. In the MQTT applet, click **Settings...**.
2. In the MQTT Settings dialog, go to the **Publish Buttons** tab.
3. Click **Add**.
4. In the dialog that opens, enter a label, a topic, and a payload for the new button.
5. Click **OK** to confirm.
6. Click **OK** in the MQTT Settings dialog to save.

### Edit an existing button

1. Click **Settings...**.
2. In the MQTT Settings dialog, go to the **Publish Buttons** tab.
3. Click the button you want to change. An edit dialog opens showing the current label, topic, and payload.
4. Change the values as needed and click **OK**.
5. Click **OK** in the MQTT Settings dialog to save.

### Remove a button

1. Click **Settings...**.
2. In the MQTT Settings dialog, go to the **Publish Buttons** tab.
3. Right-click the button you want to remove.
4. Click **Remove** in the context menu that appears.
5. Click **OK** in the MQTT Settings dialog to save.

## What each control does

| Control             | Default                                                                                                                                     | Notes                                                                                                                                                                                                           |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Settings...**     | —                                                                                                                                           | Opens the MQTT Settings dialog (MqttSettingsDialog) for broker connection, subscriptions, and publish button configuration. New in v26.5.3. Replaces the inline Host/Port/User/Pass/TLS/Topics fields.          |
| Publish buttons     | Click publishes the configured payload to the configured topic via MqttClient::publish. Buttons are configured in the MQTT Settings dialog. | Only active while connected. Configured via MqttSettingsDialog Publish Buttons tab.                                                                                                                             |
| Message log         | Displays received messages as 'topic: value' lines. Also processes antenna alias updates from MQTT.                                         | Capped to 50 entries.                                                                                                                                                                                           |
| **Enable** (Off/On) | Off                                                                                                                                         | Connects or disconnects from the broker using settings from MqttSettings. Password is loaded from system keychain on first enable. If keychain password is not yet loaded, shows 'Waiting for keychain' status. |
| Settings...         | Opens the MQTT Settings dialog (MqttSettingsDialog) for broker connection, subscriptions, and publish button configuration.                 | New in v26.5.3. Replaces the inline Host/Port/User/Pass/TLS/Topics fields.                                                                                                                                      |
## Message log behavior

The message log displays both received and published messages:
- **Received messages**: Shown as `topic: value` where topic is the last segment of the full topic path.
- **Published messages**: Shown as `TX topic: value` where topic is the last segment of the publish topic path and value is the first 80 characters of the payload.

The log is capped at 50 entries. When the limit is reached, the oldest entry is removed to make room for new entries.

## Status indicators

| Indicator     | States                                          | Meaning                                                                          |
|---------------|-------------------------------------------------|----------------------------------------------------------------------------------|
| Status label  | Disconnected, Connected, \<error message\>      | Connection state with colour: green when connected, grey when disconnected, default on error. |

## Tips

- Button tooltips show the target topic and payload when the applet is in normal mode (`topic → payload`).
- Buttons are inactive when the applet is disconnected. Connect first, then use the buttons to publish.
- If you need to publish to the same topic with different payloads, create one button per payload.
- The password is stored in the system keychain for security.
- The message log shows published messages with a "TX" prefix, helping you confirm that your publish buttons are sending correctly.

## Troubleshooting

- **Clicking a publish button does nothing** — The applet is not connected. Check that the status label reads "Connected". If it reads "Disconnected" or an error message, click **Enable** to connect.
- **Cannot add more than 12 buttons** — 12 is the maximum number of publish buttons. Remove at least one button before adding another.
- **Connection fails** — Verify the broker host, port, and credentials in Settings... are correct. Ensure the broker is running and reachable.
- **Password prompt appears on every connection** — The system keychain may not be accessible. Check your system keychain configuration.

## Related

- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Publish a canned message with a button (e.g. rotator preset)](publish-a-canned-message-with-a-button-e-g-rotator-preset.md)
- [MQTT overview](overview.md)