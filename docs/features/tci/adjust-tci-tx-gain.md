# Adjust TCI TX gain

This page explains how to set the TX gain for audio sent to TCI clients. Adjusting this value lets you match the transmit audio level that third-party software receives over the TCI connection.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The TCI server must be enabled. If it is not, see [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md).
- The TCI applet must be visible. If it is not, click the TCI tray button on the right sidebar to show it.

## Steps

1. Click the TCI tray button on the right sidebar to open the TCI applet.
2. Locate the TX row. It shows a slice assignment label (such as `Slice A`) or `—` if no TX slice is assigned, followed by the TX gain+meter.
3. Drag the TX gain+meter slider left to decrease gain or right to increase gain.
4. Release the slider. The new value is saved immediately to `TciTxGain`.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| TX gain+meter | Combined level meter and gain slider for TCI TX audio. Drag to set gain. The meter shows live TX level. | 0.5 | 0.0–1.0 | `TciTxGain` |
| RX/TX slice-assignment label | Indicator showing which slice currently drives the TX row. Displays `—` when no TX slice is assigned. | `—` | `—` or `Slice <letter>` | — |

## Tips

- The TX gain+meter shows live transmit audio level while you are transmitting, which lets you confirm the level before committing to a value.
- The slider position is restored from `TciTxGain` each time AetherSDR starts, so your setting persists across sessions.

## Related

- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [TCI Server overview](overview.md)
