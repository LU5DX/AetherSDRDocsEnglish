# Add or remove custom publish buttons

The MQTT applet supports up to 12 user-defined publish buttons. Each button sends a fixed payload to a fixed topic when clicked. This page explains how to add new buttons, edit existing ones, and remove buttons you no longer need.

## Before you start

- The MQTT applet must be visible. If it is not, click the MQTT tray button on the right sidebar to show it.
- You do not need to be connected to the broker to edit buttons. However, buttons only publish when the applet is connected (status shows "Connected").
- Button definitions are stored in `MqttButtons` and persist between sessions.

## Steps

### Add a button

1. In the MQTT applet, click **Edit**. The button area enters edit mode: existing buttons change appearance and a **+** tile appears.
2. Click the **+** tile.
3. In the dialog that opens, enter a label, a topic, and a payload for the new button.
4. Confirm the dialog.
5. Click **Done** to exit edit mode.

### Edit an existing button

1. Click **Edit**.
2. Click the button you want to change. An edit dialog opens showing the current label, topic, and payload.
3. Change the values as needed and confirm.
4. Click **Done**.

### Remove a button

1. Click **Edit**.
2. Right-click the button you want to remove.
3. Click **Remove** in the context menu that appears.
4. Click **Done**.

## What each control does

| Control | Default | Notes |
|---|---|---|
| **Edit** / **Done** | **Edit** | Toggles edit mode. In edit mode, clicking a button opens the edit dialog; right-clicking shows the Remove option; the **+** tile is visible. |
| Publish buttons | — | Each button publishes its configured payload to its configured topic. Active only while connected. Up to 12 buttons. Stored in `MqttButtons`. |
| **+** tile | — | Visible only in edit mode. Opens the add-button dialog. Disabled once 12 buttons exist. |

## Tips

- Button tooltips show the target topic and payload when the applet is in normal mode (`topic → payload`). In edit mode they show the same information prefixed with "Click to edit".
- Buttons are inactive when the applet is disconnected. Connect first, then use the buttons to publish.
- If you need to publish to the same topic with different payloads, create one button per payload.

## Troubleshooting

- **Clicking a publish button does nothing** — The applet is not connected. Check that the status label reads "Connected". If it reads "Disconnected" or an error message, click **Enable** to connect. See [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md).
- **The + tile does not appear** — You already have 12 buttons, which is the maximum. Remove at least one button before adding another.
- **Button changes are lost after restart** — Changes are saved automatically when you confirm the edit dialog. If the applet crashed before saving, the previous `MqttButtons` value is restored.

## Related

- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Publish a canned message with a button (e.g. rotator preset)](publish-a-canned-message-with-a-button-e-g-rotator-preset.md)
- [MQTT overview](overview.md)
