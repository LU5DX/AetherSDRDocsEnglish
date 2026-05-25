# Subscribe to MQTT topics and toggle panadapter display

Add MQTT topic subscriptions and control whether each topic's latest value is shown as an overlay on the panadapter. This lets you monitor station telemetry — such as antenna rotator position, weather data, or amplifier status — directly on the spectrum display.

## Before you start

- You must have a working MQTT broker accessible from your AetherSDR machine.
- The MQTT applet must be visible (toggle the MQTT tray button on the right sidebar if it is hidden).

## Steps

1. Open the MQTT Settings dialog: go to **Settings > MQTT...** or click **Settings...** in the MQTT applet header.
2. Click the **Subscriptions** tab.
3. Click **Add** to insert a new row in the topic table.
4. Double-click the **Topic** cell and type the full MQTT topic string (e.g. `rotator/azimuth`).
5. Under the **Display** column, check the box to show the topic's latest value as an overlay on the panadapter. Leave it unchecked to subscribe without displaying.
6. Click **Apply** to save the subscription list without closing the dialog, or **Ok** to save and close.
7. In the MQTT applet, click **Off** to toggle to **On** and connect to the broker.

## What each control does

| Control | Purpose | Default | Valid range | Setting key |
|---|---|---|---|---|
| Topic table | List of subscribed MQTT topics. Each row is one topic. | (empty) | Any valid MQTT topic string | `MqttSettings` (nested JSON) |
| Display checkbox | When checked, the topic's latest received value appears as an overlay on the panadapter. | Unchecked | — | same as above |
| Add | Inserts a new blank row in the topic table. | — | — | — |
| Remove | Deletes the selected row(s) from the topic table. | — | — | — |
| Internal AetherSDR Topics | Read-only list of topics subscribed automatically (e.g. antenna alias updates). These cannot be removed. | See the read-only list in the dialog | — | — |

## Tips

- The panadapter overlay shows the value of the most recently received message for each topic with Display enabled. Overlay labels are truncated to fit, so keep topic names short.
- A topic is subscribed immediately when you connect to the broker (toggle **On** in the applet). You do not need to reconnect after changing subscriptions — toggle **Off** then **On** to apply changes.

## Related

- [Overlay an MQTT value on the panadapter](overlay-an-mqtt-value-on-the-panadapter.md)
- [Configure MQTT broker connection (host, port, credentials, TLS)](../../getting-started/setup/configure-mqtt-broker-connection-host-port-credentials-tls.md)
