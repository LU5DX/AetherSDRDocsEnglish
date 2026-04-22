# MQTT overview

The MQTT applet connects AetherSDR to a station MQTT broker so you can subscribe to topics, view incoming messages in a live log, overlay topic values on the panadapter, and publish canned messages with user-defined buttons. No radio connection is required.

## Before you start

- An MQTT broker must be reachable on your network (for example, Mosquitto running on `localhost`).
- If the MQTT applet is not visible, enable it by clicking the MQTT tray button on the right sidebar. The applet is hidden by default.
- If the MQTT tray button is absent, your AetherSDR build may not include MQTT support (`HAVE_MQTT` build gate required).

## How it works

When you click Enable (switching it from Off to On), the applet saves all broker settings and opens a connection to the broker. It subscribes to every topic listed in the Topics field. Incoming messages appear in the message log as `topic: value` lines; the log retains the last 50 lines. Topics prefixed with `*` in the Topics field additionally push their latest value to the panadapter as an overlay. Publish buttons let you send a fixed payload to a fixed topic in a single click while connected.

Clicking Enable again (switching it from On to Off) disconnects immediately and clears any panadapter overlays.

Settings are saved to disk only when Enable transitions from Off to On.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Host | `localhost` | Any hostname or IP | `MqttHost` | Broker hostname or IP address. |
| Port | `1883` | 1–65535 | `MqttPort` | Broker TCP port. Automatically switches between `1883` and `8883` when TLS is toggled. |
| User | _(empty)_ | Any string | `MqttUser` | Broker username. Optional. |
| Pass | _(empty)_ | Any string | `MqttPass` | Broker password. Optional. Displayed masked. |
| Topics | _(empty)_ | Comma-separated list | `MqttTopics` | Topics to subscribe to. Prefix a topic with `*` to also overlay its value on the panadapter. Example: `*rotator/pos, *ant/selected, station/log`. |
| TLS | Off | On / Off | `MqttTls` | Enables TLS encryption. Toggling this shows or hides the CA cert row and automatically flips Port between `1883` and `8883`. |
| CA cert | _(empty)_ | File path | `MqttCaFile` | Path to a CA certificate file. Leave blank to use the system CA bundle. Row is only visible when TLS is checked. |
| Enable | Off | Off / On | _(not persisted)_ | Connects (Off → On) or disconnects (On → Off). Saving all settings to disk occurs on connect. |
| Publish buttons | _(none)_ | Up to 12 buttons | `MqttButtons` | Each button publishes a configured payload to a configured topic. Only active while connected. Stored as JSON. |
| Edit / Done | Edit | Edit / Done | _(not persisted)_ | Enters button-edit mode. In edit mode, clicking a button opens its edit dialog, right-clicking a button removes it, and a `+` tile adds a new button (up to 12). Click Done to exit edit mode. |
| Message log | _(empty)_ | Last 50 lines | _(not persisted)_ | Displays received messages as `topic: value` lines. Read-only. |

## Status indicator

The status label next to Enable shows the current connection state:

- **Connected** — shown in green when the broker connection is established.
- **Disconnected** — shown in grey when not connected.
- **\<error message\>** — shown in the default color when a connection error occurs; the text describes the error.

## Tips

- Topics are matched exactly. If a topic has a deep path such as `rotator/az/pos`, the message log shows only the last path segment (`pos`) as the label, but the full path is used for panadapter overlay matching.
- You do not need a radio connection to use MQTT. The applet operates independently of the FlexRadio connection state.
- Publish buttons are inactive (clicks have no effect) while disconnected. Connect first, then use the buttons.

## Related

- [Connect to a station MQTT broker](../../getting-started/setup/connect-to-a-station-mqtt-broker.md)
- [Subscribe to rotator / antenna switch topics](subscribe-to-rotator-antenna-switch-topics.md)
- [Overlay an MQTT value on the panadapter (prefix topic with *)](overlay-an-mqtt-value-on-the-panadapter-prefix-topic-with.md)
- [Publish a canned message with a button (e.g. rotator preset)](publish-a-canned-message-with-a-button-e-g-rotator-preset.md)
- [Add or remove custom publish buttons](add-or-remove-custom-publish-buttons.md)
- [Enable TLS with a custom CA certificate](enable-tls-with-a-custom-ca-certificate.md)
