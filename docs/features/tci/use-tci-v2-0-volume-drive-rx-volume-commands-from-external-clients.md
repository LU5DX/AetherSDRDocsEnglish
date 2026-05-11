# Use TCI v2.0 volume/drive/rx_volume commands from external clients

External clients (logging software, digital-mode software, SDR programs) can control AetherSDR using TCI v2.0 `volume`, `drive`, and `rx_volume` commands when the TCI server is enabled and the radio is connected.

## Before you start

- Enable the TCI server (click the TCI tray button on the right sidebar, then click Enable).
- Connect to a radio.
- Configure your external client to connect to AetherSDR's TCI server on the port shown in the TCI applet (default: 50001).

## Steps

1. In the TCI applet, note the Port number or change it by editing the text field and pressing Enter. Valid range: 1024–65535.
2. Configure your external client to connect to AetherSDR's IP address and that port.
3. Send TCI v2.0 commands from your client:

   - **`volume`** — Sets the master RX volume. AetherSDR maps this to the RX gain for the currently active slice.
   - **`drive`** — Sets the TX drive level. AetherSDR maps this to `TciTxGain`.
   - **`rx_volume <channel>`** — Sets the RX gain for a specific DAX channel (1–4). AetherSDR maps this to `TciRxGain1` through `TciRxGain4`.

4. The TCI server receives these commands and updates the corresponding gain settings. The changes are reflected in the TCI applet's meter/slider controls and persisted to settings.

## What each control does

| Command | Mapped setting | Default | Valid range |
|---------|---------------|---------|-------------|
| `volume` | Active slice RX gain | 0.5 | 0.0–1.0 |
| `drive` | `TciTxGain` | 0.5 | 0.0–1.0 |
| `rx_volume <channel>` | `TciRxGain1`–`TciRxGain4` | 0.5 | 0.0–1.0 |

## Tips

- The TCI server supports bidirectional state sync — changes made locally via the TCI applet's sliders are also sent back to external clients that subscribe to gain updates.
- The `rx_volume` command accepts a channel number (1–4). Channel numbers correspond to the DAX channels displayed in the TCI applet's RX1–RX4 rows.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
