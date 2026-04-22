# Adjust TCI TX gain

This page explains how to set the TCI TX gain in the TCI Server applet. Adjusting TX gain controls the level of transmit audio sent to connected TCI clients such as Log4OM or SunSDR tools.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio.
- The TCI Server applet must be visible. If it is not, click the TCI tray button on the right sidebar to show it.
- The TCI server should be running (Enable toggled on) so that gain changes take effect for connected clients.

## Steps

1. Click the TCI tray button on the right sidebar to open the TCI Server applet.
2. Locate the TX row. The label on the left reads "TX:" and shows a slice assignment indicator to its right (either "—" or "Slice \<letter\>").
3. Drag the TX gain+meter slider to set the desired gain. Drag right to increase, left to decrease.
4. Release the slider. The value is persisted automatically as `TciTxGain`.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| TX gain+meter | Combined level meter and gain slider for TCI TX audio. Drag to set gain; the meter reflects live TX signal level. | 0.5 | 0.0–1.0 | `TciTxGain` |
| TX slice indicator | Shows which slice currently drives the TX row (e.g. "Slice A"). Displays "—" when no TX slice is assigned. | — | "—" or "Slice \<letter\>" | *(none)* |

## Tips

- The TX gain+meter shows live transmit signal level while you are transmitting, letting you verify the gain setting under real conditions.
- `TciTxGain` is persisted automatically when you move the slider. No additional save step is required.

## Troubleshooting

- **TX slice indicator shows "—"** — No slice is currently designated as the TX slice on the radio. Assign a TX slice in the radio's slice controls, then return to this applet.
- **Slider position does not match what TCI clients report** — The TCI server reads `TciTxGain` on startup. If the value was changed externally, restart the TCI server by clicking Enable to off, then Enable to on again.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [TCI Server overview](overview.md)
