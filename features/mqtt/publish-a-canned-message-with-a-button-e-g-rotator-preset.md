# Publish a canned message with a button (e.g. rotator preset)

This page shows how to add a publish button to the MQTT applet and use it to send a fixed message to your broker — for example, sending a rotator preset command with a single click.

## Before you start

- The MQTT applet must be visible. If it is not, click the MQTT tray button on the right sidebar to show it.
- You must have a broker connection configured. See [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md).
- The applet must be connected (Enable shows "On" and the status label reads "Connected") before publish buttons will fire.

## Steps

1. Open the MQTT applet by clicking the MQTT tray button on the right sidebar.
2. If you are not already connected, fill in Host, Port, User, Pass, and Topics, then click Enable to set it to "On". Wait for the status label to read "Connected".
3. Click Edit. The button changes to "Done" and edit mode begins. Any existing publish buttons change appearance to indicate they are editable.
4. Click the `+` tile that appears in the button grid. An edit dialog opens.
5. In the dialog, enter the button label (the text that will appear on the button), the topic to publish to, and the payload to send. Confirm the dialog.
6. The new button appears in the grid. Repeat steps 4–5 to add more buttons (up to 12 total).
7. Click Done to exit edit mode. Buttons return to their normal appearance.
8. Click any publish button to send its configured payload to its configured topic immediately. The button is only active while connected.

## What each control does

| Control | Kind | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|---|
| Publish buttons | Push button | — | Up to 12 buttons | `MqttButtons` | Each click publishes the configured payload to the configured topic. Only active while connected. |
| Edit / Done | Toggle button | Edit | — | — | Enters or exits button-edit mode. In edit mode, clicking a button opens its edit dialog; right-clicking a button shows a Remove option; the `+` tile adds a new button. |

## Tips

- To edit an existing button, click Edit, then click the button you want to change. The edit dialog opens with the current label, topic, and payload pre-filled.
- To remove a button, click Edit, then right-click the button and choose "Remove".
- Button definitions are stored as JSON under `MqttButtons` and persist across restarts.
- Hovering over a button in normal mode shows a tooltip with the configured topic and payload so you can confirm what will be sent before clicking.

## Troubleshooting

- **Clicking a publish button does nothing** — The applet is not connected. Check that Enable reads "On" and the status label reads "Connected". If it shows an error, verify your broker settings and click Enable to reconnect.
- **The `+` tile does not appear** — You have reached the 12-button limit. Remove an existing button to make room.
- **Button is missing after restart** — Settings are saved when you confirm the edit dialog. If AetherSDR was force-closed, the `MqttButtons` key may not have been written. Re-add the button.

## Related

- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Add or remove custom publish buttons](add-or-remove-custom-publish-buttons.md)
- [Subscribe to rotator / antenna switch topics](subscribe-to-rotator-antenna-switch-topics.md)
- [MQTT overview](overview.md)
