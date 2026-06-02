# Configure broker connection settings (host, port, credentials, TLS)

Set up the MQTT broker address, authentication, and TLS options that AetherSDR uses to connect to your station’s MQTT broker.

## Before you start

- The MQTT applet must be visible in the right sidebar. If hidden, click the MQTT tray button to show it.
- You need your broker’s hostname or IP address, port, and any required username and password.

## Steps

1. Open `Settings > MQTT...` to display the MQTT Settings dialog.
2. In the **Broker Connection** tab, enter the following:
   - **Host** — your broker’s hostname or IP address.
   - **Port** — the TCP port (default depends on your broker; common values are 1883 for plain TCP or 8883 for TLS).
   - **Username** — optional; leave blank if your broker does not require authentication.
   - **Password** — optional; stored in your system keychain when you first enable the connection (not in plain text).
3. To enable TLS:
   - Check **Use TLS**.
   - If your broker uses a custom CA certificate, enter its file path in **CA Certificate File** (or click **Browse...** to locate it).
4. Click **OK** to save the settings and close the dialog.
5. In the MQTT applet, click **Off** to toggle it to **On**. AetherSDR connects using the new settings. The status label changes to **Connected** (green) on success, or shows an error message if connection fails.

## What each control does

| Control             | Default                                                                                                                     | Notes                                                                      |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Username            | (empty)                                                                                                                     | Authentication user name                                                   |
| Password            | (empty)                                                                                                                     | Stored in system keychain when first used                                  |
| Use TLS             | unchecked                                                                                                                   | Toggle TLS encryption                                                      |
| CA Certificate File | (empty)                                                                                                                     | Path to custom CA certificate for TLS                                      |
| Settings...         | Opens the MQTT Settings dialog (MqttSettingsDialog) for broker connection, subscriptions, and publish button configuration. | New in v26.5.3. Replaces the inline Host/Port/User/Pass/TLS/Topics fields. |
| Enable (Off/On)     | Off                                                                                                                         | Connects or disconnects from the broker using settings from MqttSettings.   |
| Publish buttons     | (none)                                                                                                                      | Up to 12 buttons configured in the MQTT Settings dialog. Only active while connected. |
| Message log         | (empty)                                                                                                                     | Displays received messages as "topic: value" lines. Capped to 50 entries. |
| Status label        | Disconnected                                                                                                                | Shows "Connected" (green) on success, "Disconnected" (grey) when off or failed, or an error message (default color). |

## Tips

- The password is migrated to your system keychain the first time you enable the MQTT connection. If the migration fails, AetherSDR logs a warning and preserves the plain-text entry for retry.
- If you enable the connection (“On”) but the password hasn’t been loaded from keychain yet, the status shows **Waiting for keychain** until the keychain read completes.
- v26.6.1: The MQTT applet now uses theme-aware colors for all UI elements, adapting to both light and dark themes automatically.
- Antenna alias topics are subscribed automatically.

## Troubleshooting

- **Status shows “Disconnected” after toggling On** — Check the host and port are correct and reachable from your machine. If using TLS, verify the CA certificate path is valid.
- **Status shows an error message** — The broker rejected the connection. Confirm the username and password, and that TLS settings match your broker’s configuration.
- **“Waiting for keychain” never resolves** — The system keychain may be locked or unavailable. Unlock your keychain and toggle the connection Off then On again.

## Related

- [Connect to a station MQTT broker](connect-to-a-station-mqtt-broker.md)
- [Enable TLS with a custom CA certificate](../../features/mqtt/enable-tls-with-a-custom-ca-certificate.md)
- [Open MQTT settings from the applet](../../features/mqtt/open-mqtt-settings-from-the-applet.md)