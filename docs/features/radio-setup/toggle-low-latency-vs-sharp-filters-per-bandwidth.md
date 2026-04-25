# Toggle low-latency vs sharp filters per bandwidth

Use this page to choose whether AetherSDR applies low-latency or sharp (high-selectivity) filters for each receiver bandwidth, and to force low-latency filters specifically for digital modes.

## Before you start

- AetherSDR must be connected to the radio. The Filters tab is not accessible without an active radio connection.
- Open the Radio Setup dialog via `Settings > Radio Setup...`.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Filters** tab.
3. Click **Low Latency / Sharp Filters** to toggle between the two filter families for the current bandwidth. The button reflects the active selection.
4. To force low-latency filters whenever a digital mode (DIGU or DIGL) is active, check **Use Low Latency Filters for Digital Modes**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Low Latency / Sharp Filters** | Toggle button | Switches the filter-family preference between low-latency and sharp (high-selectivity) filters for the active bandwidth. |
| **Use Low Latency Filters for Digital Modes** | Checkbox | When checked, low-latency filters are applied automatically when the mode is DIGU or DIGL, regardless of the global toggle above. |

## Tips

- Low-latency filters reduce processing delay, which benefits digital modes and real-time decoding. Sharp filters provide steeper skirts for better adjacent-signal rejection on phone and CW.
- The **Use Low Latency Filters for Digital Modes** checkbox lets you keep sharp filters for SSB and CW while still getting reduced latency on DIGU/DIGL without manually switching.

## Related

- [Radio Setup overview](overview.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
