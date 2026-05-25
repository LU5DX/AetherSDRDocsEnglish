# Subscribe to rotator / antenna switch topics

Use the MQTT applet to subscribe to topics published by your rotator controller or antenna switch. Incoming values appear in the message log and, if you prefix a topic with `*`, as an overlay on the panadapter.

## Before you start

- The MQTT applet must be visible. If you do not see it, click the MQTT tray button on the right sidebar to show it.
- Your station MQTT broker must be running and reachable from the machine running AetherSDR.
- If you have not yet configured broker credentials, complete [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md) first.

## Steps

1. Open the MQTT applet by clicking the MQTT tray button on the right sidebar.
2. Click **Settings...** to open the MQTT Settings dialog. Configure the broker connection details, subscription topics, and publish buttons there.
3. In the MQTT Settings dialog, enter the broker hostname or IP address, port, username, and password. If your broker uses TLS, enable TLS and optionally specify a CA certificate file.
4. In the **Subscriptions** tab, enter a comma-separated list of the topics you want to subscribe to. To also show a topic's value as a panadapter overlay, prefix it with `*`. Example:
   ```
   *rotator/pos, *ant/selected, station/log
   ```
5. Click **OK** to save settings and close the dialog.
6. Back in the MQTT applet, click **Enable** to connect. The button label changes to **On** and the status label reads **Connected** in green. The password is loaded from the system keychain on first enable.

## What each control does

| Control           | Default | Valid range / notes                                                                                      |
|-------------------|---------|----------------------------------------------------------------------------------------------------------|
| **Settings...**   | —       | Opens the MQTT Settings dialog for broker connection, subscriptions, and publish button configuration.   |
| **Publish buttons** | —     | Up to 12 buttons; each publishes a configured payload to a configured topic. Only active while connected.|
| **Message log**   | —       | Displays up to the last 50 received messages as `topic: value` lines. Also processes antenna alias updates from MQTT. |
| **Enable (Off/On)** | Off  | Connects or disconnects from the broker using settings from the MQTT Settings dialog. Password is loaded from system keychain on first enable. |

### Connection status indicator

| Status label | Meaning                                                       |
|--------------|---------------------------------------------------------------|
| **Disconnected** | Not connected to the broker. Grey colour.                    |
| **Connected**     | Successfully connected to the broker. Green colour.          |
| *Error message*   | Connection failed. Shows the error in default text colour.   |

## Tips

- A topic must be entered without the `*` prefix to be subscribed to; the `*` only controls whether the value appears on the panadapter overlay. The subscription itself is always active once you click **Enable**.
- The message log shows only the last segment of the topic path (after the final `/`) next to the value, so `rotator/pos` appears as `pos: 180`.
- Settings are saved when you click **OK** in the MQTT Settings dialog. No need to click **Enable** to persist them.

## Troubleshooting

- **Status label shows an error message instead of "Connected"** — The broker is unreachable or credentials are incorrect. Open **Settings...** and verify the host, port, username, and password values, then try again.
- **Topics are configured but no messages appear in the log** — Confirm that the broker is publishing on exactly those topic strings. MQTT topic matching is case-sensitive.
- **"Waiting for keychain" status appears** — The password has not yet been loaded from the system keychain. Click **Enable** again to trigger the keychain request.
- **Publish buttons are greyed out** — You must be connected to the broker. Click **Enable** to connect first.

## Related

- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Overlay an MQTT value on the panadapter (prefix topic with *)](overlay-an-mqtt-value-on-the-panadapter-prefix-topic-with.md)
- [Enable TLS with a custom CA certificate](enable-tls-with-a-custom-ca-certificate.md)
- [Publish a canned message with a button (e.g. rotator preset)](publish-a-canned-message-with-a-button-e-g-rotator-preset.md)