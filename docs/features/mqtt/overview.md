# MQTT overview

The MQTT applet connects AetherSDR to a station MQTT broker so you can subscribe to topics, view incoming and outgoing messages in a live log, overlay topic values on the panadapter, and publish canned messages with user-defined buttons. No radio connection is required.

## Before you start

- An MQTT broker must be reachable on your network (for example, Mosquitto running on `localhost`).
- If the MQTT applet is not visible, enable it by clicking the MQTT tray button on the right sidebar. The applet is hidden by default.
- If the MQTT tray button is absent, your AetherSDR build may not include MQTT support (`HAVE_MQTT` build gate required).

## How it works

When you click Enable (switching it from Off to On), the applet loads the MQTT password from the system keychain, saves all broker settings, and opens a connection to the broker. It subscribes to every topic configured in the MQTT Settings dialog. Incoming messages appear in the message log as `topic: value` lines; outgoing published messages appear as `TX topic: value` lines. The log retains the last 50 lines. Topics prefixed with `*` in the subscription list additionally push their latest value to the panadapter as an overlay. Publish buttons let you send a fixed payload to a fixed topic in a single click while connected.

Clicking Enable again (switching it from On to Off) disconnects immediately and clears any panadapter overlays.

Settings are saved to disk only when Enable transitions from Off to On.

## What each control does

| Control         | Default                                                                                                                                     | Valid range                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Enable          | Off                                                                                                                                         | Off / On                                                                            |
| Settings...     | Opens the MQTT Settings dialog (MqttSettingsDialog) for broker connection, subscriptions, and publish button configuration.                 | New in v26.5.3. Replaces the inline Host/Port/User/Pass/TLS/Topics fields.          |
| Publish buttons | Click publishes the configured payload to the configured topic via MqttClient::publish. Buttons are configured in the MQTT Settings dialog. | Up to 12 buttons. Only active while connected. Configured via MqttSettingsDialog Publish Buttons tab. |
| Message log     | Displays received messages as 'topic: value' lines and published messages as 'TX topic: value' lines. Also processes antenna alias updates from MQTT. | Capped to 50 entries. |

## Status indicator

The status label next to Enable shows the current connection state:

- **Connected** — shown in green when the broker connection is established.
- **Disconnected** — shown in grey when not connected.
- **\<error message\>** — shown in the default color when a connection error occurs; the text describes the error.

## Tips

- Topics are matched exactly. If a topic has a deep path such as `rotator/az/pos`, the message log shows only the last path segment (`pos`) as the label, but the full path is used for panadapter overlay matching.
- You do not need a radio connection to use MQTT. The applet operates independently of the FlexRadio connection state.
- Publish buttons are inactive (clicks have no effect) while disconnected. Connect first, then use the buttons.
- The MQTT password is stored in the system keychain. On first enable, the applet shows "Waiting for keychain" until the password is loaded.
- All broker connection settings (host, port, credentials, TLS, subscriptions) are configured exclusively via the MQTT Settings dialog (Settings > MQTT...).
- The MQTT applet now uses theme-aware colors for all controls and labels, adapting correctly to light and dark themes.
- The message log now shows both incoming and outgoing messages. Outgoing messages appear with a `TX` prefix (for example, `TX rotator/az/set: 180`) to distinguish them from incoming messages.

## Related

- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Subscribe to rotator / antenna switch topics](subscribe-to-rotator-antenna-switch-topics.md)
- [Overlay an MQTT value on the panadapter (prefix topic with *)](overlay-an-mqtt-value-on-the-panadapter-prefix-topic-with.md)
- [Publish a canned message with a button (e.g. rotator preset)](publish-a-canned-message-with-a-button-e-g-rotator-preset.md)
- [Add or remove custom publish buttons](add-or-remove-custom-publish-buttons.md)
- [Enable TLS with a custom CA certificate](enable-tls-with-a-custom-ca-certificate.md)